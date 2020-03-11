"""
Manipulate ciphers.
"""


class CipherTool:
    """
    Manipulate ciphers.
    """

    def __init__(self, _db_path=".synaw_cipher_db"):
        self.db_path = _db_path

    def populate(self):
        """
        Populate the list of ciphers.
        :return: None
        """
        print(self.db_path)
        print("Hello ciphers!")
