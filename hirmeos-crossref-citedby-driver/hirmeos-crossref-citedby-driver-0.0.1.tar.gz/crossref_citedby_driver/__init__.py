from datetime import datetime
from collections import defaultdict, namedtuple
import sys

from bs4 import BeautifulSoup
import requests


Citation = namedtuple('Citation', ['cited_by', 'timestamp'])


def fetch_citation_xml(
        username,
        password,
        doi_prefix,
        start_date,
        end_date,
        api_url='https://doi.crossref.org/servlet/getForwardLinks'
):
    """Fetch raw XML data response from Crossref.

    Args:
        username (str): Crossref username.
        password (str): Crossref password.
        doi_prefix (str): DOI prefix associated with Crossref account.
        start_date (str): Date to start searching from, as YYYY-MM-DD.
        end_date (str): Date to search until, as YYYY-MM-DD
        api_url (str): Crossref cited-by API endpoint

    Returns:
        tuple: string response and int status code.
    """
    params = {
        'usr': username,
        'pwd': password,
        'doi': doi_prefix,
        'startDate': start_date,
        'endDate': end_date,
    }

    response = requests.get(api_url, params=params)

    if response.status_code != 200:
        sys.stderr.write(
            f'Could not retrieve cited-by citations ({response.reason})'
            f' - Request parameters: {params}); url: {api_url}'
        )

    return response.text, response.status_code


def get_crossref_citations(xml_content, doi_prefix):
    """Extract raw data from Crossref citation XML for correct DOIs only.

    Args:
        xml_content (str): XML data returned from Crossref.
        doi_prefix (str): Prefix of DOIs searched for.

    Returns:
        dict: Each DOI that is cited and the citation entries for that DOI.
    """

    xml_data = BeautifulSoup(xml_content, 'lxml')

    relevant_entries = filter(
        lambda x: x.attrs.get('doi', '').startswith(doi_prefix),
        xml_data.find_all('forward_link')
    )

    citations = defaultdict(list)
    for entry in relevant_entries:
        doi = entry.attrs.get('doi')
        citations[doi].extend(entry.find_all('journal_cite'))
        citations[doi].extend(entry.find_all('book_cite'))

    return citations


def determine_timestamp(year, file_date):
    """Gets a 'best guess' for the timestamp when the citation occurred.

    Args:
        year (str): Citation year recorded in the Crossref entry.
        file_date (str): Date stamp in file name - based on the date queried in
            crossref when retrieving the citation (YYYY-MM-DD).

    Returns:
        str: Timestamp for citation in the form YYYY-MM-DD.
    """
    timestamp = datetime.strptime(file_date, '%Y-%m-%d')

    if timestamp.year != int(year):
        timestamp = datetime.strptime(year, '%Y')

    return timestamp.strftime('%Y-%m-%d 00:00:00')


def get_citation_data(citation_entry, citation_date):
    """Get citation data data from parsed Crossref XML.

    Args:
        citation_entry (bs4.element.Tag): Citation from querying Crossref.
        citation_date (str): Timestamp when citation was queried (YYYY-MM-DD).

    Returns:
        Citation: containing cited-by DOI and timestamp.
    """
    cited_by = citation_entry.find('doi').text
    year = citation_entry.find('year').text
    timestamp = determine_timestamp(year, citation_date)

    return Citation(cited_by=cited_by, timestamp=timestamp)
