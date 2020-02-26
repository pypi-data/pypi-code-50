import os


def src_dir():
    utils_dir_ = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(utils_dir_)


def project_dir():
    src_dir_ = src_dir()
    return os.path.dirname(src_dir_)


def test_dir():
    pro_dir_ = project_dir()
    return os.path.join(pro_dir_, 'tests')


def test_resources_dir():
    test_dir_ = test_dir()
    return os.path.join(test_dir_, 'resources')


