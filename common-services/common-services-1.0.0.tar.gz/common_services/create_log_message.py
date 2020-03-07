from datetime import datetime
import logging
import json
import os

class JSONFormatter(logging.Formatter):
    """ JSON formatter """
    def format(self, record):
        """ Format event info to json."""
        obj = record.msg

        return json.dumps(obj)

class CreateAuditMessage:



    def __init__(self, context):

        self.LOGGER = self.setup_logger()

        self.context = context




    def setup_logger(self):
        """ Create logging object."""

        logger = logging.getLogger("json_logger")
        logger.propagate=False
        handler = logging.StreamHandler()
        formatter = JSONFormatter()
        handler.setFormatter(formatter)
        if not logger.hasHandlers():
            logger.addHandler(handler)


        if "DEBUG" in os.environ and os.environ["DEBUG"] == "true":
            logger.setLevel(logging.DEBUG)  # pragma: no cover
        else:
            logger.setLevel(logging.INFO)
            logging.getLogger("boto3").setLevel(logging.WARNING)
            logging.getLogger("botocore").setLevel(logging.WARNING)

        return logger


    def createauditmessage(self, business_key, business_value, message, log_level, information=None, trace_id=None):


        audit_msg = {}
        audit_msg["timestamp"] = datetime.now().replace(microsecond=0).isoformat()
        if information:
            audit_msg["message"] = information
        audit_msg['logEvent'] = message
        audit_msg['logGroup'] = self.context.log_group_name
        audit_msg['logStream'] = self.context.log_stream_name
        audit_msg['logLevel'] = log_level
        audit_msg['componentName'] = self.context.log_group_name.split("/")[3]
        audit_msg['traceId'] = trace_id
        business_dict = dict(zip(business_key.split("|"), business_value.split("|")))
        audit_msg['businessKeyStructure'] = business_key
        audit_msg['businessKeyValue'] = business_value
        audit_msg['businessKey'] = business_dict
        audit_msg['awsRequestId'] = self.context.aws_request_id


        #logging.info(StructuredMessage( auditjson))
        if log_level=="INFO":
            self.LOGGER.info(audit_msg)
        elif log_level=="DEBUG":
            self.LOGGER.debug(audit_msg)
        elif log_level=="ERROR":
            self.LOGGER.error(audit_msg)



