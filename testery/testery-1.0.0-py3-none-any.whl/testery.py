import click
import requests
import time
import sys
import os
import mimetypes
from requests_toolbelt.multipart.encoder import MultipartEncoder

headers = {'Content-type': 'application/json', 'Accept': 'application/json'}


def report_teamcity_test_run(test_run):
    if test_run['status'] == 'FAIL':
        print("##teamcity[buildProblem description='%s: %s passing, %s failing out of %s total']" % (
            test_run['status'], test_run['passCount'], test_run['failCount'], test_run['totalCount']))
    else:
        print("##teamcity[buildStatus text='%s: %s passing, %s failing out of %s total']" % (
            test_run['status'], test_run['passCount'], test_run['failCount'], test_run['totalCount']))


def api_wait_test_run(api_url, token, test_run_id, output, fail_on_failure):
    headers['Authorization'] = "Bearer " + token

    test_run = requests.get(api_url + '/test-run-results/' + str(test_run_id), headers=headers).json()

    while test_run['status'] not in ['PASS', 'FAIL', 'CANCEL']:

        test_run = requests.get(api_url + '/test-run-results/' + str(test_run_id), headers=headers).json()
        print(test_run)
        report_teamcity_test_run(test_run)
        time.sleep(10)

    if output == "teamcity":
        report_teamcity_test_run(test_run)
    else:
        print(test_run)

    if (test_run['status'] == 'FAIL' or test_run['status'] == 'CANCEL') and fail_on_failure:
        sys.exit(1)


@click.group()
def cli():
    """
    Testery CLI\n
    Kick off test runs from your CI/CD platform and run them on Testery's next-generation, cloud-based testing grid.
    """
    pass


@click.command('verify-token')
@click.option('--api-url', default='https://api.testery.io/api', help='The URL for the Testery API. Only required for development purposes.')
@click.option('--token', help='Your Testery API token.')
def verify_token(api_url, token):
    """
    Verifies your username and authentication token are valid.
    """
    headers['Authorization'] = "Bearer " + token

    response = requests.get(api_url + '/account', headers=headers)

    print(response.json())

@click.command('create-test-run')
@click.option('--api-url', default='https://api.testery.io/api', help='The URL for the Testery API. Only required for development purposes.')
@click.option('--token', help='Your Testery API token.')
@click.option('--git-org', help='Your git organization name.')
@click.option('--git-repo', help='Your git repository name.')
@click.option('--git-ref', help='The git commit hash of the build being tested.')
@click.option('--wait-for-results', is_flag=True, help='If set, the command will poll until the test run is complete.')
@click.option('--project', help='A unique identifier for your project.')
@click.option('--environment', help='Which environment you would like to run your tests against.')
@click.option('--include-tags', help='List of tags that should be run.')
@click.option('--feature-paths', help='List of directories with feature files that should be run.')
@click.option('--copies', help='The number of copies of the tests to submit.')
@click.option('--build-id', help='A unique identifier that identifies this build in your system.')
@click.option('--output', default='json', help='The format for outputting results [json,pretty,teamcity,appveyor]')
@click.option("--fail-on-failure", is_flag=True, help='When set, the testery command will return exit code 1 if there are test failures.')
@click.option("--include-all-tags", is_flag=True, help='When set, overrides the testery.yml and runs all available tags.')
@click.option("--runner", help='Overrides the test runner for this test run instead of using the account default.')
def create_test_run(api_url, token, git_org, git_repo, git_ref, wait_for_results, output, project, environment, include_tags, feature_paths, copies, build_id, fail_on_failure, include_all_tags, runner):
    """
    Submits a Git-based test run to the Testery platform.
    """
    test_run_request = {"owner": git_org, "repository": git_repo, "ref": git_ref, "project": project, "environment": environment,
                        "buildId": build_id, "runner": runner}                  

    
    if include_tags:
        test_run_request['includeTags'] = include_tags.split(',')

    if feature_paths:
        test_run_request['directories'] = feature_paths.split(',')

    if include_all_tags:
        test_run_request['includeTags'] = []

    if copies:
        test_run_request['copies'] = copies
    
    print(test_run_request)

    headers['Authorization'] = "Bearer " + token
    test_run_response = requests.post(api_url + '/test-run-requests-build',
                                      headers=headers,
                                      json=test_run_request)

    print(test_run_response)

    test_run = test_run_response.json()

    print(test_run)

    test_run_id = str(test_run['id'])

    click.echo("test_run_id: %s" % test_run_id)

    if wait_for_results:
        api_wait_test_run(api_url, token, test_run_id, output, fail_on_failure)

@click.command('cancel-test-run')
@click.option('--api-url', default='https://api.testery.io/api', help='The URL for the Testery API. Only required for development purposes.')
@click.option('--token', help='Your Testery API token.')
@click.option('--test-run-id', help='The ID of the test run to cancel.')
def cancel_test_run(api_url, token, test_run_id):
    """
    Cancels a test run.
    """
    headers['Authorization'] = "Bearer " + token

    test_run = requests.get(api_url + '/test-run-results/' + str(test_run_id), headers=headers).json()

    if test_run['status'] not in ['PASS', 'FAIL', 'CANCEL']:

      test_run_response = requests.patch(api_url + '/test-runs/' + test_run_id,
                                      headers=headers,
                                      json={"status": "CANCEL"})

      print(test_run_response)

      test_run = test_run_response.json()

      print(test_run)


@click.command('add-file')
@click.option('--api-url', default='https://api.testery.io/api', help='The URL for the Testery API. Only required for development purposes.')
@click.option('--token', help='Your Testery API token.')
@click.option('--test-run-id', help='The ID of the test run to add the file to.')
@click.option('--kind', help='The kind of file you are uploading. For an nCover JSON file put ncover')
@click.argument('file_path')
def add_file(api_url, token, test_run_id, file_path, kind):
    """
    Adds a file to a test run.
    """
    headers['Authorization'] = "Bearer " + token

    file_name = os.path.basename(file_path)
    mime_type = mimetypes.guess_type(file_path)[0]

    if mime_type is None:
        mime_type = 'text/plain'

    data = MultipartEncoder(fields={'file': (file_name, open(file_path, 'rb'), mime_type)})
    
    headers['Content-Type'] = data.content_type

    url = api_url + '/test-runs/' + str(test_run_id) + '/add-file/' + kind

    test_run = requests.post(url, headers=headers, data=data).json()

    print(test_run)

@click.command('monitor-test-run')
@click.option('--api-url', default='https://api.testery.io/api', help='The URL for the Testery API. Only required for development purposes.')
@click.option('--token', help='Your Testery API token.')
@click.option('--test-run-id', help='The ID for the test run you would like to monitor and wait for.')
@click.option("--fail-on-failure", is_flag=True, help='When set, the testery command will return exit code 1 if there are test failures.')
@click.option('--output', default='json', help='The format for outputting results [json,pretty,teamcity,appveyor]')
def monitor_test_run(api_url, token, test_run_id, output, fail_on_failure):
    api_wait_test_run(api_url, token, test_run_id, output, fail_on_failure)


@click.command('monitor-test-runs')
@click.option('--api-url', default='https://api.testery.io/api', help='The URL for the Testery API. Only required for development purposes.')
@click.option('--token', help='Your Testery API token.')
@click.option("--fail-on-failure", is_flag=True, help='When set, the testery command will return exit code 1 if there are test failures.')
@click.option('--output', default='json', help='The format for outputting results [json,pretty,teamcity,appveyor]')
def monitor_test_runs(api_url, token, output, fail_on_failure):
    headers['Authorization'] = "Bearer " + token

    if username is None:
        username = os.environ['TESTERY_USERNAME']

    if token is None:
        token = os.environ['TESTERY_TOKEN']

    if organization is None:
        token = os.environ['ORGANIZATION']

    while True:
        test_runs = requests.get(api_url + '/test-runs?page=0&limit=250', headers=headers).json()
        try:
            for test_run in test_runs:
                if test_run['status'] in ['PENDING', 'RUNNING', 'SUBMITTED']:
                    test_run_updated = requests.get(api_url + '/test-run-results/' + str(
                        test_run['id']), headers=headers).json()
                    # print(test_run_updated)
                    print("Test run %s was %s and is now %s. There are %s passing out of %s with %s failing." % (
                        test_run.get('id'), test_run.get('status'), test_run_updated.get('status'), test_run_updated.get('passCount'), test_run_updated.get('totalCount'), test_run_updated.get('failCount')))
                    time.sleep(1)

            print('...')
            time.sleep(60)
        except TypeError:
            print("Invalid response: ", test_runs)
            return False

@click.command('load-users')
@click.option('--api-url', default='https://api.testery.io/api', help='The URL for the Testery API. Only required for development purposes.')
@click.option('--token', help='Your Testery API token.')
@click.option("--user-file", help='List of email addresses to load as user accounts.')
def load_users(api_url, token, user_file):
    headers['Authorization'] = "Bearer " + token

    user_file_data = open(user_file, "r")

    for email in user_file_data:
        print("Adding %s to account" % email.rstrip())

        user_request = {"email": email.rstrip(), "roleType": "USER"}

    
        user_response = requests.post(api_url + '/user-roles', headers=headers, json=user_request)

        print(user_response)

    # while True:
    #     test_runs= requests.get(api_url + '/test-runs?page=0&limit=100', headers=headers).json()
    #     for test_run in test_runs:
    #         if test_run['status'] in ['PENDING','RUNNING','SUBMITTED']:
    #             test_run_updated = requests.get(api_url + '/test-run-results/' + str(test_run['id']), headers=headers).json()
    #             # print(test_run_updated)
    #             print("Test run %s was %s and is now %s. There are %s passing out of %s with %s failing." % (test_run['id'], test_run['status'], test_run_updated['status'], test_run_updated['passCount'], test_run_updated['totalCount'], test_run_updated['failCount']))
        
    #     time.sleep(60)



    

cli.add_command(cancel_test_run)
cli.add_command(create_test_run)
cli.add_command(add_file)
cli.add_command(monitor_test_run)
cli.add_command(monitor_test_runs)
cli.add_command(verify_token)
cli.add_command(load_users)

if __name__ == '__main__':
    cli()
