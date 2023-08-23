# importing the required module
import matplotlib.pyplot as plt
import sys
fileinput = []
fileinput = sys.argv
print(fileinput)

def outread(output_file):

    kj_per_ev = 6.242 * (10 ** 21)
    moles = 6.022 * (10 ** 23)

    kjmol_to_ev_multiplier = moles / kj_per_ev
    # Initialize arrays for column 1 and column 2 values
    column1_values = []
    column2_values = []

    # Read the .out file line by line
    with open(output_file, 'r') as file:
        lines = file.readlines()[1:]
        for line in lines:
            parts = line.strip().split()
            if len(parts) >= 2:
                column1_values.append(float(parts[0]))
                column2_values.append(float(parts[1]) * kjmol_to_ev_multiplier)

    return column1_values, column2_values

# plotting the points


def plotpoint(plotinput):

    for i in range(1, len(plotinput)):
        plotstr = plotinput[i]
        x, y = outread(plotstr)
        print(x, y)
        plt.plot(x, y, label=[i])

    plt.xlabel("Time (ps)")
    plt.ylabel("Energy (eV)")
    plt.title('Time vs eV of simulation')
    plt.legend(loc='upper center')
    plt.show()


plotpoint(fileinput)
