from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Load your JSON file
with open('companies.json', 'r') as f:
    data = json.load(f)

@app.route('/')
def index():
    return render_template('index.html', results=None)

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')

    # Perform a simple search
    results = [camp for camp in data['companies'] if query.lower() in camp['name'].lower()]
    print(results)

    return render_template('search_results.html', results=results)

@app.route('/search', methods=['GET'])
def search_redirect():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)