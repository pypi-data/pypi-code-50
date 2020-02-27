import os_translator_xlsx.ToXlsxTranslator as excelTranslator

excelTranslator.translate_to_excel('/Users/home/Programming/Python/modules/general/os_translator/os_translator/excel.xlsx',
                                   "/Users/home/Programming/service_keys/remotes-firebase_service_account.json",
                                   "remotes-7c523",
                                   'en-US',
                                   ["what is the first thing", "what is the second thing"],
                                   ['zu'])
