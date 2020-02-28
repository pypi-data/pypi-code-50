import os

_env_variables = [
    ("debug_mode", "ENABLE_DEBUG_MODE", False, bool),
    ("flink_home", "FLINK_HOME", "/opt/flink-1.9.0"),
    ("alink_deps_dir", "ALINK_DEPS_DIR", ""),
    ("local_ip", "LOCAL_IP", "localhost"),

    ("collect_storage_root", "ALINK_COLLECT_STORAGE_ROOT", os.getcwd()),
    ("collect_storage_type", "ALINK_COLLECT_STORAGE_TYPE", "memory"),   # memory, csv, minio
    ("collect_storage_path", "ALINK_COLLECT_STORAGE_PATH", "/notebook_tmp_storage"),
]

g_config = {}

for entry in _env_variables:
    env_v = os.getenv(entry[1], entry[2])
    if len(entry) > 3:
        env_v = entry[3](env_v)
    g_config[entry[0]] = env_v
