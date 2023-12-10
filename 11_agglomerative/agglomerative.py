import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

def load_data(file_path):
    return pd.read_csv(file_path, index_col=0)

def hierarchical_clustering(data, linkage_method='single'):
    # Perform hierarchical clustering
    clusters = linkage(data, method=linkage_method)

    # Plot the dendrogram (optional)
    dendrogram(clusters, labels=data.index, leaf_rotation=90)
    plt.title('Hierarchical Clustering Dendrogram')
    plt.xlabel('Data Points')
    plt.ylabel('Distance')
    plt.show()

    return clusters

def save_clusters_to_csv(clusters, output_file):
    pd.DataFrame(clusters).to_csv(output_file, header=False, index=False)

if __name__ == "__main__":
    file_path = 'input_data.csv'
    output_file = 'hierarchical_clusters.csv'

    # Load data from CSV file
    data = load_data(file_path)

    # Perform hierarchical clustering
    clusters = hierarchical_clustering(data, linkage_method='single')

    # Save clusters to CSV file
    save_clusters_to_csv(clusters, output_file)
