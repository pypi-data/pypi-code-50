from __future__ import annotations
import attr
from kdsl.bases import K8sObjectBase
from typing import TypedDict, ClassVar


@attr.s(kw_only=True)
class Info(K8sObjectBase):
    """
    | Info contains versioning information. how we'll want to distribute that information.
    
    :param buildDate: None
    :param compiler: None
    :param gitCommit: None
    :param gitTreeState: None
    :param gitVersion: None
    :param goVersion: None
    :param major: None
    :param minor: None
    :param platform: None
    """
    buildDate: str = attr.ib(metadata={'yaml_name': 'buildDate'})
    compiler: str = attr.ib(metadata={'yaml_name': 'compiler'})
    gitCommit: str = attr.ib(metadata={'yaml_name': 'gitCommit'})
    gitTreeState: str = attr.ib(metadata={'yaml_name': 'gitTreeState'})
    gitVersion: str = attr.ib(metadata={'yaml_name': 'gitVersion'})
    goVersion: str = attr.ib(metadata={'yaml_name': 'goVersion'})
    major: str = attr.ib(metadata={'yaml_name': 'major'})
    minor: str = attr.ib(metadata={'yaml_name': 'minor'})
    platform: str = attr.ib(metadata={'yaml_name': 'platform'})


class InfoTypedDict(TypedDict, total=(True)):
    buildDate: str
    compiler: str
    gitCommit: str
    gitTreeState: str
    gitVersion: str
    goVersion: str
    major: str
    minor: str
    platform: str
