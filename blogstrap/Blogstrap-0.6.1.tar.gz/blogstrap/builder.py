# Copyright 2015 Joe H. Rahme <joehakimrahme@gmail.com>
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
import os


APP_TEMPLATE = """import os

from blogstrap import create_app

BASE = os.path.dirname(os.path.abspath(__file__))
config = lambda x: os.path.join(BASE, x)

application = create_app(config('blogstrap.conf'))

if __name__ == '__main__':
    application.run()
"""

CONF_TEMPLATE = """# The path of a directory that holds the markdown articles
BLOGROOT = "BLGRT"
# The title will be added to the top banner in every page
BLOGTITLE = "Generated with BlogStrap"
# Make the app more verbose when necessary. Don't use in production.
DEBUG = False
"""

HOMEPAGE_TEMPLATE = """# This page will be displayed at the blog root
HOMEPAGE = "homepage_blogstrap"
"""


def build(args):
    bstrp_conf_path = os.path.join(args.target, '.blogstrap')
    app_path = os.path.join(bstrp_conf_path, 'wsgi.py')
    conf_path = os.path.join(bstrp_conf_path, 'blogstrap.conf')

    if not os.path.exists(args.target):
        os.makedirs(args.target)

    if not os.path.exists(bstrp_conf_path):
        os.makedirs(bstrp_conf_path)

    with open(app_path, 'w') as wsgi_file:
        wsgi_file.write(APP_TEMPLATE)

    if not args.no_homepage:
        config_template = CONF_TEMPLATE + HOMEPAGE_TEMPLATE
        homepage_path = os.path.join(args.target, "homepage_blogstrap")
        with open(homepage_path, 'w') as homepage_file:
            homepage_file.write("Hello Blogstrap!\n")
    else:
        config_template = CONF_TEMPLATE

    with open(conf_path, 'w') as config_file:
        # Before writing the template to disk, we fill in the blogroot's
        # absolute path
        full_target = os.path.abspath(args.target)
        config_file.write(config_template.replace("BLGRT", full_target))
