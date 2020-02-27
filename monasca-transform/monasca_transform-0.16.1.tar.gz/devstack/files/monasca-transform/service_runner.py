# Copyright 2016 Hewlett Packard Enterprise Development Company LP
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import sys

activate_this_file = "/opt/monasca/transform/venv/bin/activate_this.py"
execfile(activate_this_file, dict(__file__=activate_this_file))

from monasca_transform.service.transform_service import main_service


def main():
    main_service()


if __name__ == "__main__":
    main()
    sys.exit(0)
