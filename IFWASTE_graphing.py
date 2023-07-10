import matplotlib.pyplot as plt
import csv

FW_generation = {"Total": [], "Meat & Fish": [], "Dairy & Eggs": [], "Fruits and Vegetables": [], "Baked Goods": [], "Dry Foods": [], "Snacks, Condiments, & Other": [], "Cooked/Prepared Items/Leftovers": []}

def FW_collect():
    week_FW = {"Total": 0, "Meat & Fish": 0, "Dairy & Eggs": 0, "Fruits and Vegetables": 0, "Baked Goods": 0, "Dry Foods": 0, "Snacks, Condiments, & Other": 0, "Cooked/Prepared Items/Leftovers": 0}
    for house in houses:
        for FW in house.waste_bin:
            week_FW[FW.type] += FW.amount_kg
            week_FW["Total"] += FW.amount_kg
            house.waste_bin.remove(FW)
            del FW
    for FW in week_FW: # adds total week amount to the data list
        FW_collect[FW].append(week_FW[FW])
  
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
