from flask import Flask, render_template, jsonify, session

app = Flask(__name__)
app.secret_key = '3d6f45a5fc12445daacdecade11821a3'


# Initialize counters
counters = {
    'home': 0,
    'tab1': 0,
    'tab2': 0
}

def handle_page(page_name, template_name):
    if 'last_page' not in session or counters[page_name] == 0 or session['last_page'] != page_name:
        print('adding to counter ' + page_name)
        counters[page_name] += 1
    else:
        print('not adding to counter ' + page_name)
    session['last_page'] = page_name
    return render_template(template_name, counter=counters[page_name], total=sum(counters.values()))

@app.route('/')
def home():
    return handle_page('home', 'home.html')

@app.route('/tab1')
def tab1():
    return handle_page('tab1', 'tab1.html')

@app.route('/tab2')
def tab2():
    return handle_page('tab2', 'tab2.html')

####################
# API:
####################

@app.route('/api/counters', methods=['GET'])
def get_counters():
    return jsonify(counters)

@app.route('/api/counter/<page>', methods=['GET'])
def get_counter(page):
    if page in counters:
        return jsonify({'count': counters[page]})
    else:
        return jsonify({'error': 'Invalid page'}), 400

@app.route('/api/counters/reset', methods=['POST'])
def reset_counters():
    counters['home'] = 0
    counters['tab1'] = 0
    counters['tab2'] = 0
    return jsonify(counters)


if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)
