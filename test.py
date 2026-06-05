# generate_index.py
from app import sum

result = sum(5, 3)
with open("index.html", "w") as f:
    f.write(f"""
    <!DOCTYPE html>
    <html>
    <head><title>Результат</title></head>
    <body>
        <h1>Результат вычисления</h1>
        <p>sum(5, 3) = {result}</p>
    </body>
    </html>
    """)
