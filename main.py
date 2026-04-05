from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # нужен для flash-сообщений

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/doma')
def doma():
    return render_template('doma.html')

@app.route('/transport')
def transport():
    return render_template('transport.html')

@app.route('/pitanie')
def pitanie():
    return render_template('pitanie.html')

@app.route('/energiya')
def energiya():
    return render_template('energiya.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Простая валидация
        if not name or not email or not message:
            flash('Пожалуйста, заполните все поля', 'error')
            return redirect(url_for('feedback'))
        
        # Сохраняем в текстовый файл (можно заменить на БД)
        with open('messages.txt', 'a', encoding='utf-8') as f:
            f.write(f"Имя: {name}\nEmail: {email}\nСообщение: {message}\n{'='*40}\n")
        
        flash('Спасибо! Ваше сообщение отправлено.', 'success')
        return redirect(url_for('feedback'))
    
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug=True)