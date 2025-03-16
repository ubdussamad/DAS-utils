import cv2
print("OpenCV version:", cv2.__version__)
import numpy as np
from time import sleep

# This script detects the color of a traffic light in a live video feed.
# You can optimize this for the environment you're in by tuning the color ranges
# and the minimum area threshold for detection.


shell_colors = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "unknown": "\033[94m"
}
shell_color_reset = "\033[0m"

def detect_color(frame):
    """
    Returns 'red', 'yellow', 'green', or 'none' depending on which color
    is detected with the largest contour above a certain area threshold.
    """

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define color ranges (tune for your environment)
    # Red requires two ranges due to hue wrap
    red_lower1 = (0,   150, 150)
    red_upper1 = (10,  255, 255)
    red_lower2 = (170, 150, 150)
    red_upper2 = (180, 255, 255)

    yellow_lower, yellow_upper = np.array([15, 100, 100]), np.array([35, 255, 255])
    green_lower,  green_upper  = np.array([36,  80,  80]),   np.array([85, 255, 255])

    # Create masks
    red_mask1 = cv2.inRange(hsv, red_lower1, red_upper1)
    red_mask2 = cv2.inRange(hsv, red_lower2, red_upper2)
    red_mask  = cv2.bitwise_or(red_mask1, red_mask2)

    yellow_mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    green_mask  = cv2.inRange(hsv, green_lower,  green_upper)

    # Small dilation to reduce noise
    kernel = np.ones((3,3), np.uint8)
    red_mask    = cv2.dilate(red_mask,    kernel, iterations=1)
    yellow_mask = cv2.dilate(yellow_mask, kernel, iterations=1)
    green_mask  = cv2.dilate(green_mask,  kernel, iterations=1)

    # Helper function: find largest contour area
    def largest_area(mask):
        _, contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if not contours:
            return 0
        largest = max(contours, key=cv2.contourArea)
        return cv2.contourArea(largest)

    red_area    = largest_area(red_mask)
    yellow_area = largest_area(yellow_mask)
    green_area  = largest_area(green_mask)

    # Decide which color has the largest area above a threshold
    MIN_AREA = 100  # tune based on real-world scale
    color_areas = [('red', red_area), ('yellow', yellow_area), ('green', green_area)]
    color_areas.sort(key=lambda x: x[1], reverse=True)

    best_color, best_area = color_areas[0]
    if best_area >= MIN_AREA:
        return best_color
    else:
        return 'unknown'


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    print("Trrafic light is:", end="" , flush=True)
    status_buffer = ""

    while True:
        __len_to_clear = len(status_buffer) - len(shell_color_reset) - len(shell_colors['green'])
        # Cleans out the last status string
        print( '\b' * __len_to_clear , " " * (__len_to_clear-2) , '\b' * __len_to_clear , end="")


        ret, frame = cap.read()
        if not ret:break

        # Reduce the frame size
        frame = cv2.resize(frame, (640, 480))

        color = detect_color(frame)

        status_buffer = f"{shell_colors[color]}{color}{shell_color_reset}"
        print(status_buffer, end="", flush=True)
        sleep(0.1)
