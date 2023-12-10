import pandas as pd

def perform_binning(data, column_to_bin, num_bins, bin_column_name, method):
    if method == 'width':
        data[bin_column_name] = pd.cut(data[column_to_bin], bins=num_bins, labels=[f'Bin{i+1}' for i in range(num_bins)], include_lowest=True)
    elif method == 'quantile':
        data[bin_column_name] = pd.qcut(data[column_to_bin], q=num_bins, labels=[f'Bin{i+1}' for i in range(num_bins)])
    
if __name__ == "__main__":
    input_file_path = 'input_data.csv'
    output_file_path_width = 'equal-width.csv'
    output_file_path_quantile = 'equal-frequency.csv'
    df = pd.read_csv(input_file_path)
    column_to_bin = 'value'  

    num_bins_width = int(input("Enter the number of bins for equal-width binning: "))
    num_bins_quantile = int(input("Enter the number of bins for equal-frequency binning: "))
    
    perform_binning(df, column_to_bin, num_bins_width, 'binned_width', 'width')
    df.to_csv(output_file_path_width, index=False)
    print(f"\nBinned data for equal-width saved to {output_file_path_width}\n")
    
    perform_binning(df, column_to_bin, num_bins_quantile, 'binned_quantile', 'quantile')
    df.to_csv(output_file_path_quantile, index=False)
    print(f"\nBinned data for equal-frequency saved to {output_file_path_quantile}\n")

