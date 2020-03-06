from typing import Dict


def get_dict_stats(inp_dict: Dict) -> Dict:
    '''
    Function that counts lists in your dictionary (recursively)
    :param inp_dict:
    :return:
    '''
    out_dict = {}
    for key_ in inp_dict:
        if isinstance(inp_dict[key_], dict):
            out_dict[key_] = get_dict_stats(inp_dict[key_])
        else:
            out_dict[key_] = len(inp_dict[key_])
    return out_dict
