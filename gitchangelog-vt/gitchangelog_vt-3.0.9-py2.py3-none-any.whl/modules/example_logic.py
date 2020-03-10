import re
import pystache


## Method implementation that allows users to see requests (tags or commits)
def see_request_filter(var_to_show):
    try:
        if len(var_to_show) == 2:
            first_ = var_to_show[0]
            second_ = var_to_show[1]

            return "From %s to %s." % (first_, second_)

        else:
            return False

    except ValueError:
        return False


def get_repository_url(repository, commit):
    """try:
        id = commit.sha1_short
        url = repository.git.config('remote.origin.url')

        if url:
            p_url = url[:4]

            if p_url == "git@":
                url_r = url.replace(":", "/")
                this_r = url_r[4:]
                final_r = this_r[:-4]
                p_url = "https://"
                final_url_g = p_url + final_r + "/commit/" + id
                return final_url_g

            else:
                new_url = url[:-4]
                final_url = new_url + "/commit/" + id
                return final_url

        else:
            return url

    except Exception:
        return None"""

    return "https://gitlab.com"


## Dividing commits
def commit_split_a(general_split):
    t_split = []
    to_string = list(general_split)
    this_list = []
    new_list = []
    for i in general_split:
        this_list.append(i)
        to_string.remove(i)
        string = "".join(to_string)

        if i == ":":
            new_list.append(string)  ## Removing first []
            break

    second_split = "".join(new_list)
    first_split = "".join(this_list)
    ## Save the SGI:...
    t_split.append(first_split)
    ## Save what it has after of SGI:
    t_split.append(second_split)
    return t_split  ## It should return SGI:...


def commit_split_b(first_split):
    second_split = first_split[1]
    third_split = []
    n_spaces = second_split.lstrip()
    to_split = n_spaces.split(" ")

    the_identifier = str(to_split[0])

    del(to_split[0])
    final_s = " ".join(to_split)

    ## Save the identifiers. For example, NONE, ANTA, etc.
    third_split.append(the_identifier)
    ## Save the complement after the  identifier
    third_split.append(final_s)

    return third_split


## Add link for others jiras.
def find_replace(second_split, jira_url):
    complement = second_split[1]

    ## Accessing Mustache directly.
    renderer = pystache.Renderer()
    parsed = pystache.parse(
        u"{{#render}}[{{{.}}}]({{#link}}{{.}}{{/link}}/{{{.}}}){{/render}}")

    to_render = renderer.render(parsed, {
        'render': r'\1',
        'link': jira_url
    })
    to_change = re.sub(r'([A-Z]+-[\d]+)', to_render, complement)

    return to_change


def commit_message(commit, jira_url):
    general_split = commit.subject
    first_split = commit_split_a(general_split)
    second_split = commit_split_b(first_split)
    to_change = find_replace(second_split, jira_url)
    if re.search(r"^[A-Z]+-[\d]+$", second_split[0]):
        links_or_not = True

    else:
        links_or_not = False

    s_dictionary = {
        "only_sgi": first_split[0],
        "jira_identifier": second_split[0],
        "complement": to_change,
        "links_or_not": links_or_not,
    }
    return s_dictionary
