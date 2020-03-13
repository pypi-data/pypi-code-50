import os
import json
import shutil


class ParkingDataset:

    def __init__(self, dir):
        self.add_allowed = True
        if not dir or not os.path.exists(dir):
            self.add_allowed = False
            return
            # raise Exception(f'Dir {dir} doesnt exists')
        self.src = os.path.join(dir, 'src')
        os.makedirs(self.src, exist_ok=True)


    def add_src_entry(self, job_id, regions_map, detections_map, img_src_file):
        if not self.add_allowed:
            return None, None
        jdir = os.path.join(self.src, self._version_base_dir(job_id, regions_map))
        dnamp_file = os.path.join(jdir, os.path.splitext(os.path.basename(img_src_file))[0] + '.json')
        im_file =  os.path.join(jdir, os.path.basename(img_src_file))
        with open(dnamp_file, mode='w') as fp:
            json.dump(detections_map, fp=fp, indent=4, sort_keys=True)
        shutil.copy2(img_src_file, im_file)
        return dnamp_file, im_file

    def _version_base_dir(self, job_id, regions_map):
        base_jid = self._single_version_check(job_id, regions_map)
        if base_jid:
            return base_jid
        for x in range(100000):
            base_jid = f'{job_id}-{x}'
            if self._single_version_check(base_jid, regions_map):
                return base_jid
        raise Exception('Not possible create or detect version of entry in {} for {}'.format(self.src, job_id))


    def _single_version_check(self, base_jid, regions_map):
        rmap_file = os.path.join(self.src, base_jid+'.json')
        if not os.path.exists(rmap_file):
            with open(rmap_file, mode='w') as fp:
                json.dump(regions_map, fp=fp, indent=4, sort_keys=True)
            os.makedirs(os.path.join(self.src, base_jid), exist_ok=True)
            return base_jid
        else:
            # compare
            regions_map_existing = None
            with open(rmap_file, mode='r') as fp:
                regions_map_existing = json.load(fp)
            if json.dumps(regions_map_existing, indent=4, sort_keys=True) == \
                    json.dumps(regions_map,indent=4, sort_keys=True):
                return base_jid
        return None