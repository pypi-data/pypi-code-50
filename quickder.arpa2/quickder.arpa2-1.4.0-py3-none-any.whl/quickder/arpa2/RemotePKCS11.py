#
# asn2quickder output for RemotePKCS11 -- automatically generated
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

# ACK-ULONG ::= INTEGER (0..4294967295)
class ACK_ULONG (_api.ASN1Integer):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Integer'], 0)
    _context = globals ()
    _numcursori = 1

# ACK-ATTRIBUTE-TYPE ::= ACK-ULONG
class ACK_ATTRIBUTE_TYPE (ACK_ULONG):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['ACK-ULONG'], 0)
    _context = globals ()
    _numcursori = 1

# ACK-OPAQUE ::= OCTET STRING
class ACK_OPAQUE (_api.ASN1OctetString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OctetString'], 0)
    _context = globals ()
    _numcursori = 1

# ACK-ATTRIBUTE ::= SEQUENCE { type ACK-ATTRIBUTE-TYPE, pValue CHOICE { null NULL, data ACK-OPAQUE } OPTIONAL, ulValueLen ACK-ULONG }
class ACK_ATTRIBUTE (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'type': ('_TYPTR', ['ACK-ATTRIBUTE-TYPE'], 0),
        'pValue': ('_NAMED', {
            'null': ('_TYPTR', ['_api.ASN1Null'], 1),
            'data': ('_TYPTR', ['ACK-OPAQUE'], 2) } ),
        'ulValueLen': ('_TYPTR', ['ACK-ULONG'], 3) } )
    _context = globals ()
    _numcursori = 4

# ACK-ATTRIBUTE-ARRAY ::= SEQUENCE OF ACK-ATTRIBUTE
class ACK_ATTRIBUTE_ARRAY (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) ),4,
        ('_TYPTR', ['ACK-ATTRIBUTE'], 0) )
    _context = globals ()
    _numcursori = 1

# ACK-BBOOL ::= BOOLEAN
class ACK_BBOOL (_api.ASN1Boolean):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Boolean'], 0)
    _context = globals ()
    _numcursori = 1

# ACK-BYTE ::= OCTET STRING SIZE(1)
class ACK_BYTE (_api.ASN1OctetString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OctetString'], 0)
    _context = globals ()
    _numcursori = 1

# ACK-BYTE-ARRAY ::= OCTET STRING
class ACK_BYTE_ARRAY (_api.ASN1OctetString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1OctetString'], 0)
    _context = globals ()
    _numcursori = 1

# ACK-FLAGS ::= BIT STRING
class ACK_FLAGS (_api.ASN1BitString):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1BitString'], 0)
    _context = globals ()
    _numcursori = 1

# ACK-C-INITIALIZE-ARGS ::= SEQUENCE { createMutex CHOICE { null NULL, present BOOLEAN (TRUE) }, destroyMutex CHOICE { null NULL, present BOOLEAN (TRUE) }, lockMutex CHOICE { null NULL, present BOOLEAN (TRUE) }, unlockMutex CHOICE { null NULL, present BOOLEAN (TRUE) }, flags ACK-FLAGS, pReserved NULL, ... }
class ACK_C_INITIALIZE_ARGS (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'createMutex': ('_NAMED', {
            'null': ('_TYPTR', ['_api.ASN1Null'], 0),
            'present': ('_TYPTR', ['_api.ASN1Boolean'], 1) } ),
        'destroyMutex': ('_NAMED', {
            'null': ('_TYPTR', ['_api.ASN1Null'], 2),
            'present': ('_TYPTR', ['_api.ASN1Boolean'], 3) } ),
        'lockMutex': ('_NAMED', {
            'null': ('_TYPTR', ['_api.ASN1Null'], 4),
            'present': ('_TYPTR', ['_api.ASN1Boolean'], 5) } ),
        'unlockMutex': ('_NAMED', {
            'null': ('_TYPTR', ['_api.ASN1Null'], 6),
            'present': ('_TYPTR', ['_api.ASN1Boolean'], 7) } ),
        'flags': ('_TYPTR', ['ACK-FLAGS'], 8),
        'pReserved': ('_TYPTR', ['_api.ASN1Null'], 9) } )
    _context = globals ()
    _numcursori = 10

# ACK-CERTIFICATE-CATEGORY ::= ACK-ULONG
class ACK_CERTIFICATE_CATEGORY (ACK_ULONG):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['ACK-ULONG'], 0)
    _context = globals ()
    _numcursori = 1

# ACK-CERTIFICATE-TYPE ::= ACK-ULONG
class ACK_CERTIFICATE_TYPE (ACK_ULONG):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['ACK-ULONG'], 0)
    _context = globals ()
    _numcursori = 1

# ACK-CHAR ::= IA5String SIZE(1)
class ACK_CHAR (_api.ASN1IA5String):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1IA5String'], 0)
    _context = globals ()
    _numcursori = 1

# ACK-CHAR-ARRAY ::= IA5String
class ACK_CHAR_ARRAY (_api.ASN1IA5String):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1IA5String'], 0)
    _context = globals ()
    _numcursori = 1

# ACK-DATE ::= SEQUENCE { year IA5String SIZE(4), month IA5String SIZE(2), day IA5String SIZE(2) }
class ACK_DATE (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'year': ('_TYPTR', ['_api.ASN1IA5String'], 0),
        'month': ('_TYPTR', ['_api.ASN1IA5String'], 1),
        'day': ('_TYPTR', ['_api.ASN1IA5String'], 2) } )
    _context = globals ()
    _numcursori = 3

# ACK-VERSION ::= SEQUENCE { major ACK-BYTE, minor ACK-BYTE }
class ACK_VERSION (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'major': ('_TYPTR', ['ACK-BYTE'], 0),
        'minor': ('_TYPTR', ['ACK-BYTE'], 1) } )
    _context = globals ()
    _numcursori = 2

# ACK-FUNCTION-LIST ::= SEQUENCE { version ACK-VERSION, functionlist BIT STRING }
class ACK_FUNCTION_LIST (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'version': ('_TYPTR', ['ACK-VERSION'], 0),
        'functionlist': ('_TYPTR', ['_api.ASN1BitString'], 2) } )
    _context = globals ()
    _numcursori = 3

# ACK-HW-FEATURE-TYPE ::= ACK-ULONG
class ACK_HW_FEATURE_TYPE (ACK_ULONG):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['ACK-ULONG'], 0)
    _context = globals ()
    _numcursori = 1

# ACK-INFO ::= SEQUENCE { cryptokiVersion ACK-VERSION, manufacturerID UTF8String SIZE(32), flags ACK-FLAGS, libraryDescription UTF8String SIZE(32), libraryVersion ACK-VERSION }
class ACK_INFO (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'cryptokiVersion': ('_TYPTR', ['ACK-VERSION'], 0),
        'manufacturerID': ('_TYPTR', ['_api.ASN1UTF8String'], 2),
        'flags': ('_TYPTR', ['ACK-FLAGS'], 3),
        'libraryDescription': ('_TYPTR', ['_api.ASN1UTF8String'], 4),
        'libraryVersion': ('_TYPTR', ['ACK-VERSION'], 5) } )
    _context = globals ()
    _numcursori = 7

# ACK-JAVA-MIDP-SECURITY-DOMAIN ::= ACK-ULONG
class ACK_JAVA_MIDP_SECURITY_DOMAIN (ACK_ULONG):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['ACK-ULONG'], 0)
    _context = globals ()
    _numcursori = 1

# ACK-KEY-TYPE ::= ACK-ULONG
class ACK_KEY_TYPE (ACK_ULONG):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['ACK-ULONG'], 0)
    _context = globals ()
    _numcursori = 1

# ACK-LONG ::= INTEGER (-2147483648..2147483647)
class ACK_LONG (_api.ASN1Integer):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Integer'], 0)
    _context = globals ()
    _numcursori = 1

# ACK-MECHANISM-TYPE ::= ACK-ULONG
class ACK_MECHANISM_TYPE (ACK_ULONG):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['ACK-ULONG'], 0)
    _context = globals ()
    _numcursori = 1

# ACK-MECHANISM ::= SEQUENCE { mechanism ACK-MECHANISM-TYPE, pParameter CHOICE { null NULL, data ACK-OPAQUE }, ulParameterLen ACK-ULONG }
class ACK_MECHANISM (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'mechanism': ('_TYPTR', ['ACK-MECHANISM-TYPE'], 0),
        'pParameter': ('_NAMED', {
            'null': ('_TYPTR', ['_api.ASN1Null'], 1),
            'data': ('_TYPTR', ['ACK-OPAQUE'], 2) } ),
        'ulParameterLen': ('_TYPTR', ['ACK-ULONG'], 3) } )
    _context = globals ()
    _numcursori = 4

# ACK-MECHANISM-INFO ::= SEQUENCE { ulMinKeySize ACK-ULONG, ulMaxKeySize ACK-ULONG, flags ACK-FLAGS }
class ACK_MECHANISM_INFO (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'ulMinKeySize': ('_TYPTR', ['ACK-ULONG'], 0),
        'ulMaxKeySize': ('_TYPTR', ['ACK-ULONG'], 1),
        'flags': ('_TYPTR', ['ACK-FLAGS'], 2) } )
    _context = globals ()
    _numcursori = 3

# ACK-MECHANISM-TYPE-ARRAY ::= SEQUENCE OF ACK-ULONG
class ACK_MECHANISM_TYPE_ARRAY (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) ),1,
        ('_TYPTR', ['ACK-ULONG'], 0) )
    _context = globals ()
    _numcursori = 1

# ACK-NOTIFICATION ::= ACK-ULONG
class ACK_NOTIFICATION (ACK_ULONG):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['ACK-ULONG'], 0)
    _context = globals ()
    _numcursori = 1

# ACK-OBJECT-CLASS ::= ACK-ULONG
class ACK_OBJECT_CLASS (ACK_ULONG):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['ACK-ULONG'], 0)
    _context = globals ()
    _numcursori = 1

# ACK-OBJECT-HANDLE ::= ACK-ULONG
class ACK_OBJECT_HANDLE (ACK_ULONG):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['ACK-ULONG'], 0)
    _context = globals ()
    _numcursori = 1

# ACK-OBJECT-HANDLE-ARRAY ::= SEQUENCE OF ACK-OBJECT-HANDLE
class ACK_OBJECT_HANDLE_ARRAY (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) ),1,
        ('_TYPTR', ['ACK-OBJECT-HANDLE'], 0) )
    _context = globals ()
    _numcursori = 1

# ACK-OPAQUE-ARRAY ::= SEQUENCE OF ACK-OPAQUE
class ACK_OPAQUE_ARRAY (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_END) ),1,
        ('_TYPTR', ['ACK-OPAQUE'], 0) )
    _context = globals ()
    _numcursori = 1

# ACK-RV ::= ACK-ULONG
class ACK_RV (ACK_ULONG):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['ACK-ULONG'], 0)
    _context = globals ()
    _numcursori = 1

# ACK-SESSION-HANDLE ::= ACK-ULONG
class ACK_SESSION_HANDLE (ACK_ULONG):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['ACK-ULONG'], 0)
    _context = globals ()
    _numcursori = 1

# ACK-SLOT-ID ::= ACK-ULONG
class ACK_SLOT_ID (ACK_ULONG):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['ACK-ULONG'], 0)
    _context = globals ()
    _numcursori = 1

# ACK-STATE ::= ACK-ULONG
class ACK_STATE (ACK_ULONG):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['ACK-ULONG'], 0)
    _context = globals ()
    _numcursori = 1

# ACK-SESSION-INFO ::= SEQUENCE { slotID ACK-SLOT-ID, state ACK-STATE, flags ACK-FLAGS, ulDeviceError ACK-ULONG }
class ACK_SESSION_INFO (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'slotID': ('_TYPTR', ['ACK-SLOT-ID'], 0),
        'state': ('_TYPTR', ['ACK-STATE'], 1),
        'flags': ('_TYPTR', ['ACK-FLAGS'], 2),
        'ulDeviceError': ('_TYPTR', ['ACK-ULONG'], 3) } )
    _context = globals ()
    _numcursori = 4

# ACK-SLOT-ID-ARRAY ::= SEQUENCE OF ACK-SLOT-ID
class ACK_SLOT_ID_ARRAY (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) ),1,
        ('_TYPTR', ['ACK-SLOT-ID'], 0) )
    _context = globals ()
    _numcursori = 1

# ACK-SLOT-INFO ::= SEQUENCE { slotDescription UTF8String SIZE(64), manufacturerID UTF8String SIZE(32), flags ACK-FLAGS, hardwareVersion ACK-VERSION, firmwareVersion ACK-VERSION }
class ACK_SLOT_INFO (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'slotDescription': ('_TYPTR', ['_api.ASN1UTF8String'], 0),
        'manufacturerID': ('_TYPTR', ['_api.ASN1UTF8String'], 1),
        'flags': ('_TYPTR', ['ACK-FLAGS'], 2),
        'hardwareVersion': ('_TYPTR', ['ACK-VERSION'], 3),
        'firmwareVersion': ('_TYPTR', ['ACK-VERSION'], 5) } )
    _context = globals ()
    _numcursori = 7

# ACK-TOKEN-INFO ::= SEQUENCE { label UTF8String SIZE(32), manufacturerID UTF8String SIZE(32), model UTF8String SIZE(16), serialNumber UTF8String SIZE(16), flags ACK-FLAGS, ulMaxSessionCount ACK-ULONG, ulSessionCount ACK-ULONG, ulMaxRwSessionCount ACK-ULONG, ulRwSessionCount ACK-ULONG, ulMaxPinLen ACK-ULONG, ulMinPinLen ACK-ULONG, ulTotalPublicMemory ACK-ULONG, ulFreePublicMemory ACK-ULONG, ulTotalPrivateMemory ACK-ULONG, ulFreePritvateMemory ACK-ULONG, hardwareVersion ACK-VERSION, firmwareVersion ACK-VERSION, utcTime IA5String SIZE(16) }
class ACK_TOKEN_INFO (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'label': ('_TYPTR', ['_api.ASN1UTF8String'], 0),
        'manufacturerID': ('_TYPTR', ['_api.ASN1UTF8String'], 1),
        'model': ('_TYPTR', ['_api.ASN1UTF8String'], 2),
        'serialNumber': ('_TYPTR', ['_api.ASN1UTF8String'], 3),
        'flags': ('_TYPTR', ['ACK-FLAGS'], 4),
        'ulMaxSessionCount': ('_TYPTR', ['ACK-ULONG'], 5),
        'ulSessionCount': ('_TYPTR', ['ACK-ULONG'], 6),
        'ulMaxRwSessionCount': ('_TYPTR', ['ACK-ULONG'], 7),
        'ulRwSessionCount': ('_TYPTR', ['ACK-ULONG'], 8),
        'ulMaxPinLen': ('_TYPTR', ['ACK-ULONG'], 9),
        'ulMinPinLen': ('_TYPTR', ['ACK-ULONG'], 10),
        'ulTotalPublicMemory': ('_TYPTR', ['ACK-ULONG'], 11),
        'ulFreePublicMemory': ('_TYPTR', ['ACK-ULONG'], 12),
        'ulTotalPrivateMemory': ('_TYPTR', ['ACK-ULONG'], 13),
        'ulFreePritvateMemory': ('_TYPTR', ['ACK-ULONG'], 14),
        'hardwareVersion': ('_TYPTR', ['ACK-VERSION'], 15),
        'firmwareVersion': ('_TYPTR', ['ACK-VERSION'], 17),
        'utcTime': ('_TYPTR', ['_api.ASN1IA5String'], 19) } )
    _context = globals ()
    _numcursori = 20

# ACK-ULONG-ARRAY ::= SEQUENCE OF ACK-ULONG
class ACK_ULONG_ARRAY (_api.ASN1SequenceOf):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_SEQOF', 0, (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) ),1,
        ('_TYPTR', ['ACK-ULONG'], 0) )
    _context = globals ()
    _numcursori = 1

# ACK-USER-TYPE ::= ACK-ULONG
class ACK_USER_TYPE (ACK_ULONG):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['ACK-ULONG'], 0)
    _context = globals ()
    _numcursori = 1

# ACK-UTF8CHAR ::= UTF8String SIZE(1)
class ACK_UTF8CHAR (_api.ASN1UTF8String):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1UTF8String'], 0)
    _context = globals ()
    _numcursori = 1

# ACK-UTF8CHAR-ARRAY ::= UTF8String
class ACK_UTF8CHAR_ARRAY (_api.ASN1UTF8String):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1UTF8String'], 0)
    _context = globals ()
    _numcursori = 1

# C-CancelFunction-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE }
class C_CancelFunction_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-CancelFunction-Return ::= SEQUENCE { retval ACK-RV }
class C_CancelFunction_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-CloseAllSessions-Call ::= SEQUENCE { slotID [0] ACK-SLOT-ID }
class C_CloseAllSessions_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'slotID': ('_TYPTR', ['ACK-SLOT-ID'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-CloseAllSessions-Return ::= SEQUENCE { retval ACK-RV }
class C_CloseAllSessions_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-CloseSession-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE }
class C_CloseSession_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-CloseSession-Return ::= SEQUENCE { retval ACK-RV }
class C_CloseSession_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-CopyObject-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, hObject [1] ACK-OBJECT-HANDLE, pTemplate [2] ACK-ATTRIBUTE-ARRAY, ulCount [3] ACK-ULONG }
class C_CopyObject_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'hObject': ('_TYPTR', ['ACK-OBJECT-HANDLE'], 1),
        'pTemplate': ('_TYPTR', ['ACK-ATTRIBUTE-ARRAY'], 2),
        'ulCount': ('_TYPTR', ['ACK-ULONG'], 3) } )
    _context = globals ()
    _numcursori = 4

# C-CopyObject-Return ::= SEQUENCE { retval ACK-RV, phObject [4] ACK-OBJECT-HANDLE }
class C_CopyObject_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'phObject': ('_TYPTR', ['ACK-OBJECT-HANDLE'], 1) } )
    _context = globals ()
    _numcursori = 2

# C-CreateMutex-Call ::= SEQUENCE { empty NULL OPTIONAL }
class C_CreateMutex_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'empty': ('_TYPTR', ['_api.ASN1Null'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-CreateMutex-Return ::= SEQUENCE { retval ACK-RV, ppMutex [0] ACK-OPAQUE }
class C_CreateMutex_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'ppMutex': ('_TYPTR', ['ACK-OPAQUE'], 1) } )
    _context = globals ()
    _numcursori = 2

# C-CreateObject-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pTemplate [1] ACK-ATTRIBUTE-ARRAY, ulCount [2] ACK-ULONG }
class C_CreateObject_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pTemplate': ('_TYPTR', ['ACK-ATTRIBUTE-ARRAY'], 1),
        'ulCount': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-CreateObject-Return ::= SEQUENCE { retval ACK-RV, phObject [3] ACK-OBJECT-HANDLE }
class C_CreateObject_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'phObject': ('_TYPTR', ['ACK-OBJECT-HANDLE'], 1) } )
    _context = globals ()
    _numcursori = 2

# C-Decrypt-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pEncryptedData [1] ACK-BYTE-ARRAY, ulEncryptedDataLen [2] ACK-ULONG, pulDataLen [4] ACK-ULONG }
class C_Decrypt_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pEncryptedData': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'ulEncryptedDataLen': ('_TYPTR', ['ACK-ULONG'], 2),
        'pulDataLen': ('_TYPTR', ['ACK-ULONG'], 3) } )
    _context = globals ()
    _numcursori = 4

# C-Decrypt-Return ::= SEQUENCE { retval ACK-RV, pData [3] ACK-BYTE-ARRAY, pulDataLen [4] ACK-ULONG }
class C_Decrypt_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pData': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'pulDataLen': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-DecryptDigestUpdate-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pEncryptedPart [1] ACK-BYTE-ARRAY, ulEncryptedPartLen [2] ACK-ULONG, pulPartLen [4] ACK-ULONG }
class C_DecryptDigestUpdate_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pEncryptedPart': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'ulEncryptedPartLen': ('_TYPTR', ['ACK-ULONG'], 2),
        'pulPartLen': ('_TYPTR', ['ACK-ULONG'], 3) } )
    _context = globals ()
    _numcursori = 4

# C-DecryptDigestUpdate-Return ::= SEQUENCE { retval ACK-RV, pPart [3] ACK-BYTE-ARRAY, pulPartLen [4] ACK-ULONG }
class C_DecryptDigestUpdate_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pPart': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'pulPartLen': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-DecryptFinal-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pulLastPartLen [2] ACK-ULONG }
class C_DecryptFinal_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pulLastPartLen': ('_TYPTR', ['ACK-ULONG'], 1) } )
    _context = globals ()
    _numcursori = 2

# C-DecryptFinal-Return ::= SEQUENCE { retval ACK-RV, pLastPart [3] ACK-BYTE-ARRAY, pulLastPartLen [4] ACK-ULONG }
class C_DecryptFinal_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pLastPart': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'pulLastPartLen': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-DecryptInit-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pMechanism [1] ACK-MECHANISM, hKey [2] ACK-OBJECT-HANDLE }
class C_DecryptInit_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pMechanism': ('_TYPTR', ['ACK-MECHANISM'], 1),
        'hKey': ('_TYPTR', ['ACK-OBJECT-HANDLE'], 5) } )
    _context = globals ()
    _numcursori = 6

# C-DecryptInit-Return ::= SEQUENCE { retval ACK-RV }
class C_DecryptInit_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-DecryptUpdate-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pEncryptedPart [1] ACK-BYTE-ARRAY, ulEncryptedPartLen [2] ACK-ULONG, pulPartLen [4] ACK-ULONG }
class C_DecryptUpdate_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pEncryptedPart': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'ulEncryptedPartLen': ('_TYPTR', ['ACK-ULONG'], 2),
        'pulPartLen': ('_TYPTR', ['ACK-ULONG'], 3) } )
    _context = globals ()
    _numcursori = 4

# C-DecryptUpdate-Return ::= SEQUENCE { retval ACK-RV, pPart [3] ACK-BYTE-ARRAY, pulPartLen [4] ACK-ULONG }
class C_DecryptUpdate_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pPart': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'pulPartLen': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-DecryptVerifyUpdate-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pEncryptedPart [1] ACK-BYTE-ARRAY, ulEncryptedPartLen [2] ACK-ULONG, pulPartLen [4] ACK-ULONG }
class C_DecryptVerifyUpdate_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pEncryptedPart': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'ulEncryptedPartLen': ('_TYPTR', ['ACK-ULONG'], 2),
        'pulPartLen': ('_TYPTR', ['ACK-ULONG'], 3) } )
    _context = globals ()
    _numcursori = 4

# C-DecryptVerifyUpdate-Return ::= SEQUENCE { retval ACK-RV, pPart [3] ACK-BYTE-ARRAY, pulPartLen [4] ACK-ULONG }
class C_DecryptVerifyUpdate_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pPart': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'pulPartLen': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-DeriveKey-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pMechanism [1] ACK-MECHANISM, hBaseKey [2] ACK-OBJECT-HANDLE, pTemplate [3] ACK-ATTRIBUTE-ARRAY, ulAttributeCount [4] ACK-ULONG }
class C_DeriveKey_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pMechanism': ('_TYPTR', ['ACK-MECHANISM'], 1),
        'hBaseKey': ('_TYPTR', ['ACK-OBJECT-HANDLE'], 5),
        'pTemplate': ('_TYPTR', ['ACK-ATTRIBUTE-ARRAY'], 6),
        'ulAttributeCount': ('_TYPTR', ['ACK-ULONG'], 7) } )
    _context = globals ()
    _numcursori = 8

# C-DeriveKey-Return ::= SEQUENCE { retval ACK-RV, phKey [5] ACK-OBJECT-HANDLE }
class C_DeriveKey_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(5)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'phKey': ('_TYPTR', ['ACK-OBJECT-HANDLE'], 1) } )
    _context = globals ()
    _numcursori = 2

# C-DestroyMutex-Call ::= SEQUENCE { pMutex [0] ACK-OPAQUE }
class C_DestroyMutex_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'pMutex': ('_TYPTR', ['ACK-OPAQUE'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-DestroyMutex-Return ::= SEQUENCE { retval ACK-RV }
class C_DestroyMutex_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-DestroyObject-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, hObject [1] ACK-OBJECT-HANDLE }
class C_DestroyObject_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'hObject': ('_TYPTR', ['ACK-OBJECT-HANDLE'], 1) } )
    _context = globals ()
    _numcursori = 2

# C-DestroyObject-Return ::= SEQUENCE { retval ACK-RV }
class C_DestroyObject_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-Digest-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pData [1] ACK-BYTE-ARRAY, ulDataLen [2] ACK-ULONG, pulDigestLen [4] ACK-ULONG }
class C_Digest_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pData': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'ulDataLen': ('_TYPTR', ['ACK-ULONG'], 2),
        'pulDigestLen': ('_TYPTR', ['ACK-ULONG'], 3) } )
    _context = globals ()
    _numcursori = 4

# C-Digest-Return ::= SEQUENCE { retval ACK-RV, pDigest [3] ACK-BYTE-ARRAY, pulDigestLen [4] ACK-ULONG }
class C_Digest_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pDigest': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'pulDigestLen': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-DigestEncryptUpdate-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pPart [1] ACK-BYTE-ARRAY, ulPartLen [2] ACK-ULONG, pulEncryptedPartLen [4] ACK-ULONG }
class C_DigestEncryptUpdate_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pPart': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'ulPartLen': ('_TYPTR', ['ACK-ULONG'], 2),
        'pulEncryptedPartLen': ('_TYPTR', ['ACK-ULONG'], 3) } )
    _context = globals ()
    _numcursori = 4

# C-DigestEncryptUpdate-Return ::= SEQUENCE { retval ACK-RV, pEncryptedPart [3] ACK-BYTE-ARRAY, pulEncryptedPartLen [4] ACK-ULONG }
class C_DigestEncryptUpdate_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pEncryptedPart': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'pulEncryptedPartLen': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-DigestFinal-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pulDigestLen [2] ACK-ULONG }
class C_DigestFinal_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pulDigestLen': ('_TYPTR', ['ACK-ULONG'], 1) } )
    _context = globals ()
    _numcursori = 2

# C-DigestFinal-Return ::= SEQUENCE { retval ACK-RV, pDigest [1] ACK-BYTE-ARRAY, pulDigestLen [2] ACK-ULONG }
class C_DigestFinal_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pDigest': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'pulDigestLen': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-DigestInit-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pMechanism [1] ACK-MECHANISM }
class C_DigestInit_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pMechanism': ('_TYPTR', ['ACK-MECHANISM'], 1) } )
    _context = globals ()
    _numcursori = 5

# C-DigestInit-Return ::= SEQUENCE { retval ACK-RV }
class C_DigestInit_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-DigestKey-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, hKey [1] ACK-OBJECT-HANDLE }
class C_DigestKey_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'hKey': ('_TYPTR', ['ACK-OBJECT-HANDLE'], 1) } )
    _context = globals ()
    _numcursori = 2

# C-DigestKey-Return ::= SEQUENCE { retval ACK-RV }
class C_DigestKey_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-DigestUpdate-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pPart [1] ACK-BYTE-ARRAY, ulPartLen [2] ACK-ULONG }
class C_DigestUpdate_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pPart': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'ulPartLen': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-DigestUpdate-Return ::= SEQUENCE { retval ACK-RV }
class C_DigestUpdate_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-Encrypt-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pData [1] ACK-BYTE-ARRAY, ulDataLen [2] ACK-ULONG, pulEncryptedDataLen [4] ACK-ULONG }
class C_Encrypt_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pData': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'ulDataLen': ('_TYPTR', ['ACK-ULONG'], 2),
        'pulEncryptedDataLen': ('_TYPTR', ['ACK-ULONG'], 3) } )
    _context = globals ()
    _numcursori = 4

# C-Encrypt-Return ::= SEQUENCE { retval ACK-RV, pEncryptedData [3] ACK-BYTE-ARRAY, pulEncryptedDataLen [4] ACK-ULONG }
class C_Encrypt_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pEncryptedData': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'pulEncryptedDataLen': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-EncryptFinal-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pulEncryptedDataLen [2] ACK-ULONG }
class C_EncryptFinal_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pulEncryptedDataLen': ('_TYPTR', ['ACK-ULONG'], 1) } )
    _context = globals ()
    _numcursori = 2

# C-EncryptFinal-Return ::= SEQUENCE { retval ACK-RV, pEncryptedData [3] ACK-BYTE-ARRAY, pulEncryptedDataLen [4] ACK-ULONG }
class C_EncryptFinal_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pEncryptedData': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'pulEncryptedDataLen': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-EncryptInit-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pMechanism [1] ACK-MECHANISM, hKey [2] ACK-OBJECT-HANDLE }
class C_EncryptInit_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pMechanism': ('_TYPTR', ['ACK-MECHANISM'], 1),
        'hKey': ('_TYPTR', ['ACK-OBJECT-HANDLE'], 5) } )
    _context = globals ()
    _numcursori = 6

# C-EncryptInit-Return ::= SEQUENCE { retval ACK-RV }
class C_EncryptInit_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-EncryptUpdate-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pPart [1] ACK-BYTE-ARRAY, ulPartLen [2] ACK-ULONG, pulEncryptedPartLen [4] ACK-ULONG }
class C_EncryptUpdate_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pPart': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'ulPartLen': ('_TYPTR', ['ACK-ULONG'], 2),
        'pulEncryptedPartLen': ('_TYPTR', ['ACK-ULONG'], 3) } )
    _context = globals ()
    _numcursori = 4

# C-EncryptUpdate-Return ::= SEQUENCE { retval ACK-RV, pEncryptedPart [3] ACK-BYTE-ARRAY, pulEncryptedPartLen [4] ACK-ULONG }
class C_EncryptUpdate_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pEncryptedPart': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'pulEncryptedPartLen': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-Finalize-Call ::= SEQUENCE { pReserved [0] CHOICE { null NULL, ... } }
class C_Finalize_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'pReserved': ('_NAMED', {
            'null': ('_TYPTR', ['_api.ASN1Null'], 0) } ) } )
    _context = globals ()
    _numcursori = 1

# C-Finalize-Return ::= SEQUENCE { retval ACK-RV, pReserverd [0] ANY OPTIONAL }
class C_Finalize_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pReserverd': ('_TYPTR', ['_api.ASN1Any'], 1) } )
    _context = globals ()
    _numcursori = 2

# C-FindObjects-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, ulMaxObjectCount [2] ACK-ULONG }
class C_FindObjects_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'ulMaxObjectCount': ('_TYPTR', ['ACK-ULONG'], 1) } )
    _context = globals ()
    _numcursori = 2

# C-FindObjects-Return ::= SEQUENCE { retval ACK-RV, phObject [1] ACK-OBJECT-HANDLE-ARRAY, pulObjectCount [3] ACK-ULONG }
class C_FindObjects_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'phObject': ('_TYPTR', ['ACK-OBJECT-HANDLE-ARRAY'], 1),
        'pulObjectCount': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-FindObjectsFinal-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE }
class C_FindObjectsFinal_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-FindObjectsFinal-Return ::= SEQUENCE { retval ACK-RV }
class C_FindObjectsFinal_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-FindObjectsInit-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pTemplate [1] ACK-ATTRIBUTE-ARRAY, ulCount [2] ACK-ULONG }
class C_FindObjectsInit_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pTemplate': ('_TYPTR', ['ACK-ATTRIBUTE-ARRAY'], 1),
        'ulCount': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-FindObjectsInit-Return ::= SEQUENCE { retval ACK-RV, pTemplate [1] ACK-ATTRIBUTE-ARRAY }
class C_FindObjectsInit_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pTemplate': ('_TYPTR', ['ACK-ATTRIBUTE-ARRAY'], 1) } )
    _context = globals ()
    _numcursori = 2

# C-GenerateKey-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pMechanism [1] ACK-MECHANISM, pTemplate [2] ACK-ATTRIBUTE-ARRAY, ulCount [3] ACK-ULONG }
class C_GenerateKey_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pMechanism': ('_TYPTR', ['ACK-MECHANISM'], 1),
        'pTemplate': ('_TYPTR', ['ACK-ATTRIBUTE-ARRAY'], 5),
        'ulCount': ('_TYPTR', ['ACK-ULONG'], 6) } )
    _context = globals ()
    _numcursori = 7

# C-GenerateKey-Return ::= SEQUENCE { retval ACK-RV, phKey [4] ACK-OBJECT-HANDLE }
class C_GenerateKey_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'phKey': ('_TYPTR', ['ACK-OBJECT-HANDLE'], 1) } )
    _context = globals ()
    _numcursori = 2

# C-GenerateKeyPair-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pMechanism [1] ACK-MECHANISM, pPublicKeyTemplate [2] ACK-ATTRIBUTE-ARRAY, ulPublicKeyAttributeCount [3] ACK-ULONG, pPrivateKeyTemplate [4] ACK-ATTRIBUTE-ARRAY, ulPrivateKeyAttributeCount [5] ACK-ULONG }
class C_GenerateKeyPair_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(5)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pMechanism': ('_TYPTR', ['ACK-MECHANISM'], 1),
        'pPublicKeyTemplate': ('_TYPTR', ['ACK-ATTRIBUTE-ARRAY'], 5),
        'ulPublicKeyAttributeCount': ('_TYPTR', ['ACK-ULONG'], 6),
        'pPrivateKeyTemplate': ('_TYPTR', ['ACK-ATTRIBUTE-ARRAY'], 7),
        'ulPrivateKeyAttributeCount': ('_TYPTR', ['ACK-ULONG'], 8) } )
    _context = globals ()
    _numcursori = 9

# C-GenerateKeyPair-Return ::= SEQUENCE { retval ACK-RV, phPublicKey [6] ACK-OBJECT-HANDLE, phPrivateKey [7] ACK-OBJECT-HANDLE }
class C_GenerateKeyPair_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(6)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(7)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'phPublicKey': ('_TYPTR', ['ACK-OBJECT-HANDLE'], 1),
        'phPrivateKey': ('_TYPTR', ['ACK-OBJECT-HANDLE'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-GenerateRandom-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, ulRandomLen [2] ACK-ULONG }
class C_GenerateRandom_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'ulRandomLen': ('_TYPTR', ['ACK-ULONG'], 1) } )
    _context = globals ()
    _numcursori = 2

# C-GenerateRandom-Return ::= SEQUENCE { retval ACK-RV, pSeed [1] ACK-BYTE-ARRAY }
class C_GenerateRandom_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pSeed': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1) } )
    _context = globals ()
    _numcursori = 2

# C-GetAttributeValue-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, hObject [1] ACK-OBJECT-HANDLE, pTemplate [2] ACK-ATTRIBUTE-ARRAY, ulCount [3] ACK-ULONG }
class C_GetAttributeValue_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'hObject': ('_TYPTR', ['ACK-OBJECT-HANDLE'], 1),
        'pTemplate': ('_TYPTR', ['ACK-ATTRIBUTE-ARRAY'], 2),
        'ulCount': ('_TYPTR', ['ACK-ULONG'], 3) } )
    _context = globals ()
    _numcursori = 4

# C-GetAttributeValue-Return ::= SEQUENCE { retval ACK-RV, pTemplate [2] ACK-ATTRIBUTE-ARRAY }
class C_GetAttributeValue_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pTemplate': ('_TYPTR', ['ACK-ATTRIBUTE-ARRAY'], 1) } )
    _context = globals ()
    _numcursori = 2

# C-GetFunctionList-Call ::= SEQUENCE { empty NULL OPTIONAL }
class C_GetFunctionList_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'empty': ('_TYPTR', ['_api.ASN1Null'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-GetFunctionList-Return ::= SEQUENCE { retval ACK-RV, ppFunctionList [0] ACK-FUNCTION-LIST }
class C_GetFunctionList_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'ppFunctionList': ('_TYPTR', ['ACK-FUNCTION-LIST'], 1) } )
    _context = globals ()
    _numcursori = 4

# C-GetFunctionStatus-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE }
class C_GetFunctionStatus_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-GetFunctionStatus-Return ::= SEQUENCE { retval ACK-RV }
class C_GetFunctionStatus_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-GetInfo-Call ::= SEQUENCE { empty NULL OPTIONAL }
class C_GetInfo_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'empty': ('_TYPTR', ['_api.ASN1Null'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-GetInfo-Return ::= SEQUENCE { retval ACK-RV, pInfo [0] ACK-INFO }
class C_GetInfo_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pInfo': ('_TYPTR', ['ACK-INFO'], 1) } )
    _context = globals ()
    _numcursori = 8

# C-GetMechanismList-Call ::= SEQUENCE { slotID [0] ACK-SLOT-ID, pMechanismList [1] CHOICE { null NULL } OPTIONAL, pulCount [2] ACK-ULONG }
class C_GetMechanismList_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'slotID': ('_TYPTR', ['ACK-SLOT-ID'], 0),
        'pMechanismList': ('_NAMED', {
            'null': ('_TYPTR', ['_api.ASN1Null'], 1) } ),
        'pulCount': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-GetMechanismList-Return ::= SEQUENCE { retval ACK-RV, pMechanismList [1] CHOICE { null NULL, data ACK-MECHANISM-TYPE-ARRAY }, pulCount [2] ACK-ULONG }
class C_GetMechanismList_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pMechanismList': ('_NAMED', {
            'null': ('_TYPTR', ['_api.ASN1Null'], 1),
            'data': ('_TYPTR', ['ACK-MECHANISM-TYPE-ARRAY'], 2) } ),
        'pulCount': ('_TYPTR', ['ACK-ULONG'], 3) } )
    _context = globals ()
    _numcursori = 4

# C-GetObjectSize-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, hObject [1] ACK-OBJECT-HANDLE }
class C_GetObjectSize_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'hObject': ('_TYPTR', ['ACK-OBJECT-HANDLE'], 1) } )
    _context = globals ()
    _numcursori = 2

# C-GetObjectSize-Return ::= SEQUENCE { retval ACK-RV, pulSize [2] ACK-ULONG }
class C_GetObjectSize_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pulSize': ('_TYPTR', ['ACK-ULONG'], 1) } )
    _context = globals ()
    _numcursori = 2

# C-GetOperationState-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pulOperationStateLen [2] ACK-ULONG }
class C_GetOperationState_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pulOperationStateLen': ('_TYPTR', ['ACK-ULONG'], 1) } )
    _context = globals ()
    _numcursori = 2

# C-GetOperationState-Return ::= SEQUENCE { retval ACK-RV, pOperationState [1] ACK-BYTE-ARRAY, pulOperationStateLen [2] ACK-ULONG }
class C_GetOperationState_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pOperationState': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'pulOperationStateLen': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-GetSessionInfo-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE }
class C_GetSessionInfo_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-GetSessionInfo-Return ::= SEQUENCE { retval ACK-RV, pInfo [1] ACK-SESSION-INFO }
class C_GetSessionInfo_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pInfo': ('_TYPTR', ['ACK-SESSION-INFO'], 1) } )
    _context = globals ()
    _numcursori = 5

# C-GetSlotInfo-Call ::= SEQUENCE { slotID [0] ACK-SLOT-ID }
class C_GetSlotInfo_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'slotID': ('_TYPTR', ['ACK-SLOT-ID'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-GetSlotInfo-Return ::= SEQUENCE { retval ACK-RV, pInfo [1] ACK-SLOT-INFO }
class C_GetSlotInfo_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pInfo': ('_TYPTR', ['ACK-SLOT-INFO'], 1) } )
    _context = globals ()
    _numcursori = 8

# C-GetSlotList-Call ::= SEQUENCE { tokenPresent [0] ACK-BBOOL, pSlotList [1] CHOICE { null NULL } OPTIONAL, pulCount [2] ACK-ULONG }
class C_GetSlotList_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'tokenPresent': ('_TYPTR', ['ACK-BBOOL'], 0),
        'pSlotList': ('_NAMED', {
            'null': ('_TYPTR', ['_api.ASN1Null'], 1) } ),
        'pulCount': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-GetSlotList-Return ::= SEQUENCE { retval ACK-RV, pSlotList [1] CHOICE { null NULL, data ACK-SLOT-ID-ARRAY } OPTIONAL, pulCount [2] ACK-ULONG }
class C_GetSlotList_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pSlotList': ('_NAMED', {
            'null': ('_TYPTR', ['_api.ASN1Null'], 1),
            'data': ('_TYPTR', ['ACK-SLOT-ID-ARRAY'], 2) } ),
        'pulCount': ('_TYPTR', ['ACK-ULONG'], 3) } )
    _context = globals ()
    _numcursori = 4

# C-GetTokenInfo-Call ::= SEQUENCE { slotID [0] ACK-SLOT-ID }
class C_GetTokenInfo_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'slotID': ('_TYPTR', ['ACK-SLOT-ID'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-GetTokenInfo-Return ::= SEQUENCE { retval ACK-RV, pInfo [1] ACK-TOKEN-INFO }
class C_GetTokenInfo_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_IA5STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pInfo': ('_TYPTR', ['ACK-TOKEN-INFO'], 1) } )
    _context = globals ()
    _numcursori = 21

# C-InitPIN-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pPin [1] ACK-UTF8CHAR-ARRAY, ulPinLen [2] ACK-ULONG }
class C_InitPIN_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pPin': ('_TYPTR', ['ACK-UTF8CHAR-ARRAY'], 1),
        'ulPinLen': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-InitPIN-Return ::= SEQUENCE { retval ACK-RV }
class C_InitPIN_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-InitToken-Call ::= SEQUENCE { slotID [0] ACK-SLOT-ID, pPin [1] UTF8String, ulPinLen [2] ACK-ULONG, pLabel [3] UTF8String SIZE(32) }
class C_InitToken_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'slotID': ('_TYPTR', ['ACK-SLOT-ID'], 0),
        'pPin': ('_TYPTR', ['_api.ASN1UTF8String'], 1),
        'ulPinLen': ('_TYPTR', ['ACK-ULONG'], 2),
        'pLabel': ('_TYPTR', ['_api.ASN1UTF8String'], 3) } )
    _context = globals ()
    _numcursori = 4

# C-InitToken-Return ::= SEQUENCE { retval ACK-RV }
class C_InitToken_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-Initialize-Call ::= SEQUENCE { pInitArgs [0] CHOICE { null NULL, data [0] ACK-C-INITIALIZE-ARGS, ... } }
class C_Initialize_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'pInitArgs': ('_NAMED', {
            'null': ('_TYPTR', ['_api.ASN1Null'], 0),
            'data': ('_TYPTR', ['ACK-C-INITIALIZE-ARGS'], 1) } ) } )
    _context = globals ()
    _numcursori = 11

# C-Initialize-Return ::= SEQUENCE { retval ACK-RV, pInitArgs [0] ANY OPTIONAL }
class C_Initialize_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pInitArgs': ('_TYPTR', ['_api.ASN1Any'], 1) } )
    _context = globals ()
    _numcursori = 2

# C-LockMutex-Call ::= SEQUENCE { pMutex [0] ACK-OPAQUE }
class C_LockMutex_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'pMutex': ('_TYPTR', ['ACK-OPAQUE'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-LockMutex-Return ::= SEQUENCE { retval ACK-RV }
class C_LockMutex_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-Login-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, userType [1] ACK-USER-TYPE, pPin [2] ACK-UTF8CHAR-ARRAY, ulPinLen [3] ACK-ULONG }
class C_Login_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'userType': ('_TYPTR', ['ACK-USER-TYPE'], 1),
        'pPin': ('_TYPTR', ['ACK-UTF8CHAR-ARRAY'], 2),
        'ulPinLen': ('_TYPTR', ['ACK-ULONG'], 3) } )
    _context = globals ()
    _numcursori = 4

# C-Login-Return ::= SEQUENCE { retval ACK-RV }
class C_Login_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-Logout-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE }
class C_Logout_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-Logout-Return ::= SEQUENCE { retval ACK-RV }
class C_Logout_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-MechanismInfo-Call ::= SEQUENCE { slotID [0] ACK-SLOT-ID, type [1] ACK-MECHANISM-TYPE }
class C_MechanismInfo_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'slotID': ('_TYPTR', ['ACK-SLOT-ID'], 0),
        'type': ('_TYPTR', ['ACK-MECHANISM-TYPE'], 1) } )
    _context = globals ()
    _numcursori = 2

# C-MechanismInfo-Return ::= SEQUENCE { retval ACK-RV, pInfo [2] ACK-MECHANISM-INFO }
class C_MechanismInfo_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pInfo': ('_TYPTR', ['ACK-MECHANISM-INFO'], 1) } )
    _context = globals ()
    _numcursori = 4

# C-Notify-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, event [1] ACK-NOTIFICATION, pApplication [2] ANY }
class C_Notify_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'event': ('_TYPTR', ['ACK-NOTIFICATION'], 1),
        'pApplication': ('_TYPTR', ['_api.ASN1Any'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-Notify-Return ::= SEQUENCE { retval ACK-RV }
class C_Notify_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-OpenSession-Call ::= SEQUENCE { slotID [0] ACK-SLOT-ID, flags [1] ACK-FLAGS, pApplication [2] CHOICE { null NULL, opaque ANY }, notify [3] CHOICE { null NULL, present BOOLEAN (TRUE) } }
class C_OpenSession_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BOOLEAN) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'slotID': ('_TYPTR', ['ACK-SLOT-ID'], 0),
        'flags': ('_TYPTR', ['ACK-FLAGS'], 1),
        'pApplication': ('_NAMED', {
            'null': ('_TYPTR', ['_api.ASN1Null'], 2),
            'opaque': ('_TYPTR', ['_api.ASN1Any'], 3) } ),
        'notify': ('_NAMED', {
            'null': ('_TYPTR', ['_api.ASN1Null'], 4),
            'present': ('_TYPTR', ['_api.ASN1Boolean'], 5) } ) } )
    _context = globals ()
    _numcursori = 6

# C-OpenSession-Return ::= SEQUENCE { retval ACK-RV, phSession [4] ACK-SESSION-HANDLE }
class C_OpenSession_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'phSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 1) } )
    _context = globals ()
    _numcursori = 2

# C-SeedRandom-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pSeed [1] ACK-BYTE-ARRAY, ulSeedLen [2] ACK-ULONG }
class C_SeedRandom_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pSeed': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'ulSeedLen': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-SeedRandom-Return ::= SEQUENCE { retval ACK-RV }
class C_SeedRandom_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-SetAttributeValue-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, hObject [1] ACK-OBJECT-HANDLE, pTemplate [2] ACK-ATTRIBUTE-ARRAY, ulCount [3] ACK-ULONG }
class C_SetAttributeValue_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'hObject': ('_TYPTR', ['ACK-OBJECT-HANDLE'], 1),
        'pTemplate': ('_TYPTR', ['ACK-ATTRIBUTE-ARRAY'], 2),
        'ulCount': ('_TYPTR', ['ACK-ULONG'], 3) } )
    _context = globals ()
    _numcursori = 4

# C-SetAttributeValue-Return ::= SEQUENCE { retval ACK-RV }
class C_SetAttributeValue_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-SetOperationState-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pOperationState [1] ACK-BYTE-ARRAY, ulOperationStateLen [2] ACK-ULONG, hEncryptionKey [3] ACK-OBJECT-HANDLE, hAuthenticationKey [4] ACK-OBJECT-HANDLE }
class C_SetOperationState_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pOperationState': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'ulOperationStateLen': ('_TYPTR', ['ACK-ULONG'], 2),
        'hEncryptionKey': ('_TYPTR', ['ACK-OBJECT-HANDLE'], 3),
        'hAuthenticationKey': ('_TYPTR', ['ACK-OBJECT-HANDLE'], 4) } )
    _context = globals ()
    _numcursori = 5

# C-SetOperationState-Return ::= SEQUENCE { retval ACK-RV }
class C_SetOperationState_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-SetPIN-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pOldPin [1] ACK-UTF8CHAR-ARRAY, ulOldLen [2] ACK-ULONG, pNewPin [3] ACK-UTF8CHAR-ARRAY, ulNewPin [4] ACK-ULONG }
class C_SetPIN_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_UTF8STRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pOldPin': ('_TYPTR', ['ACK-UTF8CHAR-ARRAY'], 1),
        'ulOldLen': ('_TYPTR', ['ACK-ULONG'], 2),
        'pNewPin': ('_TYPTR', ['ACK-UTF8CHAR-ARRAY'], 3),
        'ulNewPin': ('_TYPTR', ['ACK-ULONG'], 4) } )
    _context = globals ()
    _numcursori = 5

# C-SetPIN-Return ::= SEQUENCE { retval ACK-RV }
class C_SetPIN_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-Sign-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pData [1] ACK-BYTE-ARRAY, ulDataLen [2] ACK-ULONG, pulSignatureLen [4] ACK-ULONG }
class C_Sign_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pData': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'ulDataLen': ('_TYPTR', ['ACK-ULONG'], 2),
        'pulSignatureLen': ('_TYPTR', ['ACK-ULONG'], 3) } )
    _context = globals ()
    _numcursori = 4

# C-Sign-Return ::= SEQUENCE { retval ACK-RV, pSignature [3] ACK-BYTE-ARRAY, pulSignatureLen [4] ACK-ULONG }
class C_Sign_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pSignature': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'pulSignatureLen': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-SignEncryptUpdate-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pPart [1] ACK-BYTE-ARRAY, ulPartLen [2] ACK-ULONG, pulEncryptedPartLen [4] ACK-ULONG }
class C_SignEncryptUpdate_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pPart': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'ulPartLen': ('_TYPTR', ['ACK-ULONG'], 2),
        'pulEncryptedPartLen': ('_TYPTR', ['ACK-ULONG'], 3) } )
    _context = globals ()
    _numcursori = 4

# C-SignEncryptUpdate-Return ::= SEQUENCE { retval ACK-RV, pEncryptedPart [3] ACK-BYTE-ARRAY, pulEncryptedPartLen [4] ACK-ULONG }
class C_SignEncryptUpdate_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pEncryptedPart': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'pulEncryptedPartLen': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-SignFinal-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pulSignatureLen [2] ACK-ULONG }
class C_SignFinal_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pulSignatureLen': ('_TYPTR', ['ACK-ULONG'], 1) } )
    _context = globals ()
    _numcursori = 2

# C-SignFinal-Return ::= SEQUENCE { retval ACK-RV, pSignature [1] ACK-BYTE-ARRAY, pulSignatureLen [2] ACK-ULONG }
class C_SignFinal_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pSignature': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'pulSignatureLen': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-SignInit-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pMechanism [1] ACK-MECHANISM, hKey [2] ACK-OBJECT-HANDLE }
class C_SignInit_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pMechanism': ('_TYPTR', ['ACK-MECHANISM'], 1),
        'hKey': ('_TYPTR', ['ACK-OBJECT-HANDLE'], 5) } )
    _context = globals ()
    _numcursori = 6

# C-SignInit-Return ::= SEQUENCE { retval ACK-RV }
class C_SignInit_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-SignRecover-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pData [1] ACK-BYTE-ARRAY, ulDataLen [2] ACK-ULONG, pulSignatureLen [4] ACK-ULONG }
class C_SignRecover_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pData': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'ulDataLen': ('_TYPTR', ['ACK-ULONG'], 2),
        'pulSignatureLen': ('_TYPTR', ['ACK-ULONG'], 3) } )
    _context = globals ()
    _numcursori = 4

# C-SignRecover-Return ::= SEQUENCE { retval ACK-RV, pSignature [3] ACK-BYTE-ARRAY, pulSignatureLen [4] ACK-ULONG }
class C_SignRecover_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pSignature': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'pulSignatureLen': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-SignRecoverInit-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE }
class C_SignRecoverInit_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-SignRecoverInit-Return ::= SEQUENCE { retval ACK-RV }
class C_SignRecoverInit_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-SignUpdate-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pPart [1] ACK-BYTE-ARRAY, ulPartLen [2] ACK-ULONG }
class C_SignUpdate_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pPart': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'ulPartLen': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-SignUpdate-Return ::= SEQUENCE { retval ACK-RV }
class C_SignUpdate_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-UnlockMutex-Call ::= SEQUENCE { pMutex [0] ACK-OPAQUE }
class C_UnlockMutex_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'pMutex': ('_TYPTR', ['ACK-OPAQUE'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-UnlockMutex-Return ::= SEQUENCE { retval ACK-RV }
class C_UnlockMutex_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-UnwrapKey-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pMechanism [1] ACK-MECHANISM, hUnwrappingKey [2] ACK-OBJECT-HANDLE, hWrappedKey [3] ACK-OBJECT-HANDLE, ulWrappedKeyLen [4] ACK-ULONG, pTemplate [5] ACK-ATTRIBUTE-ARRAY, ulAttributeCount [6] ACK-ULONG }
class C_UnwrapKey_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(5)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(6)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pMechanism': ('_TYPTR', ['ACK-MECHANISM'], 1),
        'hUnwrappingKey': ('_TYPTR', ['ACK-OBJECT-HANDLE'], 5),
        'hWrappedKey': ('_TYPTR', ['ACK-OBJECT-HANDLE'], 6),
        'ulWrappedKeyLen': ('_TYPTR', ['ACK-ULONG'], 7),
        'pTemplate': ('_TYPTR', ['ACK-ATTRIBUTE-ARRAY'], 8),
        'ulAttributeCount': ('_TYPTR', ['ACK-ULONG'], 9) } )
    _context = globals ()
    _numcursori = 10

# C-UnwrapKey-Return ::= SEQUENCE { retval ACK-RV, phKey [7] ACK-OBJECT-HANDLE }
class C_UnwrapKey_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(7)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'phKey': ('_TYPTR', ['ACK-OBJECT-HANDLE'], 1) } )
    _context = globals ()
    _numcursori = 2

# C-Verify-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pData [1] ACK-BYTE-ARRAY, ulDataLen [2] ACK-ULONG, pSignature [3] ACK-BYTE-ARRAY, ulSignatureLen [4] ACK-ULONG }
class C_Verify_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pData': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'ulDataLen': ('_TYPTR', ['ACK-ULONG'], 2),
        'pSignature': ('_TYPTR', ['ACK-BYTE-ARRAY'], 3),
        'ulSignatureLen': ('_TYPTR', ['ACK-ULONG'], 4) } )
    _context = globals ()
    _numcursori = 5

# C-Verify-Return ::= SEQUENCE { retval ACK-RV }
class C_Verify_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-VerifyFinal-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pSignature [1] ACK-BYTE-ARRAY, ulSignatureLen [2] ACK-ULONG }
class C_VerifyFinal_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pSignature': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'ulSignatureLen': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-VerifyFinal-Return ::= SEQUENCE { retval ACK-RV }
class C_VerifyFinal_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-VerifyInit-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pMechanism [1] ACK-MECHANISM, hKey [2] ACK-OBJECT-HANDLE }
class C_VerifyInit_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pMechanism': ('_TYPTR', ['ACK-MECHANISM'], 1),
        'hKey': ('_TYPTR', ['ACK-OBJECT-HANDLE'], 5) } )
    _context = globals ()
    _numcursori = 6

# C-VerifyInit-Return ::= SEQUENCE { retval ACK-RV }
class C_VerifyInit_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-VerifyRecover-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pSignature [1] ACK-BYTE-ARRAY, ulSignatureLen [2] ACK-ULONG, pulDataLen [4] ACK-ULONG }
class C_VerifyRecover_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pSignature': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'ulSignatureLen': ('_TYPTR', ['ACK-ULONG'], 2),
        'pulDataLen': ('_TYPTR', ['ACK-ULONG'], 3) } )
    _context = globals ()
    _numcursori = 4

# C-VerifyRecover-Return ::= SEQUENCE { retval ACK-RV, pData [3] ACK-BYTE-ARRAY, pulDataLen [4] ACK-ULONG }
class C_VerifyRecover_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pData': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'pulDataLen': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-VerifyUpdate-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pPart [1] ACK-BYTE-ARRAY, ulPartLen [2] ACK-ULONG }
class C_VerifyUpdate_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pPart': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'ulPartLen': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-VerifyUpdate-Return ::= SEQUENCE { retval ACK-RV }
class C_VerifyUpdate_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0) } )
    _context = globals ()
    _numcursori = 1

# C-WaitForSlotEvent-Call ::= SEQUENCE { flags [0] ACK-FLAGS, pReserved [2] NULL OPTIONAL }
class C_WaitForSlotEvent_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_BITSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'flags': ('_TYPTR', ['ACK-FLAGS'], 0),
        'pReserved': ('_TYPTR', ['_api.ASN1Null'], 1) } )
    _context = globals ()
    _numcursori = 2

# C-WaitForSlotEvent-Return ::= SEQUENCE { retval ACK-RV, pSlot [1] ACK-SLOT-ID, pReserved [2] NULL OPTIONAL }
class C_WaitForSlotEvent_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_OPTIONAL) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pSlot': ('_TYPTR', ['ACK-SLOT-ID'], 1),
        'pReserved': ('_TYPTR', ['_api.ASN1Null'], 2) } )
    _context = globals ()
    _numcursori = 3

# C-WrapKey-Call ::= SEQUENCE { hSession [0] ACK-SESSION-HANDLE, pMechanism [1] ACK-MECHANISM, hWrappingKey [2] ACK-OBJECT-HANDLE, hKey [3] ACK-OBJECT-HANDLE, pulWrappedKeyLen [5] ACK-ULONG }
class C_WrapKey_Call (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(0)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(1)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_NULL) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(2)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(3)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(5)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'hSession': ('_TYPTR', ['ACK-SESSION-HANDLE'], 0),
        'pMechanism': ('_TYPTR', ['ACK-MECHANISM'], 1),
        'hWrappingKey': ('_TYPTR', ['ACK-OBJECT-HANDLE'], 5),
        'hKey': ('_TYPTR', ['ACK-OBJECT-HANDLE'], 6),
        'pulWrappedKeyLen': ('_TYPTR', ['ACK-ULONG'], 7) } )
    _context = globals ()
    _numcursori = 8

# C-WrapKey-Return ::= SEQUENCE { retval ACK-RV, pWrappedKey [4] ACK-BYTE-ARRAY, pulWrappedKeyLen [5] ACK-ULONG }
class C_WrapKey_Return (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(4)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_CONTEXT(5)) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_INTEGER) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'retval': ('_TYPTR', ['ACK-RV'], 0),
        'pWrappedKey': ('_TYPTR', ['ACK-BYTE-ARRAY'], 1),
        'pulWrappedKeyLen': ('_TYPTR', ['ACK-ULONG'], 2) } )
    _context = globals ()
    _numcursori = 3

# NotifierCode ::= ENUMERATED { cb-Notify (0), cb-CreateMutex (1), cb-DestroyMutex (2), cb-LockMutex (3), cb-UnlockMutex (4), ... }
class NotifierCode (_api.ASN1Enumerated):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Enumerated'], 0)
    _context = globals ()
    _numcursori = 1

# OperationCode ::= ENUMERATED { opc-Initialize-Tag (0), opc-Finalize-Tag (1), opc-GetInfo-Tag (2), opc-GetFunctionList-Tag (3), opc-GetSlotList-Tag (4), opc-GetSlotInfo-Tag (5), opc-GetTokenInfo-Tag (6), opc-GetMechanismList (7), opc-GetMechanismInfo (8), opc-InitToken (9), opc-InitPIN (10), opc-SetPIN (11), opc-OpenSession (12), opc-CloseSession (13), opc-CloseAllSessions (14), opc-GetSessionInfo (15), opc-GetOperationState (16), opc-SetOperationState (17), opc-Login (18), opc-Logout (19), opc-CreateObject (20), opc-CopyObject (21), opc-DestroyObject (22), opc-GetObjectSize (23), opc-GetAttributeValue (24), opc-SetAttributeValue (25), opc-FindObjectsInit (26), opc-FindObjects (27), opc-FindObjectsFinal (28), opc-EncryptInit (29), opc-Encrypt (30), opc-EncryptUpdate (31), opc-EncryptFinal (32), opc-DecryptInit (33), opc-Decrypt (34), opc-DecryptUpdate (35), opc-DecryptFinal (36), opc-DigestInit (37), opc-Digest (38), opc-DigestUpdate (39), opc-DigestKey (40), opc-DigestFinal (41), opc-SignInit (42), opc-Sign (43), opc-SignUpdate (44), opc-SignFinal (45), opc-SignRecoverInit (46), opc-SignRecover (47), opc-VerifyInit (48), opc-Verify (49), opc-VerifyUpdate (50), opc-VerifyFinal (51), opc-VerifyRecoverInit (52), opc-VerifyRecover (53), opc-DigestEncryptUpdate (54), opc-DecryptDigestUpdate (55), opc-SignEncryptUpdate (56), opc-DecryptVerifyUpdate (57), opc-GenerateKey (58), opc-GenerateKeyPair (59), opc-WrapKey (60), opc-UnwrapKey (61), opc-DeriveKey (62), opc-SeedRandom (63), opc-GenerateRandom (64), opc-GetFunctionStatus (65), opc-CancelFunction (66), opc-WaitForSlotEvent (67), ... }
class OperationCode (_api.ASN1Enumerated):
    _der_packer = (
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_TYPTR', ['_api.ASN1Enumerated'], 0)
    _context = globals ()
    _numcursori = 1

# RemoteNotificationCall ::= [APPLICATION 3] SEQUENCE { notecode NotifierCode, notedata ANY }
class RemoteNotificationCall (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(3)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'notecode': ('_TYPTR', ['NotifierCode'], 0),
        'notedata': ('_TYPTR', ['_api.ASN1Any'], 1) } )
    _context = globals ()
    _numcursori = 2

# RemoteNotificationReturn ::= [APPLICATION 4] SEQUENCE { notecode NotifierCode, notedata ANY }
class RemoteNotificationReturn (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(4)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'notecode': ('_TYPTR', ['NotifierCode'], 0),
        'notedata': ('_TYPTR', ['_api.ASN1Any'], 1) } )
    _context = globals ()
    _numcursori = 2

# RemoteProcedureCall ::= [APPLICATION 1] SEQUENCE { opcode OperationCode, opdata ANY }
class RemoteProcedureCall (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(1)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'opcode': ('_TYPTR', ['OperationCode'], 0),
        'opdata': ('_TYPTR', ['_api.ASN1Any'], 1) } )
    _context = globals ()
    _numcursori = 2

# RemoteProcedureReturn ::= [APPLICATION 2] SEQUENCE { opcode OperationCode, opdata ANY }
class RemoteProcedureReturn (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(2)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'opcode': ('_TYPTR', ['OperationCode'], 0),
        'opdata': ('_TYPTR', ['_api.ASN1Any'], 1) } )
    _context = globals ()
    _numcursori = 2

# TransportMessage ::= SEQUENCE { version ACK-VERSION, transportID OCTET STRING, requestID OCTET STRING, payload CHOICE { call RemoteProcedureCall, called RemoteProcedureReturn, notify RemoteNotificationCall, noted RemoteNotificationReturn, ... }, ... }
class TransportMessage (_api.ASN1ConstructedType):
    _der_packer = (
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_OCTETSTRING) +
        chr(_api.DER_PACK_CHOICE_BEGIN) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(1)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(2)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(3)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_APPLICATION(4)) +
        chr(_api.DER_PACK_ENTER | _api.DER_TAG_SEQUENCE) +
        chr(_api.DER_PACK_STORE | _api.DER_TAG_ENUMERATED) +
        chr(_api.DER_PACK_ANY) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_CHOICE_END) +
        chr(_api.DER_PACK_LEAVE) +
        chr(_api.DER_PACK_END) )
    _recipe = ('_NAMED', {
        'version': ('_TYPTR', ['ACK-VERSION'], 0),
        'transportID': ('_TYPTR', ['_api.ASN1OctetString'], 2),
        'requestID': ('_TYPTR', ['_api.ASN1OctetString'], 3),
        'payload': ('_NAMED', {
            'call': ('_TYPTR', ['RemoteProcedureCall'], 4),
            'called': ('_TYPTR', ['RemoteProcedureReturn'], 6),
            'notify': ('_TYPTR', ['RemoteNotificationCall'], 8),
            'noted': ('_TYPTR', ['RemoteNotificationReturn'], 10) } ) } )
    _context = globals ()
    _numcursori = 12

#
# Variables with ASN.1 value assignments
#


# asn2quickder output for RemotePKCS11 ends here
