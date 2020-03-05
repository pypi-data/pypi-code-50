def convert_source_file_to_user_command(source_file):
    print(source_file)
    with open(source_file, "r") as f:
        content = f.read()

    return """cat <<EOF > app.py
{}
EOF
python app.py""".format(
        content
    )


def get_job_body(jobName, imageName, gpuType, gpu, cpu, mem, userCmd, userId):
    return {
        "jobName": jobName,
        "imageName": imageName,
        "gpuType": gpuType,
        "gpu": gpu,
        "cpu": cpu,
        "mem": mem,
        "comment": "",
        "userCmd": userCmd,
        "userId": "exntu",
        "tags": [],
        "interactive": False,
    }
