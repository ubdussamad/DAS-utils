# Pairing Radiomaster TX-16s Controller to RadioMaster-R81 8CH Mini Reciever

# Rquirements
- Access to the receiver module; it typically sits under the Pi mount.

<img width="292" alt="Radio Reciever MOdule" src="https://github.com/user-attachments/assets/746adfcb-8734-4bef-83cb-a328220c225f" />
 
- TX-16s radio controller

<img width="465" alt="TX-16s transmitter" src="https://github.com/user-attachments/assets/660b5be1-4e03-4402-b4e4-7e0eb6ecd0f6" />


# Duplicating a model and renaming it

## Duping a model
The transmitters can connect to multiple radio receivers, but not at the same time.
Thus, each paired radio receiver has a model associated with it.
For our porpose, we need to clone any exsisting `Rover` model and then 
rename it to our liking *e.g. sam's-rover*.

> [!TIP]
> To go back from any menu, use the RTN button

1. Turn the transmitter on by holding the power button in the middle. It'll show a bunch of warnings. Ignore them by either pressing the return (RTN, to left to the screen) or the cylindrical button next to the screen.
2. Once you're on the screen, you'll see the model name (in the image below, it's CRF)
<img width="565" alt="" src="https://github.com/user-attachments/assets/3f9ae4f8-4379-4444-a4ab-21514ce7f097" />

3. Press the cylindrical button, and you'll go into the model select menu
<img width="563" alt="Screenshot 2025-02-27 at 10 44 52 AM" src="https://github.com/user-attachments/assets/e0136a13-0293-4b7e-81f5-cb55de74f02b" />

4. Rotate the cylindrical button till a model that goes by `rover[*]` is highlighted.
5. Press the cylindrical button again, and you'll see an option to duplicate the model.
<img width="525" alt="Dup model" src="https://github.com/user-attachments/assets/8e10b2ae-090a-436d-b0c7-4d27ac07c053" />


6. Duplicate that model by pressing the cylindrical button again.
7. The clone will show up at the end of the model list.
8. Go to the clone and select it.
9. Now, you'll see the selected model's name like you saw in step #2.
10. You have duplicated the model now.


## Renaming a model
Now we'll look into renaming the model

11. After selecting the model, press the silver MDL button on the top right of the screen.
12. It'll open a window to edit the model name like below
  <img width="540" alt="Model Setup" src="https://github.com/user-attachments/assets/d98e750e-d22e-4a6b-b9cc-b7a01290002b" />

13. Press the cylindrical button and moving it will change the character.
14. After naming it, just go back with the RTN button.


# Pairing your model with the receiver

## Turning on the pairing mode in the receiver
You'll need to pair the model to the receiver. The receiver draws power from the motor ESC, so make sure it's plugged in and the battery is plugged in.


>[!CAUTION]
> When connecting ESC or Radio receiver pins to the navio, make sure that the black wire always faces down
> and the yellow or white wire always faces up.

To put the receiver in pairing mode, do the following:

15. Plug the battery in the rover
16. Connect the ESC pins of the servo and the motor to the navio.
17. Unplug the radio receiver if it's plugged into the navio.
18. Press and hold the only button on the receiver module
19. Now, plug it back in (the way it was, the yellow wire of the receiver should face up)
20. The receiver will flash; if not, either you didn't press it or there's no power
  - Check if the ESC is on; if not, turn it on
  - If the ESC is not turning on, check the battery connection or ask TA for help
 
## Binding the transmitter

21. The Receiver should be in binding mode
22. Go to the model and model setup menu like you did before
23. Go all the way down until (on the model setup menu) you see a bind option
  - The bind option should be all within the Internal RF section
<img width="747" alt="Bind Button" src="https://github.com/user-attachments/assets/b2e3f5cd-d4de-484d-b20c-3e73517f1161" />

24. Press the cylinder on it
25. It should ask to select the channels; just select the first one
26. Now it'll say binding; wait for the receiver to flash rapidly
27 When it flashes rapidly, plug it out and back in again
28. Now you're paired with the radio.
29. Press RTN to go back to the main screen
30. You'll see an antenna symbol with a bunch of bars on the top right.






