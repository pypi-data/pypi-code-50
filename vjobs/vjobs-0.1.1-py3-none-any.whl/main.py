import importlib
import pathlib
import pkgutil
import logging

import virden_jobs.facebook_client
import virden_jobs.common.yaml


def _handle_import(name):
    try:
        return importlib.import_module(name)
    except ImportError:
        pass


def get_plugins():
    plugins = {
        name: _handle_import(name)
        for finder, name, ispkg
        in pkgutil.iter_modules()
        if name.startswith('vjobs_')
    }

    return plugins


def _get_formatted_message(job):
    return "{} {} {}".format(
        job.description,
        job.company,
        job.url
        )


def _is_job(job):
    if hasattr(job, 'url') and hasattr(
            job, 'description') and hasattr(job, 'company'):

        return True


def get_jobs(plugins):
    jobs = []
    for key, value in plugins.items():
        try:
            func = getattr(value, 'run')
            plugin_jobs = func()
            jobs.extend([x for x in plugin_jobs if _is_job(x)])
        except AttributeError:
            pass

    return jobs


def _is_in_post(post, job):

    try:  # post['message'] might throw KeyError
        if job.url in post['message']:
            return True
        else:
            return False
    except(KeyError):
        return False


def _is_existing_job(posts, job):

    for post in posts:
        if _is_in_post(post, job):
            return True


def post_jobs_to_facebook(posts, jobs, facebook, page_id):

    for job in jobs:
        if _is_existing_job(posts, job):
            logging.info('Entry already present: ' + str(job))
        else:
            is_posted = facebook.try_post(page_id, _get_formatted_message(job))
            if is_posted[0]:
                logging.info('Posted job: ' + str(job))
            else:
                logging.error(is_posted[1] + ' ' + str(job))


def run():

    logging.basicConfig(level=logging.INFO)
    config_file = pathlib.Path(__file__).parent / 'config.yml'
    config = virden_jobs.common.yaml.load(config_file)
    plugins = get_plugins()
    jobs = get_jobs(plugins)
    facebook = virden_jobs.facebook_client.Facebook()
    facebook.connect(config['token'])
    posts = facebook.get_page_posts(config['page_id'])
    post_jobs_to_facebook(posts, jobs, facebook, config['page_id'])


if __name__ == '__main__':
    run()
