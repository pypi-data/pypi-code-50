import xlsxwriter
import os_translator.Translator as translator


###########################################################################
# this module aim is to translate a string to a desired languages and save
# the output in a nice excel file
###########################################################################

def translate_to_excel(excel_file_path,
                       service_account_json_path,
                       project_id,
                       language_initials_src,
                       text_list,
                       language_initials_list):
    # open excel file
    workbook = xlsxwriter.Workbook(excel_file_path)
    worksheet = workbook.add_worksheet()

    # Widen the first column to make the text clearer.
    worksheet.set_column('A:A', 20)

    # Write some simple text.
    worksheet.write('A1', language_initials_src)

    # run on all of the sentences
    for sentenceIdx in range(len(text_list)):
        worksheet.write('A' + str((sentenceIdx + 2)), text_list[sentenceIdx])
        curr_letter = 66
        times = 1

        # run on all of the languages
        for langIdx in range(len(language_initials_list)):

            # if letter overlapped
            if curr_letter == 91:
                curr_letter = 66
                times += 1

            worksheet.write((chr(curr_letter) * times) + '1', language_initials_list[langIdx])
            translation = translator.translate_text(text_list[sentenceIdx],
                                                    service_account_json_path,
                                                    project_id,
                                                    language_initials_list[langIdx],
                                                    language_initials_src)

            if isinstance(translation, Exception):
                curr_letter += 1
                print('Error with ' + language_initials_list[langIdx] + ": " + str(translation))
                print("skipping!")
                continue
            else:
                worksheet.write(chr(curr_letter) + str(sentenceIdx + 2), translation)
                curr_letter += 1

    workbook.close()
