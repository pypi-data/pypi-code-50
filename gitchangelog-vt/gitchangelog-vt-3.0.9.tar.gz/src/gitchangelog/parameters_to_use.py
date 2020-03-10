## Cleaner parameters
def parameter_to_clean(opts):
    if opts.clean:
        cleaner = opts.clean
        return cleaner

    else:
        return None


## Title parameters
def change_title(opts):
    try:
        if opts.title:
            new_title = opts.title
            return " ".join(new_title)

        elif opts.title is []:
            return "Changelog"

        else:
            return "Changelog"

    except TypeError:
        return "Changelog"


## Parameters to show
def parameter_to_show(opts):
    try:
        if opts.show:
            to_show = opts.show
            return to_show

        else:
            return
    except TypeError:
        return None


## url parameters
def change_jira_url(opts, jira_url):
    try:
        if opts.url:
            new_url = opts.url
            return " ".join(new_url)

        else:
            return jira_url

    except TypeError:
        return None


## file parameters
def give_file_name(opts):
    try:
        if opts.file:
            new_file = opts.file
            return " ".join(new_file)

        else:
            return None

    except TypeError:
        return None


## Template parameters
def change_template(opts, config):
    if opts.template:
        try:
            from gitchangelog import mustache
        except Exception:
            from gitchangelog.gitchangelog import mustache

        new_route = " ".join(opts.template)
        config["output_engine"] = mustache(new_route)
        return config["output_engine"]

    else:
        pass


## To modules
def module_implementation(opts):
    if opts.module:
        module_to_show = " ".join(opts.module)
        return module_to_show

    else:
        pass