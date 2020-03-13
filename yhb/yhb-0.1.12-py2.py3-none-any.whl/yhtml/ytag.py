def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' {0}="{1}"'.format(attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''

    if content:
        return '\n'.join('<{0}{1}>{2}</{3}>'.format(name, attr_str, c, name) for c in content)
    else:
        return '<{0}{1} />'.format(name, attr_str)


if __name__ == '__main__':
    print(tag('br'))
    print(tag('p', 'hello'))
    print(tag('p', 'hello', 'world'))
    print(tag('p', 'hello', 'world', id=33))
    print(tag('p', 'hello', 'world', id=33, cls='sidebar'))
    print(tag(content='testing', name="img"))

    tag_d = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
    print(tag(**tag_d))
