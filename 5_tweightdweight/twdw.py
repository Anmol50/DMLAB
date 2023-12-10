import csv
from collections import defaultdict

classrowcolMap = defaultdict(dict)
colMap = defaultdict(int)
rowMap = defaultdict(int)

with open("input.csv", mode="r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header
    for row in reader:
        row_name, col_name, count = row
        val = int(count)
        classrowcolMap[row_name][col_name] = val
        colMap[col_name] += val
        rowMap[row_name] += val

with open("output.csv", mode="w", newline='') as fw:
    writer = csv.writer(fw)
    writer.writerow(["Column\\row", "", "Bollywood", "", "", "Tollywood", "", "", "Total", "", ""])
    writer.writerow(["", "Count", "t-weight", "d-weight", "Count", "t-weight", "d-weight", "Count", "t-weight", "d-weight"])

    for r, row_count in rowMap.items():
        row_data = [r]
        for c, col_count in colMap.items():
            row_data.extend([classrowcolMap[r][c], (classrowcolMap[r][c] / row_count) * 100, (classrowcolMap[r][c] / col_count) * 100])
        row_data.extend([row_count, (row_count / row_count) * 100, (row_count / sum(rowMap.values())) * 100])
        writer.writerow(row_data)

    total_row = ["Total"]
    for c, col_count in colMap.items():
        total_row.extend([col_count, (col_count / sum(colMap.values())) * 100, (col_count / col_count) * 100])
    total_row.extend([sum(colMap.values()), 100, 100])
    writer.writerow(total_row)
