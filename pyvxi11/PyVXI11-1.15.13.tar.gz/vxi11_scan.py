#!python
from __future__ import print_function
import sys
import cVXI11
import argparse,logging
#cVXI11.vxi11logger.warning("start")
logger=logging
#logging.root.setLevel(logging.DEBUG)
cVXI11.vxi11logger.setLevel(logging.DEBUG)

def scan_one(host,device, command=b"*IDN?"): # host,deivce, command are "bytes" type
    try:
        logger.warning("scanning device {} {}".format(host, device))
        cVXI11.Vxi11Device.scan(host, device)
        logger.warning("device found at {} {}".format(host, device))
    except:
        logger.warning("device NOT found at {} {}".format(host, device))
        
def main(host,command=b"*IDN?"):
    print("\n START scanning.\n")
    status=-1

    port=cVXI11.pmap_getport(host,cVXI11.device_core.prog, cVXI11.device_core.version)
    if not port:
        raise IOError("No port available for VXI11 CORE service on {}".format(host))
    
    logger.info("Port number for CORE server for {} is {}".format(host, port))
    
    try:
        device="inst0";
        scan_one(host,device)
        #return
    except:
        pass

    try:
        device="gpib0";
        scan_one(host,device)
        #return
    except:
        pass
        
    for i in range(31):
        try:
            device="gpib0,{}".format(i);
            scan_one(host,device)
            #return
        except:
            pass

    try:
        device="vxi0";
        scan_one(host,device)
        #return
    except:
        pass
        
    for i in range(31):
        try:
            device="vxi0,{}".format(i);
            scan_one(host,device)
            #return
        except:
            pass
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog=sys.argv[0],# default
        usage="{} <host> [command='*IDN?']".format(sys.argv[0]),
        description="Scan VXI11-port on <host>", 
        epilog=None,
        parents=[],
        prefix_chars="-",
        fromfile_prefix_chars=None,
        argument_default=None,
        add_help=True,
        # sys.version_info >=(3,5)
        # allow_abbrev=True
    )
    parser.add_argument("host", help="hostname of the scan target")
    parser.add_argument("-c", "--command", default="*IDN?")
    parser.add_argument("-d", "--device", default=None)
    parser.add_argument("-q", "--quiet", help="reduce info. messages", action="store_true")
    parser.add_argument("-v", "--verbose", help="more info. messages", action="store_true")
    parser.add_argument("-i", "--io-timeout", default=0 )
    args = parser.parse_args()
    print (args)
    if args.quiet :
        logging.root.setLevel( logging.ERROR )
        cVXI11.vxi11logger.setLevel( logging.ERROR )
    elif args.verbose:
        logging.root.setLevel( logging.DEBUG )
        cVXI11.vxi11logger.setLevel( logging.DEBUG )
        
    if args.device:
        scan_one(args.host.encode('ascii'),
                 args.device.encode('ascii'),
                 args.command.encode('ascii'),
                 args.io-timeout,
        )
    else:
        main(args.host.encode('ascii'), args.command.encode('ascii'))
    
