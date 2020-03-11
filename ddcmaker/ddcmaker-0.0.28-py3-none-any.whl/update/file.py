import pathlib
import requests
import zipfile


def download_file(url: str, temp_dir: str) -> pathlib.Path:
    """
    下载文件到指定目录
    :param url:文件的url
    :param temp_dir:文件下载存放路径
    :return:
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise
    file_name = url.split("/")[-1]
    temp_path = pathlib.Path(temp_dir)

    if not temp_path.exists():
        create_dir(temp_path)

    file_path = temp_path.joinpath(file_name)

    with open(file_path.as_posix(), 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
    print(f"下载{url}到{temp_dir},文件名：{file_path.as_posix()},文件状态{file_path.exists()}")
    return file_path


def unzip_file(file_path: str, unzip_dir: str):
    """
    解压文件到指定目录
    :param file_path:zip文件路径
    :param unzip_dir:指定解压文件存放位置
    """
    file_zip = zipfile.ZipFile(file_path)
    unzip_dir_path = pathlib.Path(unzip_dir).absolute()
    if not unzip_dir_path.exists():
        create_dir(unzip_dir_path)

    for file in file_zip.filelist:
        file_zip.extract(file, unzip_dir_path.as_posix())
    print(f"{file_path}已经解压到{unzip_dir}")


def create_dir(dir_path: pathlib.Path):
    """
    创建指定目录
    :param dir_path:目录路径
    :return:
    """
    for parent in list(dir_path.parents)[::-1]:
        if not parent.exists():
            print(f"创建目录：{parent.as_posix()}", )
            parent.mkdir()

    print(f"创建目录：{dir_path.as_posix()}", )
    dir_path.mkdir()
