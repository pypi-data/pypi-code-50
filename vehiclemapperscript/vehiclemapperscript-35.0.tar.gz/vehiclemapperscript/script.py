import pandas as pd
from fuzzywuzzy import process  
from pprint import pprint
import re
class script:
    def __init__(self):
        pass

    def remove_special(self,string):
        return re.sub('[^a-zA-Z.\d\s]', '', string)    

    def to_lower(self,input):
        return list(map(lambda x: x.lower(), [str(i) for i in input]))
        
    def get_structure(self,make,model,variant,fuel,code):       
        print("started creating the dict structure.....")                    
        mapped_dict = {}                    
        for i in range (0,len(make)):
            if make[i] in mapped_dict:
                if model[i] in mapped_dict[make[i]]:
                    if variant[i] in mapped_dict[make[i]][model[i]]:
                        if fuel[i] in mapped_dict[make[i]][model[i]][variant[i]]:
                            mapped_dict[make[i]][model[i]][ variant[i]][fuel[i]] = code[i]  
                        else:
                            mapped_dict[make[i]][model[i]][ variant[i]][fuel[i]] = code[i]  
                    else:
                        mapped_dict[make[i]][model[i]][variant[i]] = {}
                        mapped_dict[make[i]][model[i]][variant[i]][fuel[i]] = code[i]  

            
                else:
                    mapped_dict[make[i]][model[i]] = {} 
                    mapped_dict[make[i]][model[i]][variant[i]] = {} 
                    mapped_dict[make[i]][model[i]][variant[i]][fuel[i]] = code[i]  
                    
            else:
                mapped_dict[make[i]] = {}
                mapped_dict[make[i]][model[i]] = {}
                mapped_dict[make[i]][model[i]][variant[i]] = {}
                mapped_dict[make[i]][model[i]][variant[i]][fuel[i]]=code[i]   

        return mapped_dict   


    # sheet = pandas_excel.parse(0)
    # digit_make = to_lower(sheet['Make'])
    # digit_model = to_lower(sheet['Model'])
    # digit_variant = to_lower(sheet['Variant - Updated'])
    # digit_fuel = to_lower(sheet['FuelType'])
    # digit_code = to_lower(sheet['Vehicle Code'])

    # sheet_hdfc = pandas_excel.parse(1)
    # hdfc_make = to_lower(sheet_hdfc['MANUFACTURER'])
    # hdfc_model = to_lower(sheet_hdfc['VEHICLEMODEL'])
    # hdfc_variant = to_lower(sheet_hdfc['Variant - Updated'])
    # hdfc_fuel = to_lower(sheet_hdfc['TXT_FUEL'])
    # hdfc_code = to_lower(sheet_hdfc['VEHICLEMODELCODE'])
    def start(self):
        base_sheet_name = input("Enter base sheet name ")
        comp_sheet_name = input("Enter Comparing sheet name ")
        sheet_path = input("Enter sheet full path ")
        base_sheet_index = int(input("Enter base sheet index "))
        comparing_sheet = int(input("Enter index of sheet to be compared "))
        base_sheet_make = input("Enter base sheet make ") 
        base_sheet_model = input("Enter base sheet model ")
        base_sheet_variant = input("Enter base sheet variant ")
        base_sheet_fuel = input("Enter base sheet fuel type ")
        base_sheet_code = input("Enter base sheet vehicle code")

        comp_sheet_make = input("Enter comparing sheet make ")
        comp_sheet_model =  input("Enter comparing sheet model ")
        comp_sheet_variant = input("Enter comparing sheet variant ")
        comp_sheet_fuel = input("Enter comparing sheet fuel type ")
        comp_sheet_code = input("Enter comparing sheet vehile code ")

        # pandas_excel = pd.ExcelFile('/Users/yadu/Downloads/labeled_sheet.xlsx')
        pandas_excel = pd.ExcelFile(sheet_path)

        sheet = pandas_excel.parse(base_sheet_index)
        digit_make = self.to_lower(sheet[base_sheet_make])
        digit_model = self.to_lower(sheet[base_sheet_model])
        digit_variant = self.to_lower(sheet[base_sheet_variant])
        digit_fuel = self.to_lower(sheet[base_sheet_fuel])
        digit_code = self.to_lower(sheet[base_sheet_code])

        sheet_hdfc = pandas_excel.parse(comparing_sheet)
        hdfc_make = self.to_lower(sheet_hdfc[comp_sheet_make])
        hdfc_model = self.to_lower(sheet_hdfc[comp_sheet_model])
        hdfc_variant = self.to_lower(sheet_hdfc[comp_sheet_variant])
        hdfc_fuel = self.to_lower(sheet_hdfc[comp_sheet_fuel])
        hdfc_code = self.to_lower(sheet_hdfc[comp_sheet_code])



        ############### REMOVE THIS LINE ###############
        hdfc_variant = [self.remove_special(i) for i in hdfc_variant]
        digit_variant = [self.remove_special(i) for i in digit_variant]
        ################################################

        hdfc_struct = self.get_structure(hdfc_make,hdfc_model,hdfc_variant,hdfc_fuel,hdfc_code)
        digit_struct = self.get_structure(digit_make,digit_model,digit_variant,digit_fuel,digit_code)
        # pprint(hdfc_struct)


        model_match = 100
        variant_match = 98


        ###################
        # Make and model has filtered, by removing special characters.
        ###################
        final_dict = {}
        final_dict_re = {}
        for i in digit_struct:
            if i in hdfc_struct:
                print("Make found")
                digit_models = digit_struct[i]
                for j in digit_models:
                    # hdfc_keys_models = [k.replace(i,"") for k in hdfc_struct[i].keys()]
                    match = process.extractOne(j.replace(i,""), hdfc_struct[i].keys())
                    if match[1]>=model_match:
                        print("Model found")
                        digit_variant = digit_struct[i][j]
                        for k in digit_variant:
                            # model = match[0]
                            match1 = process.extractOne(k, hdfc_struct[i][match[0]].keys())
                            if match1[1]>variant_match:
                                print("Variant match found")
                                digit_fuels = digit_struct[i][j][k]
                                for m in digit_fuels:
                                    match2 = process.extractOne(m, hdfc_struct[i][match[0]][match1[0]].keys())
                                    if match2[1]>=95:
                                        print("Fuel type found   ",match2)
                                        final_dict[digit_struct[i][j][k][m]] =  hdfc_struct[i][match[0]][match1[0]][match2[0]]
                                        final_dict_re[hdfc_struct[i][match[0]][match1[0]][match2[0]]] = digit_struct[i][j][k][m]

        super_list = []
        for i in digit_code:
            if i in final_dict:
                super_list.append(final_dict[i])
            else:
                super_list.append("No values")      

        super_list_2 = []
        for j in hdfc_code:
            if j in final_dict_re:
                super_list_2.append(final_dict_re[j])
            else:
                super_list_2.append("No values") 

        sheet["SCRIPT OUT"] = super_list
        sheet_hdfc["SCRIPT OUT"] = super_list_2
        writer = pd.ExcelWriter(sheet_path, engine='xlsxwriter')

        # Convert the dataframe to an XlsxWriter Excel object.
        sheet.to_excel(writer,sheet_name=base_sheet_name)
        sheet_hdfc.to_excel(writer,sheet_name=comp_sheet_name)
        names = pandas_excel.sheet_names
        names.remove(base_sheet_name)
        names.remove(comp_sheet_name)
        for i in names:
            sheet_oth = pandas_excel.parse(i)
            sheet_oth.to_excel(writer,sheet_name=i)

        # pandas_excel.parse(base_sheet_index)


        # Close the Pandas Excel writer and output the Excel file.
        writer.save()
        writer.close()



    # print(final_dict.keys())
    # print(final_dict.values())
                                    

                    
