from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def homework():
  return render_template('homework.html')

@app.route('/about')
def about():
  works = ["Screaming Face", "Russian sadness", "Trapped inside my mind", "Loving"]
  return render_template('About.html', works=works)

@app.route('/works')
def works():
  return render_template('Works.html')


if __name__ == '__main__':
  app.run(debug=True)

