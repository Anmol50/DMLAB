import csv
from collections import defaultdict
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder

def read_transactions(file_path):
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        return defaultdict(list, {i + 1: [item.strip() for item in row if item.strip()] for i, row in enumerate(reader) if any(row)})

def mine_frequent_itemsets(transactions, min_support):
    te = TransactionEncoder()
    transformed_df = te.fit_transform(list(transactions.values()))
    frequent_itemsets = apriori(pd.DataFrame(transformed_df, columns=te.columns_), min_support=min_support, use_colnames=True)
    frequent_itemsets['itemsets'] = frequent_itemsets['itemsets'].apply(set)
    return frequent_itemsets

def main():
    input_file_path = 'input.csv'
    transactions = read_transactions(input_file_path)
    min_support = float(input("Enter the minimum support threshold (a value between 0 and 1): "))
    frequent_itemsets = mine_frequent_itemsets(transactions, min_support)

    print("\nFrequent Itemsets:")
    print(frequent_itemsets)

    output_file_path = 'output_frequent_itemsets.csv'
    frequent_itemsets.to_csv(output_file_path, index=False)
    print(f"\nFrequent itemsets saved to {output_file_path}")

if __name__ == "__main__":
    main()
