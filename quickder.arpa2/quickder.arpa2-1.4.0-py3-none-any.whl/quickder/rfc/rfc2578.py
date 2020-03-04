#
# asn2quickder output for RFC2578 -- automatically generated
#
# Read more about Quick `n' Easy DER on https://gitlab.com/arpa2/quick-der
#


#
# Import general definitions and package dependencies
#

from arpa2.quickder import api as _api

#
# Classes for ASN.1 type assignments
#

# Counter64 ::= [APPLICATION 6] IMPLICIT INTEGER (0..18446744073709551615)
class Counter64 (_api.ASN1Integer):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(6)) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Integer'], 0)
    _context = globals ()
    _numcursori = 1

# IpAddress ::= [APPLICATION 0] IMPLICIT OCTET STRING SIZE(4)
class IpAddress (_api.ASN1OctetString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(0)) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OctetString'], 0)
    _context = globals ()
    _numcursori = 1

# TimeTicks ::= [APPLICATION 3] IMPLICIT INTEGER (0..4294967295)
class TimeTicks (_api.ASN1Integer):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(3)) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Integer'], 0)
    _context = globals ()
    _numcursori = 1

# Opaque ::= [APPLICATION 4] IMPLICIT OCTET STRING
class Opaque (_api.ASN1OctetString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(4)) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OctetString'], 0)
    _context = globals ()
    _numcursori = 1

# Counter32 ::= [APPLICATION 1] IMPLICIT INTEGER (0..4294967295)
class Counter32 (_api.ASN1Integer):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(1)) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Integer'], 0)
    _context = globals ()
    _numcursori = 1

# Unsigned32 ::= [APPLICATION 2] IMPLICIT INTEGER (0..4294967295)
class Unsigned32 (_api.ASN1Integer):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(2)) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Integer'], 0)
    _context = globals ()
    _numcursori = 1

# ApplicationSyntax ::= CHOICE { ipAddress-value IpAddress, counter-value Counter32, timeticks-value TimeTicks, arbitrary-value Opaque, big-counter-value Counter64, unsigned-integer-value Unsigned32 }
class ApplicationSyntax (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(6)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(2)) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'ipAddress_value': ('_TYPTR', ['IpAddress'], 0),
        'counter_value': ('_TYPTR', ['Counter32'], 1),
        'timeticks_value': ('_TYPTR', ['TimeTicks'], 2),
        'arbitrary_value': ('_TYPTR', ['Opaque'], 3),
        'big_counter_value': ('_TYPTR', ['Counter64'], 4),
        'unsigned_integer_value': ('_TYPTR', ['Unsigned32'], 5) } )
    _context = globals ()
    _numcursori = 6

# ExtUTCTime ::= OCTET STRING SIZE(11..13)
class ExtUTCTime (_api.ASN1OctetString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OctetString'], 0)
    _context = globals ()
    _numcursori = 1

# Gauge32 ::= [APPLICATION 2] IMPLICIT INTEGER (0..4294967295)
class Gauge32 (_api.ASN1Integer):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(2)) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Integer'], 0)
    _context = globals ()
    _numcursori = 1

# Integer32 ::= INTEGER (-2147483648..2147483647)
class Integer32 (_api.ASN1Integer):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Integer'], 0)
    _context = globals ()
    _numcursori = 1

# NotificationName ::= OBJECT IDENTIFIER
class NotificationName (_api.ASN1OID):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OID'], 0)
    _context = globals ()
    _numcursori = 1

# ObjectName ::= OBJECT IDENTIFIER
class ObjectName (_api.ASN1OID):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OID'], 0)
    _context = globals ()
    _numcursori = 1

# SimpleSyntax ::= CHOICE { integer-value INTEGER (-2147483648..2147483647), string-value OCTET STRING SIZE(0..65535), objectID-value OBJECT IDENTIFIER }
class SimpleSyntax (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'integer_value': ('_TYPTR', ['_api.ASN1Integer'], 0),
        'string_value': ('_TYPTR', ['_api.ASN1OctetString'], 1),
        'objectID_value': ('_TYPTR', ['_api.ASN1OID'], 2) } )
    _context = globals ()
    _numcursori = 3

# ObjectSyntax ::= CHOICE { simple SimpleSyntax, application-wide ApplicationSyntax }
class ObjectSyntax (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(6)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(2)) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'simple': ('_TYPTR', ['SimpleSyntax'], 0),
        'application_wide': ('_TYPTR', ['ApplicationSyntax'], 3) } )
    _context = globals ()
    _numcursori = 9

#
# Variables with ASN.1 value assignments
#

# org OBJECT IDENTIFIER ::= {1 3}
org = _api.ASN1OID (bindata=[_api.der_format_OID ('1.3')], context={})

# dod OBJECT IDENTIFIER ::= {org 6}
dod = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (org.get()) + '.6')], context={})

# internet OBJECT IDENTIFIER ::= {dod 1}
internet = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (dod.get()) + '.1')], context={})

# directory OBJECT IDENTIFIER ::= {internet 1}
directory = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (internet.get()) + '.1')], context={})

# private OBJECT IDENTIFIER ::= {internet 4}
private = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (internet.get()) + '.4')], context={})

# enterprises OBJECT IDENTIFIER ::= {private 1}
enterprises = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (private.get()) + '.1')], context={})

# experimental OBJECT IDENTIFIER ::= {internet 3}
experimental = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (internet.get()) + '.3')], context={})

# mgmt OBJECT IDENTIFIER ::= {internet 2}
mgmt = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (internet.get()) + '.2')], context={})

# mib-2 OBJECT IDENTIFIER ::= {mgmt 1}
mib_2 = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (mgmt.get()) + '.1')], context={})

# security OBJECT IDENTIFIER ::= {internet 5}
security = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (internet.get()) + '.5')], context={})

# snmpV2 OBJECT IDENTIFIER ::= {internet 6}
snmpV2 = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (internet.get()) + '.6')], context={})

# snmpDomains OBJECT IDENTIFIER ::= {snmpV2 1}
snmpDomains = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (snmpV2.get()) + '.1')], context={})

# snmpModules OBJECT IDENTIFIER ::= {snmpV2 3}
snmpModules = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (snmpV2.get()) + '.3')], context={})

# snmpProxys OBJECT IDENTIFIER ::= {snmpV2 2}
snmpProxys = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (snmpV2.get()) + '.2')], context={})

# transmission OBJECT IDENTIFIER ::= {mib-2 10}
transmission = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (mib_2.get()) + '.10')], context={})

# zeroDotZero OBJECT IDENTIFIER ::= {0 0}
zeroDotZero = _api.ASN1OID (bindata=[_api.der_format_OID ('0.0')], context={})


# asn2quickder output for RFC2578 ends here
