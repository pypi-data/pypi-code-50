# Copyright 2020 Joe H. Rahme <joehakimrahme@gmail.com>
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


def context(app, message=None):
    def toc():
        result = []
        for entry in os.listdir(app.config['BLOGROOT']):
            if os.path.isfile(entry) and not entry.startswith("."):
                result.append("* [{article}](../{article})".format(
                    article=entry))
        return "\n".join(result)

    context_dict = {
        "author": app.config['AUTHOR'],
        "description": app.config['DESCRIPTION'],
        "lang": app.config['DEFAULT_LANG'],
        "title": app.config['BLOGTITLE'],
        "toc": toc()
    }
    if message:
        context_dict['text'] = message['content']
        context_dict.update(message['metadata'])
    return context_dict
