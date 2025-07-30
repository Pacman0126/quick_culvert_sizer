import numpy as np
from matplotlib import pyplot as plt

###x1 = np.linspace(0.0, 20.0)
###x2 = np.linspace(0.0, 20.0)

##!#y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
###y2 = np.cos(2 * np.pi * x2)

x_values = [1,5,7,15]
y_values = [8,10,6,10]

#plt.subplot(1, 2, 1)
plt.scatter(x_values, y_values)
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')
plt.ion()
plt.show()

while True:
        print("Please enter target coordinates e.g. x,y")

        coord_str = input("Enter your data here:\n")
        coordinate = coord_str.split(",")

        if any(item == "-1" for item in coordinate):
            print("Exit game")
            plt.close("all")
            break
        else:
             x_values.append(int(coordinate[0]))
             y_values.append(int(coordinate[1]))
             #plt.close("all")
             plt.scatter(x_values, y_values)             
             #plt.show()    
    #return sales_data

#plt.subplot(1, 2, 2)
#plt.plot(x2, y2, 'r.-')
#plt.xlabel('time (s)')
#plt.ylabel('Undamped')




