# Gravity Joystick

![BeautifulUI Logo](https://drive.google.com/uc?export=download&id=1QoIUpMFY0hq_7lWUBdmaJ-TmWokfj9y9)

This joystick app is based on the Xbox 360 controller, it transforms the accelerometer (gravity sensor) of the mobile into the left analog stick (for the gaming steering wheel), it also includes all the other buttons, the left and right trigger have been transformed into a single one slider (easier to hold the mobile while accelerating or braking). On Windows you will download the Server Receiver from this repository, and the joystick app from Google Play.

[![](https://drive.google.com/uc?export=download&id=1itkU6b4DT5FAnzztb_5ZTpRZhJp-A5yK)](https://play.google.com/store/apps/details?id=com.caiosilva.gravityjoystick&hl=pt&gl=US)

[Get it on Google Play](https://play.google.com/store/apps/details?id=com.caiosilva.gravityjoystick&hl=pt&gl=US&pli=1)

Some games have the option "steering axis dead zone" like Euro Truck Simulator 2, I recommend greatly reduce it to control 100% of the steering, high sensitivity is recommended.

## [DOWNLOAD Windows Receiver](https://github.com/Suundumused/Windows-Joystick-Receiver/releases/tag/GravityJoystickReceiverSetup)
## **Download and install third-party** [DRIVER](https://github.com/Suundumused/Windows-Joystick-Receiver/tree/main/ServerGravityJoystick/Driver)

**The license files in this document refer only to the Receiver for Windows and the Drivers. Does not apply to the mobile client.**

## Features

- **Components:** All joystick buttons.

- **Connection:** WI-FI.

- **Differential:** Mobile accelerometer as Left Analog control.

- **Target OS:** Android 8 - 13.

- **Types of games:** Designed for car and plane games.

## Screenshots
![Screenshot 0](https://drive.google.com/uc?export=download&id=1ict_dwXYI4CSEyqfmtTGDhqUEPTDV1S-) 
![Screenshot 2](https://drive.google.com/uc?export=download&id=1iGodTQTsNZCx_szvJmUA2_6q6e_zfAi3)

*BeautifulUI components in action.*

## Sensibility

The mobile being connected to the 5G network is highly recommended.:

- **Desktop and mobile must be on the same network.**
- **Enter the IP that is appearing in the Windows terminal on the mobile.**
- **You can change the server's IP and port by editing and opening the .bat file inside the program's folder.**
- **Driver is installed automatically on first run.**

## Setup (Follow the steps below only if you are having problems.)

- **Download and install third-party driver that will create "fake" xbox 360 joystick hardware** [DRIVER](https://github.com/Suundumused/Windows-Joystick-Receiver/tree/main/ServerGravityJoystick/Driver)
- **Download and run Receiver Joystick in this repository**
- **Connect on mobile through the Gravity Joystick app.**

## Support (Follow the steps below only if you are having problems.)

Follow these simple solution steps (option):

1. Firewall(if you have problems):

![Screenshot 3](https://drive.google.com/uc?export=download&id=1PxNbTq7ZDhWFkyhB328Sl59hJrg42-fW)

[If the image doesn't load click here.](https://drive.google.com/file/d/1PxNbTq7ZDhWFkyhB328Sl59hJrg42-fW/view)

   Select the Start menu, type Allow an app through Windows Firewall, and select it from the list of results. Select Change settings. 
   You might be asked for an administrator password or to confirm your choice. To add an app, select the check box next to the app, 
   or select Allow another app and enter the path for the app.

--

2. Unable to connect(Tips):

   Incorrect and corret structure IF using routers together with modem.

![Screenshot 4](https://drive.google.com/uc?export=download&id=1d-8nwoCNWNvgh6z8658iMQBgjaWRS_Fz)

[If the image doesn't load click here.](https://drive.google.com/file/d/1d-8nwoCNWNvgh6z8658iMQBgjaWRS_Fz/view)

3. Changing to the correct Listen IP and Port
   
   Open start menu search and open CMD, type ipconfig . Look for the IPV4 address corresponding to the computer connection with the modem/router,
   (Ethernet if via cable and WI-FI if wireless), copy the IPV4 address.

   With notepad, create a file named run.bat in the folder: C:\Program Files (x86)\Gravity Joystick Receiver (default)
   write this command substituting the IP and port if you need it. Save with type: "All" and open it.

   @echo off
   
   start "" "%~dp0GJWirelessReceiver.exe" --host 127.0.0.1 --port 3470
   

