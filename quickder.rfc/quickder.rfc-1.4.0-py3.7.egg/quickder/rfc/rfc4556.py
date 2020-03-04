#
# asn2quickder output for KerberosV5-PK-INIT-SPEC -- automatically generated
#
# Read more about Quick `n' Easy DER on https://gitlab.com/arpa2/quick-der
#


#
# Import general definitions and package dependencies
#

from arpa2.quickder import api as _api

from rfc3280 import SubjectPublicKeyInfo, AlgorithmIdentifier
from rfc4120 import KerberosTime, PrincipalName, Realm, EncryptionKey, Checksum


#
# Classes for ASN.1 type assignments
#

# ExternalPrincipalIdentifier ::= SEQUENCE { subjectName [0] IMPLICIT OCTET STRING OPTIONAL, issuerAndSerialNumber [1] IMPLICIT OCTET STRING OPTIONAL, subjectKeyIdentifier [2] IMPLICIT OCTET STRING OPTIONAL, ... }
class ExternalPrincipalIdentifier (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'subjectName': ('_TYPTR', ['_api.ASN1OctetString'], 0),
        'issuerAndSerialNumber': ('_TYPTR', ['_api.ASN1OctetString'], 1),
        'subjectKeyIdentifier': ('_TYPTR', ['_api.ASN1OctetString'], 2) } )
    _context = globals ()
    _numcursori = 3

# AD-INITIAL-VERIFIED-CAS ::= SEQUENCE OF ExternalPrincipalIdentifier
class AD_INITIAL_VERIFIED_CAS (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) ),3,
        ('_TYPTR', ['ExternalPrincipalIdentifier'], 0) )
    _context = globals ()
    _numcursori = 1

# PKAuthenticator ::= SEQUENCE { cusec [0] INTEGER (0..999999), ctime [1] KerberosTime, nonce [2] INTEGER (0..4294967295), paChecksum [3] OCTET STRING OPTIONAL, ... }
class PKAuthenticator (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_GENERALIZEDTIME) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'cusec': ('_TYPTR', ['_api.ASN1Integer'], 0),
        'ctime': ('_TYPTR', ['KerberosTime'], 1),
        'nonce': ('_TYPTR', ['_api.ASN1Integer'], 2),
        'paChecksum': ('_TYPTR', ['_api.ASN1OctetString'], 3) } )
    _context = globals ()
    _numcursori = 4

# DHNonce ::= OCTET STRING
class DHNonce (_api.ASN1OctetString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OctetString'], 0)
    _context = globals ()
    _numcursori = 1

# AuthPack ::= SEQUENCE { pkAuthenticator [0] PKAuthenticator, clientPublicValue [1] SubjectPublicKeyInfo OPTIONAL, supportedCMSTypes [2] SEQUENCE OF AlgorithmIdentifier OPTIONAL, clientDHNonce [3] DHNonce OPTIONAL, ... }
class AuthPack (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_GENERALIZEDTIME) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'pkAuthenticator': ('_TYPTR', ['PKAuthenticator'], 0),
        'clientPublicValue': ('_TYPTR', ['SubjectPublicKeyInfo'], 4),
        'supportedCMSTypes': ('_SEQOF', 7, (
            chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
            chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
            chr(_api.DER_PACK_OPTIONAL) +
            chr(_api.DER_PACK_ANY) +
            chr(_api.DER_PACK_LEAVE) +
            chr(_api.DER_PACK_END) ),2,
            ('_TYPTR', ['AlgorithmIdentifier'], 0) ),
        'clientDHNonce': ('_TYPTR', ['DHNonce'], 8) } )
    _context = globals ()
    _numcursori = 9

# DHRepInfo ::= SEQUENCE { dhSignedData [0] IMPLICIT OCTET STRING, serverDHNonce [1] DHNonce OPTIONAL, ... }
class DHRepInfo (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'dhSignedData': ('_TYPTR', ['_api.ASN1OctetString'], 0),
        'serverDHNonce': ('_TYPTR', ['DHNonce'], 1) } )
    _context = globals ()
    _numcursori = 2

# KDCDHKeyInfo ::= SEQUENCE { subjectPublicKey [0] BIT STRING, nonce [1] INTEGER (0..4294967295), dhKeyExpiration [2] KerberosTime OPTIONAL, ... }
class KDCDHKeyInfo (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_GENERALIZEDTIME) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'subjectPublicKey': ('_TYPTR', ['_api.ASN1BitString'], 0),
        'nonce': ('_TYPTR', ['_api.ASN1Integer'], 1),
        'dhKeyExpiration': ('_TYPTR', ['KerberosTime'], 2) } )
    _context = globals ()
    _numcursori = 3

# KRB5PrincipalName ::= SEQUENCE { realm [0] Realm, principalName [1] PrincipalName }
class KRB5PrincipalName (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_GENERALSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'realm': ('_TYPTR', ['Realm'], 0),
        'principalName': ('_TYPTR', ['PrincipalName'], 1) } )
    _context = globals ()
    _numcursori = 3

# PA-PK-AS-REP ::= CHOICE { dhInfo [0] DHRepInfo, encKeyPack [1] IMPLICIT OCTET STRING, ... }
class PA_PK_AS_REP (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'dhInfo': ('_TYPTR', ['DHRepInfo'], 0),
        'encKeyPack': ('_TYPTR', ['_api.ASN1OctetString'], 2) } )
    _context = globals ()
    _numcursori = 3

# PA-PK-AS-REQ ::= SEQUENCE { signedAuthPack [0] IMPLICIT OCTET STRING, trustedCertifiers [1] SEQUENCE OF ExternalPrincipalIdentifier OPTIONAL, kdcPkId [2] IMPLICIT OCTET STRING OPTIONAL, ... }
class PA_PK_AS_REQ (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'signedAuthPack': ('_TYPTR', ['_api.ASN1OctetString'], 0),
        'trustedCertifiers': ('_SEQOF', 1, (
            chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
            chr(_api.DER_PACK_OPTIONAL) +
            chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
            chr(_api.DER_PACK_OPTIONAL) +
            chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(1)) +
            chr(_api.DER_PACK_OPTIONAL) +
            chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(2)) +
            chr(_api.DER_PACK_LEAVE) +
            chr(_api.DER_PACK_END) ),3,
            ('_TYPTR', ['ExternalPrincipalIdentifier'], 0) ),
        'kdcPkId': ('_TYPTR', ['_api.ASN1OctetString'], 2) } )
    _context = globals ()
    _numcursori = 3

# ReplyKeyPack ::= SEQUENCE { replyKey [0] EncryptionKey, asChecksum [1] Checksum, ... }
class ReplyKeyPack (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'replyKey': ('_TYPTR', ['EncryptionKey'], 0),
        'asChecksum': ('_TYPTR', ['Checksum'], 2) } )
    _context = globals ()
    _numcursori = 4

# TD-DH-PARAMETERS ::= SEQUENCE OF AlgorithmIdentifier
class TD_DH_PARAMETERS (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OBJECTIDENTIFIER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) ),2,
        ('_TYPTR', ['AlgorithmIdentifier'], 0) )
    _context = globals ()
    _numcursori = 1

# TD-INVALID-CERTIFICATES ::= SEQUENCE OF ExternalPrincipalIdentifier
class TD_INVALID_CERTIFICATES (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) ),3,
        ('_TYPTR', ['ExternalPrincipalIdentifier'], 0) )
    _context = globals ()
    _numcursori = 1

# TD-TRUSTED-CERTIFIERS ::= SEQUENCE OF ExternalPrincipalIdentifier
class TD_TRUSTED_CERTIFIERS (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) ),3,
        ('_TYPTR', ['ExternalPrincipalIdentifier'], 0) )
    _context = globals ()
    _numcursori = 1

#
# Variables with ASN.1 value assignments
#

# ad-initial-verified-cas INTEGER ::= 9
ad_initial_verified_cas = _api.ASN1Integer (bindata=[_api.der_format_INTEGER (9)], context={})

# id-pkinit OBJECT IDENTIFIER ::= {iso(1) identified-organization(3) dod(6) internet(1) security(5) kerberosv5(2) pkinit(3)}
id_pkinit = _api.ASN1OID (bindata=[_api.der_format_OID ('1.3.6.1.5.2.3')], context={})

# id-pkinit-DHKeyData OBJECT IDENTIFIER ::= {id-pkinit 2}
id_pkinit_DHKeyData = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_pkinit.get()) + '.2')], context={})

# id-pkinit-KPClientAuth OBJECT IDENTIFIER ::= {id-pkinit 4}
id_pkinit_KPClientAuth = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_pkinit.get()) + '.4')], context={})

# id-pkinit-KPKdc OBJECT IDENTIFIER ::= {id-pkinit 5}
id_pkinit_KPKdc = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_pkinit.get()) + '.5')], context={})

# id-pkinit-authData OBJECT IDENTIFIER ::= {id-pkinit 1}
id_pkinit_authData = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_pkinit.get()) + '.1')], context={})

# id-pkinit-rkeyData OBJECT IDENTIFIER ::= {id-pkinit 3}
id_pkinit_rkeyData = _api.ASN1OID (bindata=[_api.der_format_OID (_api.der_parse_OID (id_pkinit.get()) + '.3')], context={})

# id-pkinit-san OBJECT IDENTIFIER ::= {iso(1) org(3) dod(6) internet(1) security(5) kerberosv5(2) x509SanAN(2)}
id_pkinit_san = _api.ASN1OID (bindata=[_api.der_format_OID ('1.3.6.1.5.2.2')], context={})

# pa-pk-as-rep INTEGER ::= 17
pa_pk_as_rep = _api.ASN1Integer (bindata=[_api.der_format_INTEGER (17)], context={})

# pa-pk-as-req INTEGER ::= 16
pa_pk_as_req = _api.ASN1Integer (bindata=[_api.der_format_INTEGER (16)], context={})

# td-dh-parameters INTEGER ::= 109
td_dh_parameters = _api.ASN1Integer (bindata=[_api.der_format_INTEGER (109)], context={})

# td-invalid-certificates INTEGER ::= 105
td_invalid_certificates = _api.ASN1Integer (bindata=[_api.der_format_INTEGER (105)], context={})

# td-trusted-certifiers INTEGER ::= 104
td_trusted_certifiers = _api.ASN1Integer (bindata=[_api.der_format_INTEGER (104)], context={})


# asn2quickder output for KerberosV5-PK-INIT-SPEC ends here
