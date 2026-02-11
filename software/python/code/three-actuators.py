import myactuator_rmd_py as rmd
import time
import numpy as np

# Function to control all actuators inside the same while loop
def control_all_actuators():
    # Define amplitude and frequency as lists, one for each node
    amplitudes = [0, 0, 30]  # Amplitude of sine wave (degrees) for nodes 1, 2, 3
    frequencies = [2, 2, 1]  # Frequency of sine wave (Hz) for nodes 1, 2, 3
    sample_rate = 500  # Sample rate for smoothness of motion (samples per second)

    # List of node IDs to control
    node_ids = [1, 2, 3]

    # Create the CAN driver
    driver = rmd.CanDriver("can0")

    # Create actuator interfaces for each node ID
    actuators = [rmd.ActuatorInterface(driver, node_id) for node_id in node_ids]

    # Set acceleration and deceleration for each actuator
    for actuator in actuators:
        actuator.setAcceleration(0, rmd.actuator_state.AccelerationType.POSITION_PLANNING_ACCELERATION)
        actuator.setAcceleration(0, rmd.actuator_state.AccelerationType.POSITION_PLANNING_DECELERATION)

    # Generate time values for one full sine wave period (set max frequency)
    x_max_freq = max(frequencies)  # Get the highest frequency for the sine wave duration
    x = np.linspace(0, 2 * np.pi * x_max_freq, sample_rate * 2)  # 2 seconds for one full period
    i = 0  # Index for accessing sine wave values

    # Store the initial angles of the actuators
    initial_angles = [actuator.getMultiTurnAngle() for actuator in actuators]

    # Main control loop for actuators
    while True:
        # Calculate sine wave values for all actuators and scale it to their respective amplitude range
        angles = [
            np.sin(x[i] * frequencies[idx]) * amplitudes[idx] + initial_angles[idx]
            for idx in range(len(node_ids))
        ]

        # Send the calculated sine wave angles as absolute setpoints for all actuators
        for idx, actuator in enumerate(actuators):
            # Use node_id directly for printing
            node_id = node_ids[idx]
            actuator.sendPositionAbsoluteSetpoint(angles[idx], 500.0)
            # Print the angle sent to the actuator
            print(f"Sent angle to Node {node_id}: {angles[idx]:.2f} degrees")

        # Update the index for the next angle
        i += 1
        if i >= len(x):
            i = 0  # Reset to loop through the sine wave again

        # Small pause to match the sample rate
        time.sleep(1 / sample_rate)

        # Get and print the current angles from all actuators
        for idx, actuator in enumerate(actuators):
            node_id = node_ids[idx]
            current_angle = actuator.getMultiTurnAngle()
            print(f"Node {node_id} - Current angle: {current_angle:.2f} degrees")

    # Shutdown the motors (optional: add a stopping condition or keyboard interrupt)
    for actuator in actuators:
        actuator.shutdownMotor()

# Start controlling all actuators
if __name__ == "__main__":
    control_all_actuators()
