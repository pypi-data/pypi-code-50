def download_file(url: str, out_file_dir: str) -> str:
    import requests
    import os

    local_filename = url.split("/")[-1]
    local_file_path = os.path.join(out_file_dir, local_filename)
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True, verify=False) as r:
        r.raise_for_status()
        with open(local_file_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    # f.flush()
    return local_file_path


def sanitize_string_as_path(unsanitized_str: str) -> str:
    import re

    sanitized_str = re.sub(r'[/\\:*?"<>|]', "", unsanitized_str)
    return sanitized_str


def save_webpage(url: str, file_path: str):
    import pdfkit
    import sys
    import logging

    try:
        pdfkit.from_url(url, file_path)
    except:
        logging.fatal(
            f"Likely did not have wkhtmltopdf installed: `brew install Caskroom/cask/wkhtmltopdf`\nError:{sys.exc_info()}"
        )


def save_youtube_video(url: str, out_file_dir: str, logger=None) -> str:
    import youtube_dl
    import os

    ydl_opts = {
        "restrictfilenames": True,
        "simulate": False,
        "noplaylist": True,
        "format": "[filesize<100M]",
        "outtmpl": os.path.join(out_file_dir, "%(title)s.%(ext)s"),
    }

    if logger:
        ydl_opts["logger"] = logger

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def dict_merge(dct: dict, merge_dct: dict, add_keys: bool = True) -> dict:
    """
    A recursive implementation of a dictionary merge with deepcopy
    @param dct: Dictionary which is merged into (overwritten)
    @param merge_dct: Dictionary to merge (writer)
    @param add_keys: Should you add keys from merge_dct which are not in dct?
    @return: A deepcopy of the merged dictionary
    """
    dct = dct.copy()
    if not add_keys:
        merge_dct = {k: merge_dct[k] for k in set(dct).intersection(set(merge_dct))}

    for k, v in merge_dct.items():
        if isinstance(dct.get(k), dict) and isinstance(v, collections.Mapping):
            dct[k] = dict_merge(dct[k], v, add_keys=add_keys)
        else:
            dct[k] = v

    return dct
