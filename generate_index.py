# generate_index.py
from app import sum

# Вычисляем что-то с помощью функции из app.py
result = sum(5, 7)
message = "Тесты пройдены успешно!"  # можно и результат test.py сюда добавить

html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>CI/CD Демо</title>
    <style>
        body {{
            font-family: sans-serif;
            max-width: 600px;
            margin: 50px auto;
            text-align: center;
            background: #f0f4ff;
        }}
        .result {{
            font-size: 2em;
            color: #1e466e;
            background: white;
            padding: 20px;
            border-radius: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }}
    </style>
</head>
<body>
    <h1>🚀 Результат работы CI/CD</h1>
    <div class="result">
        <p>sum(5, 7) = <strong>{result}</strong></p>
        <p>✅ {message}</p>
    </div>
    <p><small>Страница сгенерирована автоматически из Python‑скрипта</small></p>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("index.html успешно создан!")
