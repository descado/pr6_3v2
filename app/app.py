from flask import Flask, request
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )
    return connection

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None  # Инициализируем переменную результата как None
    if request.method == 'POST':
        try:
            # Получаем числа из формы
            number1 = int(request.form['number1'])
            number2 = int(request.form['number2'])
            result = number1 + number2

            # Запись в базу данных
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO operations (number1, number2, result) VALUES (%s, %s, %s)",
                           (number1, number2, result))
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            result = f"Произошла ошибка: {e}"

    # Генерация HTML-кода как строки
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Sum Numbers</title>
    </head>
    <body>
        <h1>Sum Two Numbers</h1>
        <form method="post">
            <label for="number1">Number 1:</label>
            <input type="text" id="number1" name="number1" required>
            <br>
            <label for="number2">Number 2:</label>
            <input type="text" id="number2" name="number2" required>
            <br>
            <button type="submit">Submit</button>
        </form>
    """
    
    # Если результат вычисления есть, выводим его
    if result is not None:
        html += f"<h2>Result: {result}</h2>"
    else:
        html += "<p>Введите два числа и нажмите Submit.</p>"
    
    html += """
    </body>
    </html>
    """

    return html  # Возвращаем HTML строку

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
