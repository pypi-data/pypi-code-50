import subprocess

from ddcmaker.basic.system import process


class Host(object):
    def run(self, cmd: str, timeout: int = 30):
        """
        执行相应的操作系统指令
        :param cmd:执行的指令
        :param timeout:指令超时时间，单位为s
        :return:
        """
        try:
            print("run ", cmd)
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, shell=True)
            try:
                proc.communicate(timeout=timeout)
            except Exception as e:
                print("超时中断动作，该动作默认执行最长时间为" + str(timeout) + "秒")
                raise e
        except Exception as e:
            print(e)
        finally:
            process.kill_process(cmd.split(" ")[1])
