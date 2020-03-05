import pandas as pd
import requests
import os


class BIO465:
    """
    BIO 465 is a container object that gets content associated with
    the BIO465 course at Brigham Young University
    """

    def __init__(self):
        self.dataframes = []
        self.homeworks = []
        self.labs = []
        self.lab_links = {'bacterial growth': "https://byu.box.com/shared/static/b0gn4i6v4h9a4owilv8of5m6x5tj82u7.xlsx",
                          'rna seq': "https://byu.box.com/shared/static/k5mdefkiqkj4bm9umd8naiaq20p1tpkk.txt",
                          'cancer types': "https://byu.box.com/shared/static/u3czp6p3q76x2nh0x7rmiw8il2751ehk.txt"}
        # TODO make comments based on the markdown
        self.hints = {
            '1a': 'string of hints',
            '1b': 'string of hints',
            '1c': 'string of hints',
        }
        self.answer_links = {
            '1': 'link',
        }

    """Queries box to get whatever link is within the lab_links parameter"""
    def get_data_frame(self, lab_string: str, file_type: str):
        file = f'./file{file_type}'

        lab_link = self.lab_links[lab_string]
        response = requests.get(lab_link, allow_redirects=True, stream=True)  # query box to get the file
        with open(file, "wb") as xl_file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    xl_file.write(chunk)

        df = pd.read_excel(open(file, 'rb'))
        os.remove('./' + file)
        return df

    def get_lab(self, lab_string: str) -> pd.array:
        """
        :type lab_string: str
        """
        error_message = "Lab does not exist, returning empty pandas array."
        if not isinstance(lab_string, str):
            print(error_message)
            return pd.array([])
        lab_string = lab_string.lower()
        if lab_string not in self.lab_links.keys():
            print(error_message)
            return pd.array([])
        if lab_string == 'bacterial growth':
            file_type = ".xlsx"
            df = self.get_data_frame(lab_string, file_type)
            df = df.drop(columns=["Min_MSGF", "Peptides", "Ref1", "Ref2", "Ref3", "Ref4", "Spectra"])
            df = df.set_index(["Protein"])
            df = df.transpose()
            df = df.reset_index()
            temp_cols = df["index"].str.split('_', n=1, expand=True)
            plate_type = temp_cols[0]
            time_plate = temp_cols[1].str.split('.', n=1, expand=True)
            df = df.assign(Experimental_Condition=plate_type, Time_Point=time_plate[0], Replicate=time_plate[1])
            df = df.set_index(["Experimental_Condition", "Time_Point", "Replicate"])
            df = df.sort_index().transpose()
        if lab_string == 'rna seq':
            file_type = ".txt"
            df = self.get_data_frame(lab_string, file_type)
        if lab_string == 'cancer types':
            file_type = ".txt"
            df = self.get_data_frame(lab_string, file_type)
        return df

    def hint(self, lab_string, problem_number, sub_problem=''):
        hint_string = ""
        if lab_string == "bacterial growth":
            if problem_number:
                hint_string = ""
        if lab_string == "rna seq":
            pass #TODO insert code for getting a hint
        if lab_string == "rna seq":
            pass #TODO insert code for getting a hint
        print(hint_string)


if __name__ == "__main__":
    b = BIO465()
    df = b.get_lab("bacterial growth")
    print(df)
