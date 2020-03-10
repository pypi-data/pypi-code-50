import re
import pystache


def see_request_filter(var_to_show):
    try:
        if len(var_to_show) == 2:
            first_request = var_to_show[0]
            second_request = var_to_show[1]

            return "Instance review from %s to %s." % (first_request, second_request)

        else:
            return False

    except ValueError:
        return False


def send_parser(commit, repository, jira_url, template_data):
    commit_message(commit, jira_url)
    template_data["commit_url"] = get_repository_url(repository, commit)
    template_data["only_sgi"] = commit_dictionary["only_sgi"]
    template_data["second_parameter"] = commit_dictionary["jira_identifier"]
    template_data["commit_title"] = commit_dictionary["complement"]
    template_data["links_or_not"] = commit_dictionary["links_or_not"]

    return template_data


commit_dictionary = {}


def commit_message(commit, jira_url):
    general_split = commit.subject
    first_split = separating_sgi(general_split)
    second_split = getting_identifier(first_split)
    edit_complement = find_replace(general_split, jira_url)
    if re.search(r'^[A-Z]+-[\d]+$', second_split[0]):
        links_or_not = True

    else:
        links_or_not = False

    commit_dictionary["only_sgi"] = first_split[0]
    commit_dictionary["jira_identifier"] = second_split[0]
    commit_dictionary["complement"] = edit_complement
    commit_dictionary["links_or_not"] = links_or_not


def get_repository_url(repository, commit):
    try:
        id = commit.sha1_short
        url = repository.git.config('remote.origin.url')

        if url:
            protocol_url = url[:4]

            if protocol_url == "git@":
                replace_url = url.replace(":", "/")
                replace = replace_url[4:]
                final_replace = replace[:-4]
                protocol_url = "https://"
                final_url_g = protocol_url + final_replace + "/commit/" + id
                return final_url_g

            else:
                new_url = url[:-4]
                final_url = new_url + "/commit/" + id
                return final_url

        else:
            return url

    except Exception:
        return None


def separating_sgi(general_split):
    final_split = []
    commit_list = list(general_split)
    list_to_sgi = []
    commit_identifier = []
    for i in general_split:
        list_to_sgi.append(i)
        commit_list.remove(i)
        commit_string = "".join(commit_list)

        if i == ":":
            commit_identifier.append(commit_string)  ## Removing first []
            break

    second_split = "".join(commit_identifier)
    first_split = "".join(list_to_sgi)
    ## Save the SGI:...
    final_split.append(first_split)
    ## Save what it has after of SGI:
    final_split.append(second_split)
    return final_split  ## It should return SGI:...


def getting_identifier(first_split):
    second_split = first_split[1]
    third_split = []
    not_spaces = second_split.lstrip()
    new_split = not_spaces.split(" ")

    the_identifier = str(new_split[0])

    del (new_split[0])
    final_split = " ".join(new_split)

    ## Save the identifiers. For example, NONE, ANTA, etc.
    third_split.append(the_identifier)
    ## Save the complement after the  identifier
    third_split.append(final_split)

    return third_split


def find_replace(general_split, jira_url):
    ## Accessing Mustache directly.
    renderer = pystache.Renderer()
    parsed = pystache.parse(
        u"{{#render}}[{{{.}}}]({{#link}}{{.}}{{/link}}/{{{.}}}){{/render}}")

    render = renderer.render(parsed, {
        'render': r'\1',
        'link': jira_url
    })

    edit_complement = re.sub(r'([A-Z]+-[\d]+)', render, general_split)
    if re.search(r'(^[A-Za-z]{3}:)', edit_complement):
        ignore_sgi = edit_complement.split(" ")
        ## Deleting SGI more identifier NONE or jira for convenience.
        del (ignore_sgi[0])  ## Deleting SGI.

        if len(ignore_sgi) > 0:
            del (ignore_sgi[0])  ## Deleting Identifier.

        return " ".join(ignore_sgi)
    else:
        return edit_complement