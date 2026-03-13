try:
    with open('input.txt','r',encoding='utf-8') as file:
        lines = file.readlines()

    n = int(lines[0].strip())
    actual_count = len(lines) - 1

    if actual_count == n:
        result = "YES"
    else:
        result = "NO"

except ValueError:
    result = "ERROR"

except Exception:
    result = "ERROR"

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(result)