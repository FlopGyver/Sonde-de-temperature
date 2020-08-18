#!/usr/bin/pyhton
# -*- coding: utf-8 -*-

import sys, glob, os
import datetime
import smtplib
import calendar

def get_temp(device_file):
    temp_c = 0

    if os.path.isfile(device_file):
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()

        if lines[0].strip()[-3:] == 'YES':
            equals_pos = lines[1].find('t=')

            if equals_pos != -1:
                temp_string = lines[1][equals_pos+2:]
                temp_c = float(temp_string) / 1000.0

    return temp_c

base_dir = '/sys/bus/w1/devices/'
devices_folder = glob.glob(base_dir + '28*')

for device_dir in devices_folder:
    device = os.path.basename(device_dir)

    temp = round(get_temp(device_dir+'/w1_slave'), 1)

print 'temperature : '+str(temp)+'°C'

temperature = temp

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587 
GMAIL_USERNAME = 'sondetemp@gmail.com' 
GMAIL_PASSWORD = 'Azerty42'

class Emailer:
    def sendmail(self, recipient, subject, content):

        #Create Headers
        headers = ["From: " + GMAIL_USERNAME, "Subject: " + subject, "To: " + recipient,
                   "MIME-Version: 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)

        #Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()

        #Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

        #Send Email & Exit
        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        session.quit

sender = Emailer()

sendTo = 'fvallet@istp-france.com'
emailSubject = "Temperature anormale"
emailContent = "Temperature anormale dans le local serveur de Copernic :"+str(temp)+"*C"


if temperature > 30:sender.sendmail(sendTo, emailSubject, emailContent);

