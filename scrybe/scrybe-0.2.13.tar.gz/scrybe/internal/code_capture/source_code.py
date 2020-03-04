import sys
import ast
from typing import Union

from scrybe.internal.uploader import DataReceiver


class CodeCapture(object):
    _is_ipython = None
    _is_zeppelin = None
    _is_notebook = None
    execution_count = -1
    code_tracking_node = None
    filename = None
    zeppelin_execution_count = 0
    zeppelin_execution_key = 0
    zeppelin_code_dict = dict()
    module_zeppelin_code_mapping = dict()

    @classmethod
    def __is_ipython__(cls):
        try:
            import IPython
        except Exception as e:
            return False
        ipython = IPython.get_ipython()
        if ipython is None:
            return False
        else:
            return True

    @classmethod
    def __is_zeppelin__(cls):
        try:
            import sys
            if "__main__" not in sys.modules:
                return False
            if not hasattr(sys.modules["__main__"], "intp"):
                return False
            intp = sys.modules["__main__"].intp
            zc = intp.getZeppelinContext()
            if zc is None:
                return False
            return True
        except Exception as e:
            return False

    @classmethod
    def is_zeppelin(cls):
        if cls._is_zeppelin is None:
            cls._is_zeppelin = cls.__is_zeppelin__()
        return cls._is_zeppelin

    @classmethod
    def is_notebook(cls):
        try:
            import IPython
        except Exception as e:
            return False
        ipython = IPython.get_ipython()
        if ipython is None or not hasattr(ipython, 'kernel'):  # For jupyter notebook
            return False
        else:
            return True

    @classmethod
    def is_ipython(cls):
        if cls._is_ipython is None:
            cls._is_ipython = cls.__is_ipython__()
        return cls._is_ipython

    @classmethod
    def get_ipython_code(cls, ipython):
        def get_input_key(n):
            return "_i" + str(n)

        if cls.execution_count < 1:
            input_seq_num = 1
        else:
            input_seq_num = cls.execution_count + 1
        input_key = get_input_key(n=input_seq_num)
        src_code = []
        while input_key in ipython.ns_table['user_local']:
            src_code.append(ipython.ns_table['user_local'][input_key])
            input_seq_num += 1
            input_key = get_input_key(n=input_seq_num)
        return src_code

    @classmethod
    def get_zeppelin_code(cls):
        def get_input_key(n):
            return "_i" + str(n)

        if cls.execution_count < 1:
            input_seq_num = 1
        else:
            input_seq_num = cls.execution_count + 1
        input_key = get_input_key(n=input_seq_num)
        src_code = []
        while input_key in cls.zeppelin_code_dict:
            src_code.append(cls.zeppelin_code_dict[input_key])
            input_seq_num += 1
            input_key = get_input_key(n=input_seq_num)
        return src_code

    @classmethod
    def get_new_code_tracking_node(cls, oid):
        # The import must be here to avoid cyclic dependency
        from scrybe.internal.depgraph.nodes import CodeTrackingNode
        code_tracking_node = CodeTrackingNode(oid=oid, version=0)
        return code_tracking_node

    @classmethod
    def upload_code_payload(cls):
        module_names = list(sys.modules.keys())
        for module_name in module_names:
            module = sys.modules[module_name]
            if hasattr(module, '__version__') and hasattr(module, '__name__'):
                version = module.__version__
                if isinstance(version, bytes):
                    version = version.decode("utf-8")
                if not isinstance(version, str):
                    continue
                cls.code_tracking_node.add_package(module_name=module.__name__, version=version)
        DataReceiver.receive_batch(data_dict_list=cls.code_tracking_node.prepare_for_upload())

    @classmethod
    def get_code_client_id(cls) -> Union[str, None]:
        if not cls.is_ipython() and not cls.is_zeppelin():
            return None
        if cls.is_zeppelin() and len(cls.zeppelin_code_dict) > 0:
            if cls.zeppelin_execution_count <= cls.execution_count:
                if cls.code_tracking_node is not None:
                    return cls.code_tracking_node.client_id
                else:
                    return None
            else:
                if cls.code_tracking_node is None:
                    intp = sys.modules["__main__"].intp
                    cls.code_tracking_node = cls.get_new_code_tracking_node(oid=id(intp))
                cls.code_tracking_node.set_src_code_for_filename(filename="<stdin>",
                                                                 src_code=cls.get_zeppelin_code())
                cls.upload_code_payload()
                cls.execution_count = cls.zeppelin_execution_count
                return cls.code_tracking_node.client_id
        elif cls.is_ipython():
            import IPython
            ipython = IPython.get_ipython()
            if ipython.execution_count <= cls.execution_count:
                if cls.code_tracking_node is not None:
                    return cls.code_tracking_node.client_id
                else:
                    return None
            else:
                if cls.code_tracking_node is None:
                    cls.code_tracking_node = cls.get_new_code_tracking_node(oid=id(ipython))
                cls.code_tracking_node.set_src_code_for_filename(filename=ipython.filename,
                                                                 src_code=cls.get_ipython_code(ipython))
                cls.upload_code_payload()
                cls.execution_count = ipython.execution_count
                return cls.code_tracking_node.client_id

    @classmethod
    def capture_code_files(cls, filepaths: list):
        if cls.code_tracking_node is None:
            cls.code_tracking_node = cls.get_new_code_tracking_node(oid=id(filepaths))
        for filepath in filepaths:
            fp = open(filepath, "r")
            cls.code_tracking_node.set_src_code_for_filename(filename=filepath, src_code=fp.read(), overwrite=True)
            fp.close()
        cls.upload_code_payload()

    @classmethod
    def add_zeppelin_code(cls, captured_code):
        cls.zeppelin_execution_count += 1
        input_key = '_i' + str(cls.zeppelin_execution_count)
        cls.zeppelin_execution_key = input_key
        cls.zeppelin_code_dict[input_key] = captured_code
        captured_code_body = ast.parse(captured_code).body
        func_nodes = [n for n in captured_code_body if isinstance(n, ast.FunctionDef)]
        for func_node in func_nodes:
            cls.module_zeppelin_code_mapping[func_node.name] = input_key
        class_nodes = [n for n in captured_code_body if isinstance(n, ast.ClassDef)]
        for class_node in class_nodes:
            func_nodes = [n for n in class_node.body if isinstance(n, ast.FunctionDef)]
            for func_node in func_nodes:
                cls.module_zeppelin_code_mapping[class_node.name + "." + func_node.name] = input_key
            base_func_codes = []
            try:
                for base_name_node in class_node.bases:
                    base_name = base_name_node.id
                    for key in cls.module_zeppelin_code_mapping:
                        if key.startswith(base_name + "."):
                            base_func_codes.append((key.split(".")[-1], cls.module_zeppelin_code_mapping[key]))
            except:
                pass
            for base_func_name, code_seq_num in base_func_codes:
                cls.module_zeppelin_code_mapping[class_node.name + "." + base_func_name] = code_seq_num

    @classmethod
    def init_zeppelin_code(cls):
        try:
            if not cls.is_zeppelin():
                return
            final_code = sys.modules["__main__"].final_code
            cls.add_zeppelin_code("\n".join(final_code))
            import functools

            def get_statement_decorator(_cls, func):
                @functools.wraps(func)
                def inner(*args, **kwargs):
                    out = func(*args, **kwargs)
                    try:
                        stmts = out.statements().split("\n")
                        final_code = []
                        for s in stmts:
                            if s is None:
                                continue
                            # skip comment
                            s_stripped = s.strip()
                            if len(s_stripped) == 0 or s_stripped.startswith("#"):
                                continue
                            final_code.append(s)
                        if final_code:
                            _cls.add_zeppelin_code("\n".join(final_code))
                    except:
                        pass
                    return out

                return inner

            intp = sys.modules["__main__"].intp
            intp.getStatements = get_statement_decorator(cls, intp.getStatements)
        except:
            pass
