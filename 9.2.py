with open('input.txt','r',encoding='utf-8') as file:
    with open('output.txt','w',encoding='utf-8') as new_file:
        for line in file:

            if line.strip() and (line.strip()[0] == 'a' or line.strip()[0] == ' A'):
                new_file.write(line)

