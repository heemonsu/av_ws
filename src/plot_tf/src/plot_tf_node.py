import tf
import rospy
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

class PlotTrajectory():
    def __init__(self):
        # Define variable for the plot
        self.xdata=[]
        self.ydata=[]
        self.zdata=[]

        # Define plot properties
        self.ax = plt.axes(projection='3d')
        self.ax.axis('equal')
        self.ax.set_xlabel('X(m)')
        self.ax.set_ylabel('Y(m)')
        self.ax.set_zlabel('Z(m)')


    def plot_points(self, x, y, z):
        # Append input data to previous stream
        self.xdata.append(x)
        self.ydata.append(y)
        self.zdata.append(z)

        # Plot data on the figure
        self.fig = plt.figure()
        self.ax.plot3D(self.xdata, self.ydata, self.zdata, 'green')

        self.ax.relim()
        self.ax.autoscale_view()
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()


def main():
    plot = PlotTrajectory()
    zline = np.linspace(0, 15, 1000)
    xline = np.sin(zline)
    yline = np.cos(zline)

    # Plot loop
    for i in range(zline.size):
        print("Plotting point", xline[i], yline[i], zline[i])
        plot.plot_points(xline[i], yline[i], zline[i])

if __name__=="__main__":
    main()




