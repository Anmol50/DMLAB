import pandas as pd

# Load data from CSV
file_path = 'input_data.csv'  # Replace with your CSV file path
data = pd.read_csv(file_path)

# Assuming columns 'X' and 'Y' represent the coordinates of the points
points = data[['X', 'Y']]

# Compute the initial center of the cluster
initial_cluster_center = points.mean()

# Print the initial cluster center
print("Initial Cluster Center:")
print(initial_cluster_center)

# Compute distances from each point to the initial cluster center manually
initial_distances = ((points - initial_cluster_center) ** 2).sum(axis=1) ** 0.5
print("\nDistances from Initial Cluster Center:")
print(initial_distances)

# Find the nearest point as the updated cluster center
nearest_point_index = initial_distances.idxmin()
updated_cluster_center = points.loc[nearest_point_index]

# Print the updated cluster center
print("\nUpdated Cluster Center:")
print(updated_cluster_center)

# Compute distances from the updated cluster center manually
updated_distances = ((points - updated_cluster_center) ** 2).sum(axis=1) ** 0.5
print("\nDistances from Updated Cluster Center:")
print(updated_distances)
