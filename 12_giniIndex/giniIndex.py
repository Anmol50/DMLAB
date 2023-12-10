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

def calculate_gini_index(data, class_column):
    class_counts = data[class_column].value_counts()
    gini_index = 1 - sum((count / len(data))**2 for count in class_counts)
    return gini_index

file_path = 'data.csv'
data = pd.read_csv(file_path)
attributes = list(data.columns)
attributes.remove('CanGoOnTrip')
information_gains = {attribute: calculate_info_gain(data, attribute, 'CanGoOnTrip') 
                     for attribute in data.columns if attribute != 'CanGoOnTrip'}
max_gain_attribute = max(information_gains, key=information_gains.get)
max_gain_gini_index = calculate_gini_index(data, max_gain_attribute)
print("Information Gain for Each Attribute:")
for attribute, gain in information_gains.items():
    print(f"{attribute}: {gain}")
print(f"\nFor Attribute with Maximum Information Gain ('{max_gain_attribute}'):")
print(f"Information Gain: {information_gains[max_gain_attribute]}")
print(f"Gini Index: {max_gain_gini_index}")
