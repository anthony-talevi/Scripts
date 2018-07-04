# numpy is used for creating fake data
import numpy as np
import matplotlib as mpl
import sys
import csv
## agg backend is used to create plot as a .png file
mpl.use('agg')
import matplotlib.pyplot as plt

# Get the command line arguments
# Check for correctness
num_args = len(sys.argv)

if(len(sys.argv)>3):
    print("Parameter Error: Too many parameters given.  Continuing, but ignoring the extra arguments.")
elif(len(sys.argv)<3):
    print("Parameter Error: No data file specified.  Cannot proceed.")
    quit()
else:
    try:
        # Get the data from the csv
        with open(sys.argv[1], 'rt', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            raw_data = list(reader)
        # Convert raw_data to numerical data
        data = []
        for c in raw_data:
            for j in c:
                data.append(float(j))

        #Create figure
        fig = plt.figure(1, figsize=(9,6))

        #Create the axis
        ax = fig.add_subplot(111)

        #Create the box boxplot
        ax.boxplot(data)

        #Save the figure as a png
        fig.savefig(sys.argv[2], bbox_inches='tight')

    except FileNotFoundError:
        print("ERROR: Could not find file.")
    except IOError:
        print("ERROR: Could not read file.")
