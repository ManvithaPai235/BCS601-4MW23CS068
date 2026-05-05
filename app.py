from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    password = request.form['password']
    
    strength = 0

    if len(password) >= 8:
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in "!@#$%^&*()" for c in password):
        strength += 1

    if strength <= 2:
        result = "Weak ❌"
    elif strength <= 4:
        result = "Medium ⚠️"
    else:
        result = "Strong ✅"

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
