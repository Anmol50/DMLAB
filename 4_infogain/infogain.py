import pandas as pd
import math

def calculate_entropy(data, target_class):
    class_count = data[target_class].value_counts()
    entropy = 0
    for count in class_count:
        probability = count/len(data)
        entropy -= probability * math.log2(probability)

    return entropy

def calculate_info_gain(data, attribute, target_class):
    total_entropy = calculate_entropy(data, target_class)
    attribute_values = data[attribute].unique()

    attribute_entropy = 0
    for value in attribute_values:
        subset = data[data[attribute] == value]
        subset_entropy = calculate_entropy(subset, target_class)
        weight = len(subset) / len(data)
        attribute_entropy += weight * subset_entropy

    info_gain = total_entropy - attribute_entropy
    return info_gain

file_path = 'input_data.csv'
data = pd.read_csv(file_path)

attributes = list(data.columns)
attributes.remove('CanGoOnTrip')

for name in attributes:
    info_gain = calculate_info_gain(data, name ,'CanGoOnTrip')
    print(f"Info gain for attribute: {name} is {info_gain}")