## Troubleshooting PI connection issues

So you're in the trenches and everything is cooked! Be not afraid, this guide will help you.

### Ways of connecting to the Pi

1. Through UART
2. SSH via Wifi (Needs you to use the first method once)


### Troubleshooting UART

##### UART may not work because of
<img width="275" alt="USB-c to USB-A adapter " src="https://github.com/user-attachments/assets/b1f17f8d-abed-406e-bad8-152e6b48bdc9" />

- **Faulty USB-c to USB-A adapter**
    - See if the adapter is disfunctional or janky
    - Plug in the UART cable with the adapter and do `ls /dev/cu.*` in your terminal
    - You should see something like `/dev/cu.usbserial-***`
    - If you don't see that, try using a diffrent adapter.
    - If you see that but as soon as you move the able a lit it stops showing then either your adapter is janky or your port is
    - Try using a diffrent adapter

- **Faulty UART cable**
<img width="275" align="center" alt="Uart Cable" src="https://github.com/user-attachments/assets/dd951240-686c-4a95-9822-b8a0a3d752a9">

    - If you made sure that your adapter is good and you still dont see `/dev/cu.usbserial-***` when you do `ls /dev/cu.*` then your cable is busted.
    - Ask TAs for a new one.
    - If you can see the device, then short (using a male to male jumper) the green and white wires together
    - Connect to the cable using `screen /dev/cu.usbserial-XYZ 115200`
    - Type something in the terminal and see if it appears on the screen as you type
    - If it does then your cable is good otherwise it's not
    - Try unplugging and replugging the cable once or twice
    - If it still doesn't works, ask TAs for a new one

- **Wrong settings in the SD card**
    - If you've recently flashed the OS thein this could also be the problem
    - Go to the section `#2-connecting-to-pi-via-uart` and double-check if all the settings are correct
    - Ensure the files `config.txt` and `cmdline.txt` are set to the correct option
 
- **Wrong pi Connnection**

<img width="275" align="center" alt="Uart pin connection" src="https://github.com/user-attachments/assets/22662f1b-bd8c-4c9c-a57f-f89d4c2c2668">

  - Make sure pins are connected the same way as show above

- **Janky Connections**
  - Any of the above connections could be janky, so make sure connections are firm


If none of these work, ask TAs for help

## Troubleshooting WIFI

- 








  




