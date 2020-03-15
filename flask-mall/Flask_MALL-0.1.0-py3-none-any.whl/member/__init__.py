# -*- coding=utf-8 -*-
from flask import Blueprint


member_module = Blueprint('member', __name__)

from .auth import *
