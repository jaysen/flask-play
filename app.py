from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Initialize counters
counters = {
    'home': 0,
    'tab1': 0,
    'tab2': 0
}


@app.route('/')
def home():
    counters['home'] += 1
    return render_template('home.html', counter=counters['home'], total=sum(counters.values()))

@app.route('/tab1')
def tab1():
    counters['tab1'] += 1
    return render_template('tab1.html', counter=counters['tab1'], total=sum(counters.values()))

@app.route('/tab2')
def tab2():
    counters['tab2'] += 1
    return render_template('tab2.html', counter=counters['tab2'], total=sum(counters.values()))





if __name__ == '__main__':
    app.run(debug=True)
