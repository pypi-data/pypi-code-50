from xml.etree import ElementTree as ET
from getopt import getopt
import copy
import os
import sys
from XmindToTestlink import read_xml
from XmindToTestlink import dict_to_xml

def get_dpath(in_dict, pre_path = ''):
    path_list = []
    for k in in_dict:
        l1_path = os.path.join(pre_path, k)
        if isinstance(in_dict[k], list):
            for n,v in enumerate(in_dict[k]):
                l2_path = os.path.join(l1_path, str(n))
                path_list.append(l2_path.strip("/"))
                if k != "cases":
                    path_list.extend(get_dpath(v, l2_path))
    return path_list

def get_delem(in_dict, dpath, key = ''):
    path = dpath.strip('/').split('/')
    msg = ''
    for i in path:
        if i.isdigit():
            msg += "["  + i + "]"
        else:
            msg += "[\'"  + i + "\']"
    if key != '':
        msg += "[\'"  + key + "\']"
    return eval("in_dict" + msg)

def get_suite_case_path_list(path_list):
    suite_path_list = []
    case_path_list = []
    for path in path_list:
        if path.find('cases') >= 0:
            case_path_list.append(path)
        else:
            suite_path_list.append(path)
    return suite_path_list,case_path_list

def get_path_title(in_dict, path_list):
    path_key = {}
    for dpath in path_list:
        path_key[dpath] = get_delem(in_dict, dpath, 'title')
    return path_key

def transfer_path(in_dict, dpath):
    path = dpath.strip('/').split('/')
    cnpath = ''
    msg = ''
    for i in path:
        if i.isdigit():
            msg += "["  + i + "]"
            cnpath += eval("in_dict" + msg)['title'] + "/"
        else:
            msg += "[\'"  + i + "\']"
    return cnpath
    #return '/'.join(cnpath.split('/')[:-2]) + "/"

def parse_path(out_dict, out_dpath, down_dict, down_dpath):
    common_path = {}
    new_suite_list = []
    new_case_list = []
    for out_path in out_dpath:
        common = 0
        for  down_path in down_dpath:
            if transfer_path(out_dict, out_path) == transfer_path(down_dict, down_path):
                common_path[out_path] = down_path
                common = 1
                break
        if not common:
            if out_path.find("cases") >= 0:
                new_case_list.append(out_path)
            else:
                new_suite_list.append(out_path)
    return common_path, new_suite_list, new_case_list

def add_common(common_path, out_dict, down_dict):
    for out_path, down_path in common_path.items():
        down_req = get_delem(down_dict, down_path)
        out_req = get_delem(out_dict, out_path)
        if 'custom_field' in out_req and len(out_req['custom_field']) > 0:
            for out_custom in out_req['custom_field']:
                find = 0
                for out_k, out_v in out_custom.items():
                    if 'custom_field' in down_req and len(down_req['custom_field']) > 0:
                        for down_custom in down_req['custom_field']:
                            for down_k, down_v in down_custom.items():
                                if down_k == out_k:
                                    down_custom[down_k] = down_v + "|" + out_v
                                    find = 1
                        if not find:
                            down_req['custom_field'].append({out_k, out_v})
                    else:
                        down_req['custom_field'] = [{out_k, out_v}]
    return down_dict

def clean_suite_case(path, in_list):
    out_list = []
    for p in in_list:
        if p.find(path) != 0:
            out_list.append(p)
    return out_list

def get_common_suite(path, common_path):
    common = ''
    msg = path.split("/")
    if len(msg) >= 2:
        son_path = "/".join(path.split("/")[:-2])
        if son_path in common_path:
            common =  common_path[son_path]
        else:
            common = get_common_suite(son_path, common_path)
    return common

def usage():
    '''
    Usage:
    * xmladd -d download_xml -o output_xml

    function:
        create new xml which include out_xml and download_xml's message
        at ./_xmind_output

    parameter:
        -h : help
        -d : download_xml from testlink
        -o : output_xml from xmindtotestlink
    '''
    print(usage.__doc__)

def main():
    opts, args = getopt(sys.argv[1:], "d:o:h")
    for k,v  in opts:
        if k == "-d":
            down_xml = v
        if k == "-o":
            out_xml = v
        if k == "-h":
            usage()
            sys.exit()

    output_dir = "_xmind_output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    #out_xml = "_xmind_output/file_req.xml"
    #down_xml = "save_xml/save_chip1.xml"
    out_dict = read_xml.read_req_xml(out_xml)
    down_dict = read_xml.read_req_xml(down_xml)
    
    out_dpath = get_dpath(out_dict)
    down_dpath = get_dpath(down_dict)
    common_path, new_suite_list, new_case_list = parse_path(out_dict, \
            out_dpath, down_dict, down_dpath)
    #公共部分添加属性
    down_dict = add_common(common_path, out_dict, down_dict)

    #添加新目录
    for i in new_suite_list:
        new_case_list = clean_suite_case(i, new_case_list)
        target_path = get_common_suite(i, common_path)
        if target_path == "":
            reqs = down_dict
        else:
            reqs = get_delem(down_dict, target_path)
        req = get_delem(out_dict, i)
        reqs["suites"].append(copy.deepcopy(req))

    #添加新子项
    for i in new_case_list:
        target_path = get_common_suite(i, common_path)
        reqs = get_delem(down_dict, target_path)
        req = get_delem(out_dict, i)
        reqs["cases"].append(copy.deepcopy(req))

    #创建xml
    req_dict = down_dict
    dx = dict_to_xml.DictToXml()
    req_out = ET.Element(dx.req_tag['root'])
    name = ''
    auto_id = 0 
    root_id = read_xml.get_root_id(down_xml)
    if name != '': 
        req_total = ET.SubElement(req_out, dx.req_tag['rqs'], attrib = \
            {"title" : name, "doc_id" : root_id})
    else:
        req_total = req_out
    dx.get_req_xml(req_dict, req_total, auto_id, root_id)
    w = ET.ElementTree(req_total) 
    #dx.indent(req_total) #debug xml
    xml_name = "new_" + os.path.basename(down_xml)
    xml_path = os.path.join(output_dir, xml_name)
    w.write(xml_path, 'utf-8', True)
    print("\ncreate success\noutput : " + xml_path)

if __name__ == "__main__":
    main()
