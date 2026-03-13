def to_day_of_year(date_str):

    day = int(date_str[:2])
    month = int(date_str[3:5])
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(days_in_month[:month - 1]) + day


with open('input.txt', 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()]

current_date = lines[0]
n = int(lines[1])

current_day = to_day_of_year(current_date)

result_cells = []
for i in range(2, 2 + n):
    cell, date = lines[i].split()
    start_day = to_day_of_year(date)

    if current_day - start_day > 3:
        result_cells.append(cell)

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(result_cells))