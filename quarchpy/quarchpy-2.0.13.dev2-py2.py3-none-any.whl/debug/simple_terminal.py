from quarchpy import *
from quarchpy.device import *
from quarchpy.user_interface import*
def main():
    moduleStr = userSelectDevice(nice=True, scanFilterStr="QTL1999")
    if moduleStr == "quit":
        return 0
    print("Selected module is: " + moduleStr)
    # Create a device using the module connection string
    #moduleStr = "REST:1995-05-005"
    myDevice = quarchDevice(moduleStr)
    while True:
        user_input = requestDialog("","Send command to " + str(moduleStr) + " :")
        print(myDevice.sendCommand(user_input))
if __name__ == "__main__":
    main()