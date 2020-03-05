from pyvcloud.vcd.client import BasicLoginCredentials
from pyvcloud.vcd.client import Client
from pyvcloud.vcd.platform import Platform
client = Client("bos1-vcd-sp-static-199-190.eng.vmware.com", verify_ssl_certs=False, log_requests=True)
client.set_credentials(BasicLoginCredentials('administrator', 'System', 'ca$hc0w'))
