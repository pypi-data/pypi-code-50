

import os
import typing
import tarfile

import jk_simpleexec
import jk_utils
import mysql.connector

from .EnumTarPathMode import EnumTarPathMode
from .ThaniyaService import ThaniyaService
from .ThaniyaBackupContext import ThaniyaBackupContext
from .utils.temp import writeTempFile





class ThaniyaMySQL:

	@staticmethod
	def mySQLDump(ctx:ThaniyaBackupContext, dbName:str, dbUserName:str, dbPassword:str, outputDumpFilePath:str) -> int:

		assert isinstance(ctx, ThaniyaBackupContext)
		assert isinstance(dbName, str)
		assert dbName
		assert isinstance(outputDumpFilePath, str)
		assert outputDumpFilePath

		ctx = ctx.descend("Creating dump file " + repr(outputDumpFilePath) + " ...")
		authFile = None
		try:
			with ctx.log as nestedLog:
				outputDumpFilePath = ctx.absPath(outputDumpFilePath)

				authFile = writeTempFile("rw-------", "[mysqldump]\nuser=" + dbUserName + "\npassword=" + dbPassword + "\n")
				result = jk_simpleexec.invokeCmd("/usr/bin/mysqldump", [
					"--defaults-extra-file=" + authFile,
					"--r",
					outputDumpFilePath,
					"--routines",				# Include stored routines (procedures and functions) for the dumped databases in the output.
					"--triggers",				# Include triggers for each dumped table in the output.
					dbName,
				], workingDirectory=os.path.dirname(authFile))

				if result.returnCode == 0:
					nestedLog.notice("Succeeded.")
					return os.path.getsize(outputDumpFilePath)
				else:
					result.dump(nestedLog.error)
					raise Exception("Failed to backup database '" + dbName + "'!")

		finally:
			if authFile and os.path.isfile(authFile):
				os.unlink(authFile)
	#

	@staticmethod
	def mySQLDumpCalculateSize(ctx:ThaniyaBackupContext, dbName:str, dbUserName:str, dbPassword:str) -> int:

		assert isinstance(ctx, ThaniyaBackupContext)

		ctx = ctx.descend("Calculating size for the MySQL dump ...")
		with ctx.log as nestedLog:

			con = None
			try:
				# Segmentation fault
				# see: https://bugs.mysql.com/bug.php?id=89889
				#	(but this does not work)
				print("> Connecting ....")
				con = mysql.connector.connect(host="localhost", database=dbName, user=dbUserName, passwd=dbPassword)
				print("> Connected.")

				sqlQuery = "SELECT SUM(data_length) FROM information_schema.tables WHERE table_schema = '" + dbName + "';"

				cursor = con.cursor()
				cursor.execute(sqlQuery)
				records = cursor.fetchall()
				assert cursor.rowcount == 1

				nEstimatedSize = -1
				for row in records:
					nEstimatedSize = row[0]
					break

				return nEstimatedSize

			finally:
				if con and con.is_connected():
					cursor.close()
					con.close()
	#

#


























