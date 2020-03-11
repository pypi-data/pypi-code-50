
def check_if_string_in_file(file_name, string_to_search):
	""" Check if any line in the file contains given string """
	# Open the file in read only mode
	with open(file_name, 'r') as read_obj:
		# Read all lines in the file one by one
		for line in read_obj:
			# For each line, check if line contains the string
			if str(string_to_search) in line:
				return line
		read_obj.close()
	return "Not found"

def SearchStringThroughData(File, Filter, ToSearch):
	return check_if_string_in_file(File, ToSearch.capitalize())

def SearchIntThroughData(File, Filter, ToSearch):
	return check_if_string_in_file(File, ToSearch)

def AddData(File, Name, UID, Age, IsCool):
	while Age.isdigit() == False:
		return "Age can only contain numbers. Spaces, letters, special characters or decimals are not allowed."
	if Age.isdigit() == True:
		Age = int(Age)
	while UID.isdigit() == False:
		return "UID can only contain numbers. Spaces, letters, special characters or decimals are not allowed."
	if UID.isdigit() == True:
		UID = int(UID)
	while IsCool.lower() == "true" or "false":
		break
	else:
		return "IsCool has to be a boolean. Please enter a boolean."
	while type(Age) != int:
		return "Age has to be an integer. Please enter an integer."
	while type(UID) != int:
		return "UID has to be an integer number. Please enter an integer."
	DataBase = {}
	DataBase[Name.lower()] = dict(UIC=UID,Age=Age,IsCool=IsCool.capitalize(),Name=Name.capitalize())
	File = open(File, "a")
	File.write(str(DataBase.get(Name.lower())))
	File.close()
