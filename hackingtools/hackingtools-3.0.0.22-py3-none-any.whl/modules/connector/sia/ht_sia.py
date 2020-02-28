from hackingtools.core import Logger, Utils, Config
if Utils.amIdjango(__name__):
	from .library.core import hackingtools as ht
else:
	import hackingtools as ht
import os
from pysia import Sia

config = Config.getConfig(parentKey='modules', key='ht_sia')
output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'output'))

class StartModule():

	class Daemon():

		def __init__(self, siaParent):
			self.siaParent = siaParent

		def getConstants(self):
			self.siaParent.get_daemon_constants()

		def stop(self):
			return self.siaParent.get_daemon_stop()

		def getVersion(self):
			return self.siaParent.get_daemon_version()

	class Consensus():

		def __init__(self, siaParent):
			self.siaParent = siaParent

		def getConsensus(self):
			return self.siaParent.get_consensus()

	class Renter():

		def __init__(self, siaParent):
			self.siaParent = siaParent

		def getRenter(self):
			return self.siaParent.get_renter()

		def getRenterContracts(self):
			return self.siaParent.get_renter_contracts()

		def getRenterDownloads(self):
			return self.siaParent.get_renter_downloads()

		def getRenterFiles(self):
			return self.siaParent.get_renter_files()

		def getRenterPrices(self):
			return self.siaParent.get_renter_prices()

	class Wallet():

		def __init__(self, siaParent):
			self.siaParent = siaParent

		def getWalletTransactions(self):
			return self.siaParent.get_wallet_transactions()

		def getWalletSeeds(self):
			return self.siaParent.get_wallet_seeds()

		def getWalletBackup(self):
			return self.siaParent.get_wallet_backup()

		def getWallet(self):
			return self.siaParent.get_wallet()

		def getWalletAddress(self):
			return self.siaParent.get_wallet_address()

		def getWalletAddresses(self):
			return self.siaParent.get_wallet_addresses()
	
	class Miner():

		def __init__(self, siaParent):
			self.siaParent = siaParent

		def getMiner(self):
			return self.siaParent.get_miner()

		def getMinerHeader(self):
			return self.siaParent.get_miner_header()

		def getMinerStart(self):
			return self.siaParent.get_miner_start()

		def getMinerStop(self):
			return self.siaParent.get_miner_stop()

	def __init__(self):
		self._main_gui_func_ = ''
		self.sc = None
		self.daemon = None
		self.consensus = None
		self.renter = None
		self.wallet = None
		self.miner = None

	def help(self):
		Logger.printMessage(message=ht.getFunctionsNamesFromModule('ht_sia'), debug_module=True)

	def getDaemonConstants(self):
		self.__startSIA__()
		return self.Daemon( self.sc ).getConstants()

	def getDaemonVersion(self):
		self.__startSIA__()
		return self.Daemon( self.sc ).getVersion()

	def getConsensus(self):
		self.__startSIA__()
		return self.Consensus( self.sc ).getConsensus()

	def getRenter(self):
		self.__startSIA__()
		return self.Renter( self.sc ).getRenter()

	def getRenterContracts(self):
		self.__startSIA__()
		return self.Renter( self.sc ).getRenterContracts()

	def getRenterDownloads(self):
		self.__startSIA__()
		return self.Renter( self.sc ).getRenterDownloads()

	def getRenterFiles(self):
		self.__startSIA__()
		return self.Renter( self.sc ).getRenterFiles()

	def getRenterPrices(self):
		self.__startSIA__()
		return self.Renter( self.sc ).getRenterPrices()

	def getWalletTransactions(self):
		self.__startSIA__()
		return self.Wallet( self.sc ).getWalletTransactions()

	def getWalletSeeds(self):
		self.__startSIA__()
		return self.Wallet( self.sc ).getWalletSeeds()

	def getWalletBackup(self):
		self.__startSIA__()
		return self.Wallet( self.sc ).getWalletBackup()

	def getWallet(self):
		self.__startSIA__()
		return self.Wallet( self.sc ).getWallet()

	def getWalletAddress(self):
		self.__startSIA__()
		return self.Wallet( self.sc ).getWalletAddress()

	def getWalletAddresses(self):
		self.__startSIA__()
		return self.Wallet( self.sc ).getWalletAddresses()

	def __startSIA__(self):
		if not self.sc:
			try:
				self.sc = Sia()
			except:
				return None
		return self.sc

