class Attribute:
    @staticmethod
    def arrow_extract(s: str):
        if not isinstance(s, str):
            return None, None

        arrow = s.find('->')
        if arrow == -1:
            arrowed_str = s
        else:
            arrowed_str = s[arrow + 2:]
            s = s[:arrow]
        return s, arrowed_str

    @staticmethod
    def dictify(o, *fields):
        d = dict()
        for name in fields:  # type: str
            if isinstance(name, tuple):
                arg = name[1:]
                name = name[0]
            else:
                arg = tuple()

            name, yield_name = Attribute.arrow_extract(name)

            value = getattr(o, name, None)
            readable_func = getattr(o, '_readable_%s' % name, None)
            if callable(readable_func):
                value = readable_func(*arg)

            d[yield_name] = value
        return d
