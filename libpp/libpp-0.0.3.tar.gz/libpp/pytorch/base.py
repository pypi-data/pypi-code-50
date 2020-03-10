import os, random, numpy as np
from scipy import signal
import soundfile as sf
import librosa
import collections
import torch
import torch.nn as nn
import torch.nn.functional as F
from  torch.utils.data import Dataset

class BaseTrainer():
    def warning_print(self, s):
        ''' 输出警告性的文本信息,用于输出需要特别注意的消息
        
        :param s:要输出文本信息，如果不是str类型的话，会自动转换成str类型后输出
        :return None
        '''
        print('\033[5;33m%s\033[0m' % str(s))

    def save_model(self, net, optim, step, loss, models_dir):
        ''' 保存模型网络参数信息，优化器参数信息到pickle文件

        :param net: 网络的实现部分
        :param optim: 优化器
        :param step: 训练的步数，也可传入epoch
        :param loss: loss值
        :param models_dir: 保存模型文件的文件夹
        :return 返回保存成功之后的pickle文件的路径
        '''
        if not os.path.exists(models_dir):
            os.mkdir(models_dir)
        torch.save({
            'step': step,
            'state_dict': net.state_dict(),
            'optimizer': optim.state_dict()},
            '{}/model-{}-{}.pickle'.format(models_dir, step, loss))
        self.warning_print('save model-{}-{} success'.format(step, loss))
        return '{}/model-{}-{}.pickle'.format(models_dir, step, loss)

    def resume_model(self, net, optim, models_dir, resume_model_name=''):
        ''' 恢复保存在模型（pickle文件）网络对象， 优化器对象中的可学习参数，兼容多卡方案下模型恢复

        :param net:网络的实现部分
        :param optim: 优化器，可以传入为None，即不恢复优化器参数
        :param models_dir: 保存pickle文件的目录
        :param resume_model_name: pickle目录文件需要指定恢复的模型文件的文件名，
                                  如果传入为None，或者不传入参数，则恢复目录下面
                                  最新的pickle文件。
        :return None
        :auther peng.hu
        '''
        self.warning_print('resuming model...')
        models = {}
        for f in os.listdir(models_dir):
            if os.path.splitext(f)[1] == '.pickle':
                f = '{}/{}'.format(models_dir, f)
                id = os.path.getctime(f)
                models[id] = f
        if len(models) < 1:
            self.warning_print('there is no models to resume')
            return
        if resume_model_name.endswith('.pickle'):
            resume_model_name = resume_model_name.replace('.pickle', '')
        if len(resume_model_name) > 0:
            model_name = '{}/{}.pickle'.format(models_dir, resume_model_name)
        else:
            index = sorted(models)[-1]
            model_name = models[index]
        model_dict = torch.load(model_name)

        # 单gpu模型与多gpu模型兼容方案
        # 如果模型采用了多gpu模型，则原有模型的子模块包含在module下面
        if 'DataParallel' in str(type(net)):
            # net 为多gpu类判断  模型的类型
            if not list(model_dict['state_dict'].keys())[0].startswith('module.'):
                # 保存的是单gpu类型的模型
                new_dict = collections.OrderedDict()
                for key in model_dict['state_dict'].keys():
                    new_dict['module.' + key] = model_dict['state_dict'][key]  # 验证通过
                net.load_state_dict(new_dict, strict=False)
            else:
                # if "module.fc.bias" not in model_dict['state_dict'].keys():
                #     fc_bias = torch.from_numpy(np.array([0])).cuda()
                #     fc_weight = torch.from_numpy(np.array([[0]])).cuda()
                #     model_dict['state_dict']['module.fc.bias'] = fc_bias
                #     model_dict['state_dict']['module.fc.weight'] = fc_weight
                net.load_state_dict(model_dict['state_dict'], strict=False)  # 验证通过
        else:
            # net 是 单gpu类型的
            if list(model_dict['state_dict'].keys())[0].startswith('module.'):
                # 保存的模型是多gpu的
                # 处理的过程较为繁琐
                new_dict = collections.OrderedDict()
                for key in model_dict['state_dict'].keys():
                    new_dict[key.replace('module.', '')] = model_dict['state_dict'][key]
                net.load_state_dict(new_dict, strict=False)
            else:
                net.load_state_dict(model_dict['state_dict'], strict=False)  # 验证通过
        try:
            step = model_dict['step']
        except:
            step = 0
        optim_state = model_dict['optimizer']
        if optim is not None:
            optim.load_state_dict(optim_state)
            pass
        self.warning_print('finish to resume model {}'.format(model_name))
        return step

class BaseDataset(Dataset):
    def get_file_paths(self, work_dir, ext='.wav'):
        '''' 递归读取某一个目录下的某一个扩展名的文件，并返回所有符合条件的文件路径列表

        :param work_dir: 需要递归遍历的目录路径
        :param ext: 扩展名，默认为.wav
        :return 遍历出来的文件路径列表
        '''
        l = []
        for parent, dirnames, filenames in os.walk(work_dir,followlinks=True):
            for filename in filenames:
                if filename.lower().endswith(ext):
                    l.append(os.path.join(parent, filename))
        return l
    
    def pad_or_slice_sig(self, sig, n_samples, padding_type='normal'):
        ''' 为了获取定长的语音, 默认为normal格式，其他格式尚未实现
            若传入的语音长度大于n_sample的大小，则取最后n_sample个采样点,
            若传入的语音长度小于n_sample的大小，则在前方补零
        :param sig: 传入的语音信号，应为np.float32 array格式
        :n_samples: 采样点的个数
        :padding_type: padding的格式
                       normal: 若传入的语音长度大于n_sample的大小，则取最后n_sample个采样点,
                               若传入的语音长度小于n_sample的大小，则在前方补零
        :return 补全或者截断之后的语音
        '''
        if sig.shape[0] < n_samples:
            zeros = np.zeros(shape=n_samples-sig.shape[0], dtype=sig.dtype)
            sig = np.concatenate([zeros, sig], axis=0)
        else:
            start_idx = random.randint(0, sig.shape[0]-n_samples)
            sig = sig[start_idx: start_idx+n_samples]
        return sig

    def calc_alpha(self, speech, noise, snr):
        ''' 计算信噪比，一般是noise以一定的信噪比加在speech上面，
            这个方法是计算noise加在语音上面的比例，一般为其他方法
            内部调用

            :param speech: 语音信息，一般是纯净语音 
            :param noise: 噪音信息
            :return 噪音的比例，为float格式
        '''
        alpha = np.sqrt(np.sum(speech ** 2.0) / (np.sum(noise ** 2.0) * (10.0 ** (snr / 10.0))))
        return alpha

    def aug_sigv2(self, speech, bg_dataset, noise_dataset, snr_list=[i for i in range(0, 20)]):
        ''' v2版本只有加噪，没有加混响。
            加噪是加bg speech和noise的混合体
            bg和noise以[0-5]dB的比例相互混，作为最后的噪音
            再从snr_list里面选择一个snr，把混出来的噪音再以这个信噪比
            加到speech语音上面

        :param speech: np.array格式的语音
        :param bg_dataset: 背景人声文件的文件路径列表
        :noise_dataset: 背景噪音文件的文件路径列表
        :snr_list: 候选的SNR的列表
        :return 增强之后的语音信号
        '''
        datasets = [bg_dataset, noise_dataset]
        sigs = []
        for dataset in datasets:
            sum_sig = None
            if dataset is not None and len(dataset) > 0:
                while True:
                    wav_path = random.choice(dataset)
                    sig, sr = sf.read(wav_path)
                    if len(sig.shape) == 2:
                        rnd_ch = random.randrange(0, sig.shape[1])
                        sig = sig[:, rnd_ch]
                    if sr != 16000:
                        sig = librosa.resample(sig, sr, 16000)
                    if sum_sig is None:
                        sum_sig = sig
                    else:
                        sum_sig = np.concatenate((sum_sig, sig), 0)
                    if sum_sig.shape[0] >= speech.shape[0]:
                        break
                start_idx = random.randint(0, (sum_sig.shape[0]-speech.shape[0]))
                sum_sig = sum_sig[start_idx:start_idx+speech.shape[0]]
            sigs.append(sum_sig)
        bg_sig, noise_sig = sigs
        if bg_sig is not None and noise_sig is not None:
            if random.randint(0, 1) == 0:
                alpha = self.calc_alpha(bg_sig, noise_sig, random.randint(0, 20))
                mix_sig = bg_sig + alpha * noise_sig
            else:
                alpha = self.calc_alpha(noise_sig, bg_sig, random.randint(0, 20))
                mix_sig = noise_sig + alpha * bg_sig
            snr = random.choice(snr_list)
            alpha = self.calc_alpha(speech, mix_sig, snr)
            noisy_data = speech + alpha * mix_sig
        elif bg_sig is not None:
            snr = random.choice(snr_list)
            alpha = self.calc_alpha(speech, bg_sig, snr)
            noisy_data = speech + alpha * bg_sig
        elif noise_sig is not None:
            snr = random.choice(snr_list)
            alpha = self.calc_alpha(speech, noise_sig, snr)
            noisy_data = speech + alpha * noise_sig
        return noisy_data
    

    def get_noise(self, raw_data, noise_file_list, sample_rate=16000):
        '''     
                数据增强里面的加噪方法
                增强数据调用的噪声数据
                :param raw_data:
                :return:
                '''
        sum_n = None
        while True:
            noise_file_path = random.choice(noise_file_list)
            sig, sr = sf.read(noise_file_path)
            if len(sig.shape) != 1:
                ch = random.randint(0, sig.shape[1] - 1)
                sig = sig[:, ch]
            if sr != sample_rate:
                sig = librosa.resample(sig, sr, sample_rate)
            if sum_n is None:
                sum_n = sig
            else:
                sum_n = np.concatenate((sum_n, sig), 0)
            if sum_n.shape[0] >= raw_data.shape[0]:
                break
        max_idx = len(sum_n) - len(raw_data)
        idx = random.randint(0, max_idx)
        noise = sum_n[idx:idx + len(raw_data)]
        assert len(noise) == len(raw_data)

        return noise

    def add_noise(self, raw_data, noise_file_list, snr_list, sample_rate=16000):
        '''
        加噪方法，对raw_data进行加噪操作
        :param raw_data: 输入的原始数据
        :noise_file_list: 噪音文件，目前只兼容wav格式16位噪音文件，推荐采用musan噪音集
        :snr_list: 可以用snr列表,会从这个列表中选择一个snr进行加载操作
        :return: 加噪之后的数据
        '''
        noise = self.get_noise(raw_data, noise_file_list, sample_rate=sample_rate)
        assert len(noise) == len(raw_data)

        snr = random.choice(snr_list)
        noisy_data = raw_data + noise * self.calc_alpha(speech=raw_data, noise=noise, snr=snr)
        return noisy_data

    def add_rir(self, raw_data, rir_file_list):
        ''' 加混响方法，对raw_data进行加混响操作
        
        :param raw_data: 待加混响的数据
        :param rir_file_list： 混响文件，目前只兼容wav格式的混响文件，
                               推荐采用RIRNOISE数据集里面的混响部分
        :return: 加完混响之后的语音文件
        '''
        rir_file = random.choice(rir_file_list)
        rir, _ = sf.read(rir_file)
        if len(rir.shape) == 2:
            rir_ch_index = random.randint(0, rir.shape[1] - 1)
            rir = rir[:, rir_ch_index]
        rir_index = np.argmax(rir)  # or 0
        noisy_data = signal.fftconvolve(raw_data, rir, mode='full')[rir_index:rir_index + raw_data.size]
        return noisy_data

    def aug_sigv1(self, raw_data, noise_dataset, rir_dataset, snr_list):
        '''
        数据集增强方法
        但是目前的固定各个加噪方式出现的概率，
        应该需要自己继承了这个基类之后，重写这个方法，
        调用self.add_noise, self.add_rir这两个方法自己实现
        下面实现的只是一个样例
        :param raw_data: 输入数据
        :return: 增强之后的数据
        '''
        random_seed = random.randrange(0, 100)
        if random_seed >= 40 and random_seed < 80:
            # 加噪
            noisy_data = self.add_noise(raw_data, noise_dataset, snr_list)
        elif random_seed < 40 and random_seed >= 20:
            # 先加噪再加混响
            noisy_data = self.add_noise(raw_data, noise_dataset, snr_list)
            noisy_data = self.add_rir(noisy_data, rir_dataset)
        elif random_seed >= 0 and random_seed < 20:
            # 加混响
            noisy_data = self.add_rir(raw_data, rir_dataset)
        else:
            # 啥也不加
            noisy_data = raw_data
        return noisy_data
    
    def read_wav(self, wav_file_path, dest_sr=16000):
        sig, sr = sf.read(wav_file_path)
        if len(sig.shape) == 2:
            rnd_ch_idx = random.randrange(0, sig.shape[1])
            sig = sig[:, rnd_ch_idx]
        if sr != dest_sr:
            sig = librosa.resample(sig, sr, dest_sr)
        return sig