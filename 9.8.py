with open('input.txt','r',encoding='utf-8') as file:
    steps = [int(line.strip()) for line in file if line.strip()]

feb=29 if len(steps) == 366 else 28
days_in_month=[31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

averages = []
current_index = 0

for days in days_in_month:
    month_steps = steps[current_index: current_index + days]
    avg = sum(month_steps) / days
    averages.append(avg)
    current_index += days

with open('output.txt', 'w', encoding='utf-8') as f:
    for avg in averages:
        f.write(f"{avg}\n")