import json

class GetDictAllPaths:

	def __init__(self):
		pass



	def __chkDupPath(self,subKey,allKeys):
		chk=True
		keyPath="-"
		keyPath=keyPath.join(subKey)

		try:
			index=allKeys.index(keyPath)
		except:
			chk=False
		return chk


	def __chkPath(self,subKey,elem):

		chkDictPath=[subKey,True]
		for y in subKey:
			if (y.find('[') != -1): # To split subkey dct[k[0]] >> dct[k][0]
				start=y.find('[')
				end=y.find(']')
				index=int(y[start+1:end])
				tmpKey=y[:start]

				try:
					elem = elem[tmpKey][index]
				except:
					subKey.pop()
					subKey.pop()
					chkDictPath[0]=subKey
					chkDictPath[1]=False
					break
			else:
				try:
					elem = elem[y]
				except:
					subKey.pop()
					subKey.pop()
					chkDictPath[0]=subKey
					chkDictPath[1]=False 
					break
					
		return chkDictPath


	def __NextPath(self,subKey,key,dataDict):  # Check Next Path is correct?
		elem=dataDict
		if len(subKey)>0:
			subKey.pop()

		subKey.append(key)
		for i in range(len(subKey)):
			chkJsonPath=self.__chkPath(subKey,elem)
			if chkJsonPath[1] == True:
				break
			subKey=chkJsonPath[0]
			subKey.append(key)
		return subKey


	def __recursive_dict(self,dataDict):

		for key, value in dataDict.items():

			if type(value) is dict:
				yield (key, value)
				yield from self.__recursive_dict(value)
			elif type(value) is list:
				index=0
				for item in value:
					tmpKey=key + "[" + str(index) + "]"
					yield (tmpKey,item)
					if type(item) is dict:
						yield from self.__recursive_dict(item)
					index+=1
			else:
				yield (key, value)


	def __setFormatRobotPath(self,keyPath):
		keyPath=keyPath.replace("[",",[")
		pathList=keyPath.split(",")
		robotDictPath=""
		for item in pathList:
			if (item.find("[") == -1):  # If it not List
				robotDictPath=robotDictPath + "['" + item + "']"
			else:
				robotDictPath=robotDictPath + item
		return robotDictPath



	def getDictPaths(self,dataDict):
		'''
		This is function that get keys from dictionary type.
		Return all paths of the given dictionary as a list.
		'''
		allKeys=[]
		subKey=[]
		endPath=False
		preValue="<class 'dict'>"
		for key, value in self.__recursive_dict(dataDict):
			if type(value) in [dict]:
				if preValue == "<class 'dict'>":
					subKey.append(key)
				subKey=self.__NextPath(subKey,key,dataDict)
			elif type(value) in [list]:
				subKey=self.__NextPath(subKey,key,dataDict)
			else:
				subKey.append(key)
				for i in range(len(subKey)):
					chkPoint=self.__chkPath(subKey,dataDict,)
					if chkPoint[1] == True:
						if self.__chkDupPath(chkPoint[0],allKeys) == False:
							break
						else:
							chkPoint[0].pop()
							chkPoint[0].pop()				
					subKey=chkPoint[0]
					subKey.append(key)

				mySeparator=","
				keyPath=mySeparator.join(subKey)
				jsonPath=self.__setFormatRobotPath(keyPath)
				allKeys.append(jsonPath)
				endPath=True 

			preValue=str(type(value))

		return allKeys

	def __str__(self):
		return "This is a function that gets the keys of all values ​​in the dictionary."


if __name__ == '__main__':

	json_string='''
	{
	  	"SuperMarket": {
		    "Fruit": [
		      {
		        "Name": "Apple",
		        "Manufactured":"USA",
		        "price": 7.99
		      },
		      {
		        "Name": "Banana",
		        "Manufactured":"Japan",
		        "price": 3.99
		      }
		    ],
		    "Drink": {
				"SoftDrink":{
					"Cola": [
				      	{
				      		"Color":"Red",
				      		"Price":15.00
				      	},
				      	{
				      		"Color":"Green",
				      		"Price":17.99
				      	}
				      ],      
				      "Coffee": {
				      	"Hot":[
					      	{
					      		"Type":"Espresso",
					      		"Price":15.90
					      	},
					      	{
					      		"Type":"Cappuccino",
					      		"Price":10.90
					      	}
					    ],
					    "Ice":[
					      	{
					      		"Type":"Espresso",
					      		"Price":20.90
					      	},
					      	{
					      		"Type":"Cappuccino",
					      		"Price":15.90
					      	}
					    ]
				    }
				}     
		    }
	  	}
	}
	'''

	dictData=json.loads(json_string)
	print(dictData)
	dictKeys=GetDictAllPaths()
	keyList=dictKeys.getDictPaths(dictData)
	for item in keyList:
		print(item)
