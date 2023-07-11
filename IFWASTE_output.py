import matplotlib.pyplot as plt
import csv
  
def create_multi_plot_line_graph(data_dict):
    plt.figure(figsize=(10, 6))  # Set the figure size

    # Iterate over each key-value pair in the dictionary
    for key, values in data_dict.items():
        x = list(range(1, len(values) + 1))  # Generate x-axis values
        plt.plot(x, values, label=key)  # Plot the values with a label

    plt.xlabel('Weeks')  # Set the label for the x-axis
    plt.ylabel('kg of FW')  # Set the label for the y-axis
    plt.title('Food Waste')  # Set the title for the graph
    plt.legend()  # Show the legend
    plt.grid(True)  # Show the grid
    plt.show()  # Display the graph

def write_dict_to_csv(data_dict, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Key', 'Values'])  # Write header row

        # Iterate over each key-value pair in the dictionary
        for key, values in data_dict.items():
            writer.writerow([key] + values)
