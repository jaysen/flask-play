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

    if 'last_page' in session and session['last_page'] != page_name:
        counters[page_name] += 1
    session['last_page'] = page_name
    return render_template(template_name, counter=counters[page_name])


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
