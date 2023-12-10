import csv
import math

def load_data(file_path):
    with open(file_path, 'r') as file:
        data = list(csv.reader(file))
    return data

def calculate_mean(data):
    return sum(data) / len(data)

def calculate_correlation(x, y):
    n = len(x)
    mean_x = calculate_mean(x)
    mean_y = calculate_mean(y)

    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    denominator_x = math.sqrt(sum((xi - mean_x) ** 2 for xi in x))
    denominator_y = math.sqrt(sum((yi - mean_y) ** 2 for yi in y))

    correlation = numerator / (denominator_x * denominator_y)
    return correlation

if __name__ == "__main__":
    file_path = 'input_data.csv'

    # Load data from CSV file
    data = load_data(file_path)

    # Extract columns for X and Y variables
    x_column = [float(row[1]) for row in data[1:]]  # Assuming the first column is X
    y_column = [float(row[2]) for row in data[1:]]  # Assuming the second column is Y

    # Calculate correlation
    correlation_coefficient = calculate_correlation(x_column, y_column)

    # Print the result
    print(f"Correlation Coefficient: {correlation_coefficient}")
