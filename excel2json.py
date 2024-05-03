import pandas as pd
import json

# Открытие таблицы Excel
df = pd.read_excel('excel.xlsx')

# Преобразование таблицы в JSON
json_data = df.to_json(orient='records', force_ascii=False, indent=4)

# Запись JSON в файл
with open('output1.json', 'w', encoding='utf-8') as file:
    file.write(json_data)