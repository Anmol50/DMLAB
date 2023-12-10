import csv
def calculate_five_number_summary(data):
    sorted_data = sorted(data)
    n = len(data)

    # Calculate Minimum
    minimum = sorted_data[0]

    # Calculate Q1 (First Quartile)
    q1_index = int((n + 1) / 4) - 1
    q1 = sorted_data[q1_index]

    # Calculate Median (Second Quartile)
    median_index = int((n + 1) / 2) - 1
    median = sorted_data[median_index]

    # Calculate Q3 (Third Quartile)
    q3_index = int(3 * (n + 1) / 4) - 1
    q3 = sorted_data[q3_index]

    # Calculate Maximum
    maximum = sorted_data[-1]

    summary = {
        'Min': minimum,
        'Q1': q1,
        'Median': median,
        'Q3': q3,
        'Max': maximum
    }

    return summary

if __name__ == "__main__":
    # Input data (replace with your own data)
    # data = [1, 2, 3, 4, 5, 6, 7, 8]
    file_path = 'input_data.csv'
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [float(row[0]) for row in reader]
    # Calculate 5-number summary
    summary = calculate_five_number_summary(data)

    # Print the results
    for stat, value in summary.items():
        print(f"{stat}: {value}")
