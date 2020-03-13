import json
class ConvertJsonToDict(object):

	def __init__(self):
		pass



	import json

	def convert_json_to_dictionary(self,json_string):
		'''
		Convert from Json To Dictionary.
		'''
		dictData = json.loads(json_string)
		return dictData


	def __str__(self):
		return "This is a function that converts json to dictionary."


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



	jsonString=ConvertJsonToDict()
	dataDict=jsonString.convert_json_to_dictionary(json_string)
	print(dataDict["SuperMarket"])
