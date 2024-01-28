from flask import Flask, render_template
app = Flask(__name__)

@app.route('/Agam')
def first_webpage():
    return render_template('index.html', variable='Flask')
@app.route('/Kris')
def second_webpage():
    return render_template('index2.html', variable='Flask')
@app.route('/Mom')
def third_webpage():
    return render_template('index3.html', variable='Flask')
@app.route('/Dad')
def fourth_webpage():
    return render_template('index4.html', variable='Flask')
app.run(debug=True)