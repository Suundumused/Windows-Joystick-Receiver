import math
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
import time

import shutil
import win32api

import pystray
from PIL import Image

import customtkinter

import tkinter as tk
from tkinter import ttk, Frame

class Overlays:
    def onClose(self, Variaveis):
        Variaveis.Overlays = None
        self.root.destroy()
        
    def __init__(self, root, Variaveis):
        self.root = root
        Variaveis.Overlays = self.root
        
        self.root.wm_attributes("-alpha", 0.67)
        #self.root.overrideredirect(True)
        self.root.title(" ")
        
        self.root.lift()
        self.root.call('wm', 'attributes', '.', '-topmost', True)
        self.root.wm_attributes("-toolwindow", True)
        self.root.config(bg='red')
        self.root.wm_attributes('-transparentcolor','red')
        
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.onClose(Variaveis))
        
        config_name = 'icon'
    
        if getattr(sys, 'frozen', False):  #-----ATUALIZADO-----
            # Executando como executable (PyInstaller)
            path = os.path.dirname(sys.executable)
        else:
            # Executando como  script .py
            path = os.path.dirname(os.path.abspath(sys.argv[0]))
                
        icon_path = os.path.join(path, config_name+"/icon.ico")
        
        self.root.iconbitmap(icon_path)
        
        self.app_width = int(0.125 * self.root.winfo_screenwidth())
        self.app_height = int(0.25 * self.root.winfo_screenheight())
        
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        
        self.root.geometry('%dx%d+%d+%d' % (self.app_width, self.app_height, (self.screen_width - (self.app_width * 2)), (self.app_height)))
        
        self.root.resizable(0,0)
        #self.root.eval('tk::PlaceWindow . top-right')
        
        self.frame = Frame(root)
        self.frame.configure(bg='red')
        self.frame.pack(pady=0, padx=0, fill="both", expand=True)
        
        self.slider = customtkinter.CTkProgressBar(master=self.frame, orientation = 'vertical', width=int(0.01 * self.root.winfo_screenwidth()))
        self.slider.configure(border_color ='red', progress_color = '#00FFFF', fg_color = 'black')
        self.slider.pack(pady=0, padx=0, fill="y", expand=True)
        
        Variaveis.accslider = self.slider
        
        try:
            root.mainloop()
        except:
            pass

class UI:
    def msgbox(self, txt):
        win32api.MessageBox(0, f'{txt}', 'Alert')       
    
    def tkinter_thread2(self, Variaveis):
        root2 = customtkinter.CTk()
        app2 = Overlays(root2, Variaveis)
        
    def NewWindow2(self, Variaveis):
        if Variaveis.Overlays == None:
            tkinter_thread_thread = threading.Thread(target=self.tkinter_thread2, args=(Variaveis, ))
            tkinter_thread_thread.start()
    
    def SaveAll(self, Variaveis):
        self.MB_ICONERROR = 0x10
        self.MB_OK = 0x0
        
        try:
            self.cwd=os.path.expanduser(os.getenv('USERPROFILE'))
            self.cwd=self.cwd=str(str(self.cwd) + r'\Documents\\GravityJoystick\Settings\Settings.json')
                
            if os.path.exists(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\\GravityJoystick\Settings')):
                pass
            else:
                os.makedirs(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\\GravityJoystick\Settings'))
                
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(0, repr(e), "Error", self.MB_ICONERROR | self.MB_OK)

        try:
            self.cwd=os.path.expanduser(os.getenv('USERPROFILE'))
            self.cwd=self.cwd=str(str(self.cwd) + r'\Documents\\GravityJoystick\Settings\Settings.json')
                        
            Variaveis.data['Smooth_Input'] = self.switch_3.get()
            Variaveis.data['Sensibility'] = self.slider.get()
            Variaveis.data['Start_Hidden'] = self.switch_1.get()
            Variaveis.data['Show_Overlay'] = self.switch_2.get()
            Variaveis.data['ServerIP'] = self.IP.get()
            Variaveis.data['ServerPort'] = self.PORT.get()
            
            if Variaveis.data['Show_Overlay'] == 1 and Variaveis.Overlays == None:
                self.NewWindow2(Variaveis)
            
            Variaveis.Sensibility = Variaveis.data['Sensibility'] * 2

            Variaveis.alpha = 1 - Variaveis.data['Smooth_Input']
                
            self.data = Variaveis.data
                
            with open(self.cwd, 'w') as self.outfile:
                json.dump(self.data, self.outfile)
                
            msg = threading.Thread(target = self.msgbox, args=("Some options will require the app to be restarted.", ))
            msg.start()
                    
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(0, repr(e), "Error", self.MB_ICONERROR | self.MB_OK)
            

    def openSaveFile(self, Variaveis):
        self.MB_ICONERROR = 0x10
        self.MB_OK = 0x0
        
        try:
            self.cwd=os.path.expanduser(os.getenv('USERPROFILE'))
            self.cwd=self.cwd=str(str(self.cwd) + r'\Documents\\GravityJoystick\Settings\Settings.json')
                
            if os.path.exists(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\\GravityJoystick\Settings')):
                pass
            else:
                os.makedirs(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\\GravityJoystick\Settings'))
                
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(0, repr(e), "Error", self.MB_ICONERROR | self.MB_OK)

        try:
            self.cwd=os.path.expanduser(os.getenv('USERPROFILE'))
            self.cwd=self.cwd=str(str(self.cwd) + r'\Documents\\GravityJoystick\Settings\Settings.json')
                
            if os.path.exists(str(str(os.path.expanduser(os.getenv('USERPROFILE'))) + r'\Documents\\GravityJoystick\Settings\Settings.json')):
                pass
            else:
                self.data={
                    "Smooth_Input": 0.875,
                    "Sensibility": 1,
                    "Start_Hidden": 0,
                    "Show_Overlay": 0,
                    "ServerIP": "0.0.0.0",
                    "ServerPort": 3470
                }
                
                with open(self.cwd, 'w') as self.outfile:
                    json.dump(self.data, self.outfile)
                    
            self.File = open(self.cwd)
            Variaveis.data = json.load(self.File)
            
            Variaveis.Sensibility = Variaveis.data['Sensibility'] * 2
            
            Variaveis.alpha = 1 - Variaveis.data['Smooth_Input']
                
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(0, repr(e), "Error", self.MB_ICONERROR | self.MB_OK)
            
    def Restart(self, Variaveis):  
        MB_ICONERROR = 0x10
        MB_OK = 0x0
        
        try:
            Variaveis.StartStop = False
            
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            try:
                self.client_socket.connect((Variaveis.ServerIP, int(Variaveis.ServerPort)))
                
                Variaveis.ResCallSave = True
                Variaveis.ServerIP = self.IP.get()
                Variaveis.ServerPort = self.PORT.get()
                
                self.client_socket.close()
                        
            except Exception as e:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(('10.255.255.255', 1))
                
                if Variaveis.ServerIP == "0.0.0.0":
                    self.client_socket.connect((s.getsockname()[0], int(Variaveis.ServerPort)))
                    
                else:
                    self.client_socket.connect((Variaveis.ServerIP, int(Variaveis.ServerPort)))
                
                Variaveis.ResCallSave = True
                Variaveis.ServerIP = s.getsockname()[0]
                Variaveis.ServerPort = self.PORT.get()
                
                self.client_socket.close()
            
            finally:
                self.SaveAll(Variaveis)

        except Exception as e:
            ctypes.windll.user32.MessageBoxW(0, repr(e), "Error", MB_ICONERROR | MB_OK)
                
    def onClose(self, Variaveis):        
        Variaveis.UI = None
        self.root.destroy()
        Variaveis.sair()
        
    def __init__(self, root, Variaveis):
        self.openSaveFile(Variaveis)
        
        config_name = 'icon'
    
        if getattr(sys, 'frozen', False):  #-----ATUALIZADO-----
            # Executando como executable (PyInstaller)
            path = os.path.dirname(sys.executable)
        else:
            # Executando como  script .py
            path = os.path.dirname(os.path.abspath(sys.argv[0]))
                
        icon_path = os.path.join(path, config_name+"/icon.ico")
        
        customtkinter.set_default_color_theme("green")
        
        self.root = root
        
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.onClose(Variaveis))
        
        self.root.title("Gravity Joystick Receiver V1.2.1")
        
        Variaveis.UI = self.root
        
        self.app_width = int(0.25 * self.root.winfo_screenwidth())
        self.app_height = int(0.5 * self.root.winfo_screenheight())
        
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        
        self.root.resizable(0,0)
        self.root.eval('tk::PlaceWindow . center')
        
        self.root.iconbitmap(icon_path)
                
        self.root.geometry('%dx%d+%d+%d' % (self.app_width, self.app_height, (self.app_width * 1.5), (self.app_height // 2)))
        
        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=(20,0), padx=60, fill="x", expand=False)
        
        self.title = customtkinter.CTkLabel(master = self.frame, text="Gravity Joystick Receiver", font = ("Roboto", 22))
        self.title.pack(pady=12, padx=10)
        
        self.title2 = customtkinter.CTkLabel(master = self.frame, text = f"Listening set to: {Variaveis.MasterIP}:{Variaveis.data['ServerPort']}", font = ("Roboto", 14))
        self.title2.pack(pady=12, padx=10)
        
        self.IP = customtkinter.CTkEntry(master = self.frame, placeholder_text="0.0.0.0", justify="right")
        self.IP.pack(pady=12, padx=(10,1), side = "left", expand=True, fill="x")
                                
        self.IP.insert(0, Variaveis.data['ServerIP'])
        
        self.dott = customtkinter.CTkLabel(master = self.frame, text=":", font = ("Roboto", 18))
        self.dott.pack(pady=12, padx=1, side = "left")
        
        self.PORT = customtkinter.CTkEntry(master = self.frame, placeholder_text="3470")
        self.PORT.pack(pady=12, padx=(1,10), side = "right", expand=False, fill="x")
        
        self.PORT.insert(0, Variaveis.data['ServerPort'])
        
        '''self.frame2 = customtkinter.CTkFrame(master=self.root)
        self.frame2.pack(pady=0, padx=60, fill="x", expand=False)
        
        self.button = customtkinter.CTkButton(master=self.frame2, border_width=0, corner_radius=8, text="Restart", command = lambda: self.Restart(Variaveis))
        self.button.pack(pady=12, padx=1)'''
        
        self.frame3 = customtkinter.CTkFrame(master=self.root)
        self.frame3.pack(pady=(0,0), padx=60, fill="both", expand=True)
        
        self.SenseLabel = customtkinter.CTkLabel(master = self.frame3, text="Sensibility: ", font = ("Roboto", 14))
        self.SenseLabel.pack(pady=1, padx=(6,1), side = "left")
        
        self.slider = customtkinter.CTkSlider(master=self.frame3, border_width=5.5, from_ = 0.5, to = 1)
        self.slider.pack(pady=1, padx=(1,6), fill="x", expand=True, side = "right")
        self.slider.set(Variaveis.data['Sensibility'])
        
        self.frame45 = customtkinter.CTkFrame(master=self.root)
        self.frame45.pack(pady=(0,0), padx=60, fill="both", expand=True)
        
        self.frame4 = customtkinter.CTkFrame(master=self.root)
        self.frame4.pack(pady=(0,20), padx=60, fill="both", expand=True)
        
        if Variaveis.data['Show_Overlay'] and Variaveis.once == True:
            self.NewWindow2(Variaveis)
            
        self.SenseLabel3 = customtkinter.CTkLabel(master = self.frame45, text="Smooth Input: ", font = ("Roboto", 14))
        self.SenseLabel3.pack(pady=1, padx=(6,1), side = "left")
        
        self.switch_3 = customtkinter.CTkSlider(master=self.frame45,  border_width=5.5, number_of_steps = 1000, from_ = 0.5, to = 0.975)
        self.switch_3.pack(pady=1, padx=(1,6), fill="x", expand=True, side = "right")
        self.switch_3.set(Variaveis.data['Smooth_Input'])
        
        self.switch1_var = customtkinter.IntVar(value = Variaveis.data['Start_Hidden'])
        self.switch_1 = customtkinter.CTkSwitch(master=self.frame4, text="Start Hidden",  onvalue=1, offvalue=0, variable = self.switch1_var, command = lambda: self.SaveAll(Variaveis))
        self.switch_1.pack(pady=1, padx=6, fill="x", expand=True)
        
        self.switch2_var = customtkinter.IntVar(value = Variaveis.data['Show_Overlay'])
        self.switch_2 = customtkinter.CTkSwitch(master=self.frame4, text="Show Overlay ( Beta! may cause Input Lag. )",  onvalue=1, offvalue=0, variable = self.switch2_var, command = lambda: self.SaveAll(Variaveis))
        self.switch_2.pack(pady=1, padx=6, fill="x", expand=True)
        
        self.button = customtkinter.CTkButton(master=self.frame4, border_width=0, corner_radius=8, text="Save", command = lambda: self.SaveAll(Variaveis))
        self.button.pack(pady=12, padx=1)
        
        if Variaveis.once == True and Variaveis.data['Start_Hidden'] == 1:            
            Variaveis.once = False
            Variaveis.UI = None
            self.root.destroy()

        else:
            Variaveis.once = False
    
        try:
            root.mainloop()
        except:
            pass

class Variables:
    def __init__(self):
        self.once = True
        self.StartStop = True
        self.Sensibility = 2
        self.ServerIP = ""
        self.ServerPort = ""
        self.start_time = time.time()
        self.valor3 = 0.0
        
        self.accslider = None
        self.fov = False
        
        self.alpha = 0.125 #smooth rate 
        
        self.WheelXValue = 0.0
        self.WheelYValue = 0.0
        
        self.filtered_valueX = None
        self.filtered_valueY = None
        
        self.FinalXValue = 0.0
        self.FinalYValue = 0.0
        
        self.MasterIP = ""
        
        self.Socket = None
        self.UI = None
        self.Overlays = None
        self.ResCallSave = False
        
        self.data = {
                    "Smooth_Input": 0.875,
                    "Sensibility": 1,
                    "Start_Hidden": 0,
                    "Show_Overlay": 0,
                    "ServerIP": "0.0.0.x",
                    "ServerPort": 3470
                }
        
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
                os.startfile(installer)
            elif bits == '64bit':
                installer=os.path.join(path, config_name+"\DriverX64\ViGEmBusSetup_x64.msi")
                os.startfile(installer)
            else:
                ctypes.windll.user32.MessageBoxW(0, "Architecture information not available.", "Error", MB_ICONERROR | MB_OK)
                
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(0, str(e), "Error", MB_ICONERROR | MB_OK)
        
    def sair(self):
        self.StartStop = False
        os._exit(0)
        
    def XADJSensibility(self,valor):            
        if Variaveis.filtered_valueX is None:
            Variaveis.filtered_valueX = valor
        else:
            Variaveis.filtered_valueX = (1 - Variaveis.alpha) * Variaveis.filtered_valueX + Variaveis.alpha * valor #low pass filter
            
        if (Variaveis.filtered_valueX * (self.Sensibility + Variaveis.alpha)) >= 1.0:
            return 1.0
        elif (Variaveis.filtered_valueX * (self.Sensibility + Variaveis.alpha)) <= -1.0:
            return -1.0
        else:
            return (Variaveis.filtered_valueX * (self.Sensibility + Variaveis.alpha))
            
    def YADJSensibility(self,valor):            
        if Variaveis.filtered_valueY is None:
            Variaveis.filtered_valueY = valor
        else:
            Variaveis.filtered_valueY = (1 - Variaveis.alpha) * Variaveis.filtered_valueY + Variaveis.alpha * valor #low pass filter
        
        if (Variaveis.filtered_valueY * (self.Sensibility + Variaveis.alpha)) >= 1.0:
            return 1.0
        elif (Variaveis.filtered_valueY * (self.Sensibility + Variaveis.alpha)) <= -1.0:
            return -1.0
        else:
            return (Variaveis.filtered_valueY * (self.Sensibility + Variaveis.alpha))
        
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
        
async def smoothWheel(Variaveis):
    while True:
        start_time = time.time()
    
        Variaveis.FinalXValue = Variaveis.XADJSensibility(Variaveis.WheelXValue)
        Variaveis.FinalYValue = Variaveis.YADJSensibility(Variaveis.WheelYValue)
            
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        if elapsed_time < 1/250:
            time.sleep(1/250 - elapsed_time)
            
async def fovUpdate(Variaveis):
    await asyncio.sleep(0.25)
    Variaveis.fov = False

async def update_slider_overlay(Variaveis, value):
    try:
        if Variaveis.fov == False:
            Variaveis.fov = True
            Variaveis.accslider.set(value)
            await fovUpdate(Variaveis)

    except Exception as e:
        if Variaveis.fov == True:
            await fovUpdate(Variaveis)

async def handle_client(client_socket, Variaveis):
    MB_ICONERROR = 0x10
    MB_OK = 0x0

    try:
        import vgamepad as vg
    except:
        Variaveis.install_drivers()
        try:
            import vgamepad as vg
        except:
            Variaveis.sair()
        
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
            loop = asyncio.get_event_loop()
            
            data = await asyncio.to_thread(client_socket.recv, 2048)
            if not data:
                break
            
            received_data = data.decode()
            received_list = json.loads(received_data)
            
            Variaveis.WheelXValue = received_list[20]
            Variaveis.WheelYValue = received_list[19]
            
            gamepad.right_trigger_float(Variaveis.acceleratorCor(received_list[17]*2-1))
            gamepad.left_trigger_float(Variaveis.acceleratorCor(-2*received_list[17]+1))
            
            gamepad.left_joystick_float(Variaveis.FinalXValue, Variaveis.FinalYValue)
            gamepad.right_joystick_float((Variaveis.boolToFloat(received_list[9])-Variaveis.boolToFloat(received_list[8])), (Variaveis.boolToFloat(received_list[10])-Variaveis.boolToFloat(received_list[11])))
            
            if Variaveis.data['Show_Overlay'] == 1:
                task = asyncio.create_task(update_slider_overlay(Variaveis, received_list[17]))
            
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
            
            await loop.sock_sendall(client_socket, response.encode('utf8'))

        except Exception as e:
            es = repr(e)
            ctypes.windll.user32.MessageBoxW(0, es, "Error", MB_ICONERROR | MB_OK)
            break
            
    os.system('cls')
    print(f"Listening on {Variaveis.ServerIP}:{int(Variaveis.ServerPort)}")
    print(f"\nDisconnected. Stopped!")
    client_socket.close()
    gamepad.reset()
    #print(f"Connection closed for {client_socket.getpeername()}")

async def main(ServerAdd, Variaveis):
    MB_ICONERROR = 0x10
    MB_OK = 0x0
    
    while Variaveis.data['ServerIP'] == "0.0.0.x":
        pass

    try:
        #server_ip, server_port = ServerAdd.split(":")
        server_ip = Variaveis.data['ServerIP']
        server_port = Variaveis.data['ServerPort']
        
    # Create a socket object
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        '''parser = argparse.ArgumentParser(  #descrição do app
            description='Joystick Gravity Wireless Receiver',
            epilog="Started!")
    
        parser.add_argument("-ip","--host", help="Set/Get Local IPV4, default = '0.0.0.0'", type=str, default="0.0.0.0")#criar argumento alterar ip
        parser.add_argument("-p","--port", help="Set Port Forwarding, default = 8080", type=int, default=3470) #alterar porta
    
        args = parser.parse_args()'''
        
        if server_ip == "0.0.0.0":
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(('10.255.255.255', 1))
                
                IP = s.getsockname()[0]
            except Exception as e:
                IP = '127.0.0.1'
                ctypes.windll.user32.MessageBoxW(0, str(e), "Error", MB_ICONERROR | MB_OK)
            finally:
                server_ip = IP
                Variaveis.MasterIP = server_ip
                
                s.close()
                
        '''else:
            if args.host != "0.0.0.0":
                server_ip = args.host
                
        if args.port != 3470:
            server_port = str(args.port)'''

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
        ctypes.windll.user32.MessageBoxW(0, repr(e), "Error", MB_ICONERROR | MB_OK)
        
def tkinter_thread(Variaveis):
    root = customtkinter.CTk()
    app = UI(root, Variaveis)
    
def NewWindow(Variaveis):
    if Variaveis.UI == None:
        tkinter_thread_thread = threading.Thread(target=tkinter_thread, args=(Variaveis, ))
        tkinter_thread_thread.start()

def smooth_Thread(Variaveis):
    asyncio.run(smoothWheel(Variaveis))

if __name__ == "__main__":
    myappid = 'Suundumused.GravityJoystickReceiver.GravityJoystickReceiver.1' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    
    '''root = tk.Tk()
    root.withdraw()'''
    
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
    
    tkinter_thread_thread = threading.Thread(target=tkinter_thread, args=(Variaveis, ))
    tkinter_thread_thread.start()
    
    MainMenu = pystray.MenuItem("Menu", lambda: NewWindow(Variaveis))
    
    menu = (
        MainMenu,
        pystray.MenuItem("Exit", Variaveis.sair),
    )
    
    icon = pystray.Icon("name", icon=icon_image, title="Wireless Gravity Joystick", menu=menu)
    
    tray_thread = threading.Thread(target=icon.run)
    # Start the thread
    tray_thread.start()
    
    smooth_ThreadA = threading.Thread(target=smooth_Thread, args=(Variaveis, ))
    smooth_ThreadA.start()
    
    asyncio.run(main("0.0.0.0:3470", Variaveis))