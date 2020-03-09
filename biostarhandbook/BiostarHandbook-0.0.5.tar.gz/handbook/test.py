import mistune

x = [
    (10, 20),
    (30, 40),
    (40, 50),
    (60, 70),
    (70, 90),
]


if __name__ == '__main__':
    text = "<div><div><div>foo</div></div></div>"
    html1 = mistune.markdown(text, escape=False, parse_block_html=False, parse_inline_html=False)
    print (html1)

    html2 = mistune.markdown(text, escape=False, parse_block_html=True)
    print (html2)

    print ('.')
    def generate(x):
        start = end = None
        for (x1, y1), (x2, y2) in zip(x, x[1:]):
            start = start or x1
            end = end or y1
            if x2 <= end:
                end = y2
            else:
                yield (start, end)
                start = end = None

        if start:
            yield (start, end)
        else:
            yield (x1, y1)

    #for p in generate(x):
    #    print (p)


