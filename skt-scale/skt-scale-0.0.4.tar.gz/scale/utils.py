def convert_source_file_to_user_command(source_file):
    with open(source_file, "r") as f:
        content = f.read()

    return """cat <<EOF > app.py
{}
EOF
python app.py""".format(
        content
    )


def get_job_body(
    job_name, image_name, gpu_type, gpu, cpu, mem, user_cmd, user_id
):
    return {
        "jobName": job_name,
        "imageName": image_name,
        "gpuType": gpu_type,
        "gpu": gpu,
        "cpu": cpu,
        "mem": mem,
        "comment": "",
        "userCmd": user_cmd,
        "userId": user_id,
        "tags": [],
        "interactive": False,
    }
