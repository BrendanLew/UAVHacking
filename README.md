# UAVHacking

A NASA-funded project conducted through GVSU College of Computing. 
 
Cybersecurity research on UAV communications. Conduct reconnaissance. Exploit vulnerabilities.  Take control.

---

By Brendan Lewis - Grand Valley State University
BS. Cybersecurity

---
## 1. Abstract

This project will focus on researching and exploiting vulnerabilities in UAV communications. Preliminary research shows that UAV's are being used for personal and military applications. An increase in the ammount of UAV's increase the attack surface for drone communication. Hackers can passivly eavesdrop on Air to Ground (A2G) and Ground to Air (G2A) communications, and they can uncover important telemetry data that can be used to locate and attack the UAV. Furthermore, an active attack, such as GPS spoofing, can mislead the drones sensors and cause it to crash or fly in an unrestricted area.

By conducting this research we hope to investigate _why_ drone communication has such a large attack surface, and exploit these vulnerabilities in real time using a DJI Tello drone and an ESP32-S3 running Marauder. 


## 2. Requirements

### Hardware

- DJI Tello drone
- ESP32-S3
- MacOS, Windows, or Linux machine

### Software

- FZEEFlasher
- Marauder
- Djitellopy
- Wireshark

---
## 3. Getting Started

### Connecting to the DJI Tello for the first time.

1. Download the DJI Tello mobile application.
2. Press the power button on the side of the drone.
3. Connect to the Tello-xxxxx network from your devices Wi-Fi settings menu.
4. Open the Tello App.

### Flashing Marauder on the ESP32-S3

There are a few ways to do this, but I've found FZEEFlasher is the easiest and most convienient. This guide follows only MacOS for now. 

1. Plug in your ESP32-S3 to your computer via USB.

Note: You must use the USB Type-C **USB & OTG** port.

2. To verify your device is connected fun the command:
'''lsusb'''

Note: This should be something like /dev/cu.usbmodemxxxx on MacOS.

3. Open FZEEFlasher: https://fzeeflasher.com/index.html

4. Click **Connect** and select your ESP32-S3 Device. 

5. Select your hardware 'ESP32-S3 multimedia board'.

6. Select **Marauder** in the drop down.

7. Flash.

8. Once the flashing has completed. Unplug the ESP32-S3 for 5 seconds and plug into the USB Type-C **USB to Serial** port.

9. Open the serial terminal
   
10. Using FZEEFlasher, connect to the serial port.

Note: Should be something like /dev/cu.usbmodemxxxxxxxxxxxx. Different from the first time.

11. Interact with Marauder and verify its working.

'''scanap'''

This will show all available networks within range of the device. 

---
## 4. Remotely Controling the DJI Tello 

To remotely control the DJI Tello, we will use the DJI Tello SDK. [Tello SDK](https://dl-cdn.ryzerobotics.com/downloads/tello/20180910/Tello%20SDK%20Documentation%20EN_1.3.pdf)

1. Open your favorite IDE, in this example Virtual Studio Code.

2. In the terminal, clone the djitellopy repository.

'''
git clone https://github.com/damiafuentes/DJITelloPy.git
cd DJITelloPy
pip install -e .
'''

3. Install the requirements.

'''
pip install -r requirements.txt
'''

4. Create a new .py file. _Tello_testing.py_

cont.

---

## 5. Using the ESP32-S3 for a Passive Attack

---

## 6. Using the ESP32-S3 for an Active Attack
---

## References

- [Tengu Marauder](https://github.com/Lexicon121/Tengu-Marauder/blob/main/Guides/Workshop.md)
- [Djitellopy](https://github.com/damiafuentes/DJITelloPy)
- [Tello SDK](https://dl-cdn.ryzerobotics.com/downloads/tello/20180910/Tello%20SDK%20Documentation%20EN_1.3.pdf)
- [ESP32 Marauder](https://github.com/justcallmekoko/ESP32Marauder)
- [FZEEFlasher](https://fzeeflasher.com/index.html)
- [Espressif ESP32-S3 Documentation](https://docs.espressif.com/projects/esptool/en/latest/esp32s3/installation.html)
- [Espressif Serical Connection](https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/get-started/establish-serial-connection.html)
- 
