import myactuator_rmd_py as rmd
import time
import numpy as np

start_time = time.time()  # Record the start timea

driver = rmd.CanDriver("can0")
node_id = 3
actuator = rmd.ActuatorInterface(driver, node_id)

actuator.setAcceleration(0, rmd.actuator_state.AccelerationType.POSITION_PLANNING_ACCELERATION)
actuator.setAcceleration(0, rmd.actuator_state.AccelerationType.POSITION_PLANNING_DECELERATION)

# Define the frequency of the sine wave (0.5 Hz for 1 period every 2 seconds)
frequency = 2
sample_rate = 500  # Number of samples per second (controls smoothness)

# Generate an array of time values from 0 to 2 seconds, for one period of the sine wave
x = np.linspace(0, 2 * np.pi * frequency, sample_rate * 2)  # 2 seconds for one full period
i = 0  # Index for accessing sine wave values
initial_angle = actuator.getMultiTurnAngle()

while True:
    # Calculate sine wave value and scale it to range between -45 and 45 degrees
    # angle = np.sin(x[i]) * 2 # current 
    angle = np.sin(x[i])*10 # position 

    #relative to initial angle 
    angle = angle + initial_angle

    # Send the calculated sine wave angle as an absolute setpoint
    actuator.sendPositionAbsoluteSetpoint(angle, 500.0)
    # actuator.sendVelocitySetpoint(angle)
    # output = actuator.sendCurrentSetpoint(angle)
    # Print the angle sent to the actuator
    print(f"Sent angle: {angle:.2f} degrees")
    
    # Update the index for the next angle
    i += 1
    if i >= len(x):
        i = 0  # Reset to loop through the sine wave again
    
    # Small pause (to match the sample rate)
    time.sleep(1 / sample_rate)
    # Get the current angle from the actuator
    current_angle = actuator.getMultiTurnAngle()
    print(f"Current actuator angle: {current_angle}")

    


# Shutdown the motor
actuator.shutdownMotor()
