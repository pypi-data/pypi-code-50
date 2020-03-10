from ctypes import *
from .OctopusUtils import *
from datetime import datetime
from .generalUtils import *

dll = windll.LoadLibrary("rml.dll")

device_TID = None
company_MID = None
TimeOut = None

OCT_BASCI_TIMESTAMP = 946684800

def openOCTCom(octCOM,octOutID,octTimeOut):
    global TimeOut
    TimeOut = int(int(octTimeOut)/3)
    result = dll.InitComm(int(octCOM),115200)
    output = (c_char *1024)()
    if result == 0:
        result = dll.RMS_Init(int(octOutID),output)
    return result

def closeOCTCom():
    result = dll.PortClose()
    return result

def getDeviceInfo():
    device_info = []
    global device_TID
    global company_MID
    output = (c_uint * 56)()
    result = dll.TimeVer(output)
    device_info.append(result)
    if result == 0:
        device_TID = hex(output[0])[2:].upper()
        company_MID = str(output[3])

        device_info.append(device_TID)
        device_info.append(company_MID)
    return device_info

def polling(option,transData,pollType):
    output = (c_char * 1024)()
    #RMS polling require 128
    if option == "REWARDBAL":
        pollType = 128

    for t in range(0,int(TimeOut)):
        result = dll.PollEx(pollType,30,output)
        if result == 100032:
            pass
        else:
            break

    if result  < 100000:
        list_output_string = output.value.decode("utf-8").split(",")
        if pollType == 2:
            list_customer_info = list_output_string[3].split("-")
            transData["OCTTYPE"] = list_customer_info[0]
            transData["OCTOLDPAN"] = list_output_string[0]
            transData["PAN"] = list_output_string[2]
        elif pollType == 128:
            list_customer_info = list_output_string[2].split("-")
            transData["OCTTYPE"] = list_customer_info[0]
            transData["OCTOLDPAN"] = list_output_string[0]
            transData["PAN"] = list_output_string[1]


        #less than 100000 is valid
        transData["CMD"] = "ENQ"
        transData["TYPE"] = "OCT_REWARDS"

        
        transData["TID"] = device_TID
        transData["DEVICENO"] = device_TID
        transData["MID"] = company_MID

        now = datetime.now()
        transData["DATE"] = now.strftime("%Y%m%d")
        transData["TIME"] = now.strftime("%H%M%S")
        transData["ACQNAME"] = "OCT_REWARDS"
        transData["CARD"] = "OCT_REWARDS"
        transData["STATUS"] = "APPROVE"
        transData["RESP"] = str(result)
        transData["REMINBAL"] = float(result)/10

        if option == "HISTORY":
            #from index 5 - 10 record, each record has 5 elements
            list_history = []
            for x in range(5, 55, 5):
                try:
                    dict_history = {}
                    txn_datetime = datetime.fromtimestamp(OCT_BASCI_TIMESTAMP+int(list_output_string[x+2]))
                    dict_history["DATE"] = txn_datetime.strftime("%Y%m%d")
                    dict_history["TIME"] = txn_datetime.strftime("%H%M%S")
                    dict_history["AMT"] = float(list_output_string[x+1])/10
                    dict_history["TID"] = list_output_string[x+3]
                    list_history.append(dict_history)
                except:
                    #skip this record
                    pass
            transData["HISTORY"] = list_history
        elif option == "REWARDBAL":
            result = __RMS_get()
            transData["REWARDBAL"] = result/100
    return result

def topUp(ecr_ref,amount,transData):
    UD_list = []
    transData["ECRREF"] = ecr_ref
    if amount == 0:
        list_subsidy = []
        transData["AMT"] = 0
        #Transport subsidy
        result = polling("SUBSIDY",transData,2)
        if result < 100000:
            int_ecr = int(ecr_ref)
            if int_ecr >= 65535:
                #too large for Octopus device
                return "PF"
            else:
                print('Ecr ref OK')
                result =  __CollectSubsidy(int_ecr,list_subsidy)
                if result[0] < 100000:
                    transData["CMD"] = "SUBSIDY"
                    transData["REMINBAL"] = float(result[0])/10
                    #Subsidy data
                    transData["Sub_Total"] = float(result[1])/10
                    transData["Sub_TotalCollect"] = float(result[2])/10
                    transData["Sub_Outstand"] = float(result[3])/10
                    transData["Sub_reason"] = int(result[4])
                    #NO of sub collect ignore

                    if __getInstantUD(UD_list) == 0:
                        formatTransDataOctopus(UD_list,transData)
                    return result[0]
                return result[0]
        else:
            return result
    else:
        #do a Poll
        result = polling("TOPUP",transData,2)
        if result < 100000:

            #Poll success
            output = (c_char * 1024)()

            if len(ecr_ref) > 5:
                temp_ecr_ref = '0'+ecr_ref[0:5]
                b_ecr = temp_ecr_ref.encode('utf-8')
                memmove(output,b_ecr,6)

            result = dll.AddValue(amount,1,output)
            if result < 100000:
                if __getInstantUD(UD_list) == 0:
                    transData["CMD"] = "TOPUP"
                    formatTransDataOctopus(UD_list,transData)
                return result
            else:
                return result
        else:
            return result

def saleOCT(payment_type,ecr_ref,amount,additional_amount,payment_option,transData,printOut):
    list_last_txn = []
    transData["ECRREF"] = ecr_ref
    if "OCT_LAST" in transData:
        list_last_txn = transData["OCT_LAST"]
        #shift the octopus payment to the last
        list_last_txn.append(list_last_txn.pop(0))
    
    if payment_option != "REDEEM_COMP":
        result = polling("SALE",transData,128)
        if result < 100000:
            result = __RMS_get()
            if result < 100000:
                if payment_option == "" or payment_option == None: 
                    result = __RMS_TXN(0,list_last_txn,amount,ecr_ref,transData)
                    return result
                if payment_option == "DO_NOT_REDEEM" or payment_option == "ISSUE":
                    #issue R$ only, settle by Octopus
                    result = __RMS_TXN(1,list_last_txn,amount,ecr_ref,transData)
                    return result
                elif payment_option == "NORMAL_REDEEM":
                    #redeem and issue, by Octopus only
                    result = __RMS_TXN(3,list_last_txn,amount,ecr_ref,transData)
                    return result
                elif payment_option == "REDEEM_CHECK":
                    #Redeem Check, return eligble R$
                    result =__RMS_Redeem_Check(amount,amount)
                    transData["REWARDBAL"] = result/100
                    return result
            else:
                return result
        else:
            return 0
    else:
        #Complete the transaction by previous REDEEM_CHECK command
        result = __RMS_TXN(3,list_last_txn,amount,ecr_ref,transData)
        return result

def __RMS_get():
    buf = (c_int * 1)()
    result = dll.RMS_Get(0,1,buf)
    if result < 100000:
        return buf[0]
    else:
        return result

def __RMS_TXN(option,list_lastTxn,amount,ecr_ref,transData):
    input = (c_int32*26)()
    output = (c_int*6)()

    #extra_issue;redeem;redeem_off
    #should be provided as setting
    input[0] = 0
    input[1] = 0
    input[2] = 0

    #total amount 
    input[3] = amount
    #redeem or not; bit 1 issue ;bit 2 redeem; bit 3 RMS register; 0 normal deduct
    input[4] = option
    #split payment

    if option > 0:
        if len(list_lastTxn) == 0:
            input[5] = 2
            input[6] = 0
            input[7] = amount
            input[8] = 128
            input[9] = 0
        else:
            input[5] = len(list_lastTxn) *2
            for x in range(0,len(list_lastTxn)):
                input[6+(4*x)] = (x + 1) % 4
                input[7+(4*x)] = inputAmountStringToLong(list_lastTxn[x])
                input[8+(4*x)] = (x + 1) % 4 + 128
                input[9+(4*x)] = 0
    else:
        input[5] = 1
        input[6] = 0
        input[7] = amount


    if len(ecr_ref) < 6:
        temp_ecr_ref = ecr_ref+("               ")
    else:
        temp_ecr_ref = ecr_ref[0:6]

    b_ecr = temp_ecr_ref.encode('utf-8')
    b1 = b_ecr[0]
    b2 = b_ecr[1]
    b3 = b_ecr[2]
    b4 = b_ecr[3]
    y = 0
    y = (y|b4)<<8
    y = (y|b3)<<8
    y = (y|b2)<<8
    y = (y|b1)
    input[22] = y
    b3 = b_ecr[4]
    b4 = b_ecr[5]
    y = 0
    y = (y|b3)<<8
    y = (y|b4)<<8
    y = (y|b1)<<8
    y = (y|b2)
    input[23] = y

    result = dll.RMS_TXN(input,output)
    #success
    if result == 0:
        result = dll.RMS_Update(0)
        __GetExtraInfo(transData)
        if result == 0:

            #get data from output.  
            transData["R_EARN"] = output[0]/100          
            transData["NETAMT"] = output[3]/100
            transData["R_REDEEMED"] = output[1]/100
            transData["R_BALANCE"] = output[5]/100

            UD_list = []
            if __getInstantUD(UD_list) == 0:
                transData["CMD"] = "SALE"
                formatTransDataOctopus(UD_list,transData)
            return result
        else:
            return result
    else:
        return result

    return result

def __getInstantUD(ud_content):
    UD_length = c_int32()
    UD = c_void_p() 
    result = dll.GetInstantUD(byref(UD),byref(UD_length))
    ptrt = POINTER(c_char * UD_length.value) 
    mydblPtr = cast(UD, POINTER(c_char * UD_length.value)) 

    indexes = ptrt(mydblPtr.contents)


    if UD_length.value <= 0:
        return result


    #Get total number of UD contained.
    ud_content.append(str(int.from_bytes(indexes.contents[0],'big')))

    idx = 1

    #get thet UD info 1 by 1
    for no_UD in range(0,int.from_bytes(indexes.contents[0],'big')):

        # The size of this UD
        size = int.from_bytes(indexes.contents[idx],'big')

        #the type
        idx = idx + 1

        # UD Type
        ud_content.append(str(int.from_bytes(indexes.contents[idx],'big')))

        #The starting idx of content
        idx = idx + 1

        for x in range(idx,size + idx,4):
            b1 = int.from_bytes(indexes.contents[x],'big')
            b2 = int.from_bytes(indexes.contents[x+1],'big')
            b3 = int.from_bytes(indexes.contents[x+2],'big')
            b4 = int.from_bytes(indexes.contents[x+3],'big')
            y = 0
            y = (y|b4)<<8
            y = (y|b3)<<8
            y = (y|b2)<<8
            y = (y|b1)
            ud_content.append(str(y))

        idx = idx + size
    return result

def __GetExtraInfo(transData):
    output = (c_char *1024)()
    result = dll.GetExtraInfo(0,1,output)
    if result == 0:
        transData["LAST_ADD"] = output.value.decode("utf-8")
    else:
        return result

def settleOCT():
    output = (c_char * 1024)()
    result = dll.XFile(output)
    return result

def __RMS_Redeem_Check(totalAmt,netAmt):
    result = dll.RMS_RedeemCheck(totalAmt,netAmt)
    return result

def initSubsidy():
    result = dll.InitSubsidyList()
    return result

def __CollectSubsidy(int_ecr,list_subsidy):
    output = (c_char * 1024)()
    result = dll.CollectSubsidy(int_ecr,output)
    list_subsidy.append(result)
    if result < 100000:
        for x in range(0,20,4):
            b1 = int.from_bytes(output[x],'big')
            b2 = int.from_bytes(output[x+1],'big')
            b3 = int.from_bytes(output[x+2],'big')
            b4 = int.from_bytes(output[x+3],'big')
            y = 0
            y = (y|b4)<<8
            y = (y|b3)<<8
            y = (y|b2)<<8
            y = (y|b1)

            print( str(y))
            list_subsidy.append(str(y))
    return list_subsidy

    
