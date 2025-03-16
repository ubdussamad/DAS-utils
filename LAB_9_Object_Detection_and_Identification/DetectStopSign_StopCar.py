import sys
import os
import cv2
from time import sleep

# Detect Stop Sign Via RPi cam
# Note: There's a delay between what you see on the terminal, so expect some lag
# in stop sign detection

shell_color_green = "\033[0;32m"
shell_color_red =   "\033[0;31m"
shell_color_reset = "\033[0m"

cascade_path = 'stopsign_good.xml'

if not os.path.exists(cascade_path):
	print(f"Error: The file {cascade_path} does not exist.")
	sys.exit()

stop_sign_cascade = cv2.CascadeClassifier(cascade_path)

if stop_sign_cascade.empty():
	print("Error loading stop_sign_good.xml")
	sys.exit()
else:print("Model: Stop sign cascade loaded successfully.")

is_car_running = True



def main():
	global is_car_running
	
	cap = cv2.VideoCapture(0)

	if not cap.isOpened():
		print("Error: Could not open camera.")
		sys.exit()
	
	print("Vechile is:", end="" , flush=True)
	status_buffer = ""

	while True:
		__len_to_clear = len(status_buffer) - len(shell_color_reset) - len(shell_color_green)
		# Cleans out the last status string
		print( '\b' * __len_to_clear , " " * (__len_to_clear-2) , '\b' * __len_to_clear , end="") # Clear status buffer
		
		ret, frame = cap.read()
		if not ret:
			print("Error: could not read frame.")
			break
		# Resize the ROI for faster processing
		frame = cv2.resize(frame,(640, 480))
		# Convert to grayscale
		gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		# Detect stop signs
		stop_signs = stop_sign_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

		# If the stop_signs list has something in it, it means that a stop sign was detected
		if (len(stop_signs)):
			status_buffer = shell_color_red + "Stopped at Stop sign!" + shell_color_reset
			print( status_buffer , flush=True  , end="")
			is_car_running = False
			# For future refrence,
			# You can add a call back or set a flag for the actual rover to stop;
			# the rover will have a control loop, you can pause that
			# loop with a flag

			sleep(1) # you should wait for few seconds before checking again
		else: # No stop sign detected
			status_buffer = shell_color_green + "Moving!" + shell_color_reset
			print( status_buffer , flush=True , end="")
			is_car_running = True

	cap.release()
	cv2.destroyAllWindows()


if __name__ == "__main__":
	main()
