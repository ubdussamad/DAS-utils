

###############################
#### Stop Car at Stop Sign ####
#### --------------------- ####
#### Objective:        ####
#### > Drive car forward   ####
####   until a sotpsign is ####
####   spotted on the cam  ####
###############################
import sys
import os
import cv2
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
enA=13
in1=27
in2=17
GPIO.setup(enA,GPIO.OUT)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
pwm_motor=GPIO.PWM(enA,1000)
pwm_motor.start(0)

cascade_path = '/home/pi/TrafficLightDetection/stopsign_good.xml'

if not os.path.exists(cascade_path):
	print(f"Error: The file {cascade_path} does not exist.")
	sys.exit()

stop_sign_cascade = cv2.CascadeClassifier(cascade_path)

if stop_sign_cascade.empty():
	print("Error loading stop_sign_good.xml")
	sys.exit()
else:
	print("Stop sign cascade loaded successfully.")


def stop_car():
	print("Stopping the car!")
	GPIO.output(in1, GPIO.LOW)
	GPIO.output(in2, GPIO.LOW)
	pwm_motor.ChangeDutyCycle(0)

def move_car():
	print("Moving the car!")
	GPIO.output(in1, GPIO.HIGH)
	GPIO.output(in2, GPIO.LOW)	
	pwm_motor.ChangeDutyCycle(100)

def main():
	cap = cv2.VideoCapture(0)

	if not cap.isOpened():
		print("Error: Could not open camera.")
		sys.exit()

	#stop_sign_detected = False

# Begin Camera video and driving forward #
	while True:
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
	
	#if len(stop_signs) > 0:
		#stop_sign_detected = True
		for (x, y, w, h) in stop_signs:
			roi = frame[y:y+h, x:x+w]
			stop_car()
			cv2.rectangle(frame, (x , y), (x + w, y + h), (255,0, 0), 2)
			cv2.putText(frame, "Stop Sign", (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9,  (255,0,0), 2)
			#stop_car()
			#sleep(1)
			#break

	#else:
		#if stop_sign_detected:
			#print("stop sign removed, moving forward.")
			#move_car()
			#stop_sign_detected = False


		if os.environ.get("DISPLAY"," ") == " ":
			print("Running in headless mode, skipping display.")
		else:
			cv2.imshow("Stop Sign Detection", frame)
			sleep(1)
			if cv2.waitkey(1) & 0xFF ==ord("q"):
				break

	cap.release()
	cv2.destroyAllWindows()
	GPIO.cleanup()

if __name__ == "__main__":
	#try:
	move_car()
	main()
	#except KeyboardInterrupt:
	#	print("Existing programs...")
	#	GPIO.cleanup()
	#	sys.exit()
