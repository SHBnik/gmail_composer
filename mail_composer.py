import os
import time
import schedule
from datetime import date
from gmail_server import Gmail_server
from google_sheet import Google_sheet
from passwords import  privacy
from shahab_template import template







Test = True


if Test:
    workbook_name = 'PythonTest'
    mail_each_day = 150
else:
    workbook_name = 'Python_Apply_2021'
    mail_each_day = 150

sheet_index = 0
my_col = 3
prof_name_col = 1
email_col = 2 
    

mail_sender_time = '18:30' # tehran_timezone









def mail_composer():
    old_time = time.time()
    sheet = Google_sheet(_privacy.jason_cret_filename(),workbook_name,sheet_index,base_dir)
    profs_name,emails,new_mail_start_row = sheet.get_new_rows(my_col,prof_name_col,email_col,mail_each_day)
    gmail = Gmail_server(_privacy.my_email(),_privacy.my_email_app_pass())
    today = date.today()
    for name,prof_email in zip(profs_name,emails):
        gmail.send_email(prof_email,_template.my_template_subject(),_template.my_template_body(name),base_dir,_template.cv_file_name())
    sheet.fill_rows(new_mail_start_row,len(profs_name),my_col,today.strftime("%d/%m/%Y"))
    gmail.close_email_server()
    print('Done today !')
    print('Time elapsed -> %d minute(s)'%((time.time()-old_time)/60))









if __name__ == "__main__":

    print('Start')
    print('waiting for %s oclock'%mail_sender_time)

    base_dir = os.path.dirname(os.path.realpath(__file__))

    _privacy = privacy()
    _template = template()


    if Test:
        schedule.every(1).minutes.do(mail_composer)
    else:
        schedule.every().monday.at(mail_sender_time).do(mail_composer)
        schedule.every().tuesday.at(mail_sender_time).do(mail_composer)
        schedule.every().wednesday.at(mail_sender_time).do(mail_composer)
        schedule.every().thursday.at(mail_sender_time).do(mail_composer)
        schedule.every().friday.at(mail_sender_time).do(mail_composer)

    while True:
        schedule.run_pending()
        time.sleep(1)
        