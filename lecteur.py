#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import datetime
import time
import calendar
import smtplib
import glob, os, sys
import MySQLdb
from datetime import datetime

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

writer = open("/var/www/html/temperature/temp.txt", "w")
writer.write(str(temp))
writer.close()

writer = open("/var/www/html/temperature/result.json", "w")
writer.write('[{"result":"'+str(temp)+'"}]')
writer.close()



temperature = temp
date = datetime.now()

# Connexion à la base de donnée DHT22
bdd = MySQLdb.connect(host="localhost",           # en local
                      user="root",                # l'utilisateur
                      passwd="password",      # son mot de passe
                      db="pi3b")                 # la base de donnée
req = bdd.cursor()

# insert la date, la température et l'humidité dans la table temphumi

if temperature < 30: 

    req.execute("""insert into releves (`temperature`,`date`) values (%s,%s)""",(temperature,date))
    bdd.commit()

    bdd.rollback()
# Fermeture de la connexion    
#bdd.close()


if temperature > 30:

#try:
    req.execute("""insert into releves (`temperature`,`date`) values (%s,%s)""",(temperature,date))
    req.execute("""insert into surchauffe (`temperature`,`date`) values (%s,%s)""",(temperature,date))
    bdd.commit()
#except:
    bdd.rollback()
    
# Fermeture de la connexion    
bdd.close()



exit
