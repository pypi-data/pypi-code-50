import pathlib
from urllib.parse import urljoin

import virden_jobs.common.web_content
import virden_jobs.common.yaml
import virden_jobs.common.job


def _get_jobs(raw_web_content):
    job_collection = raw_web_content.find_all(
        "div", class_="large-6 medium-7 columns")

    lst = []

    for job in job_collection:
        for job_content in job.find_all('a'):
            url = (urljoin(raw_web_content.url, job_content.get('href')))
            ebrandon_job = virden_jobs.common.job.Job(job_content.string, url)
            lst.append(ebrandon_job)
    return lst


def run():
    config_file = pathlib.Path(__file__).parent / 'config.yml'
    config = virden_jobs.common.yaml.load(config_file)

    ebrandon = virden_jobs.common.web_content.RawWebContent()
    ebrandon.populate(config['url'])
    return _get_jobs(ebrandon)
