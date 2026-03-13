import os

os.makedirs('simple', exist_ok=True)

with open('input.txt', 'r', encoding='utf-8') as file:
    with open('simple/output.txt', 'w', encoding='utf-8') as catalog:

        for line_number, line in enumerate(file, start=1):
            if line_number % 2 == 0:
                catalog.write(line)