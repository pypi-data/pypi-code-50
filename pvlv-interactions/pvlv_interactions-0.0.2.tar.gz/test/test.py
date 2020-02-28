from pvlv_interactions import Interactions


def main():
    i = Interactions('ciao madonna bello chuck', 'ita')
    out = i.response()
    print(out)


if __name__ == '__main__':
    main()
