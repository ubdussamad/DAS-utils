# Troubleshooting PI Connection Issues

So you’re in the trenches and everything is cooked! Don’t worry—this guide will help you.

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

