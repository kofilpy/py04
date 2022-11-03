# 3 рази на день зберігати на гіт на роботі
# ssh-keygen Згенерувати ключ
# cat ~/.ssh/id_rsa.pub Дізнатись ключ




def row_new_change(row: str) -> str:
    """Операції з рядками2"""
    if len(row) <= 10:
        first_part, last_part = row[:-3], row[-3:].lower()
        middle_length = int(len(first_part) / 2)
        new_row = first_part[:middle_length] + last_part + first_part[middle_length:]
        return new_row
    else:
        return "Введіть рядок розміром не більше 10 символів"


row = input()
row_new_change1 = row_new_change(row)
print(row_new_change1)

