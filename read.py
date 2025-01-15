import board
import digitalio
import time

# Set up pins
pins = [board.GP0, board.GP1, board.GP2, board.GP3]  # Data lines
clock_pin = board.GP4  # Clock line

# Initialize pins with pull-down resistors
data_lines = [digitalio.DigitalInOut(pin) for pin in pins]
for line in data_lines:
    line.direction = digitalio.Direction.INPUT
    line.pull = digitalio.Pull.DOWN  # Pull-down for stability

clock = digitalio.DigitalInOut(clock_pin)
clock.direction = digitalio.Direction.INPUT
clock.pull = digitalio.Pull.DOWN  # Pull-down for stability

def read():
    """
    Read a 4-bit nibble from the data lines.
    :return: Integer value (0-15) representing the nibble.
    """
    
    value = 0
    for i, pin in enumerate(data_lines):
        value |= (pin.value << i)  # Combine bits into a nibble
    return value

# Variables for tracking clock state
previous_clock_state = False

# Main loop
while True:
    # Read the current clock state
    current_clock_state = clock.value

    # Detect a rising edge (low -> high transition)
    if not previous_clock_state and current_clock_state:
        # Rising edge detected, read data
        data = read()
        print(f"Data received: {data}")

    # Update previous clock state
    previous_clock_state = current_clock_state

    # Small delay to prevent busy-waiting
    

