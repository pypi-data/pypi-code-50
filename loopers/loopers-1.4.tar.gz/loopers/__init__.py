import re
from bs4 import BeautifulSoup
from requests import get

name = "loopers"


def regex(parsed_html):
    email_regex = re.compile(r'''(
                [a-zA-Z0-9._%+-]+
                @
                [a-zA-Z0-9.-]+
                (\.[a-zA-Z]{2,4})
                )''', re.VERBOSE)
    try:
        text = str(parsed_html)
        matches = set([groups[0] for groups in email_regex.findall(text)])
        return matches if matches else None
    except Exception as err:
        print(" {} \nFailed to read page!".format(err))
        return None


def loop(*urls):
    """

    :param urls:
    :return a dictionary:

    Dictionary keys:
     emails: A list of emails found in the page
     n_links: Number of links found in the page
     links: A list/array of links found in the page
    """
    all_urls = {}
    for url in urls:
        url_dict = {}
        print("Opening link: {}".format(url))
        if url.startswith('http') or url.startswith('https:'):
            pass
        else:
            url = 'https://' + url
        header = get(url)
        parsed_html = BeautifulSoup(header.content, features='html.parser')

        list_link = [link.attrs['href'] for link in parsed_html.findAll('a') if 'href' in link.attrs]

        links = set(
            [a for a in list_link if a.startswith('https://') or a.startswith('http://') or a.startswith('/')])

        new_link = []
        for link in links:
            if link.startswith('/'):
                new_link.append(url + link)
            else:
                new_link.append(link)
        all_emails = regex(parsed_html)
        url_dict['emails'] = all_emails
        try:
            if len(list(new_link)) > 0:
                url_dict['n_links'] = len(new_link)
                url_dict['links'] = new_link
                all_urls[url] = url_dict
            else:
                print('[--] No links generated')
        except Exception as err:
            print('[ALERT!] An error occurred\n{}'.format(err))
    return all_urls
