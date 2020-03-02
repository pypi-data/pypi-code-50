def gen_model_file_name(project_slug, model_slug, version, suffix):
    name = f"AI_{project_slug}_{model_slug}_{version}.{suffix}"
    return name


def model_upload_to(instance, filename):
    return f'model_file/{instance.gen_model_file_name()}'
