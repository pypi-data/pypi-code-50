import os
import traceback
from stat import S_ISDIR as isdir
import paramiko

from common.logger import log

def _call_fun(path, function):
    path = path.replace('\\', '/')
    try:
        return function(path)
    except Exception as e:
        log.error(e.__cause__)
        return None

def sftp_get(remote_file, local_file, **host):
    """
    sftp 拉取文件

    :param remote_file:  远程目标文件
    :param local_file:   本地文件
    :param host:        {'ip': SFTP_IP, 'port': SFTP_PORT, 'username': SFTP_USERNAME, 'password': SFTP_PASSWORD}
    :return:
    """
    t = None
    log.info('remote_file:{0}, local_file:{1}, host：{2}'.format(remote_file, local_file, host))
    try:
        t = paramiko.Transport(sock=(host['ip'], host['port']))
        folder_path = os.path.split(local_file)[0]
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        t.connect(username=host['username'], password=host['password'])
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.get(remote_file, local_file)
    finally:
        try:
            t.close()
        except:
            pass


class Sftp(object):
    SftpObjectDict = dict()

    def __new__(cls, *args, **kwargs):
        key = kwargs["host"] + kwargs["username"] + str(kwargs["password"])
        if not cls.SftpObjectDict.get(key):
            log.info('start create PostgresqlDB object')
            cls.SftpObjectDict.setdefault(key, object.__new__(cls))
        return cls.SftpObjectDict.get(key)

    def __init__(self, host, username, password, port=22):
        self.user_name = username
        self.pass_word = password
        self.host = host
        self.port = port
        key = host + username + str(password)
        try:
            self.sftp = self.SftpObjectDict[key].sftp
            self.client = self.SftpObjectDict[key].client
        except:
            self.sftp = None
            self.client = None
        try:
            if not self.sftp:
                self.connect()
                log.info('Sftp连接成功')
        except:
            log.error('Sftp连接失败')
            log.error(traceback.format_exc())

    # 建立连接，获取sftp句柄
    def connect(self):
        self.client = paramiko.Transport((self.host, self.port))
        self.client.connect(username=self.user_name, password=self.pass_word)
        self.sftp = paramiko.SFTPClient.from_transport(self.client)

        return self.client, self.sftp

    # 断开连接
    def disconnect(self):
        try:
            self.client.close()
        except Exception as error:
            log.error("连接SFTP异常了，用户名{} 密码{}".format(self.user_name, self.pass_word, error.__cause__))

    def exist(self, path):
        if not _call_fun(path, function=self.sftp.stat):
            return False
        return True

    def _copy(self, local, remote, dir_level=0):
        result = self.sftp.stat(remote)
        if isdir(result.st_mode):
            # 是，获取local路径中的最后一个文件名拼接到remote中
            if dir_level > 0:
                filename = os.path.basename(os.path.normpath(local))
                remote = os.path.join(remote, filename).replace('\\', '/')
        # 如果local为目录
        if os.path.isdir(local) and os.path.basename(local) != '__pycache__' and os.path.basename(local) != '.idea':
            # 在远程创建相应的目录
            _call_fun(remote, function=self.sftp.mkdir)
            # 遍历local
            for file in os.listdir(local):
                # 取得file的全路径
                localfile = os.path.join(local, file).replace('\\', '/')
                # 深度递归_copy()
                self._copy(local=localfile, remote=remote, dir_level=dir_level+1)
        # 如果local为文件
        if os.path.isfile(local):
            self.sftp.put(local, remote)

    def put_dir(self, local_dir, remote_dir):
        if not _call_fun(local_dir, function=os.stat):
            log.error("本地文件或者路径不存在{}".format(local_dir))
            return False
        if not _call_fun(remote_dir, function=self.sftp.stat):
            log.warn("远程目录{}不存在,尝试新建远程目录".format(remote_dir))
            self._make_dirs_remote(remote_dir)
        self._copy(local=local_dir, remote=remote_dir)

    def delete(self, remote_path):
        try:
            if not self.connect():
                return False
            if _call_fun(remote_path, function=self.sftp.stat):
                self.sftp.remove(remote_path)
        except Exception as e:
            log.error("删除{}文件失败:{}", remote_path, e.__cause__)
        finally:
            self.disconnect()

    def _make_dirs_remote(self, remote_path):
        parent_path = remote_path
        remote_paths = []
        while True:
            remote_paths.insert(0, parent_path)
            temp = os.path.dirname(parent_path)
            if temp == parent_path:
                break
            parent_path = temp
        for path in remote_paths:
            if not _call_fun(path, function=self.sftp.stat):
                log.warn("远程目录{}不存在,尝试新建远程目录".format(parent_path))
                self.sftp.mkdir(path)

    def put_file(self, local_file, remote_file):
        if not _call_fun(local_file, function=os.stat):
            log.error("本地文件或者路径不存在{}".format(local_file))
            return False
        remote_parent = os.path.dirname(os.path.normpath(remote_file))
        remote_parent = remote_parent.replace('\\', '/')
        if not _call_fun(remote_parent, function=self.sftp.stat):
            log.warn("远程目录{}不存在,尝试新建远程目录".format(remote_parent))
            self._make_dirs_remote(remote_parent)
        self.sftp.put(local_file, remote_file)
        return True

    def get_file(self, remote_file, local_file):
        if not _call_fun(remote_file, function=self.sftp.stat):
            log.warn("远程文件{}不存在".format(remote_file))
            return False
        local_parent = os.path.dirname(local_file)
        if not os.path.exists(local_parent):
            log.debug("文件的保存目录{}不存在，新建目录...".format(local_parent))
            os.makedirs(local_parent)
        self.sftp.get(remote_file, local_file)

    def get_dir(self, remote_dir, local_dir, dir_level=0):
        result = self.sftp.stat(remote_dir)
        if isdir(result.st_mode):  # 判断远程文件是否为目录,本地必须是一个目录，并且会把远程的目录直接拷贝到local下
            if dir_level >0:
                dirname = os.path.basename(os.path.normpath(remote_dir))
                local_dir = os.path.join(local_dir, dirname)
            if not os.path.exists(local_dir):
                log.debug("文件的保存目录{}不存在，新建目录...".format(local_dir))
                os.makedirs(local_dir)
            for file in self.sftp.listdir(remote_dir):
                sub_remote = os.path.join(remote_dir, file)
                sub_remote = sub_remote.replace('\\', '/')
                self.get_dir(sub_remote, local_dir, dir_level+1)
        else:
            if os.path.isdir(local_dir):
                local_dir = os.path.join(local_dir, os.path.basename(remote_dir))
            self.sftp.get(remote_dir, local_dir)


