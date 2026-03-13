with open('input.txt','r',encoding='utf-8') as f:
    content=f.read()
upp_content=content.upper()
with open('output.txt','w',encoding='utf-8') as new_f:
    new_f.write(upp_content)
print(upp_content)