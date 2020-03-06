import json, glob, os, re, cv2, numpy as np, logging, hashlib, tempfile, shutil
from typing import Any, Tuple, List, Dict
from lxml import etree
from syncvtools.utils.aws_tools import download_file as s3_download_file
from urllib.parse import urlparse
import yaml
from PIL import Image


### YAML
def yaml_read_to_object(input_file: str) -> Any:
    '''
    Func Yaml reader
    :param input_file:
    :return:
    '''
    if not os.path.exists(input_file):
        raise ValueError("File doesn't exist: {}".format(input_file))
    with open(input_file, 'r') as stream:
        try:
            return yaml.safe_load(stream)

        except yaml.YAMLError as exc:
            logging.error(exc)
    return None


### JSON
def json_read_to_object(input_file: str) -> Dict:
    '''
    Parses a valid JSON file to a python dict.
    :param input_file:
    :return: a dict object
    '''
    with open(input_file, 'r') as f:
        json_dict = json.load(f)
    return json_dict


def json_object_to_file(path_src: str, data_obj: Any) -> None:
    '''
    Saves dict to file as JSON
    :param path_src:
    :param data_obj:
    :return:
    '''
    full_path = os.path.abspath(path_src)
    dir_path = os.path.dirname(full_path)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
    with open(path_src, 'w') as f:
        json.dump(data_obj, f, indent=4)


## read files

def file_to_list(file_src: str) -> List:
    '''
    Reads input file to list (splint by new lines)
    :param file_src:
    :return:
    '''
    with open(file_src) as f:
        lines = f.read().splitlines()
    return lines


def list_to_file(path_dest: str, list_obj: List[str]) -> None:
    '''
    Reads input file to list (splint by new lines)
    :param file_src: path to file
    :return:
    '''
    with open(path_dest, "w") as f:
        for elem_ in list_obj:
            f.write("%s\n" % elem_)


## directory traversal
def get_file_list_by_ext(dir: str, ext: Tuple[str], recursive: bool = False) -> List[str]:
    def insensitive_glob(pattern):
        def either(c):
            return '[%s%s]' % (c.lower(), c.upper()) if c.isalpha() else c

        return ''.join(map(either, pattern))

    '''
    Takes a directory and uses `glob` to grab all files of provided extensions. case insensitive
    :param dir: directory to scan
    :param ext: tuple of extensions i.e. ('jpg', 'jpeg', 'tif')
    :param recursive: is search recursive? Works on Python 3.5+ only
    :return: a list of paths (abs or relative depends on input) to matching files
    '''
    if dir is None:
        raise ("Directory for grabbing files from is not provided")
    if ext is None:
        raise ("Extensions should be provided: ext=('jpg','png')")
    ext_formatted = []
    for ex in ext:
        ex = ex
        if ex.startswith('.'):
            ex = ex[1:]
        if not ex:
            continue
        ext_formatted.append(ex)

    if not ext_formatted:
        raise ("No extensions left after formatting. Provide in format ext=('jpg','png')")

    ext = tuple(ext_formatted)
    if dir.endswith('/'):
        dir = dir[:-1]
    types_masks = ["{}/{}*.{}".format(dir, '**/' if recursive else '', x) for x in ext]
    result_list = []
    for type_mask in types_masks:
        result_list.extend(glob.glob(insensitive_glob(type_mask), recursive=recursive))
    return result_list


def cut_extension(file_path: str, long_extensions: Tuple[str] = ('tfrecord',)) -> str:
    '''
    Cuts extension from filename (SHOULD BE [0;7] symbols or in the list of long_extensions (tuple of strings)).
    Relays on os.path.splittext logic.
    Examples:
    file.jpg => file
    /home/file. => /home/file
    /home/file.big_extension => /home/file.big_extension (unless it's in long_extensions)
    Default: file.tfrecord => file (since 'tfrecord' is in default long_extensions)
    :param file_path:
    :return:
    '''
    base, ext = os.path.splitext(file_path)
    if ext is not None and len(ext) > 7:
        if ext[1:] not in long_extensions:
            # it's not extension!
            return file_path
    return base


def replace_extension(file_path: str, new_extension: str) -> str:
    '''
    Replace extension in a given file/path.
    :param file_path: input path
    :param new_extension: new extension. i.e. 'jpg' or 'png'
    :return: path with replaced extension
    '''
    no_ext = cut_extension(file_path=file_path)
    if not new_extension:
        return no_ext
    if new_extension[0] == '.':
        new_extension = new_extension[1:]
    return "{}.{}".format(no_ext, new_extension)


def dataset_filename_to_key(file_path: str) -> str:
    '''
    For now Just cuts extension if it is present
    :param file_path:
    :return:
    '''
    file_name = os.path.basename(file_path)
    key = cut_extension(file_name)
    return key


def pbmap_read_to_dict(input_file: str) -> Dict[int, str]:
    '''
    Reads TF pbtxt file dictionary
    :param input_file: TF Format of storing label indices. (usually pbtxt)
    :return: Dict
    '''
    if input_file is None or not os.path.exists(input_file):
        raise ValueError("Labels file doesn't exist: {}".format(input_file))
    try:
        with open(input_file) as f:
            protobuf = f.read()
            indx2label = {}
            # parsed = re.findall(r'{[^}]+}', protobuf, re.U)
            names = re.findall(r"name: '([^']+)'", protobuf)
            ids = re.findall(r"id: (\d+)", protobuf)
            for id, name in zip(ids, names):
                indx2label[int(id)] = name

            if indx2label is None:
                raise Exception("Cannot parse labels file: {}".format(input_file))
            return indx2label
    except Exception as e:
        raise Exception("Can't read file {}".format(input_file)).with_traceback(e.__traceback__)


####XML

def parse_xml_pascalvoc(xml_path) -> Dict:
    '''
    Parses a valid XML file (which follows PascalVOC annotation) to a python dict.
    :param xml_path: path to the XML file with PascalVOC annotation for single image
    :return: a dictionary
    '''
    with open(xml_path, 'r') as file:
        xml_text = file.read()
    xml = etree.fromstring(xml_text)
    parse = recursive_parse_xml_to_dict(xml)
    return parse


def recursive_parse_xml_to_dict(xml) -> Dict:
    """Recursively parses XML contents to python dict.
    Credit: Object Detection API (TensorFlow)
    We assume that `object` tags are the only ones that can appear
    multiple times at the same level of a tree.

    Args:
      xml: xml tree obtained by parsing XML file contents using lxml.etree

    Returns:
      Python dictionary holding XML contents.
    """
    if xml is None or len(xml) == 0:
        return {xml.tag: xml.text}
    result = {}
    for child in xml:
        child_result = recursive_parse_xml_to_dict(child)
        if child.tag != 'object':
            result[child.tag] = child_result[child.tag]
        else:
            if child.tag not in result:
                result[child.tag] = []
            result[child.tag].append(child_result[child.tag])
    return {xml.tag: result}


def _xml_from_obj_recursive(result_xml=None, obj: Any = None, key: str = None):
    if key is None:
        first_key = next(iter(obj))
        result_xml = etree.Element(first_key)
        _xml_from_obj_recursive(result_xml=result_xml, obj=obj[first_key], key=first_key)
        return result_xml
    if isinstance(obj, dict):
        for key_ in obj:
            if not isinstance(obj[key_], list):
                new_xml = etree.SubElement(result_xml, key_)
            else:
                new_xml = result_xml
            _xml_from_obj_recursive(new_xml, obj[key_], key_)
    elif isinstance(obj, list):
        for elem_ in obj:
            new_xml = etree.SubElement(result_xml, key)
            _xml_from_obj_recursive(new_xml, elem_, key)
    else:
        result_xml.text = str(obj)


def xml_from_obj(obj: dict) -> etree.ElementTree:
    '''
    Converts dict into XML object that can be later dumped to file as XML
    :param obj:
    :return:
    '''
    res = _xml_from_obj_recursive(obj=obj)
    return etree.ElementTree(res)


def xml_write_to_file(input_obj: dict, output_file: str):
    '''
    Write Dict as XML file
    :param input_obj:
    :param output_file:
    :return:
    '''
    tree = xml_from_obj(obj=input_obj)
    dir = os.path.dirname(output_file)
    if dir:
        os.makedirs(dir, exist_ok=True)
    try:
        tree.write(output_file, pretty_print=True)
    except IOError as e:
        raise ValueError("Unable to copy file {}: {}".format(output_file, e))


##########IMAGES

def img_np_from_disk(file_src: str) -> np.ndarray:
    '''
    Wrapper to cv2 imread which converts BGR to RGB
    :param file_src:
    :return:
    '''
    img_np = cv2.imread(filename=file_src)
    if img_np.dtype != np.uint8:
        raise ValueError("Image should be uint8! Given: {}".format(img_np.dtype))
    if img_np is None:
        raise ValueError("None value is provided instead of numpy array")
    if len(img_np.shape) != 3:
        raise ValueError("Image shape should be always 3. Given: {}".format(img_np.shape))
    img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    return img_np


def img_np_to_disk(img_np: np.ndarray, save_path: str) -> None:
    '''
    Takes image as numpy array RGB and saves it to disk
    :param img_np:
    :return:
    '''
    img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    dir = os.path.dirname(save_path)
    if dir:
        os.makedirs(dir, exist_ok=True)
    cv2.imwrite(filename=save_path, img=img_np)


def get_img_size(path: str) -> Tuple[int, int]:
    '''
    Get img size without loading it to memory. Very fast.
    :param path:
    :return:
    '''

    with Image.open(path) as img:
        width, height = img.size
    return width, height


def cache_file(file_path):
    '''
    cache_file_str that supports strings and arrays
    :param file_path: path or array of paths. Example s3 path.
    :return:
    '''
    if isinstance(file_path, str):
        return cache_file_str(file_path)
    elif isinstance(file_path, tuple) or isinstance(file_path, list):
        res = []
        for file_str in file_path:
            res.append(cache_file_str(file_str))
        return res
    else:
        raise ValueError("Unknown file type of file_path:{}".format(type(file_path)))


def cache_file_str(file_path):
    '''
    Cache file locally if it's a s3 (future http, etc)
    :param file_path: s3://, local filename or sth else [not yet implemented]
    :return: local temp filename
    '''
    if file_path.startswith('s3://'):
        logging.info("Caching file: {}".format(file_path))
        parsed_url = urlparse(file_path)
        path = parsed_url.path.lstrip('/')
        file_name = os.path.basename(path)
        hash = hashlib.md5(file_path.encode('utf-8')).hexdigest()[:5]
        base_name, extension = os.path.splitext(file_name)
        tmp_dir = os.path.join(tempfile.gettempdir(), "syncvtools")
        os.makedirs(os.path.join(tmp_dir), exist_ok=True)
        save_name = os.path.join(tmp_dir, "{}_{}".format(hash, file_name))
        if not os.path.exists(save_name):
            s3_download_file(file_path, save_name)
        return save_name
    else:
        if not os.path.exists(file_path):
            raise ValueError("File doesn't exist: {}".format(file_path))
        return file_path


def _mpath(path):
    '''
    Makes an absolute path from relative (related to module)
    :param path: path starting from syncvtools
    :return:
    '''
    # TODO it is defined in main __init__ file as ROOTDIR
    dir_path = __file__
    dir_path = os.path.dirname(os.path.dirname(os.path.dirname(dir_path)))
    return os.path.join(dir_path, path)


if __name__ == "__main__":
    tree = xml_from_obj(obj={'annotation': {'size': {'width': 532, 'height': 235},
                                            'object': [{'name': 'first obj1'}, {'name': 'first obj2'}]}})
    print(etree.tostring(tree))
