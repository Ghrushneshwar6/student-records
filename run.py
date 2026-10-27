from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/save_data', methods=['POST'])
def save_data():
    regno = request.form.get('regno', '')
    name = request.form.get('name', '')
    standard = request.form.get('class', '')
    math = request.form.get('math', '')
    english = request.form.get('english', '')
    science = request.form.get('science', '')
    computer = request.form.get('computer', '')
    print(regno, name, standard, math, english, science, computer)

    return "Data Saved Successfully"


if __name__ == "__main__":
    app.run()
