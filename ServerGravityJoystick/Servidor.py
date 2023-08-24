import socket
import asyncio
import json
import os
import sys
import ctypes
import threading
import psutil
import argparse
import platform
import subprocess

import pystray
from PIL import Image

import tkinter as tk
from tkinter import ttk

class Variables:
    def __init__(self):
        self.StartStop = True
        self.Sensibility = 2
        self.ServerIP = ""
        self.ServerPort = ""
        
    def install_drivers(self):
        MB_ICONERROR = 0x10
        MB_OK = 0x0
        
        bits = platform.architecture()[0]
        
        config_name = 'Driver'
        
        try:
            if getattr(sys, 'frozen', False):  #-----ATUALIZADO-----
                # Executando como executable (PyInstaller)
                path = os.path.dirname(sys.executable)
            else:
                # Executando como  script .py
                path = os.path.dirname(os.path.abspath(sys.argv[0]))
            
            if bits == '32bit':
                installer=os.path.join(path, config_name+"\DriverX86\ViGEmBusSetup_x86.msi")
                os.system('msiexec /i %s /qn' % installer)
            elif bits == '64bit':
                installer=os.path.join(path, config_name+"\DriverX64\ViGEmBusSetup_x64.msi")
                os.system('msiexec /i %s /qn' % installer)
            else:
                ctypes.windll.user32.MessageBoxW(0, "Architecture information not available.", "Error", MB_ICONERROR | MB_OK)
                
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(0, str(e), "Error", MB_ICONERROR | MB_OK)
        
    def sair(self):
        self.StartStop = False
        os._exit(0)
        
    def ADJSensibility(self,valor):
        if (valor * self.Sensibility) > 1.0:
            return 1.0
        elif (valor * self.Sensibility) < -1.0:
            return -1.0
        else:
            return (valor * self.Sensibility)
        
    def boolToFloat(self, valor):
        if valor:
            return 1.0
        else:
            return 0.0
        
    def acceleratorCor(self, valor):
        if valor < 0:
            return 0.0
        else:
            return valor

async def handle_client(client_socket, Variaveis):
    try:
        import vgamepad as vg
    except:
        Variaveis.install_drivers()
        import vgamepad as vg
        
    os.system('cls')
    print(f"Listening on {Variaveis.ServerIP}:{int(Variaveis.ServerPort)}")
    print(f"\nAccepted connection from {client_socket.getpeername()}\nConnected. Running!")
        
    MB_ICONERROR = 0x10
    MB_OK = 0x0
    
    gamepad = vg.VX360Gamepad()
    
    XUSB_GAMEPAD_DPAD_UP = 0x0001
    XUSB_GAMEPAD_DPAD_DOWN = 0x0002
    XUSB_GAMEPAD_DPAD_LEFT = 0x0004
    XUSB_GAMEPAD_DPAD_RIGHT = 0x0008
    XUSB_GAMEPAD_START = 0x0010
    XUSB_GAMEPAD_BACK = 0x0020
    XUSB_GAMEPAD_LEFT_THUMB = 0x0040
    XUSB_GAMEPAD_RIGHT_THUMB = 0x0080
    XUSB_GAMEPAD_LEFT_SHOULDER = 0x0100
    XUSB_GAMEPAD_RIGHT_SHOULDER = 0x0200
    XUSB_GAMEPAD_GUIDE = 0x0400
    XUSB_GAMEPAD_A = 0x1000
    XUSB_GAMEPAD_B = 0x2000
    XUSB_GAMEPAD_X = 0x4000
    XUSB_GAMEPAD_Y = 0x8000

    while Variaveis.StartStop:
        try:
            data = await asyncio.to_thread(client_socket.recv, 1024)
            if not data:
                break
            
            received_data = data.decode()
            received_list = json.loads(received_data)
            
            gamepad.right_trigger_float(Variaveis.acceleratorCor(received_list[17]*2-1))
            gamepad.left_trigger_float(Variaveis.acceleratorCor(-2*received_list[17]+1))
            
            gamepad.left_joystick_float(Variaveis.ADJSensibility(received_list[20]),Variaveis.ADJSensibility(received_list[19]))
            gamepad.right_joystick_float((Variaveis.boolToFloat(received_list[9])-Variaveis.boolToFloat(received_list[8])), (Variaveis.boolToFloat(received_list[10])-Variaveis.boolToFloat(received_list[11])))
            
            if received_list[0]:
                gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
            else:
                gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
                
            if received_list[1]:
                gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
            else:
                gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
            
            if received_list[12]:
                gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
            else:
                gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
                
            if received_list[13]:
                gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
            else:
                gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
                
            if received_list[14]:
                gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            else:
                gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
                
            if received_list[15]:
                gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            else:
                gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
                
            if received_list[16]:
                gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            else:
                gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                
            if received_list[2]:
                gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            else:
                gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
                
            if received_list[3]:
                gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            else:
                gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
                
            if received_list[4]:
                gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
            else:
                gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)

            if received_list[5]:
                gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
            else:
                gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
            
            if received_list[6]:
                gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
            else:
                gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
                
            if received_list[7]:
                gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
            else:
                gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
            
            gamepad.update()
                        
            response = "0"
            client_socket.send(response.encode())

        except Exception as e:
            ctypes.windll.user32.MessageBoxW(0, str(e), "Error", MB_ICONERROR | MB_OK)
            
    os.system('cls')
    print(f"Listening on {Variaveis.ServerIP}:{int(Variaveis.ServerPort)}")
    print(f"\nDisconnected. Stopped!")
    client_socket.close()
    gamepad.reset()
    #print(f"Connection closed for {client_socket.getpeername()}")

async def main(ServerAdd, Variaveis):
    MB_ICONERROR = 0x10
    MB_OK = 0x0

    try:
        server_ip, server_port = ServerAdd.split(":")
    # Create a socket object
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        parser = argparse.ArgumentParser(  #descrição do app
            description='Joystick Gravity Wireless Receiver',
            epilog="Started!")
    
        parser.add_argument("-ip","--host", help="Set/Get Local IPV4, default = '0.0.0.0'", type=str, default="0.0.0.0")#criar argumento alterar ip
        parser.add_argument("-p","--port", help="Set Port Forwarding, default = 8080", type=int, default=3470) #alterar porta
    
        args = parser.parse_args()
        
        if server_ip == "0.0.0.0" and args.host == "0.0.0.0":
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(('10.255.255.255', 1))
                
                IP = s.getsockname()[0]
            except Exception as e:
                IP = '127.0.0.1'
                ctypes.windll.user32.MessageBoxW(0, str(e), "Error", MB_ICONERROR | MB_OK)
            finally:
                server_ip = IP
                s.close()
                
        else:
            if args.host != "0.0.0.0":
                server_ip = args.host
                
        if args.port != 3470:
            server_port = str(args.port)

    # Bind the socket to the server address
        server_socket.bind((server_ip, int(server_port)))

    # Listen for incoming connections
        server_socket.listen(1)
        
        Variaveis.ServerIP = server_ip
        Variaveis.ServerPort = server_port
        
        print(f"Listening on {server_ip}:{int(server_port)}")

        while Variaveis.StartStop:
            client_socket, _ = await asyncio.to_thread(server_socket.accept)
            asyncio.create_task(handle_client(client_socket, Variaveis))
            
    except Exception as e:
        ctypes.windll.user32.MessageBoxW(0, str(e), "Error", MB_ICONERROR | MB_OK)


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    
    config_name = 'icon'
        
    if getattr(sys, 'frozen', False):  #-----ATUALIZADO-----
        # Executando como executable (PyInstaller)
        path = os.path.dirname(sys.executable)
    else:
        # Executando como  script .py
        path = os.path.dirname(os.path.abspath(sys.argv[0]))
            
    icon_path = os.path.join(path, config_name+"/icon2.ico")
    icon_image = Image.open(icon_path)
    
    Variaveis = Variables()
    
    menu = (pystray.MenuItem("Exit", Variaveis.sair),)
    icon = pystray.Icon("name", icon=icon_image, title="Wireless Gravity Joystick", menu=menu)
    
    tray_thread = threading.Thread(target=icon.run)
    # Start the thread
    tray_thread.start()
    
    asyncio.run(main("0.0.0.0:3470", Variaveis))