# zabbix_sms
With this python script for Zabbix you can send easily SMS Alerts.

ZABBIX SETUP
1. Clone the latest version of Zabbix script
2. Edit following lines in the script:
Set the following three values: smsurl = "10.10.10.1"; login = "-----"; password = "-----";
3. Put the script in the directory, you specified in the zabbix_server.conf,
key AlertScriptsPath: Location for custom alert scripts AlertScriptsPath=/usr/lib/zabbix/alertscripts 
and ensure that it's executable (chmod 755 sendsms.py).
4. Test the script, by running: ./sendsms.py 994702414284 "Test sms"

After a few seconds, you should receive an SMS.
5. In Zabbix goto Administration, Media Types, add a new media called sendsms, and choose that it's a script, and enter the filename sendsms.py as the script name and add this 2 parametrs: {ALERT.SENDTO}, {ALERT.MESSAGE}  

6. Finally, in Zabbix, Administration, Users, click on a user, and add a new media called sendsms. Enter their phone number, and press save.
