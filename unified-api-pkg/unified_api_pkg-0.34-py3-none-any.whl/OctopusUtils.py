from datetime import datetime
from .generalUtils import *

OCT_BASCI_TIMESTAMP = 946684800

bilingualDict = {
	"SALE":"銷售",
    "TOPUP":"增值",
    "REFUND":"退款",
    "MID":"商戶號",
    "TID":"終端號",
    "DATE":"日期",
    "TIME":"時間",
    "PAN":"卡號",
    "TOTAL":"總計",
    "NET":"淨額",
    "ACCEPTED":"接受",
    "REJECTED":"不接受",
    "TOPUPVALUE":"增值金額",
    "REMINBAL":"餘額",
    "ENQ":" 查詢",
    "CASH":"現金增值",
    "AAVS":"自動增值",
    "ONLINE":"線上增值",
    "OTHER":"其他",
    "REDEEMED":"兌換日日賞$",
    "EARN":"賺取日日賞$",
    "R_BAL":"日日賞$餘額",
    "R_TITLE":"八達通日日賞"
}

list_last_topup_eng = [
    "","CASH","ONLINE","REFUND","AAVS","OTHERS"
]

list_last_topup_chinese = [
    "","現金增值","線上增值","退款","自動增值","其他"
]


def __add_minus(cmd):
    if cmd == "TOPUP":
        return ""
    else:
        return "-"

def formatTransDataOctopus(UD_list,transData):
    idx = 0
    for x in UD_list:
        print(str(idx) + ":" + str(x))
        idx = idx + 1

    idx = 1
    for x in range(0,int(UD_list[0])):

        #Normal UD
        if int(UD_list[idx]) == 0:
            idx = idx + 1
            transData["CARD"] = "OCTOPUS"
            transData["UDSN"] = str(UD_list[idx])
            txn_datetime = datetime.fromtimestamp(OCT_BASCI_TIMESTAMP+int(UD_list[idx+1]))
            transData["DATE"] = txn_datetime.strftime("%Y%m%d")
            transData["TIME"] = txn_datetime.strftime("%H%M%S")
            transData["TXNSEQ"] = str(UD_list[idx+5])
            transData["AMT"] = float(UD_list[idx+6])/10
            transData["REMINBAL"] = float(UD_list[idx+7])/10
            transData["RESP"] = str(UD_list[idx+7])
            #Go though normal UD.
            idx = idx + 7

            #Next UD type
            idx = idx + 1
        
        #RMS UD
        elif int(UD_list[idx]) == 1:
            idx = idx + 1
            #the UD contain RMS information
            transData["CARD"] = "OCTOPUS"
            transData["RDSN"] = UD_list[idx]
            txn_datetime = datetime.fromtimestamp(OCT_BASCI_TIMESTAMP+int(UD_list[idx+1]))
            transData["DATE"] = txn_datetime.strftime("%Y%m%d")
            transData["TIME"] = txn_datetime.strftime("%H%M%S")
            transData["RMSTXNSEQ"] = UD_list[idx+6]
            transData["AMT"] = float(UD_list[idx+8])/10
            #Go though RMS UD
            idx = idx + 10

            #Next UD type
            idx = idx + 1

def formatTransReceiptOctopus(transData,printOut,props,receiptType):

    if receiptType == "REDEEM_COMP" or receiptType == "ISSUE":
        #Partial Receipt
        printOut.append("")
        if props["language"] == "C":
            printOut.append(print_at_middle(bilingualDict["R_TITLE"],False))
        else:
            printOut.append(print_at_middle("Octopus Rewards",True))

        printOut.append(mix_1_column_b(bilingualDict["TID"],"TID",props["OCTTID"]))
        printOut.append(mix_1_column_b(bilingualDict["PAN"],"PAN",transData["PAN"]))
        printOut.append(mix_1_column("ECRREF",transData["ECRREF"]))

        if "R_REDEEMED" in transData:
            if props["language"] == "C":
                printOut.append(mix_1_column_c(bilingualDict["REDEEMED"],props["region"]+" "+__add_minus(transData["CMD"])+'%.2f' % transData["R_REDEEMED"]))
            else:
                printOut.append(mix_1_column("Redeem Reward$",props["region"]+" "+__add_minus(transData["CMD"])+'%.2f' % transData["R_REDEEMED"]))
        
        if "R_EARN" in transData:
            if props["language"] == "C":
                printOut.append(mix_1_column_c(bilingualDict["EARN"],props["region"]+" "+'%.2f' % transData["R_EARN"]))
            else:
                printOut.append(mix_1_column("Earn Reward$",props["region"]+" "+'%.2f' % transData["R_EARN"]))

        if "R_BALANCE" in transData:
            if props["language"] == "C":
                printOut.append(mix_1_column_c(bilingualDict["R_BAL"],props["region"]+" "+'%.2f' % transData["R_BALANCE"]))
            else:
                printOut.append(mix_1_column("Reward$ Balance",props["region"]+" "+'%.2f' % transData["R_BALANCE"]))
        
    else:
        #Normal receipt
        printOut.append(bilingualDict[transData["CMD"]] +" "+ transData["CMD"])
        printOut.append("")
        printOut.append(mix_2_column_b(bilingualDict["DATE"],"DATE",formatDateTimeInReceipt(True,transData["DATE"]),bilingualDict["TIME"],"TIME",formatDateTimeInReceipt(False,transData["TIME"])))
        #printOut.append(mix_1_column_b(bilingualDict["MID"],"MID",props["OCTMID"]))
        printOut.append(mix_1_column_b(bilingualDict["TID"],"TID",props["OCTTID"]))
        printOut.append(mix_1_column_b(bilingualDict["PAN"],"PAN",transData["PAN"]))
        printOut.append(mix_1_column("ECRREF",transData["ECRREF"]))
        printOut.append(transData["CARD"])
        printOut.append("")

        if transData["CMD"] == "TOPUP" and transData["AMT"] != 0:
            #normal add value
            printOut.append(mix_1_column_b(bilingualDict["TOPUPVALUE"],"TOPUP AMT",props["region"]+" "+__add_minus(transData["CMD"])+'%.2f' % transData["AMT"]))
            if transData["OCTTYPE"] != str(1):
                printOut.append(mix_1_column_b(bilingualDict["REMINBAL"],"REMAINING AMT",props["region"]+" "+'%.2f' % transData["REMINBAL"]))
        elif transData["CMD"] == "TOPUP" and transData["AMT"] == 0:
            #transport subsidy
            print("XXXX")
        
        elif transData["CMD"] == "SALE":
            printOut.append(mix_1_column_b(bilingualDict["TOTAL"],"TOTAL",props["region"]+" "+__add_minus(transData["CMD"])+'%.2f' % transData["AMT"]))
            if "R_REDEEMED" in transData:
                if props["language"] == "C":
                    printOut.append(mix_1_column_c(bilingualDict["REDEEMED"],props["region"]+" "+__add_minus(transData["CMD"])+'%.2f' % transData["R_REDEEMED"]))
                else:
                    printOut.append(mix_1_column("Redeem Reward$",props["region"]+" "+__add_minus(transData["CMD"])+'%.2f' % transData["R_REDEEMED"]))
                printOut.append("-"*40)
            if "NETAMT" in transData:
                printOut.append(mix_1_column_b(bilingualDict["NET"],"NET",props["region"]+" "+__add_minus(transData["CMD"])+'%.2f' % transData["NETAMT"]))
            

            if transData["OCTTYPE"] != str(1):
                printOut.append(mix_1_column_b(bilingualDict["REMINBAL"],"REMAINING AMT",props["region"]+" "+'%.2f' % transData["REMINBAL"]))
            
            printOut.append("")

            if "LAST_ADD" in transData:
                list_last_topup = transData["LAST_ADD"].split(",")
                printOut.append("LAST TOPUP BY " + list_last_topup_eng[int(list_last_topup[1])]+ " ON "+list_last_topup[0])
                printOut.append("上一次於 "+ list_last_topup[0] +" "+ list_last_topup_chinese[int(list_last_topup[1])])
                transData.pop("LAST_ADD")
                printOut.append("")

            if "R_EARN" in transData:
                if props["language"] == "C":
                    printOut.append(print_at_middle(bilingualDict["R_TITLE"],False))
                    printOut.append(mix_1_column_c(bilingualDict["EARN"],props["region"]+" "+'%.2f' % transData["R_EARN"]))
                else:
                    printOut.append(mix_1_column("Earn Reward$",props["region"]+" "+'%.2f' % transData["R_EARN"]))

            if "R_BALANCE" in transData:
                if props["language"] == "C":
                    printOut.append(mix_1_column_c(bilingualDict["R_BAL"],props["region"]+" "+'%.2f' % transData["R_BALANCE"]))
                else:
                    printOut.append(mix_1_column("Reward$ Balance",props["region"]+" "+'%.2f' % transData["R_BALANCE"]))




