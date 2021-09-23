import pandas as pd
import xlsxwriter
import smtplib
from smtplib import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from sources.time import time_now, time_now_email_subject
from sources.excel_format import *

def mysql_to_excel():
    fromaddr = "report@autodkms.com"
    
    #recipients = "oktoberlin@gmai.com"
    #fromaddr = 'report@autodkms.com'
    #toaddr=['oktoberlin@gmail.com', 'idzarahmana@gmail.com']
    toaddr=['oktoberlin@gmail.com']
    cc=['linibelajar@gmail.com']
    #toaddr=to+cc
    msg = MIMEMultipart()

    msg['From'] = 'Report DKM Lampung <report@autodkms.com>'
    msg['To'] = ", ".join(toaddr)
    msg['CC'] = ", ".join(cc)
    msg['Subject'] = f"DKM Lampung- REPORT OTOMATIS - {Client} - {time_now_email_subject}"

    #body = f"Auto Generate Excel Report PNPP DKM JAKARTA List {time_now}"


    #toaddr = ["oktoberlin@gmail.com","linibelajar@gmail.com"]
    #recipients = "oktoberlin@gmai.com"
    #msg = MIMEMultipart()

    #msg['From'] = 'Report DKM Jakarta <report@autodkms.com>'
    #msg['To'] = ", ".join(toaddr)
    #msg['Subject'] = f"DKM JAKARTA - REPORT OTOMATIS PER 10 MENIT - {Client} - {time_now_email_subject}"

    body = f"Auto Generate Excel Report {Client} DKM JAKARTA List {time_from} - {time_now}"

    msg.attach(MIMEText(body, 'plain'))

    filename = excel_filename
    attachment = open(filename, "rb")

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % file_name)

    msg.attach(part)
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        #server.set_debuglevel(3)
        server.starttls()
        server.login("linibelajar@gmail.com", "pflugwrmuymomkis")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr+cc, text)

        print('email successfully sent')
        server.quit()
    except SMTPResponseException as e:
        error_code = e.smtp_code
        error_message = e.smtp_error
        if (error_code==422):
            print("Recipient Mailbox Full")
        elif(error_code==431):
            print ("Server out of space")
        elif(error_code==447):
            print ("Timeout. Try reducing number of recipients")
        elif(error_code==510 or error_code==511):
            print ("One of the addresses in your TO, CC or BBC line doesn't exist. Check again your recipients' accounts and correct any possible misspelling.")
        elif(error_code==512):
            print ("Check again all your recipients' addresses: there will likely be an error in a domain name (like mail@domain.coom instead of mail@domain.com)")
        elif(error_code==541 or error_code==554):
            print ("Your message has been detected and labeled as spam. You must ask the recipient to whitelist you")
        elif(error_code==550):
            print ("Though it can be returned also by the recipient's firewall (or when the incoming server is down), the great majority of errors 550 simply tell that the recipient email address doesn't exist. You should contact the recipient otherwise and get the right address.")
        elif(error_code==553):
            print ("Check all the addresses in the TO, CC and BCC field. There should be an error or a misspelling somewhere.")
        else:
            print (error_code+": "+error_message)
        

if __name__ == '__main__':
    mysql_to_excel()