import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
import os

class Google_sheet:
    def __init__(self,jason_cret_filename,workbook_name,sheet_index,base_dir):
        while True:
            try:
                scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
                creds = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(base_dir,jason_cret_filename), scope)
                client = gspread.authorize(creds)
                sheet = client.open(workbook_name)
                self.sheet_instance = sheet.get_worksheet(sheet_index)
                break
            except Exception as e:
                print('error in sheet connection')
                print(e)
                time.sleep(150)




    def get_col(self,col):
        while True:
            try:
                _list = self.sheet_instance.col_values(col)
                print('list read -> ok')
                break
            except:
                print('list read -> fail')
                print('list read -> retry')
                time.sleep(150)
        return _list


    def get_new_rows(self,my_col,profs_name_col,emails_col,mail_each_day,paper_col = 0):
        
        while True:
            try:
                all_mail_sent_date_list = self.sheet_instance.col_values(my_col)
                print('mail sent date list read -> ok')
                break
            except:
                print('mail sent date list read -> fail')
                print('mail sent date list read -> retry')
                time.sleep(150)

        while True:
            try:
                all_profs_name_list = self.sheet_instance.col_values(profs_name_col)
                print('profs name list read -> ok')
                break
            except:
                print('profs name list read -> fail')
                print('profs name list read -> retry')
                time.sleep(150)
                        

        while True:
            try:
                all_email_list = self.sheet_instance.col_values(emails_col)
                print('emails list read -> ok')
                break
            except:
                print('emails list read -> fail')
                print('emails list read -> retry')
                time.sleep(150)

        if paper_col:
            while True:
                try:
                    all_paper_list = self.sheet_instance.col_values(paper_col)
                    print('papers list read -> ok')
                    break
                except:
                    print('papers list read -> fail')
                    print('papers list read -> retry')
                    time.sleep(150)

        all_profs_name_list,all_email_list,all_paper_list = self.check_cols_lenght(all_profs_name_list,all_email_list,all_paper_list)
        new_mail_start_cell = len(all_mail_sent_date_list)
        new_profs_name = []
        new_emails = [] 
        new_papers = []
        if new_mail_start_cell + mail_each_day >= len(all_profs_name_list):
            for i in range(new_mail_start_cell, len(all_profs_name_list)):
                    new_profs_name.append(all_profs_name_list[i])
                    new_emails.append(all_email_list[i])
                    if paper_col: 
                            new_papers.append(all_paper_list[i])
        else:
            for i in range(new_mail_start_cell, new_mail_start_cell + mail_each_day):
                    # if all_profs_name_list[i] != '':
                    new_profs_name.append(all_profs_name_list[i])
                    new_emails.append(all_email_list[i])
                    if paper_col: 
                            new_papers.append(all_paper_list[i])

        return new_profs_name,new_emails,new_papers,new_mail_start_cell
        

    def fill_row(self,row,my_col,data):
        while True:
            try:
                self.sheet_instance.update_cell(row, my_col, data)
                print('row %d fill -> ok'%(row))
                break
            except Exception as e:
                print('row %d fill -> fail'%(row))
                print(e)
                print('row %d fill -> retry'%(row))
                time.sleep(150)  


    def check_cols_lenght(self,_profs_name,_emails,_papers):
        len_list = [len(_profs_name),len(_emails),len(_papers)]
        if len_list[0] == len_list[1] == len_list[2]:
            return _profs_name,_emails,_papers
        else: 
            for index,number in enumerate(len_list):
                if number == max(len_list):
                    continue
                else: 
                    for i in range(max(len_list) - number):
                        if   index == 0 : _profs_name.append('')
                        elif index == 1 : _emails.append('')
                        elif index == 2 : _papers.append('')

            return _profs_name,_emails,_papers