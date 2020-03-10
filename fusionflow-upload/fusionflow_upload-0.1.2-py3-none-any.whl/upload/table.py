from types import CodeType
from typing import (Any, Callable, Dict, Generator, List, Mapping, Optional,
                    Sequence, Text, Tuple, TypeVar, Union)

from .base import PartialTable, TableMeta
from .fields import Field, FieldTV, FieldType, ValidationError, get_field_type
from .parameter import Parameter
from .sql import Sql
from .utils import get_tz

FieldLikeType = TypeVar('FieldLikeType', Mapping[str, Any],
                        Union[Tuple[str, Any]], List[Tuple[str, Any]])


def table(uri: str, *args, **kwargs):
    """
    uri -- identical resource location, indicate it's
    access protocol, authentication, location and stored format
    (explictly or implictly)

    current support schema include:

    * file
    * db
        * oralce
    * http

    current support foramt include:

    * csv
    * json
    * db
        * oracle

    if cann't parse, raise :py:class:`TypeError`

    :param str uri: universal resource identifier
    """
    # TODO: implement class method ``from_uri`` and ``to_uri``
    service = Table(uri)
    return service


class Table(metaclass=TableMeta):
    increment_import = Parameter(
        bool, positional=False, default=False,
        help="table import strategy, every time import new full, \
            or partially amending"
    )
    infer_field_type = Parameter(
        bool, default=True,
        help="should infer each field type from first record values or \
            get it by other way (database?)"
    )
    validation_mode = Parameter(
        str, default="loose",
        help="""import mode, loose: keep running, retrive erorr info thorugh\
             validations, strict: raise Exception immediately"""
    )
    validators = Parameter(dict, default=lambda: {'row': [], 'field': {}},
                           help="""validation list contains all validator related to this
                           table and related fields,
                           use :method:`Table.register_validator`_
                           to register new validator""")

    timezone = Parameter(str, required=True,
                         help="""data source tz info,  impact how native datetime object
                         iterpretted,
                         value will tralsate into utc time internally""")

    def __new__(cls, *args, final_=False, **kwargs):
        """check required parameters all supplied

        :raises TypeError: [description]
        :return: [description]
        :rtype: [type]
        """
        parameters = cls.__parameters__

        # collect missing required parameters
        # both args, and kwargs checked
        missing = set()

        # check keyword
        for name, param in parameters:
            if param.required and param.name not in kwargs:
                missing.add(name)

        # check positional args can fill optional parameters required
        position = 0
        for name, param in parameters:
            # postitional first
            if not param.positional:
                break

            if not isinstance(getattr(cls, name), Parameter):
                # subclass override this attribute
                missing.discard(name)
                continue
            if len(args) <= position:
                break

            position += 1
            missing.discard(name)

        if len(missing):
            if final_:
                raise TypeError(
                    """{}() missing {} required option{}: {}""".format(
                        cls.__name__, len(missing),
                        "s" if len(missing) > 1 else "",
                        ", ".join(map(repr, sorted(missing)))
                    )
                )
            return PartialTable(cls, *args, missing_=missing, **kwargs)
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        # parameter's value cache
        self._parameter_values = {**kwargs}
        # set keywork parameters, if name is parameter type
        # it will format value use type_ , this will override
        # `_parameter_values`'s value
        for name, value in kwargs.items():
            # pass out validate* method, this can be
            # methods
            if name.startswith("validate"):
                continue
            setattr(self, name, value)

        position = 0
        for name, param in self.__parameters__:
            if not param.positional:
                break

            # remove overrided attr
            cls_attr = getattr(type(self), name)
            if not isinstance(cls_attr, Parameter):
                continue
            # travel all args
            if len(args) <= position:
                break

            # check if keyword value set conflicted or not
            if name in self._parameter_values:
                raise ValueError("already set value for parameter {}".
                                 format(name))

            setattr(self, name, args[position])
            position += 1

        self._fields: Optional[List[Any]] = None

        # insert cached
        self._cached_rows = []
        self._cached_count = 100
        self._extract_generator = None
        # validators used to validation value correct or not
        # add validator method
        self.validators['row'].extend(self.__validators__['row'])
        for name, methods in self.__validators__['field'].items():
            self.validators['field'].setdefault(name, []).extend(
                [getattr(self, method) for method in methods]
            )
        # add validator kwarg
        for name, value in kwargs.items():
            if name == "validate":
                self.validators['row'].extend(kwargs["validate"])
            elif name.startswith("validate_"):
                v_name = name[len("validate_"):]
                self.validators['field'].setdefault(v_name, []).extend(value)
        self._current_failed = 0
        self._current_extract = 0
        self._validation_error = []

    def to_sql(self, stmt_type='create') -> Text:
        # validate table structure first
        if not self.fields:
            raise ValueError("cant specific field")

        sql = Sql(self)
        return sql.stmt(stmt_type)

    @property
    def table_name(self):
        return self._table_name

    @table_name.setter
    def table_name(self, value):
        self._table_name = value

    def set_configs(self, override=True, **kwargs):
        """set table level configures, like import category,
        table level native datatime timezone, etc

        :param override: override value if configure already set,
        defaults to True
        :type override: bool, optional
        """
        for name, value in kwargs.items():
            if name in self.__dict__ and not override:
                continue
            self.__dict__[name] = value

    def registe_validator(self, field: Union[None, str, Field], func:
                          Union[str, CodeType, Callable]):
        """add validator to fields

        validtor can be any thing that callable,
        raise Exception if requried condition not satisfied
        when this callable return a value, this value will get instead input
        arguement.

        it also can return a value type not same with input type, it this
        case, field type will depend on last validtor in field validator
        list.

        **Caution**: if last validator modify field type, it must contain a
        return annontation type list in :module:`feild`, otherwise, TypeError
        will raise if runtime.

        one field can have many validtors, but for clarity and simple,
        one validtor is enough,

        .. code-block:: python

            from fusionflow.upload import Table
            t = Table()

            def validator_empno(field):
                "validator on empno feild"
                assert field > 1000

            def validator(row):
                "validator on one row"
                # number of no None field value
                assert len(fliter(None, row)) > 4

            t.registe_validator('empno', validator_empno)

        :param feild: field to add validator, if is None, add this
            validator to row scope
        :param validator: callable raise Error if validation fails
        """
        # TODO: support change data type in validators,
        # get first callable from source str
        validator = None
        if not callable(func):
            g: Dict[str, Any] = {}
            exec(func, g)
            for var in g:
                if var == "__builtins__":
                    continue
                if callable(g[var]):
                    validator = g[var]
                    break
            else:
                raise ValueError("no calable found in %s" % func)
        else:
            validator = func

        if field is None:
            self.validators['row'].append(validator)
        else:
            for f in self.fields:
                if f.field_name == field or f == field:
                    self.validators["field"].setdefault(
                        f.field_name, []
                    ).append(validator)

                    f.registe_validator(validator)

    @property
    def validations(self) -> Dict:
        """informations about last running
        contains numberof validated rows, invalidated rows whith failed reasons

        {
            "success": int, // num of extracted rwos
            "failed: int, // num of failed rows
            "details":[{
                "input": [], // raw input
                "errors":{field1: [error], feild2: [error]}

            }]
        }
        :rtype: :class:`dict`_
        """
        return {
            "success": self._current_extract,
            "failed": self._current_failed,
            "details": self._validation_error
        }

    @property
    def tzinfo(self):
        return get_tz(self.timezone)

    @property
    def fields(self):
        """generate fields dynamicly if INFER_FIELD_TYPE
            set to true
        :raises ValueError: [description]
        :return: [description]
        :rtype: [type]
        """
        if self.infer_field_type is True and self._fields is None:
            generator = self.extract()
            raw_fields = next(generator)
            if raw_fields is None:
                raise ValueError("con't get data from source")
            self._fields = self._to_fields(raw_fields)

            # save for later insert reuse
            self._extract_generator = generator
            self._cached_rows.append(self._fields)
        return self._fields

    @property
    def field_names(self):
        return [f._field_name for f in self.fields]

    @property
    def field_name_types(self):
        return [(f._field_name, f._field_type) for f in self.fields]

    @property
    def django_fields(self):
        # lazy import
        def dunder_str(obj):
            return list(getattr(obj, f) for f in fields)

        fields = {field.field_name: field.django for field in self.fields}
        return {**fields, "__str__": dunder_str}

    def _to_fields(self, fields: Any) -> List[FieldTV]:
        """transform ``FieldikeType`` to ``Field`` type

        :param fields: [description]
        :type fields: Sequence[FieldLikeType]
        :raises ValueError: [description]
        :raises ValueError: [description]
        :raises ValueError: [description]
        :return: [description]
        :rtype: List[Field]
        """
        if isinstance(fields, Sequence):
            return self._to_sequence_fields(fields)
        if isinstance(fields, Mapping):
            return self._to_mapping_fields(fields)

        raise ValueError("input feilds type not afford ")

    def _to_sequence_fields(
        self, fields: Sequence[Union[FieldTV, FieldLikeType]]
    ) -> List[FieldTV]:

        res: List[FieldTV] = []
        for raw_field in fields:
            if isinstance(raw_field, Field):
                res.append(raw_field)
                # jump to next field
                continue

            raw_field_map: Dict[str, Any] = {}
            if isinstance(raw_field, (list, tuple)):
                if len(raw_field) == 2 and not \
                       isinstance(raw_field[0], (list, tuple)):

                    raw_field_map = {raw_field[0]: raw_field[1]}
                elif isinstance(raw_field[0], (tuple, list)):
                    # change to dict
                    raw_field_map = dict(raw_field)
                else:
                    raise ValueError(
                            "filed must be [name, value] or [(name, relname),\
                             (value, relvalue), ...], got: {}".
                            format(raw_field)
                    )
            else:
                raw_field_map = raw_field  # type: ignore

            try:
                field: FieldTV = self._parse_field_from_dict(raw_field_map)
            except ValueError as e:
                raise ValueError(e.args[0] + " field:\n{}".format(raw_field))
            res.append(field)
        return res

    def _to_mapping_fields(
        self, fields: Mapping[str, Union[FieldTV, FieldLikeType]]
    ) -> List[FieldTV]:

        res: List[FieldTV] = []

        for name, value in fields.items():
            if isinstance(value, Field):
                res.append(value)
                continue

            # str is sequence, not use Sequence
            if not isinstance(value, (list, tuple, Mapping)):
                raw_field_map = {name: value}

            elif isinstance(value, (tuple, list)):
                if len(value) == 2 and not\
                      isinstance(value[0], (tuple, list)):
                    raw_field_map = {value[0]: value[1]}
                elif isinstance(value[0], (tuple, list)):
                    raw_field_map = dict(value)
                else:
                    raise ValueError(
                            "filed must be [name, value] or [(name, relname),\
                             (value, relvalue), ...], got: {}".
                            format(value)
                    )
            else:
                raw_field_map = dict(value)

            try:
                field: FieldTV = self._parse_field_from_dict(raw_field_map)
            except ValueError as e:
                raise ValueError(e.args[0] + " field:\nkey:%s \tvalue:%s" %
                                 (name, value))

            res.append(field)
        return res

    def _parse_field_from_dict(
        self, raw_field_map: Dict[str, Any]
    ) -> FieldTV:

        # only one key-value pair(field name,field type)
        if len(raw_field_map) == 1:
            key, value = list(raw_field_map.items())[0]
            if value is None:
                raise ValueError(
                    "can't infer type from None, place spefice it explicitly"
                )
            field_type = FieldType(type(value))
            field = get_field_type(field_type)(
                key, table=self, default_value=value
            )
        else:
            # if multiple key-value pair found, pass through as arguements
            # check requirement fields
            field_type = raw_field_map.pop('type', None)

            if field_type is None:
                field_type = raw_field_map.get("value", None)
                if field_type is None:
                    raise ValueError("field type and field value not specific")
                else:
                    field_type = FieldType(type(field_type))
            else:
                field_type = FieldType(field_type)

            name = raw_field_map.get("name", None)
            if name is None:
                raise ValueError("field name not specific")
            value = raw_field_map.get("value", None)
            field = get_field_type(
                field_type
            )(name, default_value=value, table=self)
        return field

    def extract(self) -> Generator:
        """data extract from source return by row, each row has one or more fields,
        when row returned by list
        each feild can be:

        * :class:`Field`
        * dict : {attr:value, ...} -- attr pairs attrs must contain name, value
        * sequence: (name, value) or ((attr, value), ...) first format
            preferred if sequence len is 2

        when row returned by dict
        like list, each feild can be:

        * name: value pair -- name is feild name , value is field value()
        * name: {attr:value, ...}/[(atrr, value), ...] -- name is field name,
            attr is field attr, value is field attr value
        * name: :cls:`Field` pair -- name is field name, Field is Field
            instance

        :raises NotImplementedError: subclass implement this
        """
        raise NotImplementedError()

    def __iter__(self) -> Generator[List[Field], None, None]:
        """get row from extract
        row should

        if multiple for loop breaked and continued
        all will be use the same _extract_generator
        :return: [description]
        :rtype: Generator
        :yield: [description]
        :rtype: Generator
        """

        def get_value(data):
            errors = {}
            row = []
            fields = self._to_fields(data)
            for f in fields:
                try:
                    f.registe_validator(
                        *self.validators["field"].get(f.field_name, [])
                    )
                    row.append(f.value)
                except ValidationError as e:
                    if self.validation_mode == "loose":
                        errors.update({f.field_name: f.error_message})
                    else:
                        raise e
            # error is not empoty, error happend, otherwise row is validated
            if errors:
                self._validation_error.append(errors)
                self._current_failed += 1
                return None
            else:
                return row

        # reuse generator in `self.fields` call
        if self._extract_generator is None:
            self._extract_generator = self.extract()

        if self._cached_rows:
            for data in self._cached_rows:
                transformed = get_value(data)
                # error happend next row
                if transformed:
                    yield transformed
                    # must after yield, must run will stop at yield
                    self._current_extract += 1

        for data in self._extract_generator:
            transformed = get_value(data)
            # error happened, next row
            if transformed:
                yield transformed
                # must after yield, must run will stop at yield
                self._current_extract += 1

    def __str__(self) -> Text:
        return """{table_name}({fields})""".format(
            table_name=self._table_name, fields=",".join(self.field_names)
        )

    @property
    def __parameters__(self):
        return type(self).__parameters__

    @property
    def __validators__(self):
        return type(self).__validators__
