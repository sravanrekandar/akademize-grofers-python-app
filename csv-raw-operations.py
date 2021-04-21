content = open("dummy-data.csv", "r").read()
lines = content.split("\n")

# Extracting the header row
header_row = lines[0].split(",")

# extracting the record rows
lines = lines[1:]

# Preparing a multi dimensional array - records
records = []
count = 0
for line in lines:
    cells = line.split(",")
    cells = cells[:5]  # keeping only the first 5 cells
    records.append(cells)

# Printing the first 5 records
for record in records[:5]:
    print(record)

"""
[
    ['1', '0', '0', '1', '410'],
    ['2', '0', '0', '1', '361'],
    ['3', '0', '0', '1', '19'],
    ['4', '0', '0', '1', '57'],
    ['5', '0', '0', '1', '190']
]
"""


# Summing up the 5th column values
sum = 0
for record in records[:5]:
    sum += int(record[4])

print(f"Sum of {header_row[4]} = {sum}")


# Filtering out the records with 4th column value = 0
filtered_records = []
for record in records:
    is_flat_d = int(record[3])
    if is_flat_d == 0:
        filtered_records.append(record)

print("Filtered records..")
for record in filtered_records:
    print(record)

# Extract required columns 0 and 1 (Item Id and d_value)
new_record_set = [
    ["item_id", "d_value"]
]
for record in records:
    item_id = record[0]
    d_value = record[4]
    new_record = [item_id, d_value]
    new_record_set.append(new_record)

print("First 5 records in new record set..")
for record in new_record_set[:5]:
    print(record)

# Prepare a string of csv
new_record_lines = []
for record in new_record_set:
    new_record_lines.append(",".join(record))

new_records_content = "\n".join(new_record_lines)
f = open("out_put.csv", "w")
f.write(new_records_content)
print("New record set has been written to out_put.csv")
