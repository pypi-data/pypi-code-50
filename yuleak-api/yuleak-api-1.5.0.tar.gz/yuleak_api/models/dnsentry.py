class DNSEntry:
    def __init__(self):
        self.domain = None
        self.ip = None
        self.classification = None

    @classmethod
    def from_json(cls, dns_json):
        dns = cls()
        dns.domain = dns_json.get('domain')
        dns.ip = dns_json.get('ip')
        dns.classification = dns_json.get('classification')
        return dns

    def __repr__(self):
        return '<DNS {0}> {1}'.format(self.domain, self.classification)
