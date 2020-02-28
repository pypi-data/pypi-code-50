from django.template.loader import render_to_string
import os


def create_file_path(path, exists_message=None):
    try:
        os.makedirs(path)
    except FileExistsError:
        if exists_message is None:
            exists_message = '{} already exists'.format(path)
        print (exists_message)
    except OSError as e:
        raise Exception(e)


def template_to_out(path_to_template, context, file_path=None):
    template_string = render_to_string(
        path_to_template,
        context=context
    )
    if file_path:
        with open(file_path, 'w') as f:
            f.write(template_string)
            print('Created file: {}'.format(file_path))
    return template_string
