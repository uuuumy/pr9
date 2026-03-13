a=[]
with open('input.txt','r',encoding='utf-8') as file:
    with open('output.txt','w',encoding='utf-8') as new_file:
        for line in file:
            if line:
                a.append(line[0])
        new_file.write(''.join(a))