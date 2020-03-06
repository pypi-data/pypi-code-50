import argparse
import re
from glob import glob
from os import path, mkdir, makedirs, remove
from sys import argv
from shutil import rmtree

TEMPLATE_NAME = '.template.html'
CONTENTS_MAGIC_STRING = '%%'

def build(src='./src', dist='./dist', paths=None, with_deps=False):
    src = path.realpath(src)
    dist = path.realpath(dist)

    if not paths:
        paths = [src]

    # dir path to template contents
    templates_cache = {}
    # path to contents
    template_regex = re.compile('%%{\s*(.*)\s*}%%')

    paths = map(path.realpath, paths)
    
    filepaths = []
    for build_dir in paths:
        if not build_dir.startswith(src):
            raise Exception('Invalid build directory "%s"' % build_dir)
        src_path = path.realpath(build_dir)

        # must have been deleted from src dir
        if not path.exists(src_path):
            dist_path = path.join(dist, build_dir[len(src) + 1:])
            if path.exists(dist_path):
                if path.isdir(dist_path):
                    rmtree(dist_path)
                else:
                    remove(dist_path)
            continue

        if not path.isdir(src_path):
            filepaths.append(src_path)
        else:
            output_dir = build_dir.replace(src, dist, 1)
            if path.exists(output_dir):
                rmtree(output_dir)

            if not path.exists(output_dir):
                makedirs(output_dir)
                
            filepaths += filter(lambda x: not path.isdir(x), glob(path.join(build_dir, '**', '*'), recursive=True))

    dirs = set(map(path.dirname, filepaths))
    for dir in dirs:
        dir = path.realpath(dir)
        cursor = dir
        while len(cursor) >= len(src):
            template_path = path.join(cursor, TEMPLATE_NAME)
            if cursor not in templates_cache and path.exists(template_path):
                contents = open(template_path, encoding='utf8').read()
                includes = template_regex.findall(contents)

                templates_cache[cursor] = {
                    'contents': contents,
                    'includes': includes
                }
                
            cursor = path.dirname(cursor)
            

    if with_deps:
        for dir in templates_cache:
            for include in templates_cache[dir]['includes']:
                if include != CONTENTS_MAGIC_STRING:
                    filepaths.append(path.join(dir, include))
                    
    # copy all files from src dir to dist dir
    # if html, append header and footer
    for filepath in filepaths:
        output_filepath = filepath.replace(src, dist, 1)        
        leaf_dir = output_filepath[:-len(path.basename(output_filepath))]
        if not path.exists(leaf_dir):
            makedirs(leaf_dir)

        if filepath.endswith('html'):
            contents = open(filepath, encoding='utf8').read()
            dir = path.realpath(path.dirname(filepath))
            
            # make sure we are going from least length to greater
            # going thru all parent directories and adding the templates starting with the farthest away dir
            template_dirs = sorted(filter(lambda x: dir.startswith(x), templates_cache), key=len, reverse=True)

            for template_dir in template_dirs:
                cache_item = templates_cache[template_dir]
                template = cache_item['contents']
                includes = cache_item['includes']

                for include in includes:
                    if include == '%%':
                        # re.sub turns \n into real newlines :(
                        template = template.replace('%%{' + CONTENTS_MAGIC_STRING + '}%%', contents)
                    else:
                        distance = -1
                        cursor = filepath
                        while template_dir != cursor and len(cursor) > len(template_dir):
                            cursor = path.dirname(cursor)
                            distance += 1
                            
                        relative_include = path.join('../'*distance, include)
                        template = re.sub('%%{' + include + '}%%', relative_include, template)                        

                # if there is no '%%{%%}%%' put the template to the top of the page
                if '%%' not in includes:
                    template = '\n'.join([template, contents])
                    
                contents = template
                open(output_filepath, 'w', encoding='utf8').write(contents)
        else:
            contents = open(filepath, 'rb').read()
            open(output_filepath, 'wb').write(contents)
            
