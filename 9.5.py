result_message = ""

try:

    with open('input.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

        if len(lines) < 3:
            raise ValueError("Файл input.txt должен содержать как минимум 3 числа.")

        num1 = int(lines[0].strip())
        num2 = int(lines[1].strip())
        num3 = int(lines[2].strip())


    division_result = num1 / num2
    final_result = division_result + num3
    result_message = f"Результат: {final_result}"

except ValueError as e:
    result_message = f"ValueError: {str(e)}"

except ZeroDivisionError:
    result_message = "Ошибка вычисления: Деление на ноль невозможно."

except Exception as e:
    result_message = f"Неизвестная ошибка: {str(e)}"

finally:

    with open('output.txt', 'w', encoding='utf-8') as f_out:
        f_out.write(result_message)