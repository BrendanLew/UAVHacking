from djitellopy import tello
import time

# Initialize the Tello drone
drone = tello.Tello()

# Connect to the drone

drone.connect()
print("Battery:", drone.get_battery())

# Take off
drone.takeoff()
time.sleep(5)  # Wait for the drone to stabilize after takeoff

# Move forward
drone.move_forward(50)  # Move forward 100 cm
time.sleep(2)  # Wait for the movement to complete
drone.rotate_clockwise(90)  # Rotate 90 degrees clockwise
time.sleep(2)  # Wait for the rotation to complete

# Land the drone
drone.land()
time.sleep(5) # Wait for the drone to land

# Disconnect from the drone
drone.end()
print("Disconnected from the drone.")

# Print final battery status
print("Final Battery:", drone.get_battery())

# End the script
print("Test completed successfully.")
