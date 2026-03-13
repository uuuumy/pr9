with open('input.txt','r',encoding='utf-8') as file:
    with open('output.txt','w',encoding='utf-8') as new_file:
        for line in file:
            if len(line) > 20:
                new_file.write(line)