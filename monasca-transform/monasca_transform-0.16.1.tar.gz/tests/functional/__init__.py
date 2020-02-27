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

# Add the location of Spark to the path
# TODO(someone) Does the "/opt/spark/current" location need to be configurable?
import os
import sys

try:
    sys.path.append(os.path.join("/opt/spark/current", "python"))
    sys.path.append(os.path.join("/opt/spark/current",
                                 "python", "lib", "py4j-0.10.4-src.zip"))
except KeyError:
    print("Error adding Spark location to the path")
    # TODO(someone) not sure what action is appropriate
    sys.exit(1)
