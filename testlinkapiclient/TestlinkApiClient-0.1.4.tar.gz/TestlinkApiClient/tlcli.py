#!/usr/bin/env python
# -*- coding: utf-8 -*-

from TestlinkApiClient.tlxmlrpc import TestlinkClient


def help_doc():
    pass


if __name__ == '__main__':
    testlink_url = input('TestLink URL: ')
    testlink_user = input('TestLink User: ')
    testlink_devkey = input('TestLink DevKey: ')
    testlink = TestlinkClient(testlink_url, testlink_user, testlink_devkey)
    while True:
        cmd = input('> ')
        if cmd == "quit":
            print('GoodBye')
            break
        elif cmd == 'help':
            help_doc()
        # Project Operations
        elif cmd == 'listProject':
            print(testlink.list_project())
        elif cmd == 'getProject':
            pass
        elif cmd == 'createProject':
            pass
        elif cmd == 'deleteProject':
            pass
        # Plan Operations
        elif cmd == 'listPlan':
            pass
        elif cmd == 'getPlan':
            pass
        elif cmd == 'createPlan':
            pass
        elif cmd == 'deletePlan':
            pass
        # Suite Operations
        elif cmd == 'listSuite':
            pass
        elif cmd == 'getSuite':
            pass
        elif cmd == 'createSuite':
            pass
        elif cmd == 'deleteSuite':
            pass
        # Case Operations
        elif cmd == 'listCase':
            pass
        elif cmd == 'getCase':
            pass
        elif cmd == 'createCase':
            pass
        elif cmd == 'deleteCase':
            pass
        elif cmd == 'updateStep':
            pass
        elif cmd == 'setExecutionResult':
            pass
        elif cmd == 'getLastExecutionResult':
            pass
        # Unknown Operations
        else:
            help_doc()
