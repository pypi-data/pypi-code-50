from typing import Any

class SchemaHolder(object):

    def __setattr__(self, name: str, value: Any) -> None:
        if self.is_all_type_vals(value):
            self.__dict__[name] = value
    
    def __getattr__(self, attr):
        scheme = self.schema(attr)
        if scheme is None: return {}
        return scheme


    def schema(self, name:str):
        schema = self.__dict__.get(name, None)
        return schema

    def is_schema(self, name:str):
        schema = self.schema(name)
        if schema is None:
            return False
        return True

    def is_all_type_vals(self, _schema:dict):
        for sval in _schema.values():
            type_cast = type(sval)
            is_typing = isinstance(type_cast, type)
            if is_typing != True:
                return False
        return True
    
    def validate(self, name, item:dict) -> bool:
        if self.is_schema(name): return True
        for skey, sval in self.schema(name).items():
            if skey not in item:
                return False
            if not isinstance(item[skey], sval):
                return False
        return True



def main():
    schema_holder = SchemaHolder()
    schema_holder.hello = {
        "name": str
    }
    print(schema_holder.hello)
    print(schema_holder.validate("hello", {"name": "world"}))

if __name__ == "__main__":
    main()