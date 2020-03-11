from __future__ import unicode_literals
import zipfile
import os
import codecs
import json
import argparse
from XmindToTestlink import markdown_to_dict
from XmindToTestlink import dict_to_json
from XmindToTestlink import zip_need
#import markdown_to_dict
#import dict_to_json
#import zip_need


def md_to_xmind():
    output_zip = "_xmind_output/zip_need"
    output_dir = "_xmind_output"
    if not os.path.exists(output_zip):
        os.makedirs(output_zip)

    parser = argparse.ArgumentParser(description = "") 
    parser.add_argument('-f', '--file', dest='file', metavar='File', nargs="+",
            help='Markdown file')
    args = parser.parse_args()
    #print(args)
    test_file_list = args.file
    md_file = test_file_list[0]
    xmind_name = md_file.split(".md")[0] + ".xmind"

    md = markdown_to_dict.MarkdownToDict()
    dj = dict_to_json.DictToJson()

    re_dict = md.start(md_file)
    js_dict = dj.start(re_dict)

    json_str = json.dumps(js_dict, ensure_ascii=False)
    of = codecs.open(os.path.join(output_zip,"content.json"),"w",'utf-8')
    of.write(json_str)
    of.close()

    json_str = json.dumps(zip_need.manifest, ensure_ascii=False)
    of = codecs.open(os.path.join(output_zip,"manifest.json"),"w",'utf-8')
    of.write(json_str)
    of.close()

    json_str = json.dumps(zip_need.metadata, ensure_ascii=False)
    of = codecs.open(os.path.join(output_zip,"metadata.json"),"w",'utf-8')
    of.write(json_str)
    of.close()

    z = zipfile.ZipFile(os.path.join(output_dir,xmind_name), 'w')
    for d in os.listdir(output_zip):
        z.write(os.path.join(output_zip, d), d)
    z.close()
    #print(json_str)
    print("\ncreate success\noutput : " + os.path.join(output_dir,xmind_name))

if __name__ == "__main__":
    md_to_xmind()
