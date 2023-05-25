import time
import keyboard

# Function to perform key press and release actions
def perform_action(key, action_type):
    if action_type == 'Hold':
        keyboard.press(key)
    elif action_type == 'Release':
        keyboard.release(key)
    else:
        raise ValueError("Invalid action type: " + action_type)

# Delay function to pause execution
def delay(duration):
    time.sleep(duration)

# Macro actions
actions = [
    ('S', 'Hold', 0.25),
    ('', 'Delay', 0.25),
    ('space', 'Hold', 0.12),
    ('', 'Delay', 0.12),
    ('S', 'Release', 0),
    ('D', 'Hold', 0.25),
    ('', 'Delay', 0.25),
    ('W', 'Hold', 0),
    ('space', 'Release', 0.04),
    ('', 'Delay', 0.04),
    ('A', 'Hold', 0.05),
    ('', 'Delay', 0.05),
    ('D', 'Release', 0.03),
    ('', 'Delay', 0.03),
    ('W', 'Release', 0.15),
    ('', 'Delay', 0.15),
    ('A', 'Release', 0)
]

# Set initial delay
initial_delay = 0.5

# Wait for the user to focus on the desired window
print("Please click on the window where you want to perform the macro.")
time.sleep(initial_delay)

# Execute the macro
for action in actions:
    key, action_type, duration = action
    delay(duration)
    perform_action(key, action_type)
    print("Performed action:", key, action_type)

# Exit gracefully
keyboard.release('A')
keyboard.release('D')
keyboard.release('W')
keyboard.release('S')
print("Macro execution completed.")
