
import sys

from jvm.jvm         import JVM, _JVM
from jvm.jobjectbase import JObjectBase
from jvm.jmember     import JMember
from jvm.jmodifiers  import JModifiers
from jvm.jhost       import JHost
from jvm.jframe      import JFrame
from jvm.jstring     import JString

import jt.jtypes as jt
jvm_path = jt.JVM.defaultPath()

print("Running using JVM:", jvm_path, "\n", file=sys.stderr)

jvm = jt.JVM()
jvm.start()
_jvm = jvm._state.jt_jvm

print("JVM\t\t\t",                 dir(JVM))
print("_JVM\t\t\t",                dir(_JVM))
print()
print("jvm.JPackage\t\t",          dir(_jvm.JPackage))
print("jvm.JClassLoader\t",        dir(_jvm.JClassLoader))
print("jvm.JClass\t\t",            dir(_jvm.JClass))
print("jvm.JField\t\t",            dir(_jvm.JField))
print("jvm.JConstructor\t",        dir(_jvm.JConstructor))
print("jvm.JMethod\t\t",           dir(_jvm.JMethod))
print("jvm.JArguments\t\t",        dir(_jvm.JArguments))
print("jvm.JPropertyDescriptor\t", dir(_jvm.JPropertyDescriptor))
print("jvm.JObject\t\t",           dir(_jvm.JObject))
print("jvm.JArray\t\t",            dir(_jvm.JArray))
print("jvm.JProxy\t\t",            dir(_jvm.JProxy))
print("jvm.JMonitor\t\t",          dir(_jvm.JMonitor))
print("jvm.JReferenceQueue\t",     dir(_jvm.JReferenceQueue))
print("jvm.JException\t\t",        dir(_jvm.JException))
print()
print("JObjectBase\t\t",           dir(JObjectBase))
print("JMember\t\t\t",             dir(JMember))
print("JModifiers\t\t",            dir(JModifiers))
print()
print("JHost\t\t\t",               dir(JHost))
print("JHost.ThreadState\t",       dir(JHost.ThreadState))
print("JHost.CallbackState\t",     dir(JHost.CallbackState))
print("JFrame\t\t\t",              dir(JFrame))
print("JString\t\t\t",             dir(JString))

jvm.shutdown()
