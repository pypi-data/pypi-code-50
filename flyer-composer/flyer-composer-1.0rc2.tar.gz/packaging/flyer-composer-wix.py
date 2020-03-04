"""
https://github.com/sk1project/wixpy/blob/master/docs/writing-json.md
"""

import wixpy
# HACK: Make wixpy minimally work with Python 3
import builtins; builtins.long = int ; builtins.basestring = str

import packaging.version
import pkginfo

meta_data = pkginfo.get_metadata("flyer_composer")
VERSION = meta_data.version

def version_to_numbers(ver):
    """
    7 numbers:
      (major, minor, micro,
      (1=alpha,2=beta,3=rc,5=release,9=post), #num
      (0=dev,1=non-dev), #dev)
    """
    ver = packaging.version.parse(ver)
    assert not isinstance(ver, packaging.version.LegacyVersion), \
        "is a legacy version: %s" % ver
    parts = [ver.major, ver.minor, ver.micro]
    if ver.pre is not None:
        parts += [('a', 'b', 'rc').index(ver.pre[0]) + 1 , ver.pre[1]]
    elif ver.post is not None:
        parts += [9, ver.post]
    else:
        parts += [5, 0]
    if ver.dev is not None:
        parts += [0, ver.dev]
    else:
        parts += [1, 0]
    return '.'.join(map(str, parts))

# Language codes from <https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-lcid/70feba9f-294e-491e-b6eb-56532684c37f>
LANG_de    = 0x0007 # 7
LANG_en    = 0x0009 # 9
LANG_de_DE = 0x0407 # 1031
LANG_en_US = 0x0409 # 1033

# see  https://github.com/sk1project/wixpy/blob/master/docs/writing-json.md
MIN_OS_WIN7 = 601  # also Windows Server 2008R2

MSI_DATA = {
    "Name": "Flyer Composer",
    "UpgradeCode": "974692B0-8AEE-4A76-9CA3-5A3BDFFF36AD",
    "Version": version_to_numbers(VERSION),  # Must be numbers only!
    "Manufacturer": "Hartmut Goebel - Crazy Compilers",
    "Description": "Flyer Composer %s Installer" % VERSION,
    "Comments": "Licensed under GNU Affero General Public License v3 or later (AGPLv3+)",
    "Keywords": "pdf, flyer, leaflet",
    "Win64": True,
    "Codepage": "1251",
    "SummaryCodepage": "1251",
	"Language": str(LANG_en_US),
    "Languages": ",".join(map(str, (
        LANG_en, #LANG_en_US, #str(LANG_en_GB),
        #LANG_de, LANG_de_DE
    ))),
    "_OsCondition": str(MIN_OS_WIN7),
    "_CheckX64": True,
    "_Conditions": [],
    #"_AppIcon": "../artwork/projecticon.ico", # where is this used?
    "_Icons": [],
    "_ProgramMenuFolder": "PDF Tools",
    "_Shortcuts": [
        {"Name": "Flyer Composer",
         "Description": "Rearrange PDF pages to print as flyers on one paper",
         "Target": "flyer-composer-gui.exe",
         "AddOnDesktop": True,
         "OpenWith": [".pdf"],
         "Open": [],
        }
    ],
    "_AddToPath": [""],  # yes, add to path in front
    "_AddBeforePath": [],
    "_SourceDir": "dist/flyer-composer",
    "_InstallDir": "Flyer Composer",
    "_OutputName": "flyer-composer-%s-win64.msi" % VERSION,
    "_OutputDir": "./",
    "_SkipHidden": True,
}

# Verify version
try:
    [int(n) for n in MSI_DATA["Version"].split(".")]
except ValueError:
    raise SystemExit("`Version` must only be numbers")

wixpy.build(MSI_DATA)
