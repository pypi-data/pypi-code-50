#!/usr/bin/env python3

"""
    \r
    ScaleGrid Help Menu

    Usage:
        sg-cli [mongo | redis | mysql | postgresql] <command> [<args>...]

    Options:
        -v, --verbose  Increase verbosity
        -h, --help     Show this menu
        -V --version   Show version

    Commands:
        (mongo | redis | mysql | postgresql) add-firewall-rules
        (mongo | redis | mysql | postgresql) build-index
        check-job-status
        (mongo | redis | mysql | postgresql) compact
        (mongo | redis | mysql | postgresql) create-alert-rule
        (mongo | redis | mysql | postgresql) create-cloud-profile
        (mongo | redis | mysql | postgresql) create-cluster
        (mongo | redis | mysql | postgresql) create-follower-cluster
        (mongo | redis | mysql | postgresql) delete-backup
        delete-alert-rule
        delete-cloud-profile
        (mongo | redis | mysql | postgresql) delete-cluster
        (mongo | redis | mysql | postgresql) get-active-alerts
        (mongo | redis | mysql | postgresql) get-cluster-credentials
        (mongo | redis | mysql | postgresql) get-backup-schedule
        (mongo | redis | mysql | postgresql) list-alert-rules
        (mongo | redis | mysql | postgresql) list-backups
        list-cloud-profiles
        (mongo | redis | mysql | postgresql) list-clusters
        login
        logout
        (mongo | redis | mysql | postgresql) patch-os
        (mongo | redis | mysql | postgresql) pause-cluster
        (mongo | redis | mysql | postgresql) peek-at-backup
        (mongo | redis | mysql | postgresql) resolve-alerts
        (mongo | redis | mysql | postgresql) restore-backup
        (mongo | redis | mysql | postgresql) resume-cluster
        (mongo | redis | mysql | postgresql) scale-up
        (mongo | redis | mysql | postgresql) set-backup-schedule
        (mongo | redis | mysql | postgresql) start-backup
        update-cloud-profile-keys
        wait-until-job-done

    Help commands:
        sg-cli -h
        sg-cli <command> -h
        sg-cli (mongo | redis | mysql | postgresql) -h
        sg-cli [mongo | redis | mysql | postgresql] <command> -h\n
"""

import sys

if sys.version_info[0] < 3:
    sys.stderr.write("Python 3 required\n")
    sys.exit(1)

import logging
import traceback
import os
from os import path
from os import listdir
from os.path import isfile, join
import http.client, ssl, urllib
import json
from pathlib import Path
from time import sleep
from datetime import datetime
import getpass
from stat import *
import io
from docopt import docopt, DocoptExit

# set environment variable SGServerIP from the command line to change SERVER_IP
# SERVER_IP will be 'console.scalegrid.io' by default (if environment variable not assigned)
SERVER_IP = "console.scalegrid.io"
PORT = 443
VERSION = '1.0'

# lists containing all the keys to display for list functions (used with print_obj)
# "created" is converted from an integer to a datetime timestamp
# first.second --> indicates the value of key 'first' is a dictionary, and 'second' is a key within the dictionary
# list within the list (instead of normal strings) --> first item in the list is the key that points to a list of dictionaries
    # Each subsequent item in the list is a value in each dictionary within the list of dictionaries
CLUSTER_VALS_MONGO = ["name", "id", "clusterType", "shared", "status", "size", "diskSizeGB", "usedDiskSizeGB", "versionStr",
                      "displayMachinePoolName", ["monitoringServerData", "id", "name", "shardName", "type"], "encryptionEnabled",
                      "sslEnabled", "engine", "compressionAlgo"]
CLUSTER_VALS_REDIS = ["name", "id", "clusterType", "shared", "status", "size" , "versionStr",["shards", ["redisServers", "VM-addressableName", "VM-diskSizeGB", "VM-diskUsedGB"]],
                      "encryptionEnabled"]
BACKUP_VALS = ["all","name", "id", "object_id", "created", "type", "comment"]
STATUS_VALS = ["name", "object_name", "object_type", "cancelled", "progress", "status", "run_by"]
PROFILE_VALS = ["providerMachinePoolName", "configJSON.regionDesc", "configJSON.region", "configJSON.secretKey", "configJSON.deploymentStyle", "configJSON.vpcID",
                "configJSON.vpcSubnetID", "configJSON.vpcCIDR", "configJSON.vpcSubnetCIDR", "configJSON.securityGroupName", "configJSON.vpcSecurityGroupID",
                "configJSON.securityGroupId", "configJSON.subscriptionID", "configJSON.vnetId", "id", "dbType", "type", "created", "owner", "status", "shared"]
ALERT_VALS = ["alertDescription", "clusterID", "created", "dismissComment", "dismissedDate", "id", "machineName", "state", "userAlertRuleId"]
RULE_VALS = ["alertRuleDescription", "averageType", "clusterId", "created", "databaseType", "enabled", "id", "metric", "notifications", "operator", "ruleMetricName", "threshold", "type"]

conn = None
header = None

params = None

def get_filepath(fileName):
    __location__ = os.path.join(str(Path.home()), ".sg")
    if not os.path.isdir(__location__):
        os.mkdir(__location__)
    return os.path.join(__location__, fileName)

logging.basicConfig(
    format="%(asctime)s %(funcName)s():%(lineno)s %(levelname)s %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p %Z",
    level="DEBUG",
    filename=get_filepath('sg.log')
)
logger = logging.getLogger(__name__)

class SGException(Exception):
    message = None
    recAction = None

    def __init__(self, msg, recommendation=""):
        self.message = msg
        self.recAction = recommendation
        super(SGException, self).__init__()

    def getMessage(self):
        return self.message

    def getRecAction(self):
        return self.recAction

    def __str__(self):
        return self.message

def create_handler():
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter("%(levelname)s %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)

def set_server_ip():
    global SERVER_IP
    for i in os.environ:
        if i.lower() == "sgserverip":
            SERVER_IP = os.environ['SGSERVERIP']

def display_error_message(error, action=""):
    logger.error("Something went wrong. " + error)
    if action != "":
        logger.error("Recommended action: " + action)
    traceback.print_exc(file=open(get_filepath('sg.log'), 'a'))

def check_resp(expected):
    r2 = conn.getresponse()

    if r2.status != expected:
        raise SGException("Unexpected HTTP response - " + str(r2.status))
    return r2

def append_to_cookie(snippet, cookie):
    e = snippet.split(";", 1)
    a = e[0].split("=", 1)
    if not a[1]:
        logger.debug("Value of cookie %s is empty, ignoring it", a[0])
        return cookie

    separator = "; "
    if not cookie:
        separator = ""
    return cookie + separator + e[0]

def connect():
    global conn
    global SERVER_IP
    if SERVER_IP == "console.scalegrid.io":
        conn = http.client.HTTPSConnection(
            SERVER_IP, PORT
        )
    else:
        conn = http.client.HTTPSConnection(
            SERVER_IP, PORT, context=ssl._create_unverified_context()
        )
    conn.connect()

def load_header():
    global header
    cookieFile = get_filepath("sg_cookie.txt")
    logger.debug("Loading cookie info")
    try:
        with open(cookieFile, "r") as f:
            content = f.read()
    except FileNotFoundError as e:
        params['--email'] = None
        login()
        load_header()
        return
    header = {"Cookie": content, "User-Agent": "ScaleGridCLI/" + VERSION}

def get_resp(url, reqType, body={}):
    conn.request(reqType, url, body=json.dumps(body), headers=header)
    r2 = check_resp(200)
    resp = json.loads(r2.read())
    if resp["error"]["code"] != "Success":
        raise SGException(resp["error"]["errorMessageWithDetails"], resp["error"]["recommendedAction"])

    return resp

def print_obj_helper(obj, argv):
    newObj = {}
    if isinstance(obj, list):
        innerList = []
        for i in obj:
            innerList += [print_obj_helper(i, argv)]
        return innerList
    for arg in argv:
        if arg=='all':
            newObj = obj
            break
        if isinstance(arg, list):
            key = arg[0]
            subArgs = print_obj_helper(obj[key], arg)
            temp = {key: subArgs}
            arg = key
        else:
            if arg.lower()=="notifications":
                obj[arg] = eval(obj[arg])
            if arg.lower()=="created" or (arg.lower()=="dismisseddate" and obj[arg] != None):
                newObj[arg] = str(datetime.fromtimestamp(int(obj[arg])/1000.0))
                continue
            elif "." in arg:
                arg = arg.split(".")
                temp = json.loads(obj[arg[0]])
                arg = arg[1]
            elif "-" in arg:
                arg = arg.split("-")
                temp = json.loads(json.dumps(obj[arg[0]]))
                arg = arg[1]
            else:
                temp = obj
        try:
            newObj[arg] = temp[arg]
        except KeyError as e:
            pass
    return newObj

def print_obj(obj, argv):
    sys.stdout.write(json.dumps(print_obj_helper(obj, argv), indent=4, separators=(',', ': ')))
    sys.stdout.write("\n")

def print_action_id(resp):
    logger.info("Use your action ID to monitor the job status.")
    logger.info("Action ID: " + str(resp["actionID"]))

def print_id(id, objType):
    logger.info("New %s ID: %s. Keep this ID and use it to perform commands on your %s once it is created." % (objType, id, objType))
    logger.info("To get more information about your %s once it is created, run the list-%ss command." % (objType, objType.replace(' ', '-')))

def delete_cookie():
    if os.path.isfile(get_filepath("sg_cookie.txt")):
        os.chmod(get_filepath("sg_cookie.txt"), S_IWUSR)
        os.remove(get_filepath("sg_cookie.txt"))

def convert_mongo():
    if params['db-type'].lower() == "mongo":
        params['db-type'] = "mongodb"

def login():
    """
    \r
    Login to your ScaleGrid account

    Usage:
        sg-cli login [options]

    Options:
        --email [<email-address>]  Email address associated with your account
        -v, --verbose              Increase verbosity
    """

    if not params['--email']:
        params['--email'] = input("Enter your email address: ")
    # getpass bypasses input-redirection and forces customer to enter the password at the terminal. This makes it impossible to use sg-cli login in a script. So we don't use getpass unless the stdin is a terminal.
    if sys.stdin.isatty():
        password = getpass.getpass()
    else:
        password = sys.stdin.readline().rstrip()

    body = {"username": params['--email'], "password": password}

    conn.request("POST", "/login", body=json.dumps(body))
    r2 = check_resp(200)

    loginResponse = json.loads(r2.read())
    if loginResponse["error"]["code"] == "TwoFactorAuthNeeded":
        auth = input("Enter your Two Factor Authentication code: ")
        body["inputCode"] = auth
        conn.request("POST", "/login", body=json.dumps(body))
        r2 = check_resp(200)
        loginResponse = json.loads(r2.read())

    if loginResponse["error"]["code"] != "Success":
        raise SGException(loginResponse["error"]["errorMessageWithDetails"], loginResponse["error"]["recommendedAction"])

    logger.info("Connection successful, setting up cookie")
    delete_cookie()

    clientCookie = ""
    for hdr, value in r2.getheaders():
        if hdr.casefold() == "set-cookie":
            clientCookie = append_to_cookie(value, clientCookie)
    cookieFile = get_filepath("sg_cookie.txt")
    try:
        with open(cookieFile, "w") as f:
            f.write(clientCookie)
        os.chmod(cookieFile, 0o400)
    except Exception as e:
        raise SGException("There was an error writing to " + cookieFile, "Check permissions for the file")
    logger.info("Cookie created successfully")
    logger.debug("Cookie written to " + cookieFile)

def create_cluster():
    """
    \r
    Create a Standalone Cluster or Replica Set

    Usage:
        sg-cli (mongo | redis | mysql | postgresql) create-cluster --cluster-name <unique-cluster-name> --shard-count <number-of-shards> --size <cluster-size> --version <version-number> --machine-list <list-of-machine-names> [options]

    Options:
        --cluster-name <unique-cluster-name>            Name of the cluster
        --shard-count <number-of-shards>                Number of shards
                                                        1 for standalone or ReplicaSet, more for Sharded
                                                        Must be 3 or 4 for Redis when cluster-mode when is enabled
        --size <cluster-size>                           New size of the cluster
                                                        Size options: micro, small, medium, large, xlarge, x2xlarge, or x4xlarge
        --version <version-number>                      Version of database
                                                        Version options for Mongo: V366, V401, V3416, V3220, V2611
                                                        Version options for Redis: V505, V4010, V3212
                                                        Version options for MySQL: V5725, V5721, V5718
        --machine-list <list-of-machine-names>          List of comma separated cloud profile names
                                                        Number of names should match:
                                                            number of replicas (number of replicas + 1 if even)
                                                            times number of shards
                                                        Example: --machine-list ['CloudProfile1','CloudProfile2','CloudProfile3']
        --encrypt-disk                                  Include option to encrypt disk [default: false]
        --engine <storage-engine>                       MongoDB only, name of storage engine [default: wiredtiger]
                                                        Engine options for Mongo: wiredtiger | mmapv1
        --compression-algo <algorithm>                  MongoDB only, compression algorithm for MongoDB. Include option to compress data
                                                        Compression options: snappy | zlib
        --enable-ssl                                    MongoDB only, include option to enable SSL [default: false]
        --replica-count <nodes-per-shard>               MongoDB only, number of nodes in each shard of your cluster.
                                                        1 for standalone, more for ReplicaSet or Sharded
                                                        An even number will automatically add an Arbiter Instance
        --server-count <nodes-per-shard>                Redis only, number of nodes in each shard of your cluster. 1 for standalone.
                                                        For master/slave deployment, if this is an even number,
                                                        ensure to set the sentinel-count as one higher than this.
        --sentinel-count <number-of-sentinels>          Redis only, number of sentinel nodes in a master/slave deployment
                                                        Should be one more than server count if it is even otherwise the same as it
        --sentinel-machine-list <list-of-machine-names> Redis only, list of comma separated cloud profiles where the sentinels must be created
                                                        when sentinel count > server count
                                                        Number of entries must be equal to (sentinel count - server count)                               
        --enable-cluster-mode                           Redis only, include option to create a Redis cluster mode deployment [default: false]
        --interval <interval_in_hours>                  Redis only, use this field to set up a Backup Schedule for your Redis deployment
                                                        to take a snapshot every 1-24 hours so your data is always accessible.
                                                        0 to disable scheduled backups
        --maxmemory-policy <policy>                     Redis only, eviction policy when Redis is used as a cache
                                                        Options: volatile-lru, allkeys-lru, volatile-lfu, allkeys-lfu, volatile-random,
                                                        allkeys-random, volatile-ttl, noeviction
        --enable-rdb                                    Redis only, include option to enable regular RDB saves to disk for your Redis deployment
        --enable-aof                                    Redis only, enable AOF persistence for your Redis deployment
        --cidr-list <list_of_CIDR_ranges>               Redis only, list of CIDR ranges to whitelist
        -v, --verbose                                   Increase verbosity
    """
    machines = eval(params['--machine-list'])
    machineIDs = []
    for i in machines:
        params['--cloud-profile-name'] = i
        machineIDs += [list_cloud_profiles()["id"]]

    if params['db-type'].lower() == "mongo":
        if params['--replica-count'] == None:
            logger.warning("Required fields are missing.\nExample: sg-cli mongo create-cluster --cluster-name <unique-cluster-name> --shard-count <number-of-shards> --replica-count <nodes-per-shard> --size <cluster-size> --version <version-number> --machine-list <list-of-machine-names> ")
            exit()
        body = {"clusterName": params['--cluster-name'], "shardCount": int(params['--shard-count']), "replicaCount": int(params['--replica-count']),
                "size": params['--size'], "version": params['--version'].upper(), "machinePoolIDList": machineIDs, "enableAuth": True, "engine": params['--engine'],
                "enableSSL": params['--enable-ssl'], "encryptDisk": params['--encrypt-disk']}
        if params['--compression-algo'] != None:
            body['compressionAlgo'] = params['--compression-algo']
        resp = get_resp("/%sClusters/create" % params['db-type'], "POST",  body=body)

        logger.info("Cluster creation started successfully")
        print_id(resp["clusterID"], "cluster")
        print_action_id(resp)

    elif params['db-type'].lower() == "redis":
        if (params['--server-count'] == None) or (params['--interval'] == None) or (params['--sentinel-count'] == None):
            logger.warning("Required fields are missing.\nExample: sg-cli redis create-cluster --cluster-name <unique-cluster-name> --shard-count <number-of-shards> --server-count <nodes-per-shard> --sentinel-count <number-of-sentinels> --size <cluster-size> --version <version-number> --machine-list <list-of-machine-names> ")
            exit()

        body = {"clusterName": params['--cluster-name'], "version": params['--version'].upper(), "size": params['--size'], "serverCount": int(params['--server-count']),
                "sentinelCount": int(params['--sentinel-count']), "shardCount": int(params['--shard-count']), 'cidrList': eval(params['--cidr-list']),
                "machinePoolIDList": machineIDs, "backupIntervalInHours": int(params['--interval']), "encryptDisk": params['--encrypt-disk'],
                "clusterMode": params['--enable-cluster-mode']}
        if params['--sentinel-machine-list'] != None:
            sentinelMachines = eval(params['--sentinel-machine-list'])
            sentinelMachineIDs = []            
            for i in sentinelMachines:
                params['--cloud-profile-name'] = i
                sentinelMachineIDs += [list_cloud_profiles()["id"]]
            body['sentinelMachinePool'] = sentinelMachineIDs
        
        myRedisConfigParams = {}
        if params['--enable-rdb'] == False:
            myRedisConfigParams['save'] = {"value": "", "split": 0}
        if params['--enable-aof'] == True:
            myRedisConfigParams['appendonly'] = {"value": "yes", "split": 0}
        if params['--maxmemory-policy'] != None:
            myRedisConfigParams['maxmemory-policy'] = {"value": params['--maxmemory-policy'], "split": 0}        
        body['redisConfigParams'] = myRedisConfigParams
        
        resp = get_resp("/%sClusters/create" % params['db-type'], "POST",  body=body)
        
        logger.info("Cluster creation started successfully")
        print_id(resp["clusterID"], "cluster")
        print_action_id(resp)
    
    else:
        logger.info("Not supported")

def delete_cluster():
    """
    \r
    Delete an old cluster

    Usage:
        sg-cli (mongo | redis | mysql | postgresql) delete-cluster --cluster-name <unique-cluster-name> [options]

    Options:
        --cluster-name <unique-cluster-name>  Name of a cluster
        -v, --verbose                         Increase verbosity
    """

    id = str(list_clusters()["id"])
    call = "/%sClusters/%s" % (params['db-type'], id)
    resp = get_resp(call, "DELETE", body={"skipVMDeletion": False})

    logger.info("Cluster delete started successfully")
    print_action_id(resp)

def get_obj(objs, objName, objType="cluster"):
    if objType=="cloudProfile":
        obj = next((i for i in objs if i["providerMachinePoolName"].lower() == objName.lower()), None)
    else:
        obj = next((i for i in objs if i["name"].lower() == objName.lower()), None)
    if obj == None:
        if objType == "backup":
            message = "The specified %sCluster Backup with name %s was not found" % (params['db-type'], objName)
            rec = "Specify a valid %sCluster Backup name and retry the operation" % params['db-type']
        elif objType == "cloudProfile":
            message = "The specified Cloud Profile with name %s was not found" % objName
            rec = "Specify a valid Cloud Profile name and retry the operation"
        else:
            message = "The specified %sCluster with name %s was not found" % (params['db-type'], objName)
            rec = "Specify a valid %sCluster name and retry the operation" % params['db-type']
        raise SGException(message, rec)
    return obj

def list_clusters():
    """
    \r
    Get a list of all your clusters of a specified database type

    Usage:
        sg-cli (mongo | redis | mysql | postgresql) list-clusters [options]

    Options:
        --cluster-name <unique-cluster-name>  Name of a cluster
        -v, --verbose                         Increase verbosity
    """    
    resp = get_resp("/%sClusters/list" % params['db-type'], "GET")
    clusters = resp["clusters"]
    if params['--cluster-name']:
        return get_obj(clusters, params['--cluster-name'])
    else:
        if len(clusters) == 0:
            sys.stdout.write("No %s clusters" % params['db-type'])
            sys.stdout.write("\n")            
        for i in clusters:
            if params['db-type'].lower() == "mongo":
                print_obj(i, CLUSTER_VALS_MONGO)
            elif params['db-type'].lower() == "redis":
                print_obj(i, CLUSTER_VALS_REDIS)
    
def list_backups():
    """
    \r
    Get a list of backups of a specified cluster

    Usage:
        sg-cli (mongo | redis | mysql | postgresql) list-backups --cluster-name <unique-cluster-name> [options]

    Options:
        --cluster-name <unique-cluster-name>  Name of a cluster
        --backup-name <unique-backup-name>    Name of a backup of your cluster
        -v, --verbose                         Increase verbosity
    """

    id = str(list_clusters()["id"])
    call = "/%sClusters/%s/listBackups" % (params['db-type'], id)
    resp = get_resp(call, "GET")
    backups = resp["backups"]

    if params['--backup-name']:
        return get_obj(backups, params['--backup-name'], "backup")
    else:
        if len(backups) == 0:
            sys.stdout.write("No %s backups for this cluster" % params['db-type'])
            sys.stdout.write("\n")
        for i in backups:
            print_obj(i, BACKUP_VALS)

def start_backup():
    """
    \r
    Create a backup of a cluster

    Usage:
        sg-cli (mongo | redis | mysql | postgresql) start-backup --cluster-name <unique-cluster-name> --backup-name <unique-backup-name> [options] [--primary | --secondary]

    Options:
        --cluster-name <unique-cluster-name>  Name of a cluster
        --backup-name <unique-backup-name>    Name of a backup of your cluster
        --comment <backup-description>        Comments associated with your backup
        [--primary | --secondary]             Virtual machine target of backup. Only for replica sets
                                              default: --secondary
        -v, --verbose                         Increase verbosity
    """

    id = str(list_clusters()["id"])
    body = {"backupName": params['--backup-name'], "comment": params['--comment'], "id": id}
    if list_clusters()["clusterType"].lower() == "replicaset":
        if params['--primary']:
            body["target"] = "PRIMARY"
        else:
            body["target"] = "SECONDARY"
    resp = get_resp("/%sClusters/backup" % params['db-type'], "POST", body)

    logger.info("%s backup started successfully" % params['--cluster-name'])
    print_action_id(resp)

def peek_at_backup():
    """
    \r
    Create a new standalone cluster from a past backup

    Usage:
        sg-cli (mongo | redis | mysql | postgresql) peek-at-backup --cluster-name <original-cluster-name> --backup-name <unique-backup-name> --new-name <new-cluster-name> [options]

    Options:
        --cluster-name <unique-cluster-name>  Name of the original cluster
        --backup-name <unique-backup-name>    Name of the backup you would like to peek at
        --new-name <new-cluster-name>         Name of new cluster to create from backup
        -v, --verbose                         Increase verbosity
    """

    clusterID = str(list_clusters()["id"])
    backupID = str(list_backups()["id"])

    body = {"destinationClusterName": params['--new-name'], "backupID": backupID, "sourceClusterID": clusterID}
    resp = get_resp("/%sClusters/peekAtBackup" % params['db-type'], "POST", body)

    logger.info("Peek started successfully")
    print_action_id(resp)

def create_follower_cluster():
    """
    \r
    Create a follower cluster

    Usage:
        sg-cli (mongo | redis | mysql | postgresql) create-follower-cluster --target-name <target-cluster-name> --source-name <source-cluster-name> --interval <hours-between-sync> [options]

    Options:
        --target-name <target-cluster-name>  Name of follower cluster
        --source-name <source-cluster-name>  Name of cluster that will be followed
        --interval <hours-between-sync>      Number of hours between each sync with source cluster
        -v, --verbose                        Increase verbosity
    """

    # setting '--cluster-name' parameter to ensure the list_clusters call returns a cluster
    params['--cluster-name'] = params['--target-name']
    targetID = str(list_clusters()["id"])
    params['--cluster-name'] = params['--source-name']
    sourceID = str(list_clusters()["id"])

    convert_mongo()
    body = {'sourceClusterID': sourceID, 'dbType': params['db-type'].upper(), 'intervalInHours': params['--interval'],
            'startTimeStr': datetime.now().isoformat()}

    resp = get_resp("/clusters/%s/createFollowerRelationship" % targetID, "POST", body=body)
    logger.info("Follower relationship between clusters %s and %s created successfully" % (params['--target-name'], params['--source-name']))

def set_backup_schedule():
    """
    \r
    Change the backup schedule of a cluster

    Usage:
        sg-cli (mongo | redis | mysql | postgresql) set-backup-schedule --cluster-name <unique-cluster-name> [options] [--primary | --secondary]

    Options:
        --cluster-name <unique-cluster-name>  Name of a cluster
        --enabled                             Scheduled backup enabled if included; otherwise, disabled
        --interval <hours-between-backups>    Number of hours between scheduled backups
        --hour <start-time>                   Hour on a 24 hour clock at which the first backup will start
                                              All subsequent backups will occur ever --interval hours
        --limit <max-scheduled-backups>       Maximum number of scheduled backups retained
        [--primary | --secondary]             Virtual machine target of backup. Only for replica sets
                                              For Redis clusters primary refers to master and secondary to slave
                                              default: --secondary
        -v, --verbose                         Increase verbosity
    """
    id = str(list_clusters()["id"])
    body = {"scheduledBackupEnabled": params['--enabled'], "backupIntervalInHours": params['--interval'], "backupHour": params['--hour'], "backupScheduledBackupLimit": params['--limit'], "id": id}
    if list_clusters()["clusterType"].lower() == "replicaset":
        if params['db-type'].lower() == "mongo":
            if params['--primary']:
                body["target"] = "PRIMARY"
            else:
                body["target"] = "SECONDARY"
            resp = get_resp("/%sClusters/setClusterBackupSchedule" % params['db-type'], "POST", body)
        elif params['db-type'].lower() == "redis":
            if params['--primary']:
                body["target"] = "MASTER"
            else:
                body["target"] = "SLAVE"
            resp = get_resp("/%sClusters/setBackupSchedule" % params['db-type'], "POST", body)

    logger.info("Backup schedule changed successfully")

def get_backup_schedule():
    """
    \r
    Get the backup schedule of a cluster

    Usage:
        sg-cli (mongo | redis | mysql | postgresql) get-backup-schedule --cluster-name <unique-cluster-name> [options]

    Options:
        --cluster-name <unique-cluster-name>  Name of a cluster
        -v, --verbose                         Increase verbosity
    """

    id = str(list_clusters()["id"])
    call = "/%sClusters/%s/getBackupSchedule" % (params['db-type'], id)
    resp = get_resp(call, "POST")

    logger.debug("Fetching backup schedule")
    logger.info("Backup hour: %s" % resp['backupHour'])
    logger.info("Backup interval in hours: %s" % resp['backupIntervalInHours'])
    logger.info("Backups retention limit: %s" % resp['backupScheduledBackupLimit'])
    logger.info("Backup target: %s" % resp['target'])
    #print_action_id(resp)

def restore_backup():
    """
    \r
    Restore a backup

    Usage:
        sg-cli (mongo | redis | mysql | postgresql) restore-backup --cluster-name <unique-cluster-name> --backup-name <unique-backup-name> [options]

    Options:
        --cluster-name <unique-cluster-name>  Name of a cluster
        --backup-name <unique-backup-name>    Name of a backup of your cluster
        -v, --verbose                         Increase verbosity
    """

    clusterID = str(list_clusters()["id"])
    backupID = str(list_backups()["id"])

    body = {"backupID": backupID, "clusterID": clusterID}
    resp = get_resp("/%sClusters/restore" % params['db-type'], "POST", body)

    logger.info("%s restore started successfully" % params['--backup-name'])
    print_action_id(resp)

def delete_backup():
    """
    \r
    Delete an old backup

    Usage:
        sg-cli (mongo | redis | mysql | postgresql) delete-backup --cluster-name <unique-cluster-name> --backup-name <unique-backup-name> [options]

    Options:
        --cluster-name <unique-cluster-name>  Cluster to delete the backup from
        --backup-name <unique-backup-name>    Name of the backup to delete
        --force                               Force backup to delete [default: false]
        -v, --verbose                         Increase verbosity
    """

    clusterID = str(list_clusters()["id"])
    backupID = str(list_backups()["id"])

    body = {"clusterID": clusterID, "backupID": backupID, "force": params['--force']}
    resp = get_resp("/%sClusters/deleteBackup" % params['db-type'], "POST", body)

    logger.info("Backup Delete started successfully")
    print_action_id(resp)

def scale_up():
    """
    \r
    Increase the size of your cluster

    Usage:
        sg-cli (mongo | redis | mysql | postgresql) scale-up --cluster-name <unique-cluster-name> --size <new-size> [options]

    Options:
        --cluster-name <unique-cluster-name>  Name of a cluster
        --size <new-size>                     New size of the cluster
                                              Size options: small, medium, large, xlarge, x2xlarge, or x4xlarge
        -v, --verbose                         Increase verbosity
    """

    id = str(list_clusters()["id"])
    body = {"id": id, "newSize": params['--size']}
    resp = get_resp("/%sClusters/scale" % params['db-type'], "POST", body)

    logger.info("Scale up started successfully")
    print_action_id(resp)

def build_index():
    """
    \r
    Create an index for a collection in a database in your cluster

    Usage:
        sg-cli (mongo | redis | mysql | postgresql) build-index --cluster-name <unique-cluster-name> --db-name <database-name> --coll-name <collection-name> --index <keys-and-options> [options]

    Options:
        --cluster-name <unique-cluster-name>  Name of a cluster
        --db-name <database-name              Name of your database
        --coll-name <collection-name>         Name of your collection
        --index <keys-and-options>            JSON formatted string containing a list of the index's keys and options
                                              Example: "[{'key': 1, 'key2': -1}, {'name': 'example', 'unique': false}]"
        -v, --verbose                         Increase verbosity
    """

    id = str(list_clusters()["id"])
    call = "/%sClusters/%s/buildIndex" % (params['db-type'], id)

    body = {"dbName": params['--db-name'], "collName": params['--coll-name'], "index": params['--index']}
    resp = get_resp(call, "POST", body)

    logger.info("Index build started successfully")
    print_action_id(resp)

def patch_os():
    """
    \r
    Patch your OS with the most recent updates

    Usage:
        sg-cli (mongo | redis | mysql | postgresql) patch-os --cluster-name <unique-cluster-name> [options]

    Options:
        --cluster-name <unique-cluster-name>  Name of a cluster
        --full-patch                          Include to execute full patch [default: false]
        --skip-shard-routers                  Include to skip shard routers [default: false]
        -v, --verbose                         Increase verbosity
    """

    id = str(list_clusters()["id"])
    convert_mongo()
    body = {"id": id, "dbType": params['db-type'].upper(), "fullPatch": params['--full-patch'], "skipShardRouters": params['--skip-shard-routers']}
    resp = get_resp("/clusters/patchos", "POST", body)

    logger.info("OS Patch started successfully")
    print_action_id(resp)

def check_job_status():
    """
    \r
    Check the status of a job that you started

    Usage:
        sg-cli check-job-status --action-id <your-action-id> [options]

    Options:
        --action-id <your-action-id>  Unique ID returned by an action you performed
        -v, --verbose                 Increase verbosity
    """

    resp = get_resp("/actions/%s" % params['--action-id'], "GET")
    return resp['action']

def wait_until_job_done():
    """
    \r
    Pause program until a job finishes

    Usage:
        sg-cli wait-until-job-done --action-id <your-action-id> [options]

    Options:
        --action-id <your-action-id>  Unique ID returned by an action you performed
        -v, --verbose                 Increase verbosity
    """

    logger.info("Waiting...")
    while check_job_status()['status'].lower() == "running":
        sleep(180)
    logger.info("Done")

def get_cluster_credentials():
    """
    \r
    Get the username and password for the root database user

    Usage:
        sg-cli (mongo | redis | mysql | postgresql) get-cluster-credentials --cluster-name <unique-cluster-name> [options]

    Options:
        --cluster-name <unique-cluster-name>  Name of a cluster
        -v, --verbose                         Increase verbosity
    """

    id = str(list_clusters()["id"])
    call = "/%sClusters/%s/getCredentials" % (params['db-type'], id)
    resp = get_resp(call, "GET")

    logger.debug("Fetching credentials")
    logger.info("Username: %s" % resp['user'])
    logger.info("Password: %s" % resp['password'])

def compact():
    """
    \r
    Defragment the data in your cluster to improve performance

    Usage:
        sg-cli (mongo | redis | mysql | postgresql) compact --cluster-name <unique-cluster-name> [options]

    Options:
        --cluster-name <unique-cluster-name>  Name of a cluster
        -v, --verbose                         Increase verbosity
    """

    id = str(list_clusters()["id"])
    call = "/%sClusters/%s/compactDatabase" % (params['db-type'], id)
    resp = get_resp(call, "POST")

    logger.info("Compact started successfully")
    print_action_id(resp)

def pause_cluster():
    """
    \r
    Pause a cluster

    Usage:
        sg-cli (mongo | redis | mysql | postgresql) pause-cluster --cluster-name <unique-cluster-name> [options]

    Options:
        --cluster-name <unique-cluster-name>  Name of a cluster
        -v, --verbose                         Increase verbosity
    """

    id = str(list_clusters()["id"])

    convert_mongo()
    body = {"clusterID": id, "dbType": params['db-type'].upper()}
    resp = get_resp("/clusters/pauseCluster", "POST", body)
    logger.info("Pause started successfully")
    print_action_id(resp)

def resume_cluster():
    """
    \r
    Resume a cluster

    Usage:
        sg-cli (mongo | redis | mysql | postgresql) resume-cluster --cluster-name <unique-cluster-name> [options]

    Options:
        --cluster-name <unique-cluster-name>  Name of a cluster
        -v, --verbose                         Increase verbosity
    """

    id = str(list_clusters()["id"])

    convert_mongo()
    body = {"clusterID": id, "dbType": params['db-type'].upper()}
    resp = get_resp("/clusters/resumeCluster", "POST", body)
    logger.info("Resume started successfully")
    print_action_id(resp)

def add_firewall_rules():
    """
    \r
    Add a list of IP CIDR to the firewall rules of your cluster

    Usage:
        sg-cli (mongo | redis | mysql | postgresql) add-firewall-rules --cluster-name <unique-cluster-name> --cidr-list <list-of-cidr> [options]

    Options:
        --cluster-name <unique-cluster-name>  Name of a cluster
        --cidr-list <list-of-cidr>            List of IP CIDR
                                              Example: --cidr-list ['10.20.0.0/16','10.30.0.0/20']
        -v, --verbose                         Increase verbosity
    """

    id = str(list_clusters()["id"])

    convert_mongo()
    body = {'clusterID': id, 'dbType': params['db-type'].upper(), 'cidrList': eval(params['--cidr-list'])}

    conn.request("POST", "/Clusters/setClusterLevelIPWhiteList", body=json.dumps(body), headers=header)
    check_resp(200)
    logger.info("Firewall rules added successfully")

def get_active_alerts():
    """
    \r
    Get all active alerts on a particular cluster

    Usage:
        sg-cli (mongo | redis | mysql | postgresql) get-active-alerts --cluster-name <unique-cluster-name>

    Options:
        --cluster-name <unique-cluster-name>  Name of a cluster
        -v, --verbose                         Increase verbosity
    """

    id = str(list_clusters()["id"])

    convert_mongo()
    body = {'clusterId': id, 'databaseType': params['db-type'].upper()}
    resp = get_resp("/alerts", "POST", body=body)

    alerts = resp["alerts"]
    if len(alerts) == 0:
        sys.stdout.write("No active alerts")
        sys.stdout.write("\n")
    for i in alerts:
        print_obj(i, ALERT_VALS)
        logger.debug("Alert ID: %s" % i["id"])

def resolve_alerts():
    """
    \r
    Dismiss alerts for a particular cluster

    Usage:
        sg-cli (mongo | redis | mysql | postgresql) resolve-alerts --cluster-name <unique-cluster-name> --alert-id-list <list-of-alert-ids> [options]

    Options:
        --cluster-name <unique-cluster-name>  Name of a cluster
        --alert-id-list <list-of-alert-ids>   List of alert IDs to dismiss
                                              Example: --alert-id-list [12345,23456,34567]
                                              Get alert IDs from the get-active-alerts command
        -v, --verbose                         Increase verbosity
    """

    id = str(list_clusters()["id"])

    convert_mongo()
    body = {'clusterId': id, 'databaseType': params['db-type'].upper(), 'alertsList': eval(params['--alert-id-list'])}
    resp = get_resp("/dismiss", "POST", body=body)

    logger.info("Alerts resolved successfully")

def create_alert_rule():
    """
    \r
    Create an alert rule for a particular cluster

    Usage:
        sg-cli (mongo | redis | mysql | postgresql) create-alert-rule --cluster-name <unique-cluster-name> --type <alert-rule-type> --operator <operator> --threshold <threshold> --notifications <notification-types> [options]

    Options:
        --cluster-name <unique-cluster-name>  Name of a cluster
        --type <alert-rule-type>              Type of alert rules
                                              Type options: METRIC, DISK_FREE, ROLE_CHANGE
        --operator <operator>                 Operator options: EQ, LT, GT, LTE, GTE
                                              EQ: equal to, LT: less than, GT: greater than, LTE: less than or equal to, GTE: greater than or equal to
        --threshold <threshold>               Decimal number that is paired with operator to create condition
                                              Example: --operator GT --threshold 10.0
                                                  = greater than 10.0
        --notifications <notification-types>  List of notification types
                                              Notification options: EMAIL, SMS, PAGERDUTY
                                              Example: --notification-types ['EMAIL', 'SMS']
        --metric <metric>                     Go to <insert link here>
                                                  for a complete list of metrics
                                              Only include --metric if --type is METRIC
        --duration <duration-of-condition>    Duration of time the condition must be true before an alert is triggered
                                              Duration options: TWO, SIX, HOURLY, DAILY
                                              TWO: 2 minutes, SIX: 6 minutes, HOURLY: 1 hour, DAILY: 1 day
                                              Duration mandatory for certain alert rule types
        -v, --verbose                         Increase verbosity
    """

    id = str(list_clusters()["id"])
    convert_mongo()

    notif = eval(params['--notifications'])
    for i in range(len(notif)):
        notif[i] = notif[i].upper()

    body = {'clusterId': id, 'databaseType': params['db-type'].upper(), 'alertRuleType': params['--type'].upper(),
            'operator': params['--operator'].upper(), 'threshold': params['--threshold'],
            'notifications': notif}
    if params['--metric'] != None:
        body['metric'] = params['--metric'].upper()
    if params['--duration'] != None:
        body['averageType'] = params['--duration'].upper()

    resp = get_resp("/AlertRules/create", "POST", body=body)

    rule = resp["rule"]
    print_obj(rule, RULE_VALS)
    logger.info("Alert rule created successfully")
    logger.debug("Alert Rule ID: %s" % rule["id"])

def list_alert_rules():
    """
    \r
    List all the alert rules for a particular cluster

    Usage:
        sg-cli (mongo | redis | mysql | postgresql) list-alert-rules --cluster-name <unique-cluster-name> [options]

    Options:
        --cluster-name <unique-cluster-name>  Name of a cluster
        -v, --verbose                         Increase verbosity
    """

    id = str(list_clusters()["id"])
    convert_mongo()
    resp = get_resp("/AlertRules/list", "POST", body={'clusterId': id, 'databaseType': params['db-type'].upper()})

    rules = resp["rules"]
    if len(rules) == 0:
        sys.stdout.write("No rules for this cluster")
        sys.stdout.write("\n")
    for i in rules:
        print_obj(i, RULE_VALS)

def delete_alert_rule():
    """
    \r
    Delete an alert rule from a particular cluster

    Usage:
        sg-cli delete-alert-rule --alert-rule-id <id-of-alert-rule> [options]

    Options:
        --alert-rule-id <id-of-alert-rule>  Alert rule ID
                                            Get ID from list-alert-rules command
        --force-delete                      Include to force the rule to delete [default: false]
        -v, --verbose                       Increase verbosity
    """

    resp = get_resp("/AlertRules/%s" % params['--alert-rule-id'], "DELETE", body={'forceDelete': params['--force-delete']})
    logger.info("Alert rule deleted successfully")

def list_cloud_profiles():
    """
    \r
    Get a list of all your cloud profiles

    Usage:
        sg-cli list-cloud-profiles [options]

    Options:
        --cloud-profile-name <unique-name-of-cloud-profile>  Unique name of a cloud profile
        -v, --verbose                                        Increase verbosity
    """

    resp = get_resp("/clouds/list", "GET")
    clouds = resp["clouds"]

    if params['--cloud-profile-name']:
        return get_obj(clouds, params['--cloud-profile-name'], "cloudProfile")
    else:
        if len(clouds) == 0:
            sys.stdout.write("No cloud profiles")
            sys.stdout.write("\n")
        for i in clouds:
            print_obj(i, PROFILE_VALS)

def create_script(resp):
    logger.info("Download and run either the PowerShell/CLI script to grant ScaleGrid the required permissions. This script creates a new ScaleGrid resource group and grants ScaleGrid permissions to it. The azure user to run this script requires account admin and global AD admin permissions.")
    scriptType = None
    while scriptType != 'azure' and scriptType != 'powershell':
        scriptType = input("Type 'azure' to download the Azure CLI script. Type 'powershell' to download the PowerShell script: ").lower()
    if scriptType == 'azure':
        scriptName = "grant-sg-permissions.sh"
        scriptContent = resp['bashPermissionsScript']
    else:
        scriptName = "grant-sg-permissions.ps1"
        scriptContent = resp['permissionsScript']
    scriptFile = get_filepath(scriptName)
    try:
        with open(scriptFile, "w") as f:
            f.write(scriptContent)
    except Exception as e:
        raise SGException("There was an error writing to " + scriptFile, "Check permissions for the file")
    logger.info("Run the script located at %s called %s" % (get_filepath(''), scriptName))

def create_cloud_profile():
    """
    \r
    Create a cloud profile

    Usage:
        sg-cli (mongo | redis | mysql | postgresql) create-cloud-profile --aws --cloud-profile-name <unique-name-of-cloud-profile> --region <region> --access-key <access-key> --secret-key <secret-key> --vpc-id <vpc-id> --subnet-id <subnet-id> --vpc-cidr <vpc-cidr> --subnet-cidr <subnet-cidr> --security-group-name <security-group-name> --security-group-id <security-group-id> [--connectivity-config <config> --enable-ssh] [-v | --verbose]
        sg-cli (mongo | redis | mysql | postgresql) create-cloud-profile --azure --cloud-profile-name <unique-name-of-cloud-profile> --region <region> --subscription-id <subscription-id> --subnet-name <subnet-name> --vnet-name <vnet-name> --vnet-resource-group <vnet-resource-group> --security-group-name <security-group-name> [--is-public] [--use-single-tennant-sp] [-v | --verbose]

    Options:
        --aws                                                Include to create AWS cloud profile
        --azure                                              Include to create Azure cloud profile
        --cloud-profile-name <unique-name-of-cloud-profile>  Unique name of a cloud profile
        --region <region>                                    AWS or Azure region
        --access-key <access-key>                            AWS account access key
        --secret-key <secret-key>                            AWS account secret key
        --vpc-id <vpc-id>                                    AWS VPC ID
        --subnet-id <subnet-id>                              AWS VPC subnet ID
        --vpc-cidr <vpc-cidr>                                AWS VPC CIDR
        --subnet-cidr <subnet-cidr>                          AWS VPC Subnet CIDR
        --security-group-name <security-group-name>          AWS or Azure security group name
        --security-group-id <security-group-id>              AWS VPC security group id
        --connectivity-config <config>                       AWS connectivity configuration [default: INTERNET]
                                                             Configuration options: INTERNET, INTRANET, SECURITYGROUP, CUSTOMIPRANGE
        --enable-ssh                                         Include to enable SSH for AWS VPC
        --subscription-id <subscription-id>                  Azure subscription id
        --subnet-name <subnet-name>                          Azure subnet name
        --vnet-name <vnet-name>                              Azure vnet name
        --vnet-resource-group <vnet-resource-group>          Azure vnet resource group name
        --is-public                                          Include to provide a static public IP for your cloud profile
        --use-single-tennant-sp                              Include to use single tennant service principal
        -v, --verbose                                        Increase verbosity
    """

    convert_mongo()
    if params['--aws']:
        body = {'accessKey': params['--access-key'], 'secretKey': params['--secret-key'], 'database': params['db-type'].upper(),
                'region': params['--region'].lower(), 'deploymentStyle': 'VPC', 'connectivityConfig': params['--connectivity-config'],
                'name': params['--cloud-profile-name'], 'vpcID': params['--vpc-id'], 'vpcSubnetID': params['--subnet-id'],
                'vpcCIDR': params['--vpc-cidr'], 'vpcSubnetCIDR': params['--subnet-cidr'], 'vpcSecurityGroupID': params['--security-group-id'],
                'vpcSecurityGroup': params['--security-group-name'], 'dbType': params['db-type'].upper(), 'enableSSH': params['--enable-ssh']}
        call = "/clouds/createMachinePoolForEC2"
    else:
        body = {'name': params['--cloud-profile-name'], 'region': params['--region'], 'subscriptionID': params['--subscription-id'],
                'dbType': params['db-type'].upper(), 'azureTenantId': None, 'subnetName': params['--subnet-name'], 'isPublic': params['--is-public'],
                'vnetName': params['--vnet-name'], 'vnetResourceGroup': params['--vnet-resource-group'], 'securityGroupName': params['--security-group-name'],
                'resourceGroupName': "ScaleGrid-%s" % params['--cloud-profile-name'], 'useSingleTennantSP': params['--use-single-tennant-sp'], 'enablePremiumStorage': False}
        resp = get_resp("/Clouds/generateScriptForAzureARMCloudProfile", "POST", body=body)

        create_script(resp)
        input("Press enter once the script has been executed...")

        body.pop('azureTenantId')
        body.pop('enablePremiumStorage')
        call = "/clouds/createMachinePoolForAzureARM"

    resp = get_resp(call, "POST", body=body)
    print_id(resp["machinePoolID"], "cloud profile")
    print_action_id(resp)

def update_cloud_profile_keys():
    """
    \r
    Update Keys in AWS Cloud Profile

    Usage:
        sg-cli update-cloud-profile-keys --cloud-profile-name <unique-name-of-cloud-profile> --access-key <new-access-key> --secret-key <new-secret-key> [options]

    Options:
        --cloud-profile-name <unique-name-of-cloud-profile>  Unique name of a cloud profile
        --access-key <new-access-key>                        New AWS access key to update in cloud profile
        --secret-key <new-secret-key>                        New AWS secret key to update in cloud profile
        -v, --verbose                                        Increase verbosity
    """

    id = list_cloud_profiles()["id"]
    body = {'machinePoolID': id, 'accessKey': params['--access-key'], 'secretKey': params['--secret-key']}
    resp = get_resp("/Clouds/updateEC2MachinePoolKeys", "POST", body=body)
    logger.info("AWS cloud profile keys updated successfully")

def delete_cloud_profile():
    """
    \r
    Delete a cloud profile

    Usage:
        sg-cli delete-cloud-profile --cloud-profile-name <unique-name-of-cloud-profile> [options]

    Options:
        --cloud-profile-name <unique-name-of-cloud-profile>  Unique name of a cloud profile
        -v, --verbose                                        Increase verbosity
    """

    id = str(list_cloud_profiles()["id"])
    call = "/clouds/%s" % id
    resp = get_resp(call, "DELETE")

    logger.info("Cloud profile delete started successfully")
    print_action_id(resp)

def logout():
    """
    \r
    Logout of your ScaleGrid account

    Usage:
        sg-cli logout [options]

    Options:
        -v, --verbose            Increase verbosity
    """

    conn.request("GET", "/logout")
    check_resp(302)

    logger.debug("Removing cookie")
    delete_cookie()
    logger.info("Cookie removed, logging out...")

def mongo_h():
    """
    \r
    MongoDB Help Menu

    Usage:
        sg-cli mongo <command> [<args>...]

    Options:
        -v, --verbose  Increase verbosity
        -h, --help     Show this menu
        -V --version   Show version

    Commands:
        add-firewall-rules
        build-index
        compact
        create-alert-rule
        create-cloud-profile
        create-cluster
        create-follower-cluster
        delete-backup
        delete-cluster
        get-active-alerts
        get-cluster-credentials
        list-alert-rules
        list-backups
        list-cloud-profiles
        list-clusters
        patch-os
        pause-cluster
        peek-at-backup
        resolve-alerts
        restore-backup
        resume-cluster
        scale-up
        set-backup-schedule
        start-backup

    Use sg-cli <command> -h to open the help menu for the command.
    """

def redis_h():
    """
    \r
    Redis Help Menu

    Usage:
        sg-cli redis <command> [<args>...]

    Options:
        -v, --verbose  Increase verbosity
        -h, --help     Show this menu
        -V --version   Show version

    Commands:
        create-cluster
        delete-backup
        delete-cluster
        get-cluster-credentials
        get-backup-schedule
        list-clusters
        list-backups
        peek-at-backup
        restore-backup
        scale-up
        set-backup-schedule
        start-backup
    
    Use sg-cli <command> -h to open the help menu for the command.
    """

def mysql_h():
    """
    \r
    MySQL Help Menu

    Usage:
        sg-cli mysql <command> [<args>...]

    Options:
        -v, --verbose  Increase verbosity
        -h, --help     Show this menu
        -V --version   Show version

    Commands:
        mysql commands
    """

def postgresql_h():
    """
    \r
    PostgreSQL Help Menu

    Usage:
        sg-cli postgresql <command> [<args>...]

    Options:
        -v, --verbose  Increase verbosity
        -h, --help     Show this menu
        -V --version   Show version

    Commands:
        postgresql commands
    """

def get_db_type(args):
    if args['mongo']:
        return 'Mongo'
    elif args['redis']:
        return 'Redis'
    elif args['mysql']:
        return 'MySQL'
    elif args['postgresql']:
        return "PostgreSQL"
    return None

def get_argv(args, command, dbType):
    if command != 'login' and command != 'logout' and dbType != None:
        return [dbType.lower()] + [args['<command>']] + args['<args>']
    else:
        return [args['<command>']] + args['<args>']

def mod_command(command, dbType):
    command = command.replace('-','_')
    if command == "__help" or command == "_h":
        command = dbType.lower() + "_h"
    return command

def create_params(command, dbType, argv):
    global params
    try:
        try:
            params = docopt(eval(command).__doc__, argv=argv)
        except DocoptExit:
            sys.stderr.write(eval(command).__doc__)
            sys.exit(1)
    except Exception as e:
        raise SGException("Error evaluating arguments. Command %s was not found" % command, "Check parameters and try again")
    try:
        params['db-type'] = dbType
    except AttributeError as e:
        pass

def mod_size():
    global params
    try:
        params['--size'] = params['--size'].lower()
        if not (params['--size'].lower() == 'micro' or params['--size'].lower() == 'small' or params['--size'].lower() == 'medium' or params['--size'].lower() == 'large' or params['--size'].lower() == 'xlarge' or params['--size'].lower() == 'x2xlarge' or params['--size'].lower() == 'x4xlarge'):
            raise SGException("Invalid size for cluster", "--size must have argument small, medium, large, xlarge, x2xlarge, or x4xlarge, not %s" % params['--size'])
        params['--size'] = params['--size'].replace('xl', 'XL')
        params['--size'] = params['--size'][0].upper() + params['--size'][1:]
    except KeyError as e:
        pass

def execute_command(command):
    connect()
    if command != 'login' and command != 'logout':
        load_header()
    return eval(command)()

def print_returned(command, returned):
    objType = command.split('_')[len(command.split('_'))-1]
    if objType.lower() == "status":
        print_obj(returned, eval(objType[:len(objType)].upper() + "_VALS"))
    else:
        print_obj(returned, eval(objType[:len(objType)-1].upper() + "_VALS"))

def main():
    global params
    set_server_ip()
    create_handler()
    try:
        try:
            args = docopt(__doc__, version=("ScaleGrid CLI " + VERSION), options_first=True)
        except DocoptExit:
            sys.stderr.write(__doc__.rstrip())
            sys.exit(1)

        command = args['<command>'].lower()
        dbType = get_db_type(args)

        argv = get_argv(args, command, dbType)
        if '-v' in set(argv) or '--verbose' in set(argv):
            logger.setLevel('DEBUG')

        command = mod_command(command, dbType)
        create_params(command, dbType, argv)
        mod_size()

        returned = execute_command(command)
        if returned != None:
            print_returned(command, returned)
    except Exception as e:
        try:
            display_error_message(e.getMessage(), e.getRecAction())
        except Exception as e:
            display_error_message("Internal error")
        sys.exit(1)

if __name__ == '__main__':
    main()

