#!/usr/bin/env python3.7
import argparse
import markdown2
import time

from bs4 import BeautifulSoup as bs


# Default class names that can be overridden with values passed through the
# -c flag
HTML_TAG_TO_CLASS_NAME_MAPPING = {
    "h1": "post-title",
    "h2": "post-heading",
    "h3": "post-heading2",
    "h4": "post-heading3",
    "h5": "post-heading4",
    "h6": "post-heading5",
    "p": "post-paragraph",
    "code": "post-code-block",
    "img": "post-img",
}


def helldive():
    args = _put_args_into_namespace()
    filename, markdown_path, html_path, add_hr = _get_argument_values(args)
    markdown_text = _get_markdown_text_from_file(filename, markdown_path)
    date, author = _get_date_and_author(markdown_text)
    html = _convert_markdown_to_html(markdown_text)
    html = _add_classes_to_html(html)
    html = _add_date_and_author_to_html(html, date, author, add_hr)
    html = _prettify_html(html)
    _write_html_to_file(html, filename, html_path)


def _put_args_into_namespace():
    def _add_markdown_filename_argument(parser):
        parser.add_argument(
            "-f",
            "--filename",
            action="store",
            nargs=1,
            type=str,
            required=True,
            help="stores the markdown file name for further processing",
        )

    def _add_markdown_file_path_argument(parser):
        parser.add_argument(
            "-m",
            "--markdown",
            action="store",
            nargs=1,
            type=str,
            required=True,
            help="stores the path to the directory containing your markdown posts",
        )

    def _add_html_file_path_argument(parser):
        parser.add_argument(
            "-ht",
            "--html",
            action="store",
            nargs=1,
            type=str,
            required=True,
            help="stores the path to the directory containing generated HTML",
        )

    def _add_class_names_argument(parser):
        parser.add_argument(
            "-c",
            "--classes",
            action="store",
            nargs=argparse.REMAINDER,
            type=str,
            required=False,
            help="stores the class names you would like to be added to\
                generated HTML. Format: ... -c h1=post-title h2=post-heading\
                and so on. Provide as many or as little HTML tags as desired.\
                Please ensure that you don't write `h1 = post-title`; this will\
                be interpreted as 3 different flag values (h1, =, post-title)",
        )
    
    def _add_hr_argument(parser):
        parser.add_argument(
            "-hr",
            "--hrule",
            action="store",
            nargs=1,
            type=bool,
            required=False,
            help="stores a boolean representing whether you would like to add\
                an <hr> tag after the title, author and date",
        )

    parser = argparse.ArgumentParser(
        description="Convert Markdown files into blog-specific HTML."
    )

    _add_markdown_filename_argument(parser)
    _add_markdown_file_path_argument(parser)
    _add_html_file_path_argument(parser)
    _add_class_names_argument(parser)
    _add_hr_argument(parser)

    return parser.parse_args()  # Fmt: Namespace(filename=['sample-post'])


def _get_argument_values(args):
    def _parse_args_for_file_name(args):
        return args.filename[0]

    def _append_file_extension_if_missing(filename):
        if ".md" not in filename:
            filename += ".md"
        return filename

    def _parse_args_for_markdown_path(args):
        return args.markdown[0]

    def _parse_args_for_html_path(args):
        return args.html[0]

    def _parse_args_for_class_names(args):
        if args.classes:
            for tag_and_class_name in args.classes:
                tag, class_name = tag_and_class_name.split("=")
                HTML_TAG_TO_CLASS_NAME_MAPPING[tag] = class_name
    
    def _parse_args_for_hr(args):
        return bool(args.hrule[0]) if args.hrule else None

    filename = _parse_args_for_file_name(args)
    filename = _append_file_extension_if_missing(filename)
    markdown_path = _parse_args_for_markdown_path(args)
    html_path = _parse_args_for_html_path(args)
    _parse_args_for_class_names(args)
    add_hr = _parse_args_for_hr(args)

    return filename, markdown_path, html_path, add_hr


def _get_markdown_text_from_file(filename, markdown_path):
    with open(markdown_path + filename) as f:
        return f.read()


def _get_date_and_author(markdown_text):
    date = ""
    author = ""

    number_of_percent_signs = 0
    current_word = []
    for x in markdown_text:
        if x == "%":
            number_of_percent_signs += 1

            if number_of_percent_signs == 1:
                date = "".join(current_word)
                current_word = []

            if number_of_percent_signs == 2:
                author = "".join(current_word)
                break
        else:
            current_word.append(x)

    return date, author


def _convert_markdown_to_html(markdown_text):
    def _strip_date_and_author_line_from_markdown(markdown_text):
        sentinel_character = "%"
        percent_signs_positions = [
            pos for pos, char in enumerate(markdown_text) if char == sentinel_character
        ]
        char_after_second_percent_sign_idx = percent_signs_positions[1] + 2
        char_after_second_percent_sign = markdown_text[
            char_after_second_percent_sign_idx
        ]

        if char_after_second_percent_sign == "\n":
            return markdown_text[char_after_second_percent_sign_idx + 1 : :]
        else:
            return markdown_text[char_after_second_percent_sign_idx::]

    def _markdown2_converter(markdown_text):
        markdowner = markdown2.Markdown()
        html = markdowner.convert(markdown_text)
        return html

    markdown_text = _strip_date_and_author_line_from_markdown(markdown_text)
    return _markdown2_converter(markdown_text)


def _add_classes_to_html(html):
    def _convert_html_to_soup(html):
        soup = bs(html, "lxml")
        return _remove_html_and_body_tags_from_soup(soup)

    def _remove_html_and_body_tags_from_soup(soup):
        for tag in ("html", "body"):
            if hasattr(soup, tag):
                getattr(soup, tag).unwrap()
        return soup

    def _add_classes(soup):
        for html_tag, class_name in HTML_TAG_TO_CLASS_NAME_MAPPING.items():
            tag_list = soup.find_all(html_tag)
            for tag in tag_list:
                tag["class"] = class_name
        return soup

    soup = _convert_html_to_soup(html)
    soup = _add_classes(soup)
    return soup


def _add_date_and_author_to_html(soup, date, author, add_hr):
    def _reformat_date(date):
        month, day, year = [int(x) for x in date.split("/")]
        time_collection = (
            year,
            month,
            day,
            0,
            0,
            0,
            0,
            0,
            0,
        )
        return _custom_strftime(time_collection, day)

    def _custom_strftime(time_collection, day):
        formatted_month_and_day = time.strftime(
            "%B %d", time.localtime(time.mktime(time_collection))
        )
        suffix = _suffix(day)
        formatted_year = time.strftime(
            "%Y", time.localtime(time.mktime(time_collection))
        )
        return formatted_month_and_day + suffix + ", " + formatted_year

    def _suffix(d):
        return "th" if 11 <= d <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(d % 10, "th")

    h1 = soup.find("h1")

    if author:
        author_tag = soup.new_tag("p")
        author_tag.append(author)
        author_tag["class"] = "post-author"
        h1.insert_after(author_tag)

    if date:
        date = _reformat_date(date)
        date_tag = soup.new_tag("p")
        date_tag.append(date)
        date_tag["class"] = "post-date"
        h1.insert_after(date_tag)
    
    if add_hr:
        hr_tag = soup.new_tag("hr")

        if author:
            author_tag.insert_after(hr_tag)
        elif not author and date:
            date_tag.insert_after(hr_tag)
        else:
            h1.insert_after(hr_tag)

    return soup


def _prettify_html(html):
    return html.prettify()


def _write_html_to_file(html, filename, html_path):
    def _convert_md_file_extension_to_html(filename):
        return filename.replace(".md", ".html")

    html_filename = _convert_md_file_extension_to_html(filename)

    with open(html_path + html_filename, "w") as f:
        f.write(html)


def main():
    helldive()


if __name__ == "__main__":
    main()
