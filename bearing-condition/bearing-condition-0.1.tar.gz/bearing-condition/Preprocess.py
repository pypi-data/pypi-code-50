from scipy.io import wavfile
import librosa
import librosa.display
from enum import Enum
import tkinter as tk
from tkinter import filedialog


class FitType(Enum):
    MFCC = "MFCC"


class Preprocess:
    def __init__(self, fit_type: FitType = FitType.MFCC):
        self.fit_type = fit_type
        self.wav_path = ""
        self.num_of_mfcc = 13
        self.processed_data = None
        self.sample_rate = None
        self.wav_data = None

    def compute(self):
        if self.wav_path != "":
            if self.fit_type is FitType.MFCC:
                self.processed_data = librosa.feature.mfcc(y=self.wav_data, sr=self.sample_rate, n_mfcc=self.num_of_mfcc).T
        else:
            raise RuntimeError("Wav is invalid/empty !")

    def load_wav(self):
        root = tk.Tk()
        root.withdraw()
        file_type = [('Wav file', '*.wav'), ]
        file_path = filedialog.askopenfilename(filetypes=file_type)
        if file_path != "":
            self.wav_path = file_path
            self.sample_rate, self.wav_data = wavfile.read(self.wav_path)
        else:
            self.wav_path = ""
            self.processed_data = None
            self.sample_rate = None
            self.wav_data = None
