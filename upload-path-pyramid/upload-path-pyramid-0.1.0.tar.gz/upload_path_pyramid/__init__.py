import os
import shutil
import uuid
import typing as t


def get_upload_path(_file: t.Any, _path: str, _extension: str) -> str:
    """Return uploaded file path."""

    input_file = _file.file
    file_path = os.path.join(f"{_path}", f"{uuid.uuid4()}.{_extension}")
    temp_file_path = file_path + "~"
    input_file.seek(0)
    with open(temp_file_path, "wb") as output_file:
        shutil.copyfileobj(input_file, output_file)
    os.rename(temp_file_path, file_path)
    os.remove(temp_file_path)

    return file_path
