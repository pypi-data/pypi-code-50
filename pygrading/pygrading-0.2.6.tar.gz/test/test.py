import pygrading.general_test as gg

print(gg.__version__)

gg.utils.bash("sleep 10")
gg.utils.bash("whoami")

gg.TestCases.SingleTestCase.name

