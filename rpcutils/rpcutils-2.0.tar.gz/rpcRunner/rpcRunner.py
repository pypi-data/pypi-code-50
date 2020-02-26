#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import json
from collections import OrderedDict

from ..fmqlIF.brokerRPC import VistARPCConnection, RPCLogger
from rpcUtils import toRPCListForm, toFMDateTime, shiftMultiLineString, fillTemplateArguments

"""
Very simple 'rpcRunner' that takes a set of connection/logon parameters and the name of an RPC sequence file (JSON)

> python rpcRunner.py setupParameters.json RPCSequences/Allergy.json
"""

def main():

    if len(sys.argv) < 3:
        print "Exiting as need to specify {Setup Parameters JSON File} and {RPC Sequence JSON File}"
        return

    TEMPLATE_SETTINGS = {}
    try:
        cpf = json.load(open(sys.argv[1]))
        HOST = cpf["HOST"]
        PORT = int(cpf["PORT"])
        ACCESS = cpf["ACCESS"]
        VERIFY = cpf["VERIFY"]
        for k in [k for k in cpf if k not in ["HOST", "PORT", "ACCESS", "VERIFY"]]:
            TEMPLATE_SETTINGS[k] = cpf[k]
        if "NOW" not in cpf:
            TEMPLATE_SETTINGS["NOW"] = toFMDateTime()
        if "USERNAMESEARCH" not in cpf and "USERNAME" in cpf:
            TEMPLATE_SETTINGS["USERNAMESEARCH"] = "{}S~".format(cpf["USERNAME"][0:-1])
    except Exception, e:
        print e
        print "Problem with Parameter File {} - exiting".format(sys.argv[1])
        return

    try:
        rpcSequence = json.load(open(sys.argv[2]))["sequence"]
    except Exception, e:
        print e
        print "Problem with RPC Sequence file {} - exiting".format(sys.argv[2])
        return

    print "Sending RPC Sequence {} to {}:{}".format(sys.argv[2], HOST, PORT)

    connection = VistARPCConnection(HOST, int(PORT), ACCESS, VERIFY, "OR CPRS GUI CHART", RPCLogger())

    rpcsSent = OrderedDict()
    for i, rpcInfo in enumerate(rpcSequence, 1):
        try:
            if "args" in rpcInfo:
                rpcArgs = fillTemplateArguments(rpcInfo["args"], TEMPLATE_SETTINGS)
                rpcArgs = [toRPCListForm(rpcArg) for rpcArg in rpcArgs]
            else:
                rpcArgs = []
            print "\n{}. Sending {}: {}".format(i, rpcInfo["name"], json.dumps(rpcArgs, indent=4))
            reply = connection.invokeRPC(rpcInfo["name"], rpcArgs)
            if rpcInfo["name"] not in rpcsSent:
                rpcsSent[rpcInfo["name"]] = 1
            else:
                rpcsSent[rpcInfo["name"]] += 1
            print "REPLY: {}".format(shiftMultiLineString(reply))
        except Exception, e:
            print "Problem with {} RPC - exiting".format(json.dumps(rpcInfo, indent=4))
            raise e
        print
        print
    print "End: {}".format(json.dumps(rpcsSent))

if __name__ == "__main__":
    main()
