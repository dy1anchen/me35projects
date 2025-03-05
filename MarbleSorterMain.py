import RPi.GPIO as GPIO
import time

# Set up GPIO mode and warnings
GPIO.setmode(GPIO.BOARD)

# Set the pins
servo_pin = 33
pusher_pin = 32
light = 37
s0 = 13
s1 = 15
s2 = 16
s3 = 18
sig = 22 #labeled "out" on your board
cycles = 10

# Set up the servo pins and sensor light
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(pusher_pin, GPIO.OUT)
GPIO.setup(light, GPIO.OUT)
GPIO.output(light, GPIO.HIGH)

# Create a PWM instance
pwm = GPIO.PWM(servo_pin, 50)  # 50Hz frequency
pwm2 = GPIO.PWM(pusher_pin, 50)

# Start PWM with 0 duty cycle
pwm.start(0)
pwm2.start(0)

# Setup GPIO and pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(s0, GPIO.OUT)
GPIO.setup(s1, GPIO.OUT)
GPIO.setup(s2, GPIO.OUT)
GPIO.setup(s3, GPIO.OUT)
GPIO.setup(sig, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Set frequency scaling
GPIO.output(s0, GPIO.HIGH)
GPIO.output(s1, GPIO.LOW)

def DetectColor():
    # Detect red values
    GPIO.output(s2, GPIO.LOW)
    GPIO.output(s3, GPIO.LOW)
    time.sleep(0.1)
    start_time = time.time()
    for count in range(cycles):
        GPIO.wait_for_edge(sig, GPIO.FALLING)
    duration = time.time() - start_time
    red = cycles / duration
   
    # Detect blue values
    GPIO.output(s2, GPIO.LOW)
    GPIO.output(s3, GPIO.HIGH)
    time.sleep(0.1)
    start_time = time.time()
    for count in range(cycles):
        GPIO.wait_for_edge(sig, GPIO.FALLING)
    duration = time.time() - start_time
    blue = cycles / duration

    # Detect green values
    GPIO.output(s2, GPIO.HIGH)
    GPIO.output(s3, GPIO.HIGH)
    time.sleep(0.1)
    start_time = time.time()
    for count in range(cycles):
        GPIO.wait_for_edge(sig, GPIO.FALLING)
    duration = time.time() - start_time
    green = cycles / duration

    return [red, blue, green]

def set_angle(angle):
    duty_cycle = angle / 18 + 2
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

def push_ball():
    duty_cycle = 10
    GPIO.output(pusher_pin, True)
    pwm2.ChangeDutyCycle(duty_cycle)
    time.sleep(1)
    GPIO.output(pusher_pin, False)
    pwm2.ChangeDutyCycle(2)

try:
    #arrays for average of each color, order is [red, green, blue]
    r = [4000, 2000, 1600]
    b = [2500, 5000, 3000]
    g = [2800, 2200, 3100]
    y = [7600, 4000, 5500]
    rge = 1000
    ball_detected = False


    while True:
        # Check ball Color
        colors = DetectColor()
        print("-----------------------------------------")
        print("red = ", colors[0])
        print("blue = ", colors[1])
        print("green = ", colors[2])

        # Move track to correct color
        # Check red
        if ((colors[0] > (r[0] - rge)) and (colors[0] < (r[0] + rge)) and (colors[1] > (r[1] - rge))
             and (colors[1] < (r[1] + rge)) and (colors[2] > (r[2] - rge)) and (colors[2]) < (r[2] + rge)):
            print("RED BALL DETECTED!")
            ball_detected = True
            set_angle(97)

        # Check blue 
        if ((colors[0] > (b[0] - rge)) and (colors[0] < (b[0] + rge)) and (colors[1] > (b[1] - rge))
             and (colors[1] < (b[1] + rge)) and (colors[2] > (b[2] - rge)) and (colors[2]) < (b[2] + rge)):
            print("BLUE BALL DETECTED!")
            ball_detected = True
            set_angle(130)
        # Check green
        if ((colors[0] > (g[0] - rge)) and (colors[0] < (g[0] + rge)) and (colors[1] > (g[1] - rge))
             and (colors[1] < (g[1] + rge)) and (colors[2] > (g[2] - rge)) and (colors[2]) < (g[2] + rge)):
            print("GREEN BALL DETECTED!")
            ball_detected = True
            set_angle(160)
        # Check yellow
        if ((colors[0] > (y[0] - rge)) and (colors[0] < (y[0] + rge)) and (colors[1] > (y[1] - rge))
             and (colors[1] < (y[1] + rge)) and (colors[2] > (y[2] - rge)) and (colors[2]) < (y[2] + rge)):
            print("YELLOW BALL DETECTED!")
            ball_detected = True
            set_angle(220)

        time.sleep(0.5)

        # Check if ball has been detected
        if (ball_detected == True):
            print("PUSHING BALL!")
            push_ball()
            time.sleep(1)
            ball_detected = False

except KeyboardInterrupt:
    # Clean up on Ctrl+C
    pwm.stop()
    GPIO.cleanup()