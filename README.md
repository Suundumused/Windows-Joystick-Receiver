# Gravity Joystick AND Windows Receiver

![BeautifulUI Logo](https://drive.google.com/uc?export=download&id=1QoIUpMFY0hq_7lWUBdmaJ-TmWokfj9y9)

This joystick app is based on the Xbox 360 controller, it transforms the accelerometer (gravity sensor) of the mobile into the left analog stick (for the gaming steering wheel), it also includes all the other buttons, the left and right trigger have been transformed into a single one slider (easier to hold the mobile while accelerating or braking). On Windows you will download the Server Receiver from this repository, and the joystick app from Google Play.

Some games have the option "steering axis dead zone" like Euro Truck Simulator 2, I recommend disabling it to control 100% of the steering, high sensitivity is recommended.

## [DOWNLOAD Windows Receiver](https://github.com/Suundumused/Windows-Joystick-Receiver/releases/tag/JoystickReceiverSetup)

## Features

- **Components:** All joystick buttons.

- **Connection:** WI-FI.

- **Differential:** Mobile accelerometer as Left Analog control.

- **Target OS:** Android 8 - 13.

- **Types of games:** Designed for car and plane games.

## Screenshots
![Screenshot 0](https://drive.google.com/uc?export=download&id=1ZQDWzuQ7b1IOH9o6A_HmnsBreETEFDm8) 
![Screenshot 2](https://drive.google.com/uc?export=download&id=1fiCMyXSn1H1i7wSz1TzoHgchwzrGR_kj) 

*BeautifulUI components in action.*

## Sensibility

The mobile being connected to the 5G network is highly recommended.:

- **Desktop and mobile must be on the same network.**
- **Enter the IP that is appearing in the Windows terminal on the mobile.**
- **You can change the server's IP and port by editing and opening the .bat file inside the program's folder.**

## Setup

- **Download and install third-party driver that will create "fake" xbox 360 joystick hardware** [DRIVER](https://github.com/Suundumused/Windows-Joystick-Receiver/tree/main/ServerGravityJoystick/Driver)
- **Download and run Receiver Joystick in this repository**
- **Connect on mobile through the Gravity Joystick app.**

## Getting Started

Follow these simple solution steps (option):

1. Firewall(if you have problems):

![Screenshot 3](https://drive.google.com/uc?export=download&id=1PxNbTq7ZDhWFkyhB328Sl59hJrg42-fW)

   Select the Start menu, type Allow an app through Windows Firewall, and select it from the list of results. Select Change settings. 
   You might be asked for an administrator password or to confirm your choice. To add an app, select the check box next to the app, 
   or select Allow another app and enter the path for the app.

--

2. Unable to connect(Tips):

   Incorrect and corret structure IF using routers together with modem.

![Screenshot 4](https://drive.google.com/uc?export=download&id=1d-8nwoCNWNvgh6z8658iMQBgjaWRS_Fz)

3. Changing to the correct Listen IP and Port
   
   Open start menu search and open CMD, type ipconfig . Look for the IPV4 address corresponding to the computer connection with the modem/router,
   (Ethernet if via cable and WI-FI if wireless), copy the IPV4 address.

   With notepad, create a file named run.bat in the folder: C:\Program Files (x86)\Gravity Joystick Receiver (default)
   write this command substituting the IP and port if you need it. Save with type: "All" and open it.

   @echo off
   
   start "" "%~dp0GJWirelessReceiver.exe" --host 127.0.0.1 --port 3470
   

