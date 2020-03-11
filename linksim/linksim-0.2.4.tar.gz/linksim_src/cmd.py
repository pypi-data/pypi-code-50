
import argparse
from linksim_src import Url


parser = argparse.ArgumentParser(usage="Manager project, can create git , sync , encrypt your repo")
parser.add_argument("-u","--url",default="", help="get group")
parser.add_argument("-r","--rank",default=3, type=int, help="set rank")



def main():
    args = parser.parse_args()
    if args.url != "":
        res = Url.Index(args.url, rank=args.rank)
        for g in res:
            print("-" * 20)
            for l in g:
                print(l)
            print()

if __name__ == "__main__":
    main()
