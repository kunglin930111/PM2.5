def sent(message):
    import smtplib 
    from email.mime.text import MIMEText 

    # 寄件者，收件者
    from_addr = 'xxxxxxxxxx'
    to_addr = 'xxxxxxxxx'


    smtpssl=smtplib.SMTP_SSL("smtp.gmail.com", 465) 
    smtpssl.login(from_addr, "xxxxxxx")

    msg = '現在空氣PM25密度:'+message+'(μg/m3) '+'時間: '+x
    mime=MIMEText(msg, "plain", "utf-8") 
    mime["Subject"]="高雄復興空氣品質"
    # 顯示的名稱
    mime["From"]="PM2.5監視器"
    mime["To"]= to_addr

    smtpssl.sendmail(from_addr, to_addr, mime.as_string())
    smtpssl.quit()

import datetime
import time
import requests, json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

while True:
    x = str(datetime.datetime.now())
    response = requests.get('https://opendata.epa.gov.tw/ws/Data/ATM00625/?$format=json', verify=False)

    sites = response.json()
    for site in sites:
        if site['Site'] == '復興':
            sent(site['PM25'])
            break
    time.sleep(60*60)


