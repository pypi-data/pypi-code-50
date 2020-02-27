from __future__ import print_function
from collections import defaultdict
from itertools import chain
from operator import itemgetter
from sys import stderr
from os import path, walk
import fnmatch

import json

from .batl_config import BATL_CONFIG, FILE_SPEC as FS, TYPE_LOOKUP as TL
from .models import ProtocolPurpose

DIR_PATH = path.dirname(path.realpath(__file__))
METADATA_PATH = path.join(DIR_PATH, 'metadata.json')
FILES_PATH = path.join(DIR_PATH, 'files.txt')

def parse_names(datadir, suffix, extension='.h5'):
    globstring = '{0}_{1}_{0}_{2}_{1}'.format('[0-9]'*3, '[0-9]'*2, '[0-9]')
    def split(filename):
        datapath = path.relpath(filename, datadir)
        datapath, extension = path.splitext(datapath)
        basename = path.basename(datapath)
        fields = basename.split("_")
        return tuple(int(f) for f in fields), datapath
    def recursive_glob(datadir, globstring):
        for root, dirnames, filenames in walk(datadir):
            for filename in fnmatch.filter(filenames, globstring):
                yield path.join(root,filename)
    data = (split(f) for f in recursive_glob(path.join(datadir, suffix), '{}{}'.format(globstring, extension)))
    return {d[0]:{'path':d[1]} for d in data}

def link_data(video_list, rppg_list):
    for basename, data in rppg_list.items():
        if video_list.get(basename) is not None:
            video_list[basename]['rppg_path']=data['path']
        else:
            print("WARNING: no video file found for {}".format(data['path']), file=stderr)
    for basename, data in video_list.items():
        if basename[FS['type_id']] == TL['Bona Fide'] and data.get('rppg_path') is None:
            print("WARNING: no rppg file found for {}".format(data['path']), file=stderr)
    return video_list

def split_by(file_list, field):
    splitted_list = defaultdict(list)
    for data, paths in file_list.items():
        splitted_list[data[FS[field]]]\
                .append(tuple(list(data)+[paths['path'], paths.get('rppg_path', '')]))
    return splitted_list

def make_bag(file_list):
    folded_bag = defaultdict(list)
    bag = defaultdict(int)
    for key, files in file_list.items():
        folded_bag[len(files)].append((key, files))
        bag[key] += len(files)
    return list(bag.items()), list(folded_bag.items())

def find_partitions(bag, npart, selector=None):
    partitions = [[list(), int()] for _ in range(npart)]
    selector = selector if selector is not None else lambda p, b: min(p, key=itemgetter(1))
    for n, clients in sorted(bag, key=itemgetter(0), reverse=True):
        for client in clients:
            dataset = selector(partitions, client)
            dataset[0].append(client)
            dataset[1] += n
    return partitions

def make_baseline_metadata(field, partitions, partition_names):
    assert(len(partitions) == len(partition_names))
    metadata = dict(field=field)
    for partition, partition_name in zip(partitions, partition_names):
        values, _ = zip(*partition[0])
        metadata[partition_name] = values
    return metadata

def make_protocol_metadata(field, partitions, partition_names, exclude=None):
    assert(len(partitions) == len(partition_names))
    metadata = dict(field=field)
    exclude = exclude if exclude is not None else {}
    metadata['exclude'] = exclude
    for partition, partition_name in zip(partitions, partition_names):
        values, _ = zip(*partition[0])
        metadata[partition_name] = values
    return metadata

def main():
    from argparse import ArgumentParser
    
    def parse_arguments():
        parser = ArgumentParser(description=__doc__)
        parser.add_argument('-d', '--datadir', metavar='DIR',
                            default='/idiap/project/batl/datasets/database-batl-idiap',
                            help="Change the relative path to the directory containing the images of the batl database.")
        parser.add_argument('-V', '--video-suffix', metavar='DIR', default='face-station',
                            help="suffix to the dir for video files")
        parser.add_argument('-r', '--rppg-suffix', metavar='DIR', default='ppg',
                            help="suffix to the dir for rppg files")
        parser.add_argument('-v', '--verbose', action='count', default=0, help="Do SQL operations in a verbose way?")

        return parser.parse_args()

    def optimize_by_attack(partitions, client):
        sorted_partitions = sorted(partitions, key=itemgetter(1))
        for dataset in sorted_partitions:
            files = []
            for d in dataset[0]:
                files += d[1]
            dataset_attacks = set(f[FS['type_id']] for f in files)
            client_attacks = set(f[FS['type_id']] for f  in client[1])
            for attack in client_attacks:
                if attack not in dataset_attacks:
                    return dataset
        return sorted_partitions[0]

    args = parse_arguments()

    video_list = parse_names(args.datadir, args.video_suffix, extension='.h5')
    rppg_list = parse_names(args.datadir, args.rppg_suffix, extension='.txt')
    
    video_list = link_data(video_list, rppg_list)
    client_indexed_list = split_by(video_list, "client_id")
    bag, folded_bag = make_bag(client_indexed_list)
    partitions = find_partitions(folded_bag, 3, optimize_by_attack)
    consolidated_file_list = list(chain.from_iterable(client_indexed_list.values()))
    baseline_metadata = make_protocol_metadata('client_id', partitions, ProtocolPurpose.GROUPS)
    exclude_wig = [(('type_id', TL['Facial disguise']),
                    ('pai_id', [key 
                                for key, value in BATL_CONFIG[TL['Facial disguise']]['pai'].items()
                                if 'Wig' in value]))]
    nowig_metadata = make_protocol_metadata('client_id', partitions, ProtocolPurpose.GROUPS,
        exclude_wig)
    output = dict(files=consolidated_file_list,
                  protocols=dict(baseline=baseline_metadata,
                                 nowig=nowig_metadata))
    with open(METADATA_PATH, 'w') as of:
        json.dump(output, of, indent=4, sort_keys=True)
    with open(FILES_PATH, 'w') as f:
        f.write('db.sql3\nmetadata.json')

    if args.verbose > 0:
        for data, paths in video_list.items():
            pai_type_id = data[FS["type_id"]]
            pai_id = data[FS["pai_id"]]
            pai_type = BATL_CONFIG[pai_type_id]
            name = pai_type['name']
            pai = pai_type['pai'].get(pai_id)
            if pai is None:
                pai = ""
                print("WARNING: no definition found for pai id {}".format(pai_id), file=stderr)
            print ("file {} with client {}, presenter {}, session {}, type {}, pai {}"\
                   .format(paths['path'], data[FS["client_id"]],
                           data[FS["presenter_id"]], data[FS["session_id"]],
                           name, pai))
            rppg_path = paths.get('rppg_path') 
            if rppg_path is not None:
                print("\twith rppg_file {}".format(rppg_path))
        total_count = 0
        for (_, count) in bag:
            total_count += count
        max_client = max(bag, key=itemgetter(1))
        min_client = min(bag, key=itemgetter(1))
        print("total occurences : {}".format(total_count))
        print("max client {} with {} occurences".format(*max_client))
        print("min client {} with {} occurences".format(*min_client))
        partition_bag, counts = zip(*partitions)
        print("train : {} occurences, validation : {} occurences, test : {} occurences".format(*counts))
    if args.verbose > 1:
        from matplotlib import pyplot as plt
        plt.figure(1)
        clients, counts = zip(*bag)
        h = plt.bar(range(len(clients)), counts, align='center', label=clients)
        plt.subplots_adjust(bottom=0.3)
        xticks_pos = [0.65*patch.get_width() + patch.get_xy()[0] for patch in h]
        plt.xticks(xticks_pos , clients, ha='right', rotation=45 )
        plt.show()
        fig, axes = plt.subplots(len(partitions), 1)
        for ax, partition in zip(axes, partitions):
            clients, files = zip(*partition[0])
            counts = [len(f) for f in files]
            h = ax.bar(range(len(clients)), counts, align='center', label=clients)
            xticks_pos = [0.65*patch.get_width() + patch.get_xy()[0] for patch in h]
            ax.set_xticks(xticks_pos)
            ax.set_xticklabels(clients, ha='right', rotation=45)
        plt.show()

if __name__ == "__main__":
    main()
