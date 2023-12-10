import csv
import os

def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [float(row[0]) for row in reader]
    return header, data

def min_max_scaling(data, min_val, max_val):
    min_data, max_data = min(data), max(data)
    scaled_data = [(x - min_data) / (max_data - min_data) * (max_val - min_val) + min_val for x in data]
    return scaled_data

def z_score_normalization(data):
    mean_data, std_data = sum(data) / len(data), (sum((x - mean_data) ** 2 for x in data) / len(data)) ** 0.5
    normalized_data = [(x - mean_data) / std_data for x in data]
    return normalized_data

def write_to_csv(original_data, normalized_data, output_file):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Original Data', 'Normalized Data'])
        for row in zip(original_data, normalized_data):
            writer.writerow(row)

if __name__ == "__main__":
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'pyInput.csv')
    header, data = read_csv(file_path)

    normalization_type = input("Enter the normalization type (min-max/z-score): ").lower()

    if normalization_type == 'min-max':
        min_val, max_val = float(input("Enter the minimum value for Min-Max normalization: ")), float(input("Enter the maximum value for Min-Max normalization: "))
        normalized_data = min_max_scaling(data, min_val, max_val)
        output_file_path = os.path.join(current_dir, 'min_max_normalized_output.csv')
    elif normalization_type == 'z-score':
        normalized_data = z_score_normalization(data)
        output_file_path = os.path.join(current_dir, 'z_score_normalized_output.csv')
    else:
        print("Invalid normalization type. Please enter 'min-max' or 'z-score'.")
        exit()

    write_to_csv(data, normalized_data, output_file_path)
    print(f"{normalization_type.capitalize()} normalized data written to {output_file_path}")
