with open('input.txt','r',encoding='utf-8') as file:
    lines = file.readlines()
    
new_lines = []
for line in lines:
    if line.strip() != '100':
        new_lines.append(line)

with open('input.txt', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)