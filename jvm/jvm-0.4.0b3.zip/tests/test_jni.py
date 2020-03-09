
import sys
import os
import os.path as path
import ctypes as ct
from pprint import pprint

test_dir  = path.dirname(path.abspath(__file__))
test_java = path.join(test_dir, "java")

def test():

    # Create the Java Virtual Machine.

    from jt.jtypes._jvm import JVM
    import jvm as _jvm

    jvm_path = JVM.defaultPath()

    global jvm
    jvm = _jvm.JVM(jvm_path)
    if jvm.isStarted():
        raise Exception("jvm.dll already startet !?")
    jvm.start("-Djava.class.path={}".format(
              os.pathsep.join([path.join(test_java, "classes")])),
              "-ea", "-Xms16M", "-Xmx512M")

    test_jni()
    test_JVM()

    jvm.shutdown()

def test_jni():

    import jni
    from jvm import JVM

    print()
    print("test JNI")
    print()

    global jvm

    penv = jni.obj(jni.POINTER(jni.JNIEnv))
    jvm._jvm.jnijvm.GetEnv(penv, JVM.JNI_VERSION)
    jenv = jni.JEnv(penv)

    _doubleClass = jni.cast(jenv.FindClass(b"Ljava/lang/Double;"), jni.jclass)
    _doubleCtor  = jenv.GetMethodID(_doubleClass, b"<init>",       b"(D)V")
    _numberClass = jni.cast(jenv.FindClass(b"Ljava/lang/Number;"), jni.jclass)
    _doubleValue = jenv.GetMethodID(_numberClass, b"doubleValue",  b"()D")

    jargs = jni.new_array(jni.jvalue, 1)
    jargs[0].d = 123.5
    jobj = jenv.NewObject(_doubleClass, _doubleCtor, jargs)

    ret = jenv.CallDoubleMethod(jobj, _doubleValue, None)
    print("jenv.CallDoubleMethod(jobj, _doubleValue, None)", type(ret), ret)

    #print("type(jenv.GetArrayLength(argTypes))", type(jenv.GetArrayLength(argTypes)), jenv.GetArrayLength(argTypes))
    #print()

    jstr = jenv.NewStringUTF(b'lala')
    print("jstr = jenv.NewStringUTF(b'lala'):", type(jstr), jstr)

    utf8_chars = jenv.GetStringUTFChars(jstr)
    print("utf8_chars = jenv.GetStringUTFChars(jstr):",
          type(utf8_chars), utf8_chars,
          type(ct.cast(utf8_chars, ct.c_char_p).value), ct.cast(utf8_chars, ct.c_char_p).value)
    jenv.ReleaseStringUTFChars(jstr, utf8_chars)

def test_JVM():

    import jni
    from jvm import JVM

    print()
    print("test JVM")
    print()

    global jvm

    penv = jni.obj(jni.POINTER(jni.JNIEnv))
    jvm._jvm.jnijvm.GetEnv(penv, JVM.JNI_VERSION)
    jenv = jni.JEnv(penv)

    pprint(jvm._jvm)
    version = jenv.GetVersion()
    print("GetVersion():", hex(version), float("{}.{}".format((version & ~0xFFFF) >> 16, version & 0xFFFF)))

    res  = jvm.JPackage.getPackage("java.lang")
    print("getPackage('java.lang'):", type(res), res)

    res  = jvm.JPackage.getPackage("org.w3c.dom")
    print(res)
    Element =  jvm.JClass.forName("org.w3c.dom.Element")
    print(Element)

    z = jvm.isThreadAttached()
    print(type(z), z)

def test_jtypes():

    import jni
    from jvm import JVM

    print()
    print("test jtypes")
    print()

    global jvm

    penv = jni.obj(jni.POINTER(jni.JNIEnv))
    jvm._jvm.jnijvm.GetEnv(penv, JVM.JNI_VERSION)
    jenv = jni.JEnv(penv)

    #try:
    #class jvalue(ct.Union):
    #    _fields_ = [("z", jboolean),
    #                ("b", jbyte),
    #                ("c", jchar),
    #                ("s", jshort),
    #                ("i", jint),
    #                ("j", jlong),
    #                ("f", jfloat),
    #                ("d", jdouble),
    #                ("l", jobject)]

    jval = jni.obj(jni.jvalue)
    jval.i = 33
    print("jint",     type(jval.i), repr(jval.i))
    jval = jni.obj(jni.jvalue)
    jval.l = jni.NULL
    print("jobject",  type(jval.l), repr(jval.l))

    jval = jni.obj(jni.jvalue)
    #print("jboolean", type(jval.z), repr(jval.z))
    #print("jbyte",    type(jval.b), repr(jval.b))
    #print("jchar",    type(jval.c), repr(jval.c))
    #print("jshort",   type(jval.s), repr(jval.s))
    #print("jint",     type(jval.i), repr(jval.i))
    #print("jlong",    type(jval.j), repr(jval.j))
    #print("jfloat",   type(jval.f), repr(jval.f))
    #print("jdouble",  type(jval.d), repr(jval.d))
    #print("jobject",  type(jval.l), repr(jval.l))
    #print()

    jval.z = 0
    #print("jboolean", type(jval.z), repr(jval.z))
    jval.z = 1
    #print("jboolean", type(jval.z), repr(jval.z))
    jval.z = 33
    #print("jboolean", type(jval.z), repr(jval.z))
    jval.b = 65
    #print("jbyte",    type(jval.b), repr(jval.b))
    jval.c = u"R"
    #print("jchar",    type(jval.c), repr(jval.c))
    jval.c = b"B"
    #print("jchar",    type(jval.c), repr(jval.c))
    jval.s = 12
    #print("jshort",   type(jval.s), repr(jval.s))
    jval.i = 234567
    #print("jint",     type(jval.i), repr(jval.i))
    jval.j = 23456744445555555
    #print("jlong",    type(jval.j), repr(jval.j))
    jval.f = 777.77
    #print("jfloat",   type(jval.f), repr(jval.f))
    jval.d = 8888888888888888.88
    #print("jdouble",  type(jval.d), repr(jval.d))
    print()

    #except Exception as exc:
    #
    #    error = "%s\n" % exc
    #    raise exc

    obj = "weweeeertyteee"

    jobj = jenv.NewDirectByteBuffer(obj, len(obj))
    print(jobj)
    jobj = jenv.NewDirectByteBuffer(ct.c_char_p(obj), len(obj))
    print(jobj)
    print()

    #ustr = JJni.javaStringFromString("SERT")
    #ustr = JJni.unicodeFromJavaString(ustr)
    #print(type(ustr), ustr)
    #ustr32 = ustr.encode("utf_32")
    #ustr16 = ustr32.decode("utf_32")
    #print(type(ustr),   ustr)
    #print(type(ustr32), ustr32)
    #print(type(ustr16), ustr16)

if __name__ == "__main__":
    test()
