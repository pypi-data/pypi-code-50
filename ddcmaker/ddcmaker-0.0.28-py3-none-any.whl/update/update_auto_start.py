import os
import pathlib
from ddcmaker.update import get_conf, create_dir

conf = get_conf()
for feature in conf.features:
    origin = pathlib.Path(feature.temp_dir).absolute().joinpath(feature.name)
    origin_zip_name = feature.url.split('/')[-1]
    origin_zip_path = pathlib.Path(feature.temp_dir).absolute().joinpath(origin_zip_name)

    # 移动已解压文件到目标目录
    if origin.exists():
        target = pathlib.Path(feature.save_dir).absolute().joinpath(feature.name)
        if not target.exists():
            create_dir(target)
        os.system(f"mv {origin.joinpath('./*').as_posix()} {target.as_posix()}")
        origin.rmdir()

    # 清理下载文件
    if origin_zip_path.exists():
        origin_zip_path.unlink()

print("自动更新完毕")
