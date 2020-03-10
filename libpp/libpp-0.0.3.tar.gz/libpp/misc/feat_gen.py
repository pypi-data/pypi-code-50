import torch
import torch.nn as nn
import librosa
import numpy as np
from torch.autograd import Variable
import torch.nn.functional as F

class LogMelFeatGen(nn.Module):
    def __init__(self, n_fft=320, hop_len=160, mel_len=40, sample_rate=16000):
        super(LogMelFeatGen, self).__init__()
        self.n_fft = n_fft
        self.hop_len = hop_len
        self.hamming_window = torch.hamming_window(n_fft, periodic=True, dtype=None, layout=torch.strided, requires_grad=False).cuda()
        self.linear_to_mel_weigt_matrix = torch.from_numpy(
            librosa.filters.mel(sr=sample_rate, n_fft=n_fft, n_mels=mel_len, fmin=20, fmax=8000, htk=True, norm=None).T.astype(np.float32)).cuda()

    def forward(self, input):
        stft_out = torch.stft(input=input, n_fft=self.n_fft, hop_length=self.hop_len, win_length=self.n_fft,
                              window=self.hamming_window, center=False, onesided=True)
        stft_out = stft_out.permute(0, 2, 1, 3)

        a = stft_out[:, :, :, 0]   # real
        b = stft_out[:, :, :, 1]   # imag
        speech_abs = (a ** 2 + b ** 2).sqrt()  # magnitude
        abs_mel = torch.matmul(speech_abs, self.linear_to_mel_weigt_matrix)
        abs_mel = abs_mel + 1e-7
        log_mel = abs_mel.log()
        return log_mel


class MelFeatGen(nn.Module):
    def __init__(self, n_fft, hop_len, mel_len, sample_rate):
        super(MelFeatGen, self).__init__()
        self.n_fft = n_fft
        self.hop_len = hop_len
        self.hamming_window = torch.hamming_window(n_fft, periodic=True, dtype=None, layout=torch.strided, requires_grad=False).cuda()
        self.linear_to_mel_weigt_matrix = torch.from_numpy(
            librosa.filters.mel(sr=sample_rate, n_fft=n_fft, n_mels=mel_len, fmin=20, fmax=8000, htk=True, norm=None).T.astype(np.float32)).cuda()

    def forward(self, input):
        stft_out = torch.stft(input=input, n_fft=self.n_fft, hop_length=self.hop_len, win_length=self.n_fft,
                              window=self.hamming_window, center=False, onesided=True)
        stft_out = stft_out.permute(0, 2, 1, 3)

        a = stft_out[:, :, :, 0]   # real
        b = stft_out[:, :, :, 1]   # imag
        speech_abs = (a ** 2 + b ** 2).sqrt()  # magnitude
        abs_mel = torch.matmul(speech_abs, self.linear_to_mel_weigt_matrix)
        abs_mel = abs_mel + 1e-7
        return abs_mel


class FBankGen(nn.Module):
    def __init__(self, win_len, win_shift, mel_len, sample_rate):
        super(FBankGen, self).__init__()
        self.log_mel_gen = LogMelFeatGen(win_len, win_shift, mel_len, sample_rate)

    def forward(self, input):
        log_mel_feat = self.log_mel_gen(input)
        zeros = torch.zeros(log_mel_feat.size(0), 1, log_mel_feat.size(2)).float().cuda()
        log_mel_feat_diff_1 = log_mel_feat - torch.cat((zeros, log_mel_feat), 1)[:, :-1, :]
        log_mel_feat_diff_2 = log_mel_feat_diff_1 - torch.cat((zeros, log_mel_feat_diff_1), 1)[:, :-1, :]
        fbank_feat = torch.cat((log_mel_feat, log_mel_feat_diff_1, log_mel_feat_diff_2), -1)
        return fbank_feat


class LPS(nn.Module):
    def __init__(self, n_fft, hop_len):
        super(LPS, self).__init__()
        self.n_fft = n_fft
        self.hop_len = hop_len
        self.hamming_window = torch.hamming_window(n_fft, periodic=True, dtype=None, layout=torch.strided, requires_grad=False).cuda()

    def forward(self, input):
        stft_out = torch.stft(input=input, n_fft=self.n_fft, hop_length=self.hop_len, win_length=self.n_fft,
                              window=self.hamming_window, center=False, onesided=True)
        stft_out = stft_out.permute(0, 2, 1, 3)

        a = stft_out[:, :, :, 0]  # real
        b = stft_out[:, :, :, 1]  # imag
        stft_abs = a ** 2 + b ** 2  # 幅度谱
        lps = torch.log(stft_abs + 1e-8)
        return lps


class ABSFeatGen(nn.Module):
    def __init__(self, n_fft, hop_len):
        super(ABSFeatGen, self).__init__()
        self.n_fft = n_fft
        self.hop_len = hop_len
        self.hamming_window = torch.hamming_window(n_fft, periodic=True, dtype=None, layout=torch.strided,
                                                   requires_grad=False).cuda()

    def forward(self, input):
        stft_out = torch.stft(input=input, n_fft=self.n_fft, hop_length=self.hop_len, win_length=self.n_fft,
                              window=self.hamming_window, center=False, onesided=True)
        stft_out = stft_out.permute(0, 2, 1, 3)

        a = stft_out[:, :, :, 0]  # real
        b = stft_out[:, :, :, 1]  # imag
        stft_abs = (a ** 2 + b ** 2).sqrt()  # 幅度谱
        return stft_abs




class STFT(torch.nn.Module):
    def __init__(self, filter_length=1024, hop_length=512):
        super(STFT, self).__init__()

        self.filter_length = filter_length
        self.hop_length = hop_length
        self.forward_transform = None
        # scale = self.filter_length / self.hop_length
        # scale = 1
        fourier_basis = np.fft.fft(np.eye(self.filter_length))
        window = np.hamming(filter_length)
        fourier_basis = fourier_basis * window
        cutoff = int((self.filter_length / 2 + 1))
        fourier_basis = np.vstack([np.real(fourier_basis[:cutoff, :]),
                                   np.imag(fourier_basis[:cutoff, :])])
        forward_basis = torch.FloatTensor(fourier_basis[:, None, :])

        inv_fourier_basis = np.fft.fft(np.eye(self.filter_length))
        cutoff = int((self.filter_length / 2 + 1))
        inv_fourier_basis = np.vstack([np.real(inv_fourier_basis[:cutoff, :]),
                                       np.imag(inv_fourier_basis[:cutoff, :])])
        inverse_basis = torch.FloatTensor(np.linalg.pinv(inv_fourier_basis).T[:, None, :])
        window_tensor = torch.FloatTensor(window).reshape(1, 1, filter_length)
        inverse_basis = inverse_basis * window_tensor

        self.register_buffer('forward_basis', forward_basis.float())
        self.register_buffer('inverse_basis', inverse_basis.float())

    def transform(self, input_data):
        num_batches = input_data.size(0)
        num_samples = input_data.size(1)

        ##
        #
        input_data = input_data.view(num_batches, 1, num_samples)
        forward_transform = F.conv1d(input_data,
                                     Variable(self.forward_basis, requires_grad=False),
                                     stride=self.hop_length,
                                     padding=0)
        cutoff = int((self.filter_length / 2) + 1)
        real_part = forward_transform[:, :cutoff, :]
        imag_part = forward_transform[:, cutoff:, :]

        # magnitude = torch.sqrt(real_part ** 2 + imag_part ** 2)
        # phase = torch.autograd.Variable(torch.atan2(imag_part.data, real_part.data))
        res = torch.stack([real_part, imag_part], dim=-1)
        res = res.permute([0, 2, 1, 3])
        return res

    def inverse(self, stft_res):
        real_part = stft_res[:, :, :, 0].permute(0, 2, 1)
        imag_part = stft_res[:, :, :, 1].permute(0, 2, 1)
        recombine_magnitude_phase = torch.cat([real_part, imag_part], dim=1)
        # recombine_magnitude_phase = stft_res.permute([0, 2, 3, 1]).contiguous().view([1, -1, stft_res.size()[]])

        inverse_transform = F.conv_transpose1d(recombine_magnitude_phase,
                                               Variable(self.inverse_basis, requires_grad=False),
                                               stride=self.hop_length,
                                               padding=0)
        return inverse_transform[:, 0, :]

    def forward(self, input_data):
        stft_res = self.transform(input_data)
        reconstruction = self.inverse(stft_res)
        return reconstruction

class STFTFeatGen(nn.Module):
    def __init__(self, n_fft, hop_len):
        super(STFTFeatGen, self).__init__()
        self.n_fft = n_fft
        self.hop_len = hop_len
        self.hamming_window = torch.hamming_window(n_fft, periodic=True, dtype=None, layout=torch.strided,
                                                   requires_grad=False).cuda()

        self.stft = STFT(n_fft, hop_len)
    def forward(self, input):
        stft_out = torch.stft(input=input, n_fft=self.n_fft, hop_length=self.hop_len, win_length=self.n_fft,
                              window=self.hamming_window, center=False, onesided=True)
        stft_out = stft_out.permute(0, 2, 1, 3)

        real = stft_out[:, :, :, 0]  # real
        imag = stft_out[:, :, :, 1]  # imag
        stft_abs = (real ** 2 + imag ** 2).sqrt()  # 幅度谱
        return (real, imag), stft_abs

    def inverse(self, stft_res):
        return self.stft.inverse(stft_res)

    def transform(self, input_data):
        stft_out = torch.stft(input=input_data, n_fft=self.n_fft, hop_length=self.hop_len, win_length=self.n_fft,
                              window=self.hamming_window, center=False, onesided=True)
        stft_out = stft_out.permute(0, 2, 1, 3)
        return stft_out
