PROTOCOL_VER = 1.0

BROKER_HANDSHAKE_HEADERS = {
    "AUTH_TOKEN": "x-thundra-auth-token",
    "SESSION_NAME": "x-thundra-session-name",
    "PROTOCOL_VER": "x-thundra-protocol-version"
}

BROKER_WS_HTTP_ERR_CODE_TO_MSG = {
    429: "Reached the concurrent session limit, couldn't start Thundra debugger.",
    401: "Authentication is failed, check your Thundra debugger authentication token.",
    409: "Another session with the same session name exists, connection closed.",
}

OPCODE_BINARY = 0x2

CONFIG_FILE_NAME = "debug-client.json"
THUNDRA_CONFIG_DIR = ".thundra"

FUNCTION_TIMEOUT_CLOSE_CODE = 4500