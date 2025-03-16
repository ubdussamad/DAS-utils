# Troubleshooting PI Connection Issues

So you can't connect to Pi? Try this step-by-step guide!

## Ways of Connecting to the Pi

1. **UART**
2. **SSH via Wi-Fi** (requires at least one initial UART connection, typically)

---

## Troubleshooting UART

### Possible reasons why UART may not work

1. **Faulty USB-C to USB-A Adapter**  
   <img width="275" alt="USB-c to USB-A adapter" src="https://github.com/user-attachments/assets/b1f17f8d-abed-406e-bad8-152e6b48bdc9" />

   - Confirm the adapter itself isn’t defective; try plugging in something that you know works, e.g, a Keyboard or mouse
   - If you don't have anything to test it with, then plug in the UART cable with the adapter and run `ls /dev/cu.*` in your terminal.  
     - expect to see something like `/dev/cu.usbserial-***`.  
     - If nothing appears, try a different adapter
     - If even the new adapter doesn't work, then move on to step #2; your UART cable must be faulty  
     - If it appears but disappears when you move the cable slightly, either the adapter or USB port may be loose or faulty.

2. **Faulty UART Cable**  
   <img width="275" align="center" alt="UART Cable" src="https://github.com/user-attachments/assets/dd951240-686c-4a95-9822-b8a0a3d752a9" />

   - If your adapter is not the problem, and you still don’t see `/dev/cu.usbserial-***` when running `ls /dev/cu.*`, your cable may be broken.  
   - ask TAs for a replacement.  
   - Once you see the adapter, check if the cable is good by,  
     1. shorting the green and white wires together (using a male-to-male jumper).  
     2. connecting via `screen /dev/cu.usbserial-XYZ 115200`.  
     3. type something in the terminal; if it echoes back, the cable is good.  
     4. Otherwise, try unplugging and re-plugging the cable. If it still fails, replace it.

3. **Incorrect SD Card Settings**  
   - If you recently flashed the OS, wrong SD card settings could also be the issue.  
   - Go to **Step 2: Connecting to Pi via UART** and verify you’ve set all parameters correctly.  
   - Double-check `config.txt` and `cmdline.txt` to ensure the UART settings are correct.

4. **Incorrect Pi Connections**  
   <img width="275" align="center" alt="UART pin connection" src="https://github.com/user-attachments/assets/22662f1b-bd8c-4c9c-a57f-f89d4c2c2668" />

   - Confirm the pins are wired exactly as shown above

5. **Loose or “Janky” Connections**  
   - Ensure every connection is firm and not intermittent.

**If none of these solutions work, ask a TA for assistance.**

---

## Troubleshooting Wi-Fi

Before troubleshooting the WiFi, you'll need a working UART connection, though which you can access the Pi

### Possible reasons why Wifi may not work

1. **Not connected to wifi properly**
   - Make sure you're close to the wifi you're trying to connect to
   - If you can't do the above, then start your phone's hotspot and connect to it
   - Make sure the hotspot is NOT 5GHz; Rpi doesn't support 5GHz
   - Make sure your computer is connected to the same network as the Pi
2. **Where to enter the wifi name and password**
   - There are two files that contain WiFi info:
       1. `/boot/wpa_supplicant.conf` <br>
         - This file is accessible from your computer after plugging in the SD card <br>
         - You can edit it using a text editor <br>
         - This file can have multiple wifi networks <br>
         - If you're using this file, then make sure the WiFi **you wanna use comes first** in the list <br>
       2. `/etc/wpa_supplicant/wpa_supplicant.conf` <br>
         - This file is accessible when the Pi is on and you're connected to it via UART <br>
         - You can edit it using `sudo nano /etc/wpa_supplicant/wpa_supplicant.conf` <br>
         - Typically, you do not need to edit this file <br>
         - In case you think this file could be the issue, you should delete everything in it <br>
         - This file can have multiple wifi networks <br>
         - If you're using this file, meaning that the above file credentials are wrong or that wifi isn't available
          - then make sure the WiFi **you want to use comes first** in the list <br>
3. **Incorrectly configured wpa_supplicant.conf**
   - Make sure you've entered the correct wifi name and password
   - It should look like this:
     ```bash
     country=US

     network={
      ssid="Sam's iPhone or your wifi name"
      scan_ssid=1
      psk="your password"
	 }
     ```
4. **Test the WiFi**
   - If you're not sure if the WiFi is working, then you can test it by:
     1. Connecting to the Pi via UART
     2. Running `ping google.com`
     3. the output should look like this:
        ```bash
        PING google.com (
        64 bytes from google.com: icmp_seq=1 ttl=54 time=23.4 ms
        64 bytes from google.com: icmp_seq=2 ttl=54 time=23.4 ms
        ...
        ```
     4. If you see the above output, then your WiFi is working
     5. Get the IP address of the Pi by running `ifconfig` and look for `wlan0` and look for the IP address next to `inet`
     6. You can also use this command to do the above ` ip addr show wlan0 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1`
     7. Now you can SSH into the Pi using the IP address you got in the previous step

**If none of these solutions work, ask a TA for assistance or maybe try to repeat Lab-1 step by step.**



