# This is replaced during release process.
__version_suffix__ = '110'

APP_NAME = "zalando-kubectl"

KUBECTL_VERSION = "v1.16.7"
KUBECTL_SHA512 = {
    "linux": "df4b8ef210f5daf5b75000f2ebc54c3e10d0f30da97adcd83eeef7bd3f193df440c47da73bc71e83dae8d52a3ea7251d2b3293c84594da36187d193a5d26576f",
    "darwin": "6379aa1a10dd6922ca4ef4e03d34c0ab02a7c955052f533c2023b34f9b79f27baec0adcee0f0da83e034de019f4c0c66738e4879505016dc47a70a57b44b100e",
}

STERN_VERSION = "1.10.0"
STERN_SHA256 = {
    "linux": "a0335b298f6a7922c35804bffb32a68508077b2f35aaef44d9eb116f36bc7eda",
    "darwin": "b91dbcfd3bbda69cd7a7abd80a225ce5f6bb9d6255b7db192de84e80e4e547b7",
}

APP_VERSION = KUBECTL_VERSION + "." + __version_suffix__
