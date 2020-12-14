import os
import time
import schedule
from datetime import date
from gmail_server import Gmail_server
from google_sheet import Google_sheet
from passwords import  privacy
from xxx_template import template
import sys


Test = False
sheet_number = 1
mail_sender_time = []
workbook_name = ''
mail_each_day = 100
log_col = 3
prof_name_col = 1
email_col = 2 
paper_col = 0
vital_info = 0












def mail_composer(sheet_index):
    print('starting the emails in sheet -> %d'%sheet_index)
    old_time = time.time()
    sheet = Google_sheet(_privacy.jason_cret_filename(),workbook_name,sheet_index,base_dir)
    profs_name,emails,papers,new_mail_start_row = sheet.get_new_rows(log_col,prof_name_col,email_col,mail_each_day,paper_col)
    gmail = Gmail_server(_privacy.my_email(),_privacy.my_email_app_pass())
    today = date.today()
    print('sending the mails ...')
    for row,(name,prof_email,paper) in enumerate(zip(profs_name,emails,papers)):
        if name == '':
            result = False
        else:
            result = gmail.send_email(prof_email,_template.my_template_subject(sheet_index),_template.my_template_body(name,paper,sheet_index),base_dir,_template.cv_file_name())
        if result: data = today.strftime("%m/%d/%Y")
        else: data = '!Fail!' 
        sheet.fill_row(( new_mail_start_row + row + 1 ),log_col,data)
    gmail.close_email_server()
    print('Done today for sheet -> %d!'%sheet_index)
    print('Time elapsed -> %d minute(s)'%((time.time()-old_time)/60))









if __name__ == "__main__":

    print('Start')


    if len(sys.argv) > 1:
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-t':
                Test = True
                print('in test mode')
                
            if sys.argv[i] == '--sheet-number':
                sheet_number = int(sys.argv[i+1])
                vital_info += 1
                print('there is %d sheet'%sheet_number)
            
            if sys.argv[i] == '--email-time':
                mail_sender_time = str(sys.argv[i+1]).split(',')
                vital_info += 1
                for i,_time in enumerate(mail_sender_time): 
                    print('send email in sheet %d at %s'%(i,_time)) 

            if sys.argv[i] == '--workbook-name':
                workbook_name = str(sys.argv[i+1])
                vital_info += 1
                print('the sheet name is %s'%workbook_name)

            if sys.argv[i] == '--email-number':
                mail_each_day = int(sys.argv[i+1])
                print('sending %d email each day'%mail_each_day)
            
            if sys.argv[i] == '--email-col':
                email_col = int(sys.argv[i+1])
                print('email column changed to -> %d'%email_col)
            
            if sys.argv[i] == '--prof-col':
                prof_name_col = int(sys.argv[i+1])
                print('professor name column changed to -> %d'%prof_name_col)
            
            if sys.argv[i] == '--log-col':
                log_col = int(sys.argv[i+1])
                print('log column change to -> %d'%log_col)
                
            if sys.argv[i] == '--paper-col':
                paper_col = int(sys.argv[i+1])
                print('paper mode enabled!')
                print('paper column is -> %d'%paper_col)


    if vital_info < 3:
        raise NameError('please pass the vital args')

    if Test:
        workbook_name = 'PythonTest'
        mail_each_day = 10

    base_dir = os.path.dirname(os.path.realpath(__file__))

    _privacy = privacy()
    _template = template()


    if Test:
        schedule.every(1).minutes.do(mail_composer,0)
    else:

        for i in range(sheet_number):
            schedule.every().monday.at(mail_sender_time[i]).do(mail_composer,i)
            schedule.every().tuesday.at(mail_sender_time[i]).do(mail_composer,i)
            schedule.every().wednesday.at(mail_sender_time[i]).do(mail_composer,i)
            schedule.every().thursday.at(mail_sender_time[i]).do(mail_composer,i)
            schedule.every().friday.at(mail_sender_time[i]).do(mail_composer,i)
            
    while True:
        schedule.run_pending()
        time.sleep(1)
        