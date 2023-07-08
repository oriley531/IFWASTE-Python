import matplotlib.pyplot as plt

def create_line_graph(weekly_average):
    # Generate x-axis values for weeks
    weeks = range(1, len(weekly_average) + 1)

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the data as a line graph
    ax.plot(weeks, weekly_average, marker='o', linestyle='-', color='b')

    # Set labels and title
    ax.set_xlabel('Weeks')
    ax.set_ylabel('Weekly Average')
    ax.set_title('Weekly Average Line Graph')

    # Display the graph
    plt.show()


