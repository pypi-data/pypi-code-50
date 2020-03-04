#
# asn2quickder output for LDAPv3 -- automatically generated
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

# MessageID ::= INTEGER (0..maxInt)
class MessageID (_api.ASN1Integer):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Integer'], 0)
    _context = globals ()
    _numcursori = 1

# AbandonRequest ::= [APPLICATION 16] MessageID
class AbandonRequest (MessageID):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(16)) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['MessageID'], 0)
    _context = globals ()
    _numcursori = 1

# LDAPString ::= OCTET STRING
class LDAPString (_api.ASN1OctetString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OctetString'], 0)
    _context = globals ()
    _numcursori = 1

# AttributeDescription ::= LDAPString
class AttributeDescription (LDAPString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['LDAPString'], 0)
    _context = globals ()
    _numcursori = 1

# AttributeValue ::= OCTET STRING
class AttributeValue (_api.ASN1OctetString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OctetString'], 0)
    _context = globals ()
    _numcursori = 1

# Attribute ::= SEQUENCE { type AttributeDescription, vals SET SIZE(1..MAX) OF AttributeValue }
class Attribute (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'type': ('_TYPTR', ['AttributeDescription'], 0),
        'vals': ('_SETOF', 1, (
            chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
            chr(_api.DER_PACK_END) ),1,
            ('_TYPTR', ['AttributeValue'], 0) ) } )
    _context = globals ()
    _numcursori = 2

# AttributeList ::= SEQUENCE OF attribute Attribute
class AttributeList (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) ),2,
        ('_TYPTR', ['Attribute'], 0) )
    _context = globals ()
    _numcursori = 1

# LDAPDN ::= LDAPString
class LDAPDN (LDAPString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['LDAPString'], 0)
    _context = globals ()
    _numcursori = 1

# AddRequest ::= [APPLICATION 8] SEQUENCE { entry LDAPDN, attributes AttributeList }
class AddRequest (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(8)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'entry': ('_TYPTR', ['LDAPDN'], 0),
        'attributes': ('_TYPTR', ['AttributeList'], 1) } )
    _context = globals ()
    _numcursori = 2

# URI ::= LDAPString
class URI (LDAPString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['LDAPString'], 0)
    _context = globals ()
    _numcursori = 1

# Referral ::= SEQUENCE SIZE(1..MAX) OF uri URI
class Referral (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) ),1,
        ('_TYPTR', ['URI'], 0) )
    _context = globals ()
    _numcursori = 1

# LDAPResult ::= SEQUENCE { resultCode ENUMERATED { success (0), operationsError (1), protocolError (2), timeLimitExceeded (3), sizeLimitExceeded (4), compareFalse (5), compareTrue (6), authMethodNotSupported (7), strongerAuthRequired (8), referral (10), adminLimitExceeded (11), unavailableCriticalExtension (12), confidentialityRequired (13), saslBindInProgress (14), noSuchAttribute (16), undefinedAttributeType (17), inappropriateMatching (18), constraintViolation (19), attributeOrValueExists (20), invalidAttributeSyntax (21), noSuchObject (32), aliasProblem (33), invalidDNSyntax (34), aliasDereferencingProblem (36), inappropriateAuthentication (48), invalidCredentials (49), insufficientAccessRights (50), busy (51), unavailable (52), unwillingToPerform (53), loopDetect (54), namingViolation (64), objectClassViolation (65), notAllowedOnNonLeaf (66), notAllowedOnRDN (67), entryAlreadyExists (68), objectClassModsProhibited (69), affectsMultipleDSAs (71), other (80), ... }, matchedDN LDAPDN, diagnosticMessage LDAPString, referral [3] Referral OPTIONAL }
class LDAPResult (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'resultCode': ('_TYPTR', ['_api.ASN1Enumerated'], 0),
        'matchedDN': ('_TYPTR', ['LDAPDN'], 1),
        'diagnosticMessage': ('_TYPTR', ['LDAPString'], 2),
        'referral': ('_TYPTR', ['Referral'], 3) } )
    _context = globals ()
    _numcursori = 4

# AddResponse ::= [APPLICATION 9] LDAPResult
class AddResponse (LDAPResult):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(9)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['LDAPResult'], 0)
    _context = globals ()
    _numcursori = 4

# AssertionValue ::= OCTET STRING
class AssertionValue (_api.ASN1OctetString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OctetString'], 0)
    _context = globals ()
    _numcursori = 1

# AttributeSelection ::= SEQUENCE OF selector LDAPString
class AttributeSelection (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) ),1,
        ('_TYPTR', ['LDAPString'], 0) )
    _context = globals ()
    _numcursori = 1

# AttributeValueAssertion ::= SEQUENCE { attributeDesc AttributeDescription, assertionValue AssertionValue }
class AttributeValueAssertion (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'attributeDesc': ('_TYPTR', ['AttributeDescription'], 0),
        'assertionValue': ('_TYPTR', ['AssertionValue'], 1) } )
    _context = globals ()
    _numcursori = 2

# SaslCredentials ::= SEQUENCE { mechanism LDAPString, credentials OCTET STRING OPTIONAL }
class SaslCredentials (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'mechanism': ('_TYPTR', ['LDAPString'], 0),
        'credentials': ('_TYPTR', ['_api.ASN1OctetString'], 1) } )
    _context = globals ()
    _numcursori = 2

# AuthenticationChoice ::= CHOICE { simple [0] OCTET STRING, sasl [3] SaslCredentials, ... }
class AuthenticationChoice (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'simple': ('_TYPTR', ['_api.ASN1OctetString'], 0),
        'sasl': ('_TYPTR', ['SaslCredentials'], 1) } )
    _context = globals ()
    _numcursori = 3

# BindRequest ::= [APPLICATION 0] SEQUENCE { version INTEGER (1..127), name LDAPDN, authentication AuthenticationChoice }
class BindRequest (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'version': ('_TYPTR', ['_api.ASN1Integer'], 0),
        'name': ('_TYPTR', ['LDAPDN'], 1),
        'authentication': ('_TYPTR', ['AuthenticationChoice'], 2) } )
    _context = globals ()
    _numcursori = 5

# BindResponse ::= [APPLICATION 1] SEQUENCE { resultCode ENUMERATED { success (0), operationsError (1), protocolError (2), timeLimitExceeded (3), sizeLimitExceeded (4), compareFalse (5), compareTrue (6), authMethodNotSupported (7), strongerAuthRequired (8), referral (10), adminLimitExceeded (11), unavailableCriticalExtension (12), confidentialityRequired (13), saslBindInProgress (14), noSuchAttribute (16), undefinedAttributeType (17), inappropriateMatching (18), constraintViolation (19), attributeOrValueExists (20), invalidAttributeSyntax (21), noSuchObject (32), aliasProblem (33), invalidDNSyntax (34), aliasDereferencingProblem (36), inappropriateAuthentication (48), invalidCredentials (49), insufficientAccessRights (50), busy (51), unavailable (52), unwillingToPerform (53), loopDetect (54), namingViolation (64), objectClassViolation (65), notAllowedOnNonLeaf (66), notAllowedOnRDN (67), entryAlreadyExists (68), objectClassModsProhibited (69), affectsMultipleDSAs (71), other (80), ... }, matchedDN LDAPDN, diagnosticMessage LDAPString, referral [3] Referral OPTIONAL, serverSaslCreds [7] OCTET STRING OPTIONAL }
class BindResponse (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(7)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'resultCode': ('_TYPTR', ['_api.ASN1Enumerated'], 0),
        'matchedDN': ('_TYPTR', ['LDAPDN'], 1),
        'diagnosticMessage': ('_TYPTR', ['LDAPString'], 2),
        'referral': ('_TYPTR', ['Referral'], 3),
        'serverSaslCreds': ('_TYPTR', ['_api.ASN1OctetString'], 4) } )
    _context = globals ()
    _numcursori = 5

# CompareRequest ::= [APPLICATION 14] SEQUENCE { entry LDAPDN, ava AttributeValueAssertion }
class CompareRequest (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(14)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'entry': ('_TYPTR', ['LDAPDN'], 0),
        'ava': ('_TYPTR', ['AttributeValueAssertion'], 1) } )
    _context = globals ()
    _numcursori = 3

# CompareResponse ::= [APPLICATION 15] LDAPResult
class CompareResponse (LDAPResult):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(15)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['LDAPResult'], 0)
    _context = globals ()
    _numcursori = 4

# LDAPOID ::= OCTET STRING
class LDAPOID (_api.ASN1OctetString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OctetString'], 0)
    _context = globals ()
    _numcursori = 1

# Control ::= SEQUENCE { controlType LDAPOID, criticality BOOLEAN DEFAULT FALSE, controlValue OCTET STRING OPTIONAL }
class Control (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'controlType': ('_TYPTR', ['LDAPOID'], 0),
        'criticality': ('_TYPTR', ['_api.ASN1Boolean'], 1),
        'controlValue': ('_TYPTR', ['_api.ASN1OctetString'], 2) } )
    _context = globals ()
    _numcursori = 3

# Controls ::= SEQUENCE OF control Control
class Controls (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) ),3,
        ('_TYPTR', ['Control'], 0) )
    _context = globals ()
    _numcursori = 1

# DelRequest ::= [APPLICATION 10] LDAPDN
class DelRequest (LDAPDN):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(10)) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['LDAPDN'], 0)
    _context = globals ()
    _numcursori = 1

# DelResponse ::= [APPLICATION 11] LDAPResult
class DelResponse (LDAPResult):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(11)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['LDAPResult'], 0)
    _context = globals ()
    _numcursori = 4

# ExtendedRequest ::= [APPLICATION 23] SEQUENCE { requestName [0] LDAPOID, requestValue [1] OCTET STRING OPTIONAL }
class ExtendedRequest (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(23)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'requestName': ('_TYPTR', ['LDAPOID'], 0),
        'requestValue': ('_TYPTR', ['_api.ASN1OctetString'], 1) } )
    _context = globals ()
    _numcursori = 2

# ExtendedResponse ::= [APPLICATION 24] SEQUENCE { resultCode ENUMERATED { success (0), operationsError (1), protocolError (2), timeLimitExceeded (3), sizeLimitExceeded (4), compareFalse (5), compareTrue (6), authMethodNotSupported (7), strongerAuthRequired (8), referral (10), adminLimitExceeded (11), unavailableCriticalExtension (12), confidentialityRequired (13), saslBindInProgress (14), noSuchAttribute (16), undefinedAttributeType (17), inappropriateMatching (18), constraintViolation (19), attributeOrValueExists (20), invalidAttributeSyntax (21), noSuchObject (32), aliasProblem (33), invalidDNSyntax (34), aliasDereferencingProblem (36), inappropriateAuthentication (48), invalidCredentials (49), insufficientAccessRights (50), busy (51), unavailable (52), unwillingToPerform (53), loopDetect (54), namingViolation (64), objectClassViolation (65), notAllowedOnNonLeaf (66), notAllowedOnRDN (67), entryAlreadyExists (68), objectClassModsProhibited (69), affectsMultipleDSAs (71), other (80), ... }, matchedDN LDAPDN, diagnosticMessage LDAPString, referral [3] Referral OPTIONAL, responseName [10] LDAPOID OPTIONAL, responseValue [11] OCTET STRING OPTIONAL }
class ExtendedResponse (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(24)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(10)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(11)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'resultCode': ('_TYPTR', ['_api.ASN1Enumerated'], 0),
        'matchedDN': ('_TYPTR', ['LDAPDN'], 1),
        'diagnosticMessage': ('_TYPTR', ['LDAPString'], 2),
        'referral': ('_TYPTR', ['Referral'], 3),
        'responseName': ('_TYPTR', ['LDAPOID'], 4),
        'responseValue': ('_TYPTR', ['_api.ASN1OctetString'], 5) } )
    _context = globals ()
    _numcursori = 6

# Filter ::= ANY
class Filter (_api.ASN1Any):
    _der_packer = (
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Any'], 0)
    _context = globals ()
    _numcursori = 1

# SubstringFilter ::= SEQUENCE { type AttributeDescription, substrings SEQUENCE SIZE(1..MAX) OF substring CHOICE { initial [0] AssertionValue, any [1] AssertionValue, final [2] AssertionValue } }
class SubstringFilter (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'type': ('_TYPTR', ['AttributeDescription'], 0),
        'substrings': ('_SEQOF', 1, (
            chr(_api.DER_PACK_CHOICE_BEGIN) +
            chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
            chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(1)) +
            chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(2)) +
            chr(_api.DER_PACK_CHOICE_END) +
            chr(_api.DER_PACK_END) ),3,
            ('_NAMED', {
                'initial': ('_TYPTR', ['AssertionValue'], 0),
                'any': ('_TYPTR', ['AssertionValue'], 1),
                'final': ('_TYPTR', ['AssertionValue'], 2) } ) ) } )
    _context = globals ()
    _numcursori = 2

# MatchingRuleId ::= LDAPString
class MatchingRuleId (LDAPString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['LDAPString'], 0)
    _context = globals ()
    _numcursori = 1

# MatchingRuleAssertion ::= SEQUENCE { matchingRule [1] MatchingRuleId OPTIONAL, type [2] AttributeDescription OPTIONAL, matchValue [3] AssertionValue, dnAttributes [4] BOOLEAN DEFAULT FALSE }
class MatchingRuleAssertion (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'matchingRule': ('_TYPTR', ['MatchingRuleId'], 0),
        'type': ('_TYPTR', ['AttributeDescription'], 1),
        'matchValue': ('_TYPTR', ['AssertionValue'], 2),
        'dnAttributes': ('_TYPTR', ['_api.ASN1Boolean'], 3) } )
    _context = globals ()
    _numcursori = 4

# FilterOperation ::= CHOICE { andFilter [0] SET SIZE(1..MAX) OF filter Filter, orFilter [1] SET SIZE(1..MAX) OF filter Filter, notFilter [2] Filter, equalityMatch [3] AttributeValueAssertion, substrings [4] SubstringFilter, greaterOrEqual [5] AttributeValueAssertion, lessOrEqual [6] AttributeValueAssertion, present [7] AttributeDescription, approxMatch [8] AttributeValueAssertion, extensibleMatch [9] MatchingRuleAssertion, ... }
class FilterOperation (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(5)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(6)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(7)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(8)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(9)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'andFilter': ('_SETOF', 0, (
            chr(_api.DER_PACK_ANY) +
            chr(_api.DER_PACK_END) ),1,
            ('_TYPTR', ['Filter'], 0) ),
        'orFilter': ('_SETOF', 1, (
            chr(_api.DER_PACK_ANY) +
            chr(_api.DER_PACK_END) ),1,
            ('_TYPTR', ['Filter'], 0) ),
        'notFilter': ('_TYPTR', ['Filter'], 2),
        'equalityMatch': ('_TYPTR', ['AttributeValueAssertion'], 3),
        'substrings': ('_TYPTR', ['SubstringFilter'], 5),
        'greaterOrEqual': ('_TYPTR', ['AttributeValueAssertion'], 7),
        'lessOrEqual': ('_TYPTR', ['AttributeValueAssertion'], 9),
        'present': ('_TYPTR', ['AttributeDescription'], 11),
        'approxMatch': ('_TYPTR', ['AttributeValueAssertion'], 12),
        'extensibleMatch': ('_TYPTR', ['MatchingRuleAssertion'], 14) } )
    _context = globals ()
    _numcursori = 18

# IntermediateResponse ::= [APPLICATION 25] SEQUENCE { responseName [0] LDAPOID OPTIONAL, responseValue [1] OCTET STRING OPTIONAL }
class IntermediateResponse (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(25)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'responseName': ('_TYPTR', ['LDAPOID'], 0),
        'responseValue': ('_TYPTR', ['_api.ASN1OctetString'], 1) } )
    _context = globals ()
    _numcursori = 2

# SearchResultDone ::= [APPLICATION 5] LDAPResult
class SearchResultDone (LDAPResult):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(5)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['LDAPResult'], 0)
    _context = globals ()
    _numcursori = 4

# UnbindRequest ::= [APPLICATION 2] NULL
class UnbindRequest (_api.ASN1Null):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(2)) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Null'], 0)
    _context = globals ()
    _numcursori = 1

# PartialAttribute ::= SEQUENCE { type AttributeDescription, vals SET OF value AttributeValue }
class PartialAttribute (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'type': ('_TYPTR', ['AttributeDescription'], 0),
        'vals': ('_SETOF', 1, (
            chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
            chr(_api.DER_PACK_END) ),1,
            ('_TYPTR', ['AttributeValue'], 0) ) } )
    _context = globals ()
    _numcursori = 2

# PartialAttributeList ::= SEQUENCE OF partialAttribute PartialAttribute
class PartialAttributeList (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) ),2,
        ('_TYPTR', ['PartialAttribute'], 0) )
    _context = globals ()
    _numcursori = 1

# SearchResultEntry ::= [APPLICATION 4] SEQUENCE { objectName LDAPDN, attributes PartialAttributeList }
class SearchResultEntry (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'objectName': ('_TYPTR', ['LDAPDN'], 0),
        'attributes': ('_TYPTR', ['PartialAttributeList'], 1) } )
    _context = globals ()
    _numcursori = 2

# ModifyDNResponse ::= [APPLICATION 13] LDAPResult
class ModifyDNResponse (LDAPResult):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(13)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['LDAPResult'], 0)
    _context = globals ()
    _numcursori = 4

# ModifyRequest ::= [APPLICATION 6] SEQUENCE { object LDAPDN, changes SEQUENCE OF change SEQUENCE { operation ENUMERATED { add (0), delete (1), replace (2), ... }, modification PartialAttribute } }
class ModifyRequest (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(6)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'object': ('_TYPTR', ['LDAPDN'], 0),
        'changes': ('_SEQOF', 1, (
            chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
            chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
            chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
            chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
            chr(_api.DER_PACK_STORE | _api.DER_TAG_SET) +
            chr(_api.DER_PACK_LEAVE) +
            chr(_api.DER_PACK_LEAVE) +
            chr(_api.DER_PACK_END) ),3,
            ('_NAMED', {
                'operation': ('_TYPTR', ['_api.ASN1Enumerated'], 0),
                'modification': ('_TYPTR', ['PartialAttribute'], 1) } ) ) } )
    _context = globals ()
    _numcursori = 2

# RelativeLDAPDN ::= LDAPString
class RelativeLDAPDN (LDAPString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['LDAPString'], 0)
    _context = globals ()
    _numcursori = 1

# ModifyDNRequest ::= [APPLICATION 12] SEQUENCE { entry LDAPDN, newrdn RelativeLDAPDN, deleteoldrdn BOOLEAN, newSuperior [0] LDAPDN OPTIONAL }
class ModifyDNRequest (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(12)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'entry': ('_TYPTR', ['LDAPDN'], 0),
        'newrdn': ('_TYPTR', ['RelativeLDAPDN'], 1),
        'deleteoldrdn': ('_TYPTR', ['_api.ASN1Boolean'], 2),
        'newSuperior': ('_TYPTR', ['LDAPDN'], 3) } )
    _context = globals ()
    _numcursori = 4

# SearchResultReference ::= [APPLICATION 19] SEQUENCE SIZE(1..MAX) OF uri URI
class SearchResultReference (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(19)) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) ),1,
        ('_TYPTR', ['URI'], 0) )
    _context = globals ()
    _numcursori = 1

# ModifyResponse ::= [APPLICATION 7] LDAPResult
class ModifyResponse (LDAPResult):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(7)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['LDAPResult'], 0)
    _context = globals ()
    _numcursori = 4

# SearchRequest ::= [APPLICATION 3] SEQUENCE { baseObject LDAPDN, scope ENUMERATED { baseObject (0), singleLevel (1), wholeSubtree (2), ... }, derefAliases ENUMERATED { neverDerefAliases (0), derefInSearching (1), derefFindingBaseObj (2), derefAlways (3) }, sizeLimit INTEGER (0..maxInt), timeLimit INTEGER (0..maxInt), typesOnly BOOLEAN, filter ANY, attributes AttributeSelection }
class SearchRequest (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'baseObject': ('_TYPTR', ['LDAPDN'], 0),
        'scope': ('_TYPTR', ['_api.ASN1Enumerated'], 1),
        'derefAliases': ('_TYPTR', ['_api.ASN1Enumerated'], 2),
        'sizeLimit': ('_TYPTR', ['_api.ASN1Integer'], 3),
        'timeLimit': ('_TYPTR', ['_api.ASN1Integer'], 4),
        'typesOnly': ('_TYPTR', ['_api.ASN1Boolean'], 5),
        'filter': ('_TYPTR', ['_api.ASN1Any'], 6),
        'attributes': ('_TYPTR', ['AttributeSelection'], 7) } )
    _context = globals ()
    _numcursori = 8

# LDAPMessage ::= SEQUENCE { messageID MessageID, protocolOp CHOICE { bindRequest BindRequest, bindResponse BindResponse, unbindRequest UnbindRequest, searchRequest SearchRequest, searchResEntry SearchResultEntry, searchResDone SearchResultDone, searchResRef SearchResultReference, modifyRequest ModifyRequest, modifyResponse ModifyResponse, addRequest AddRequest, addResponse AddResponse, delRequest DelRequest, delResponse DelResponse, modDNRequest ModifyDNRequest, modDNResponse ModifyDNResponse, compareRequest CompareRequest, compareResponse CompareResponse, abandonRequest AbandonRequest, extendedReq ExtendedRequest, extendedResp ExtendedResponse, ..., intermediateResponse IntermediateResponse }, controls [0] Controls OPTIONAL }
class LDAPMessage (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(7)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(2)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(5)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(19)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(6)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(7)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(8)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(9)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(10)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(11)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(12)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(13)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(14)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(15)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_APPLICATION(16)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(23)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(24)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(10)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(11)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(25)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'messageID': ('_TYPTR', ['MessageID'], 0),
        'protocolOp': ('_NAMED', {
            'bindRequest': ('_TYPTR', ['BindRequest'], 1),
            'bindResponse': ('_TYPTR', ['BindResponse'], 6),
            'unbindRequest': ('_TYPTR', ['UnbindRequest'], 11),
            'searchRequest': ('_TYPTR', ['SearchRequest'], 12),
            'searchResEntry': ('_TYPTR', ['SearchResultEntry'], 20),
            'searchResDone': ('_TYPTR', ['SearchResultDone'], 22),
            'searchResRef': ('_TYPTR', ['SearchResultReference'], 26),
            'modifyRequest': ('_TYPTR', ['ModifyRequest'], 27),
            'modifyResponse': ('_TYPTR', ['ModifyResponse'], 29),
            'addRequest': ('_TYPTR', ['AddRequest'], 33),
            'addResponse': ('_TYPTR', ['AddResponse'], 35),
            'delRequest': ('_TYPTR', ['DelRequest'], 39),
            'delResponse': ('_TYPTR', ['DelResponse'], 40),
            'modDNRequest': ('_TYPTR', ['ModifyDNRequest'], 44),
            'modDNResponse': ('_TYPTR', ['ModifyDNResponse'], 48),
            'compareRequest': ('_TYPTR', ['CompareRequest'], 52),
            'compareResponse': ('_TYPTR', ['CompareResponse'], 55),
            'abandonRequest': ('_TYPTR', ['AbandonRequest'], 59),
            'extendedReq': ('_TYPTR', ['ExtendedRequest'], 60),
            'extendedResp': ('_TYPTR', ['ExtendedResponse'], 62),
            'intermediateResponse': ('_TYPTR', ['IntermediateResponse'], 68) } ),
        'controls': ('_TYPTR', ['Controls'], 70) } )
    _context = globals ()
    _numcursori = 71

#
# Variables with ASN.1 value assignments
#

# maxInt INTEGER ::= 2147483647
maxInt = _api.ASN1Integer (bindata=[_api.der_format_INTEGER (2147483647)], context={})


# asn2quickder output for LDAPv3 ends here
