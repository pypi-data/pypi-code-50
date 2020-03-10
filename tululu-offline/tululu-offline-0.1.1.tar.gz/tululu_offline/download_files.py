import os
from typing import Optional

import requests
from pathvalidate import sanitize_filename  # type: ignore


def download_txt(
    url: str, filename: str, dest_folder: str, folder='books',
) -> Optional[str]:
    """Downloads a book in text format."""
    response = requests.get(url, allow_redirects=False)
    response.raise_for_status()
    books_folder_path = os.path.join(dest_folder, folder)
    os.makedirs(books_folder_path, exist_ok=True)
    if 'text/plain' in response.headers['Content-Type']:
        normalized_filename = sanitize_filename(filename)
        book_path = os.path.join(
            books_folder_path,
            f'{normalized_filename}.txt',
        )

        with open(book_path, 'w') as file_object:
            file_object.write(response.text)
        return book_path
    return None


def download_image(
    url: str, filename: str, dest_folder: str, folder='images',
) -> str:
    """Downloads image of book."""
    response = requests.get(url, allow_redirects=False)
    response.raise_for_status()
    image_folder_path = os.path.join(dest_folder, folder)
    os.makedirs(image_folder_path, exist_ok=True)
    normalized_filename = sanitize_filename(filename)
    path_to_image = os.path.join(
        image_folder_path,
        normalized_filename,
    )
    with open(path_to_image, 'wb') as file_object:
        file_object.write(response.content)
    return path_to_image
