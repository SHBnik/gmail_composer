# gmail_composer
This is a python app to read a list of emails from google sheets and send emails to them at a specific time.
I am using this to help myself in my apply process. :smile:



### Install

------------


#### Install the dependencies
on```python3```its just ok but if there is an error on```python2```feel free to report the issue.
you can use```pip3```instead of```pip```
```bash
pip install gspread oauth2client
pip install schedule
```
#### Generate a password for your Gmail
If you don't have a 2-step verification account you can just use your original password, but if you have 2-step verification you can follow this tutorial to create an app password for your account :
    https://support.google.com/accounts/answer/185833?hl=en

#### Active your google sheet API
By following this tutorial you can make a new API.
In the end, you gonna have a **jason file** and an **email address** that you should add to your spreadsheet as an **editor** :
https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html


### How to init

------------
- ##### First copy the jason file to the code directory
- #####    Edit the xxx_passwords.py
fill this strings as it says
```python
        self._my_email = 'my gmail address @gmail.com'
        self._my_email_app_pass = 'my gmail password'
        self._jason_cret_filename = 'jason cret file to access sheet.json'
```
after editing that comment this line by adding ```#``` to first of the line.
```python
raise NameError('edit xxx_password.py file')   # delete or comment this line after you edited this file
```
- #####    Edit the xxx_template.py
you must save your resume as a PDF in the code directory.
then edit this part and enter your resume file name. 
```python
        self._cv_file_name = 'my cv name.pdf'
```
you can have several templates and subjects for your emails.
every each sheet can have a specefic template and subject.
```python
        ####                       for first sheet                      ####
        self._my_template_subject.append('my email subject for first sheet')
        self._my_template_body.append(
            '''
Dear Professor {pn},
this is my email for first sheet.
            ''')
        ####                               end                           ####
```
by appending more subject and template, you can use multiple templates.
if you want to send a template to all sheets just fill the first append.

### How to use

------------
call the`mail_composer.py`
a sample command is like this :
```bash
python mail_composer.py --sheet-number 2  --email-time 18:30,17:30 --workbook-name mysheet  --email-number 150 --prof-col 1 --email-col 2 --log-col 4 --paper-col 3
```
- `--sheet-number`
the number of sheets you have in a workbook
- `--email-time`
time in your os time zone that you want to the code send the emails.
you can have a specific time for each sheet. split for every sheet by using`,`
- `--workbook-name`
the workbook name that you added the google API email as an editor to it.
- `--email-number`
the number of emails that will send every day.
- `--prof-col`
the column of professors name that will be inserted in the template
- `--email-col`
the column of the emails according to the professor's name 
- `--log-col`
the column that fills with the date of the mail sent
- `--paper-col`
the column that fills with the related papers of the mail sent
