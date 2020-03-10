import os
import shutil
import json
import numpy as np
import soundfile as sf
import random
from scipy import signal
import yagmail
import librosa
import collections

def warning_print(s):
    print('\033[5;33m%s\033[0m' % str(s))

class PerformanceEvalHelper():
    def eer_clac(self, output, label):
        if type(output) == list:
            output = np.array(output)
            label = np.array(label)
        for i in range(-1000, 1000):
            label_copy = label.copy()
            output_copy = output.copy()

            threshold = i / 1000.0
            false_reject_count = label_copy[output_copy < threshold].sum()
            label_copy = label_copy * -1 + 1
            false_alarm_count = label_copy[output_copy >= threshold].sum()

            if false_reject_count >= false_alarm_count:
                return (false_reject_count + false_alarm_count)/output.shape[0]

class Params():
    def __init__(self, json_path):
        self.update(json_path)

    def update(self, json_path):
        with open(json_path) as f:
            params = json.load(f)
            self.__dict__.update(params)

    @property
    def dict(self):
        return self.__dict__

def read_config(config):
    params = Params(config)
    return params

def save_codes_and_config(config, model_dir):
    if os.path.isdir(os.path.join(model_dir, "nnet")):
        print("Save backup to %s" % os.path.join(model_dir, ".backup"))  # log
        if os.path.isdir(os.path.join(model_dir, ".backup")):
            print("The dir %s exisits. Delete it and continue." % os.path.join(model_dir, ".backup"))  # log
            shutil.rmtree(os.path.join(model_dir, ".backup"))  # 如果已有代码，那么删除
        os.makedirs(os.path.join(model_dir, ".backup"))
        # if os.path.exists(os.path.join(model_dir, "codes")):
        #     shutil.move(os.path.join(model_dir, "codes"), os.path.join(model_dir, ".backup/"))
        if os.path.exists(os.path.join(model_dir, "nnet")):
            shutil.move(os.path.join(model_dir, "nnet"), os.path.join(model_dir, ".backup/"))
        if os.path.exists(os.path.join(model_dir, "checkpoint")):
            shutil.move(os.path.join(model_dir, "checkpoint"), os.path.join(model_dir, ".backup/"))
        if os.path.exists(os.path.join(model_dir, "log")):
            shutil.move(os.path.join(model_dir, "log"), os.path.join(model_dir, ".backup/"))

    # if os.path.isdir(os.path.join(model_dir, "codes")):
    #     shutil.rmtree(os.path.join(model_dir, "codes"))
    # os.makedirs(os.path.join(model_dir, "codes"))
    os.makedirs(os.path.join(model_dir, "log"))
    os.makedirs(os.path.join(model_dir, "checkpoint"))

    if not os.path.isdir(os.path.join(model_dir, "nnet")):
        os.makedirs(os.path.join(model_dir, "nnet"))
    shutil.copyfile(config, os.path.join(model_dir, "nnet", "config.json"))
    print("Train the model from scratch.")
    params = Params(config)
    return params


class RIRUtil2:
    def __init__(self, rir_dir=None):
        rir_file_path = os.path.join(rir_dir, 'rir_list')
        if not os.path.exists(rir_file_path):
            raise RuntimeError('rir_list is not found!')
        self.rir_wav_file_paths = []
        with open(rir_file_path, mode='r', encoding='utf-8') as rir_file:
            for line in rir_file:
                line_list = line.replace('\n', '').split()
                filename = os.path.split(line_list[-1])[-1]
                file_path = os.path.join(rir_dir, filename)
                if os.path.exists(file_path):
                    self.rir_wav_file_paths.append(file_path)

    def __call__(self, wav_sig, rir_path=None):
        if rir_path is not None:
            rir, _ = sf.read(rir_path)
        else:
            if len(self.rir_wav_file_paths) == 0:
                raise RuntimeError('rir_dir and rir_path is None')
            rir_path_index = random.randint(0, len(self.rir_wav_file_paths)-1)
            rir_path = self.rir_wav_file_paths[rir_path_index]
            rir, _ = sf.read(rir_path)

        if len(rir.shape) == 2:
            rir_ch_index = random.randint(0, rir.shape[1]-1)
            rir = rir[:, rir_ch_index]
        rir_index = np.argmax(rir)  # or 0

        s_out = signal.fftconvolve(wav_sig, rir, mode='full')[
                rir_index:rir_index + wav_sig.size]
        return s_out

def calc_alpha(speech, noise, snr):
    alpha = np.sqrt(np.sum(speech ** 2.0) / (np.sum(noise ** 2.0) * (10.0 ** (snr / 10.0))))
    return alpha

def augment_sig(noise_dataset, rir_dataset, raw_data):
    random_seed = random.randrange(0, 100)
    if random_seed > 20 and random_seed < 85:
        snr = random.randint(0, 20)
        noise_data_max_index = len(noise_dataset) - 1
        noise_data_info = noise_dataset[random.randint(0, noise_data_max_index)]
        noise_data = noise_data_info[0]
        data_parts = noise_data.shape[0]
        data_len = noise_data.shape[1]
        n_0, n_1 = random.randint(0, data_parts - 1), random.randint(0, data_len - len(raw_data) - 1)
        n = noise_data[n_0:n_0 + 1, n_1:n_1 + len(raw_data)]
        noise = np.squeeze(n) + 1e-7
        assert len(noise) == len(raw_data)
        noisy_data = raw_data + noise * _calc_alpha(speech=raw_data, noise=noise, snr=snr)
        # snr = random.randint(0, 20)
        # noise_file = random.sample(noise_dataset, 1)
        # noise_raw, _ = sf.read(noise_file[0])
        # while len(noise_raw) < len(raw_data):
        #     noise_file = random.sample(noise_dataset, 1)
        #     noise_raw, _ = sf.read(noise_file[0])
        # max_idx = len(noise_raw) - len(raw_data)
        # idx = random.randint(0, max_idx)
        # noise = noise_raw[idx:idx + len(raw_data)]
        # assert len(noise) == len(raw_data)
        # noisy_data = raw_data + noise * _calc_alpha(speech=raw_data, noise=noise, snr=snr)
    elif random_seed > 0 and random_seed < 15:
        rir_file_list = random.sample(rir_dataset, 1)
        rir_file = rir_file_list[0]
        rir, _ = sf.read(rir_file)
        if len(rir.shape) == 2:
            rir_ch_index = random.randint(0, rir.shape[1] - 1)
            rir = rir[:, rir_ch_index]
        rir_index = np.argmax(rir)  # or 0
        noisy_data = signal.fftconvolve(raw_data, rir, mode='full')[rir_index:rir_index + raw_data.size]
    else:
        noisy_data = raw_data
    return noisy_data

def augment_sig_with_bg(bg_dataset, rir_dataset, raw_data):
    random_seed = random.randrange(0, 100)
    if random_seed > 10 and random_seed < 90:
        noise_data_max_index = len(bg_dataset) - 1
        bg_path, lowest_snr = bg_dataset[random.randint(0, noise_data_max_index)]
        snr = random.randint(lowest_snr, 20)
        n, _ = sf.read(bg_path)
        if n.shape[0] < raw_data.shape[0]:
            padding_n_size = raw_data.shape[0] - n.shape[0]
            n = np.concatenate((np.zeros(shape=padding_n_size, dtype=np.float32), n), 0)
        else:
            random_start_idx = random.randint(0, n.shape[0] - raw_data.shape[0])
            n = n[random_start_idx: random_start_idx + raw_data.shape[0]]
        noise = n + 1e-7
        assert len(noise) == len(raw_data)
        noisy_data = raw_data + noise * _calc_alpha(speech=raw_data, noise=noise, snr=snr)
    elif random_seed <= 10:
        rir_file_list = random.sample(rir_dataset, 1)
        rir_file = rir_file_list[0]
        rir, _ = sf.read(rir_file)
        if len(rir.shape) == 2:
            rir_ch_index = random.randint(0, rir.shape[1] - 1)
            rir = rir[:, rir_ch_index]
        rir_index = np.argmax(rir)  # or 0
        noisy_data = signal.fftconvolve(raw_data, rir, mode='full')[rir_index:rir_index + raw_data.size]
    else:
        noisy_data = raw_data
    return noisy_data

def padding_samples(sig, n_samples):
    if sig.shape[0] < n_samples:  # 如果sig的长度小于n_samples
        padding_size = n_samples - sig.shape[0]
        if sig.shape[0] == 0:
            print('This Signal is ERROR')
        repeat_time = (padding_size + sig.shape[0] - 1) // sig.shape[0]
        padding_sig = None
        for _ in range(repeat_time):
            if padding_sig is None:
                padding_sig = sig.copy()
            else:
                padding_sig = np.concatenate((padding_sig, sig), axis=0)
        sig = np.concatenate((padding_sig, sig), axis=0)
        sig = sig[-n_samples:]
    else:  # 如果sig的长度大于n_samples
        i = 0
        while True:
            start_idx = random.randint(0, sig.shape[0] - n_samples)
            sig = sig[start_idx:start_idx + n_samples]
            if np.abs(sig).sum() > 25:
                break
            i += 1
            if i > 10:
                break
    return sig

def padding_samples_with_zero(sig, n_samples):
    if sig.shape[0] < n_samples:  # 如果sig的长度小于n_samples
        padding_size = n_samples - sig.shape[0]
        if sig.shape[0] == 0:
            print('This Signal is ERROR')
        padding_sig = np.zeros(shape=[padding_size], dtype=sig.dtype)
        sig = np.concatenate((sig, padding_sig), 0)
    else:  # 如果sig的长度大于n_samples
        i = 0
        while True:
            start_idx = random.randint(0, sig.shape[0] - n_samples)
            sig = sig[start_idx:start_idx + n_samples]
            if np.abs(sig).sum() > 25:
                break
            i += 1
            if i > 10:
                break
    return sig

def reset_sr(sig, src_sr, dst_sr):
    sig = librosa.resample(sig, src_sr, dst_sr)
    return sig

def get_file_paths(work_dir, ext='.wav'):
    l = []
    for parent, dirnames, filenames in os.walk(work_dir,followlinks=True):
        for filename in filenames:
            if filename.lower().endswith(ext):
                l.append(os.path.join(parent, filename))
    return l