import pandas as pd

# Создаем DataFrame
data = {
    'Name': ['John', 'Jane', 'Tom', 'Lucy'],
    'Age': [28,24,32,29],
    'City': ['New York', 'Paris', 'London', 'Tokyo']
}

df = pd.DataFrame(data)

# Печатаем DataFrame
print(df)

# Сохраняем DataFrame в CSV файл
df.to_csv('output.csv', index=False)