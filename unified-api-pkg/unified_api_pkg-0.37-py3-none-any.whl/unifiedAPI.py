#Provide Unified API in here
from .qrcode import saleQR,voidSaleQR,refundQR,retrievalQR
from .terminal import openPortTerminal, closePortTerminal,saleTerminal,refundTerminal,voidSaleTerminal,retrievalTerminal,membershipTerminal
from .terminalUtils import formatTransReceiptTerminal
from .Octopus import openOCTCom,closeOCTCom,polling,getDeviceInfo,topUp,settleOCT,saleOCT,initSubsidy
from .OctopusUtils import formatTransReceiptOctopus
from .generalUtils import *


class UnifiedAPI():
	props = {}

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

	#Dictonary for transData,List for printOut
	def SaleQR(self,payment_type, qr_code, ecr_ref, amount, additional_amount,transData,printOut):
		printOut.clear()
		amount = inputAmountStringToLong(amount)
		result = saleQR(qr_code,ecr_ref,amount,transData,printOut)
		return result

	def Sale(self,payment_type,ecr_ref,amount,additional_amount,payment_option,transData,printOut):
		printOut.clear()

		amount = inputAmountStringToLong(amount)

		if payment_type == "EDC" or payment_type == "UPI" or payment_type == "EPS":
			result = saleTerminal(payment_type,ecr_ref,amount,additional_amount,payment_option,transData,printOut)
			formatTransReceiptTerminal(transData,printOut,self.props)
		elif payment_type == "OCT" or payment_type == "OCT_REWARDS":
			result = saleOCT(payment_type,ecr_ref,amount,additional_amount,payment_option,transData,printOut)
			if result < 100000:
				formatTransReceiptOctopus(transData,printOut,self.props,payment_option)
		return result

	def Void(self,payment_type,invoice,originalECRREF,transData,printOut):
		printOut.clear()
		if payment_type is "QR":
			result = voidSaleQR(invoice,transData,printOut)
			return result
		elif payment_type is "EDC" or payment_type is "UPI" or "VAC":
			result = voidSaleTerminal(payment_type,invoice,originalECRREF,transData,printOut)
			formatTransReceiptTerminal(transData,printOut,self.props)
			return result
		else:
			return -1
			
	def Refund(self,payment_type,ecr_ref,amount,originalTransRef,transData,printOut):
		printOut.clear()

		amount = inputAmountStringToLong(amount)

		if payment_type is "QR":
			result = refundQR(ecr_ref,amount,originalTransRef,transData,printOut)
			return result
		elif payment_type is "EDC":
			result = refundTerminal(payment_type,ecr_ref,amount,transData,printOut)
			formatTransReceiptTerminal(transData,printOut,self.props)
			return result
		else:
			return "PE"

	def Retrieval(self,payment_type,invoice,ecr_ref,transData,printOut):
		printOut.clear()
		if payment_type is "QR":
			result = retrievalQR(invoice,ecr_ref,transData,printOut)
			return result
		elif payment_type is "EDC" or payment_type is "EPS":
			result = retrievalTerminal(payment_type,invoice,transData,printOut)
			formatTransReceiptTerminal(transData,printOut,self.props)
			return result
		else:
			return -1
	
	def Membership(self,payment_type,ecr_ref,option,amount,ciamID,transData,printOut):
		printOut.clear()
		if payment_type is "EDC" or payment_type is "VAC":
			result = membershipTerminal(payment_type,ecr_ref,option,amount,ciamID,transData,printOut)
			return result
		else:
			return -1

	def CardEnquiry(self,payment_type,option,transData,printOut):
		printOut.clear()
		if payment_type is "OCT" or payment_type is "OCT_REWARDS":
			return polling(option,transData,2)

	def QRCodeEnquiry(self,payment_type,option,qrCode,transData,printOut):
		return "0"

	def TopUp(self,payment_type,ecr_ref,amount,payment_option,transData,printOut):
		printOut.clear()
		if payment_type == "OCT" or payment_type == "OCT_REWARDS":
			result = topUp(ecr_ref,amount,transData)
			if result <100000:
				formatTransReceiptOctopus(transData,printOut,self.props,"DUMMY")
			return result
		else:
			return "ER"

	def Settlement(self,payment_type,batchesData,printOut):
		#printOut.clear()
		if payment_type is "OCT" or payment_type is "OCT_REWARDS":
			return settleOCT()
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
		return result

	def CloseEDCCom(self):
		result = closePortTerminal()
		return result
	
	def OpenOCTCom(self):
		result = openOCTCom(self.props["OctCom"],self.props["OctOutletID"],self.props["OctPollTimeOut"])
		if result == 0:
			result = getDeviceInfo()
			self.props["OCTTID"] = result[1]
			self.props["OCTMID"] = result[2]
		return result

	def CloseOCTCom(self):
		result = closeOCTCom()
		return result

	def InitTransportSubsidy(self):
		result = initSubsidy()
		return result