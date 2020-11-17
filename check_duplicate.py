import os
from google_sheet import Google_sheet
from passwords import  privacy
import sys


Test = False
workbook_name = ''
res_col = 6
email_col = 2 
vital_info = 0



    







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
                if first_email == second_emial and first_email != '':
                    sheet.fill_row(j+1,res_col,'duplicate')
                    number += 1 
    print(number)
    print('Done for sheet -> %d!'%sheet_index)









if __name__ == "__main__":

    print('Start')



    if len(sys.argv) > 1:
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-t':
                Test = True
                print('in test mode')

            elif sys.argv[i] == '--sheet-number':
                sheet_number = int(sys.argv[i+1])
                vital_info += 1
                print('there is %d sheet'%sheet_number)
            
            elif sys.argv[i] == '--sheet-name':
                workbook_name = str(sys.argv[i+1])
                vital_info += 1
                print('the sheet name is %s'%workbook_name)

            elif sys.argv[i] == '--email-col':
                email_col = int(sys.argv[i+1])
                print('email column changed to -> %d'%email_col)
            
            elif sys.argv[i] == '--res-col':
                res_col = int(sys.argv[i+1])
                print('result column change to -> %d'%res_col)

            else:
                raise NameError('unkown command %s'%sys.argv[i])


    if vital_info < 2:
        raise NameError('please pass the vital args')


    if Test:
        workbook_name = 'PythonTest'

    base_dir = os.path.dirname(os.path.realpath(__file__))

    _privacy = privacy()


    if Test:
        check_duplicate(0)
    else:
        for i in range(sheet_number):
            check_duplicate(i)

        