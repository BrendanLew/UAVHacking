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

# Move forward and rotate
# drone.move_forward(50) 
# time.sleep(2)
# drone.rotate_clockwise(90)
# time.sleep(2)

# Get telemerty data
height = drone.get_height()
temperature = drone.get_highest_temperature()
pitch = drone.get_pitch()
state = drone.get_current_state() # Gathers all telemery data in one command

print("Height:", height)
print("Temp_High:", temperature)
print("Pitch:", pitch)  

print("State:", state)

# Video Stream
drone.streamon()
frame_read = drone.get_frame_read()
frame = frame_read.frame

print(frame)

drone.streamoff()
time.sleep(3)

# Land the drone
drone.land()
time.sleep(5) # Wait for the drone to land

# Disconnect from the drone
drone.end()
print("Disconnected from the drone.")

# End the script
print("Test completed successfully.")
