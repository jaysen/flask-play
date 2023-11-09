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

# API:

@app.route('/api/counters', methods=['GET'])
def get_counters():
    return jsonify(counters)

@app.route('/api/counters/home', methods=['GET'])
def get_home_counter():
    return jsonify({'count': counters['home']})

@app.route('/api/counters/tab1', methods=['GET'])
def get_tab1_counter():
    return jsonify({'count': counters['tab1']})

@app.route('/api/counters/tab2', methods=['GET'])
def get_tab2_counter():
    return jsonify({'count': counters['tab2']})



if __name__ == '__main__':
    app.run(debug=True)
