from pathlib import Path
import pandas as pd
import pandas_profiling as pdp
import matplotlib.pyplot as plt
import japanize_matplotlib


def main():
    import argparse
    parser = argparse.ArgumentParser(description='count files')
    parser.add_argument('file', help="csv, tsv, xlsx, xlsm, xlsx")
    parser.add_argument("-o", "--out", default="", help="output file path")
    args = parser.parse_args()

    input_fpath = Path(args.file)
    output_fpath = Path(args.out).with_suffix(".html") if args.out else\
            Path(input_fpath.stem).with_suffix(".html")

    df = pd.read_excel(input_fpath)
    df = pd.read_csv(input_fpath , sep='\t') if input_fpath.suffix in ['.tsv'] else\
        pd.read_excel(input_fpath) if input_fpath.suffix in ['.xls', '.xlsm', '.xlsx'] else\
        pd.read_csv(input_fpath)
    profile = pdp.ProfileReport(df)
    profile.to_file(output_fpath)


if __name__ == "__main__":
    main()
