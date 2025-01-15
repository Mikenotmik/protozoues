import board
import digitalio
import time

# Set up pins
pins = [board.GP18, board.GP19, board.GP20, board.GP21]  # Data lines
clock_pin = board.GP15 # Clock line

# Initialize pins
data_lines = [digitalio.DigitalInOut(pin) for pin in pins]
for line in data_lines:
    line.direction = digitalio.Direction.OUTPUT
clock = digitalio.DigitalInOut(clock_pin)
clock.direction = digitalio.Direction.OUTPUT

def line(data):
    """
    Send a single 4-bit nibble on the data lines and toggle the clock.
    """
    for i, pin in enumerate(data_lines):
        pin.value = (data >> i) & 1  # Set each pin according to the nibble
    clock.value = True
    time.sleep(0.01)  # Stabilize data before toggling
    clock.value = False

def send(value):
    """
    Send a 16-bit integer value as 4 nibbles.
    """
    # Split the 16-bit value into 4 nibbles
    nibbles = [(value >> shift) & 0xF for shift in range(12, -1, -4)]
    print(f"Sending value: {value}, Nibbles: {nibbles}")

 

    # Send each nibble
    for nibble in nibbles:
        line(nibble)

    

# Main loop
value = 0  # Starting value
while True:
    send(value)  # Send the current value
    value += 1  # Increment value
    time.sleep(1)  # Delay between transmissions

