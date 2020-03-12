#Provide Unified API in here
from .qrcode import saleQR,voidSaleQR,refundQR,retrievalQR,checkTypeQR
from .terminal import openPortTerminal, closePortTerminal,saleTerminal,refundTerminal,voidSaleTerminal,retrievalTerminal,membershipTerminal
from .terminalUtils import formatTransReceiptTerminal
from .Octopus import openOCTCom,closeOCTCom,polling,getDeviceInfo,topUp,settleOCT,saleOCT,initSubsidy,RMS_Update,membershipOCT,topUpRetry,subsidyRetry
from .OctopusUtils import formatTransReceiptOctopus
from .generalUtils import *
from .logUtils import *
import pkg_resources


class UnifiedAPI():
	props = {}

	#Default Constructor
	def __init__(self):
		#get all the properties in the file
		with open("eftsolutions.properties", "r") as f:
				l = f.read()
		f.close()
		prop_list = l.split("\n")

		for item in prop_list:
			try:
				item_list = item.split("=")
				self.props[item_list[0]] = item_list[1]
			except:
				#empty line caused exception
				pass
		#Set the log file path
		if "LogLocation" in self.props:
			setLogPath(self.props["LogLocation"])
			writeLogString("API","API VERSION:"+str(pkg_resources.require("unified_api_pkg")[0].version))
			writeLogDictionary("PROPERTIES",self.props)
		
	#Dictonary for transData,List for printOut
	def SaleQR(self,payment_type, qr_code, ecr_ref, amount, additional_amount,transData,printOut):
		printOut.clear()

		writeLogString("SALEQR INPUT","TYPE:"+payment_type+"||"+"QR:"+qr_code+"||"+"ECR:"+ecr_ref+"||"+"AMT:"+str(amount))

		amount = inputAmountStringToLong(amount)

		writeLogString("SALEQR","CONVERTED AMT:"+str(amount))

		result = saleQR(qr_code,ecr_ref,amount,transData,printOut)

		writeLogString("SALEQR RETURN",str(result))
		writeLogDictionary("SALEQR RESPONSE DATA",transData)
		writeLogReceipt(printOut)

		return result

	def Sale(self,payment_type,ecr_ref,amount,additional_amount,payment_option,transData,printOut):
		printOut.clear()

		writeLogString("SALE INPUT","TYPE:"+payment_type+"||"+"ECR:"+ecr_ref+"||"+"AMT:"+str(amount)+"||"+"ADD AMT:"+str(additional_amount)+"||"+"OPTION:"+payment_option)

		amount = inputAmountStringToLong(amount)

		writeLogString("SALE","CONVERTED AMT:"+str(amount))

		if payment_type == "EDC" or payment_type == "UPI" or payment_type == "EPS":
			result = saleTerminal(payment_type,ecr_ref,amount,additional_amount,payment_option,transData,printOut)
			formatTransReceiptTerminal(transData,printOut,self.props)

			writeLogString("SALE RETURN",str(result))
			writeLogDictionary("SALE RESPONSE DATA",transData)
			writeLogReceipt(printOut)


		elif payment_type == "OCT" or payment_type == "OCT_REWARDS":
			result = saleOCT(payment_type,ecr_ref,amount,additional_amount,payment_option,transData,printOut)
			if result < 100000:
				formatTransReceiptOctopus(transData,printOut,self.props,payment_option)
				
			writeLogString("SALE RETURN",str(result))
			writeLogDictionary("SALE RESPONSE DATA",transData)
			writeLogReceipt(printOut)

		return result

	def Void(self,payment_type,invoice,originalECRREF,transData,printOut):
		printOut.clear()

		writeLogString("VOID INPUT","TYPE:"+payment_type+"||"+"INVOICE:"+str(invoice)+"||"+"ORIECR:"+originalECRREF)

		if payment_type is "QR":
			result = voidSaleQR(invoice,transData,printOut)

			writeLogString("VOID RETURN",str(result))
			writeLogDictionary("VOID RESPONSE DATA",transData)
			writeLogReceipt(printOut)
			
			return result

		elif payment_type is "EDC" or payment_type is "UPI" or "VAC":
			result = voidSaleTerminal(payment_type,invoice,originalECRREF,transData,printOut)
			formatTransReceiptTerminal(transData,printOut,self.props)
			
			writeLogString("VOID RETURN",str(result))
			writeLogDictionary("VOID RESPONSE DATA",transData)
			writeLogReceipt(printOut)

			return result
		else:
			return -1
			
	def Refund(self,payment_type,ecr_ref,amount,originalTransRef,transData,printOut):
		printOut.clear()

		writeLogString("REFUND INPUT","TYPE:"+payment_type+"||"+"ECR:"+ecr_ref+"||"+"AMT:"+str(amount)+"||"+"ORI TRANS REF:"+originalTransRef)

		amount = inputAmountStringToLong(amount)

		writeLogString("REFUND","CONVERTED AMT:"+str(amount))

		if payment_type is "QR":
			result = refundQR(ecr_ref,amount,originalTransRef,transData,printOut)

			writeLogString("REFUND RETURN",str(result))
			writeLogDictionary("REFUND RESPONSE DATA",transData)
			writeLogReceipt(printOut)

			return result
		elif payment_type is "EDC":
			result = refundTerminal(payment_type,ecr_ref,amount,transData,printOut)
			formatTransReceiptTerminal(transData,printOut,self.props)

			writeLogString("REFUND RETURN",str(result))
			writeLogDictionary("REFUND RESPONSE DATA",transData)
			writeLogReceipt(printOut)

			return result
		else:
			return "PE"

	def Retrieval(self,payment_type,invoice,ecr_ref,transData,printOut):
		printOut.clear()

		writeLogString("RETRIV INPUT","TYPE:"+payment_type+"||"+"INVOICE:"+invoice+"||"+"ECRREF:"+ecr_ref)

		if payment_type is "QR":
			result = retrievalQR(invoice,ecr_ref,transData,printOut)

			writeLogString("RETRIV RETURN",str(result))
			writeLogDictionary("RETRIV RESPONSE DATA",transData)
			writeLogReceipt(printOut)

			return result
		elif payment_type is "EDC" or payment_type is "EPS":
			result = retrievalTerminal(payment_type,invoice,transData,printOut)
			formatTransReceiptTerminal(transData,printOut,self.props)

			writeLogString("RETRIV RETURN",str(result))
			writeLogDictionary("RETRIV RESPONSE DATA",transData)
			writeLogReceipt(printOut)

			return result
		else:
			return -1
	
	def Membership(self,payment_type,ecr_ref,option,amount,ciamID,transData,printOut):
		printOut.clear()

		writeLogString("MEMBER INPUT","TYPE:"+payment_type+"||"+"ECRREF:"+ecr_ref+"||"+"OPTION:"+option+"||"+"AMT:"+str(amount)+"||"+"ciamID:"+ciamID+"||")

		amount = inputAmountStringToLong(amount)

		writeLogString("MEMBER","CONVERTED AMT:"+str(amount))

		if payment_type is "EDC" or payment_type is "VAC":
			result = membershipTerminal(payment_type,ecr_ref,option,amount,ciamID,transData,printOut)

			writeLogString("MEMBER RETURN",str(result))
			writeLogDictionary("MEMBER RESPONSE DATA",transData)
			writeLogReceipt(printOut)

			return result
		elif payment_type is "OCT" or payment_type is "OCT_REWARDS":
			result = membershipOCT(transData,printOut)

			writeLogString("MEMBER RETURN",str(result))
			writeLogDictionary("MEMBER RESPONSE DATA",transData)
			writeLogReceipt(printOut)

			return result
		else:
			return -1

	def CardEnquiry(self,payment_type,option,transData,printOut):
		printOut.clear()

		writeLogString("CARD ENQ INPUT","TYPE:"+payment_type+"||"+"OPTION:"+option)

		if payment_type is "OCT" or payment_type is "OCT_REWARDS":
			result = polling(option,transData,2)

			writeLogString("CARD ENQ RETURN",str(result))
			writeLogDictionary("CARD ENQ RESPONSE DATA",transData)
			
			return result

	def QRCodeEnquiry(self,payment_type,option,qrCode,transData,printOut):

		writeLogString("QR ENQ INPUT","TYPE:"+payment_type+"||"+"OPTION:"+option +"||"+"QR:"+qrCode)

		result = checkTypeQR(qrCode,transData)

		writeLogString("QR ENQ RETURN",str(result))
		writeLogDictionary("QR ENQ RESPONSE DATA",transData)

		return result


	def TopUp(self,payment_type,ecr_ref,amount,transData,printOut):
		printOut.clear()

		writeLogString("TOPUP INPUT","TYPE:"+payment_type+"||"+"ECR REF:"+ecr_ref+"||"+"AMT:"+str(amount))

		if payment_type == "OCT" or payment_type == "OCT_REWARDS":
			result = topUp(ecr_ref,amount,transData)
			if result <100000:
				formatTransReceiptOctopus(transData,printOut,self.props,"DUMMY")

			writeLogString("TOPUP RETURN",str(result))
			writeLogDictionary("TOPUP RESPONSE DATA",transData)
			writeLogReceipt(printOut)

			return result
		else:
			return "ER"

	def Settlement(self,payment_type,batchesData,printOut):
		#printOut.clear()

		writeLogString("SETTLE INPUT","TYPE:"+payment_type)

		if payment_type is "OCT" or payment_type is "OCT_REWARDS":
			result = settleOCT()

			writeLogString("SETTLE RETURN",str(result))

			return result
		else:
			return "ER"

	def OpenEDCCom(self):
		model = 0
		if self.props["EdcModel"] == "PAX_S60":
			model = 2
		elif self.props["EdcModel"] == "SPECTRA_T300":
			model = 1
		else:
			model = 0
		result = openPortTerminal(self.props["EdcCom"],self.props["LogLocation"],model)

		writeLogString("OPEN EDC PORT RETURN",str(result))

		return result

	def CloseEDCCom(self):
		result = closePortTerminal()
		writeLogString("CLOSE EDC PORT RETURN",str(result))
		return result
	
	def OpenOCTCom(self):
		result = openOCTCom(self.props["OctCom"],self.props["OctOutletID"],self.props["OctPollTimeOut"])
		if result == 0:
			result = getDeviceInfo()
			self.props["OCTTID"] = result[1]
			self.props["OCTMID"] = result[2]

		writeLogString("OPEN OCT PORT RETURN",str(result))

		return result

	def CloseOCTCom(self):
		result = closeOCTCom()

		writeLogString("CLOSE OCT PORT RETURN",str(result))
		return result

	def InitTransportSubsidy(self):
		result = initSubsidy()

		writeLogString("INIT SUBSIDY RETURN",str(result))	

		return result
	
	def OctRetry(self, cmd, timeInterval,transData):
		result = 100001

		writeLogString("OCTRETRY INPUT","CMD:"+cmd+"||"+"TimeInterval:"+str(timeInterval))
		writeLogDictionary("OCTRETRY INPUT",transData)

		if "CMD" in transData:
			if transData["CMD"] == "TOPUP" and transData["AMT"] >0:
				result = topUpRetry(transData)
			elif transData["CMD"] == "TOPUP" and transData["AMT"] == 0:
				result = subsidyRetry(transData)
			else:
				result = RMS_Update(cmd,timeInterval,transData)

			writeLogString("OCTRETRY RETURN",str(result))
			writeLogDictionary("OCTRETRY RESPONSE DATA",transData)
			
		return result