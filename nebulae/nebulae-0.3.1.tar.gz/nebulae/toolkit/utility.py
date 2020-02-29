#!/usr/bin/env python
'''
utility
Created by Seria at 14/11/2018 8:33 PM
Email: zzqsummerai@yeah.net

                    _ooOoo_
                  o888888888o
                 o88`_ . _`88o
                 (|  0   0  |)
                 O \   。   / O
              _____/`-----‘\_____
            .’   \||  _ _  ||/   `.
            |  _ |||   |   ||| _  |
            |  |  \\       //  |  |
            |  |    \-----/    |  |
             \ .\ ___/- -\___ /. /
         ,--- /   ___\<|>/___   \ ---,
         | |:    \    \ /    /    :| |
         `\--\_    -. ___ .-    _/--/‘
   ===========  \__  NOBUG  __/  ===========
   
'''
# -*- coding:utf-8 -*-

import json
import numpy as np
import subprocess as subp
import h5py
import os
from math import ceil
from copy import deepcopy
from ..law import Law


class _ImperativeSymbol(object):
    def __init__(self):
        self.operands_counter = {'+': 0, '-': 0, '*': 0, '@': 0, '&': 0}
        self.tensors_out = {}
        self.tensors_in = {}

    def enroll(self, name, shape):
        self.tensors_out[name] = list(shape)
        self.tensors_in[name] = list(shape)

    def __walk(self, info, in_shape):
        out_shape = in_shape
        stride = info['stride']
        kernel = info['kernel']
        dim = len(kernel)
        if info['cmajor']:
            offset = 0
            if 'out_chs' in info:
                out_shape[1] = info['out_chs']
            size = in_shape[-dim:]
        else:
            offset = 1
            if 'out_chs' in info:
                out_shape[-1] = info['out_chs']
            size = in_shape[-dim - offset:-offset]
        if info['auto_pad']:
            for d in range(dim):
                out_shape[d + (2 - offset)] = ceil(size[d] / stride[d])
        else:
            for d in range(dim):
                out_shape[d + (2 - offset)] = (size[d] - kernel[d]) // stride[d] + 1
        return out_shape

    def _infer(self, name, info):
        in_shape = deepcopy(self.tensors_out[name])
        # convolution (include 1d, 2d, 3d)
        if info['type'] == 'CONV':
            out_shape = self.__walk(info, in_shape)
        # pooling (include max- and avg-)
        elif info['type'] == 'POOL':
            kernel = info['kernel']
            dim = len(kernel)
            if info['if_global']:
                out_shape = in_shape
                if info['cmajor']:
                    out_shape[2:] = dim * [1]
                else:
                    out_shape[1:-1] = dim * [1]
            else:
                out_shape = self.__walk(info, in_shape)
        elif info['type'] in ['RESHAPE', 'OTS']:
            out_shape = info['shape']
        elif info['type'] == 'FLAT':
            out_shape = [in_shape[0], 0]
            product = 1
            for d in range(1, len(in_shape)):
                product *= in_shape[d]
            out_shape[-1] = product
        elif info['type'] == 'DENSE':
            out_shape = in_shape
            out_shape[info['axis']] = info['out_chs']
        elif info['type'] in ('LOSS', 'OPTZ', 'ACC'):
            out_shape = [1]
        else:
            out_shape = in_shape
        return out_shape

    def infer(self, component, assemblage=None, sub_scope=''):
        symbol = component.symbol
        message = component.message
        info = component.info
        if sub_scope:
            sub_prefix = sub_scope + '/'
        else:
            sub_prefix = sub_scope
        if symbol == '>':
            for comp in component.component:
                assemblage = self.infer(comp, assemblage=assemblage, sub_scope=sub_scope)
            return assemblage
        elif symbol in ['+', '-', '*', '@', '&']:
            operator = None
            self.operands_counter[symbol] += 1
            # TODO: if a pod is expanded to more than two comps, assemblage_name needs modification
            assemblage_name = component.name + '_' + str(self.operands_counter[symbol])
            init_assemblage = assemblage
            for comp in component.component:
                assemblage = self.infer(comp, assemblage=init_assemblage, sub_scope=sub_scope)
                if operator is None:
                    operator = self.tensors_out[assemblage]
                else:
                    if symbol == '&':
                        dim = self.tensors_out[assemblage][-1]
                        operator[-1] += dim
                    elif symbol == '@':
                        dim = self.tensors_out[assemblage][-1]
                        operator[-1] = dim
                    else:
                        pass
            asmb_full_name = sub_prefix + assemblage_name
            self.tensors_out[asmb_full_name] = operator
            component.info['full_name'] = asmb_full_name
            return asmb_full_name
        else: # this is an atomic component
            node_name = sub_prefix + component.name
            component.info['full_name'] = node_name
            if node_name in self.tensors_out.keys():  # Reuse or Redefine an existent node
                return node_name
            if assemblage is None:
                if symbol[0] == 'penalty':
                    self.tensors_out[node_name] = [1]
                else:
                    self.tensors_in[node_name] = self.tensors_out[message[0]]
                    self.tensors_out[node_name] = self._infer(message[0], info)
            else:
                if symbol[0] == 'penalty':
                    self.tensors_out[node_name] = [1]
                else: # message includes input at least
                    self.tensors_in[node_name] = self.tensors_out[assemblage]
                    self.tensors_out[node_name] = self._infer(assemblage, info)
            return node_name


def toDenseLabel(labels, nclasses, on_value=1, off_value=0):
    batch_size = labels.shape[0]
    # initialize dense labels
    dense = off_value * np.ones((batch_size * nclasses))
    indices = []
    if isinstance(labels[0], str):
        for b in range(batch_size):
            indices += [int(s) + b * nclasses for s in labels[b].split(Law.CHAR_SEP)]
    else: # labels is a nested array
        for b in range(batch_size):
            indices += [l + b * nclasses for l in labels[b]]
        dense[indices] = on_value
    return np.reshape(dense, (batch_size, nclasses))


def getAvailabelGPU(ngpus, least_mem):
    p = subp.Popen('nvidia-smi', stdout=subp.PIPE)
    gpu_id = 0  # next gpu we are about to probe
    flag_gpu = False
    id_mem = []  # gpu having avialable memory greater than least requirement
    for l in p.stdout.readlines():
        line = l.decode('utf-8').split()
        if len(line) < 1:
            break
        elif len(line) < 2:
            continue
        if line[1] == str(gpu_id):
            flag_gpu = True
            continue
        if flag_gpu:
            vacancy = int(line[10].split('M')[0]) - int(line[8].split('M')[0])
            if vacancy > least_mem:
                if len(id_mem) < ngpus:
                    id_mem.append((gpu_id, vacancy)) # (id, mem) of gpu
                else:
                    id_mem.sort(key=lambda x: x[1])
                    if vacancy > id_mem[0][0]:
                        id_mem[0] = (gpu_id, vacancy)
            gpu_id += 1
            flag_gpu = False
    return [elem[0] for elem in id_mem]

def parseConfig(config_path):
    with open(config_path, 'r') as config_file:
        return json.load(config_file)

def recordConfig(config_path, config):
    while os.path.exists(config_path):
        config_path = config_path[:-5]+'_.json'
    with open(config_path, 'w') as config_file:
        json.dump(config, config_file, indent=4)

def _mergeFuel(src_dir, src, dst, dtype, keep_src=True):
    data = {}
    info_keys = []
    shards = len(src)
    print('+' + (23 + 2 * shards + len(dst)) * '-' + '+')
    # read
    ending_char = '\r'
    for i, f in enumerate(src):
        hdf5 = h5py.File(os.path.join(src_dir, f), 'r')
        if i == 0:
            for key in hdf5.keys():
                info_keys.append(key)
            for key in info_keys:
                if key == Law.FRAME_KEY:
                    data[key] = 0
                else:
                    data[key] = []
        for key in info_keys:
            if key == Law.FRAME_KEY:
                frames = hdf5[key]
                data[key] = frames if frames>data[key] else data[key]
            else:
                data[key].extend(hdf5[key][()].tolist())
        hdf5.close()
        if not keep_src:
            os.remove(os.path.join(src_dir, f))

        progress = i+1
        yellow_bar = progress * '❖-'
        space_bar = (shards - progress) * '◇-'
        if progress == shards:
            ending_char = '\n'
        print('| Merging data  \033[1;35m%s\033[0m  ⊰⟦-%s%s⟧⊱ |'
              % (dst, yellow_bar, space_bar), end=ending_char)
    # write
    hdf5 = h5py.File(os.path.join(src_dir, dst), 'w')
    for key in info_keys:
        if dtype[key].startswith('v'):  # dealing with encoded / varied data
            dt = h5py.special_dtype(vlen=dtype[key])
            hdf5.create_dataset(key, dtype=dt, data=np.array(data[key]))
        elif key == Law.FRAME_KEY:
            hdf5[key] = data[key]
        else:
            hdf5[key] = np.array(data[key]).astype(dtype[key])
    hdf5.close()
    print('+' + (23 + 2 * shards + len(dst)) * '-' + '+')

def _fillFuel(src, key, data):
    hdf5 = h5py.File(src, 'a')
    hdf5[key] = data
    hdf5.close()

def _deductFuel(src, key):
    hdf5 = h5py.File(src, 'a')
    del hdf5[key]
    hdf5.close()