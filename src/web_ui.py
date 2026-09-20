import matplotlib.pyplot as plt


class RobotDashboard:

    def __init__(self):
        # Store the data received from the simulator
        self.times = []
        self.axis1_values = []

        # Create the chart
        plt.ion()

        self.fig, self.ax = plt.subplots()

    def updateDashboard(self, data_point):

        # Get values from the received record
        time_value = data_point["Time"].iloc[0]
        axis1_value = data_point["Axis #1"].iloc[0]

        # Add the new data
        self.times.append(time_value)
        self.axis1_values.append(axis1_value)

        # Clear and redraw the chart
        self.ax.clear()

        self.ax.plot(self.times, self.axis1_values)

        self.ax.set_title("Robot Axis #1 Streaming Data")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Axis #1")

        self.ax.tick_params(axis="x", rotation=45)

        plt.tight_layout()
        plt.pause(0.01)