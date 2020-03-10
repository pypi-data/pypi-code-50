import json
from os import path
from pathlib import Path

import boto3
from AWSIoTPythonSDK.exception.AWSIoTExceptions import connectTimeoutException
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

from ..constants import BASEPATH
from .base import Platform
from .jitp_role import create_jitp_role


class AWSIoT(Platform):
    platform_name = "aws"

    def __init__(self, thing_type):
        self.IOT = boto3.client("iot")
        self.log_level = "DEBUG"
        super().__init__(thing_type)

    @property
    def jitp_role(self):
        return create_jitp_role("wintergreen")

    def _do_get_preferred_common_name(self):
        return self.IOT.get_registration_code().get("registrationCode", None)

    def _do_process_certs(self, ca_cert, verification_cert):
        ca_response = self.IOT.register_ca_certificate(
            caCertificate=ca_cert,
            verificationCertificate=verification_cert,
            setAsActive=True,
            allowAutoRegistration=True,
            registrationConfig=self.registration_config,
        )

        self.IOT.set_v2_logging_options(
            roleArn=self.jitp_role["role_arn"], defaultLogLevel=self.log_level
        )

        thing_type_response = self.IOT.create_thing_type(thingTypeName=self.thing_type)

        return {
            "platform_response": {
                "thingTypeName": thing_type_response["thingTypeName"],
                "thingTypeArn": thing_type_response["thingTypeArn"],
                "thingTypeId": thing_type_response["thingTypeId"],
                "jitpRoleArn": self.jitp_role["role_arn"],
                "certificateArn": ca_response["certificateArn"],
            },
            "success": True,
        }

    @property
    def registration_config(self):
        with open(path.join(BASEPATH, "templates", "policy.json"), "r") as policy:
            json_policy = json.loads(policy.read())

        with open(
            path.join(BASEPATH, "templates", "provisioning.json"), "r"
        ) as provisioning_file:
            pf = json.loads(provisioning_file.read())

        pf["Resources"]["thing"]["Properties"]["ThingTypeName"] = self.thing_type
        pf["Resources"]["policy"]["Properties"]["PolicyDocument"] = json.dumps(
            json_policy
        )

        return {"roleArn": self.jitp_role["role_arn"], "templateBody": json.dumps(pf)}

    def _do_verify_cert(self, key_path, cert_path, common_name):

        endpoint = self.IOT.describe_endpoint(endpointType="iot:Data-ATS")[
            "endpointAddress"
        ]

        my_mqtt_client = AWSIoTMQTTClient(common_name)
        my_mqtt_client.configureEndpoint(endpoint, 8883)
        my_mqtt_client.configureCredentials(
            Path(BASEPATH) / "assets" / "aws_root_ca.pem", key_path, cert_path
        )

        my_mqtt_client.configureConnectDisconnectTimeout(2)  # 10 sec
        n_tries = 2
        for _ in range(n_tries):
            try:
                return my_mqtt_client.connect()
            except connectTimeoutException:
                pass

        return False
