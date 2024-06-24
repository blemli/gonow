import RPi.GPIO as GPIO
import time

# GPIO-Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# Pin-Nummer festlegen
GPIO_PIN = 14

# Pin als Eingang festlegen
GPIO.setup(GPIO_PIN, GPIO.IN)

def is_dark():
    potentiometer=GPIO.input(GPIO_PIN)
    return bool(potentiometer)


if __name__ == "__main__":
    try:
        while True:
            input_state = GPIO.input(GPIO_PIN)
            print(f"GPIO14 state: {input_state}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Programm beendet")
    finally:
        GPIO.cleanup()
