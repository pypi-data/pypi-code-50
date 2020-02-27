from ..exceptions import CastError


class CustomType:
    pass


class _BuiltInType(CustomType):
    pass


class FloatType(_BuiltInType):
    def _convert(self, fvalue):
        try:
            if type(fvalue) is bool:
                raise TypeError
            return float(fvalue)
        except (ValueError, TypeError):
            raise CastError(f'Cannot cast {fvalue} as float')

    def decode(self, fvalue):
        return self._convert(fvalue)

    def encode(self, fvalue):
        return self._convert(fvalue)


class IntType(FloatType):
    def decode(self, fvalue):
        return int(super().decode(fvalue))

    def encode(self, fvalue):
        return int(super().encode(fvalue))


class BoolType(_BuiltInType):
    def _to_bool(self, fvalue):
        if not type(fvalue) is bool:
            raise CastError(f'Cannot cast {fvalue} as bool')
        return fvalue

    def decode(self, fvalue):
        return self._to_bool(fvalue)

    def encode(self, fvalue):
        return self._to_bool(fvalue)


class StrType(_BuiltInType):
    def _to_str(self, fvalue):
        if not type(fvalue) in [str, int, float]:
            raise CastError(f'Cannot cast {fvalue} as str')
        return str(fvalue)

    def decode(self, fvalue):
        return self._to_str(fvalue)

    def encode(self, fvalue):
        return self._to_str(fvalue)
