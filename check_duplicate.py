import os
from google_sheet import Google_sheet
from passwords import  privacy
import sys


Test = False

if len(sys.argv) > 1:
    for arg in sys.argv:
        if arg == '-t':
            Test = True
            print('in test mode')






if Test:
    workbook_name = 'PythonTest'
else:
    workbook_name = 'Python_Apply_2021'

US_sheet_index = 0
CA_sheet_index = 1
res_col = 6
email_col = 2 
    







def check_duplicate(sheet_index):
    print('starting to check emails duplicate in sheet -> %d'%sheet_index)
    sheet = Google_sheet(_privacy.jason_cret_filename(),workbook_name,sheet_index,base_dir)
    email_list = sheet.get_col(email_col)
    number = 0
    for i,first_email in enumerate(email_list):
        for j,second_emial in  enumerate(email_list):
            if i == j:
                break
            else:
                if first_email == second_emial:
                    sheet.fill_row(j+1,res_col,'duplicate')
                    number += 1 
    print(number)
    print('Done for sheet -> %d!'%sheet_index)









if __name__ == "__main__":

    print('Start')

    base_dir = os.path.dirname(os.path.realpath(__file__))

    _privacy = privacy()


    if Test:
        check_duplicate(0)
    else:
        check_duplicate(US_sheet_index)
        check_duplicate(CA_sheet_index)

        