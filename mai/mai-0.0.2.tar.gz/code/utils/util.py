from __future__ import absolute_import, division, print_function, unicode_literals
import os,shutil,sys
try:
    from tqdm.auto import tqdm 
except ImportError:
    from tqdm import tqdm
import tempfile
import torch
if sys.version_info[0] == 2:
    from urlparse import urlparse
    from urllib2 import urlopen  # noqa f811
else:
    from urllib.request import urlopen
    from urllib.parse import urlparse  # noqa: F401

def photo_process(food_path, train_data_path, val_data_path, test_data_path, traintest_cent, trainval_cent):
    for classes in os.listdir(food_path):
        filelist = os.listdir(os.path.join(food_path, classes))
        filelen = len(filelist)
        trainval_data = filelist[0:int(filelen*traintest_cent)]
        test_data = filelist[int(filelen*traintest_cent):]

        filelen = len(trainval_data)
        train_data = trainval_data[0:int(filelen*trainval_cent)]
        val_data = trainval_data[int(filelen*trainval_cent):]

        os.makedirs(os.path.join(train_data_path, classes), exist_ok=True)
        os.makedirs(os.path.join(val_data_path, classes), exist_ok=True)
        os.makedirs(os.path.join(test_data_path, classes), exist_ok=True)
        for i in train_data:
            src = os.path.join(food_path, classes, i)
            dst = os.path.join(train_data_path, classes, i)
            shutil.copy(src, dst)
        for i in val_data:
            src = os.path.join(food_path, classes, i)
            dst = os.path.join(val_data_path, classes, i)
            shutil.copy(src, dst)
        for i in test_data:
            src = os.path.join(food_path, classes, i)
            dst = os.path.join(test_data_path, classes, i)
            shutil.copy(src, dst)

            
def download_url_to_file(url, dst, hash_prefix=None, progress=True):
    file_size = None
    u = urlopen(url)
    meta = u.info()
    if hasattr(meta, 'getheaders'):
        content_length = meta.getheaders("Content-Length")
    else:
        content_length = meta.get_all("Content-Length")
    if content_length is not None and len(content_length) > 0:
        file_size = int(content_length[0])

    dst = os.path.expanduser(dst)
    dst_dir = os.path.dirname(dst)
    f = tempfile.NamedTemporaryFile(delete=False, dir=dst_dir)

    try:
#         with tqdm(total=file_size) as pbar:
        with tqdm(total=file_size, disable=not progress, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
            while True:
                buffer = u.read(8192)
                if len(buffer) == 0:
                    break
                f.write(buffer)
                if hash_prefix is not None:
                    sha256.update(buffer)
                pbar.update(len(buffer))

        f.close()
        shutil.move(f.name, dst)
    finally:
        f.close()
        if os.path.exists(f.name):
            os.remove(f.name)

def download_file(url, filedir):
    r"""Download object at the given URL to a local path.

    Args:
        url (string): URL of the object to download
        dst (string): Full path where object will be saved, e.g. `/tmp/temporary_file`
        hash_prefix (string, optional): If not None, the SHA256 downloaded file should start with `hash_prefix`.
            Default: None
        progress (bool, optional): whether or not to display a progress bar to stderr
            Default: True

    Example:
        >>> torch.hub.download_url_to_file('https://s3.amazonaws.com/pytorch/models/resnet18-5c106cde.pth', '/tmp/temporary_file')

    """
    os.makedirs(filedir, exist_ok=True)
    parts = urlparse(url)
    filename = os.path.basename(parts.path)
    cached_file = os.path.join(filedir, filename)
    print(cached_file)
    download_url_to_file(url, cached_file)
    
    
def test():
    url = 'https://publicmodels.blob.core.windows.net/container/aa/efficientnet-b0-355c32eb.pth'
    path = 'data'
    download_file(url, path)
    
# test()