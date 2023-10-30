from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Load your JSON file
with open('companies.json', 'r') as f:
    data = json.load(f)

# Extract a list of unique categories from the data
categories = set(company['category'] for company in data['companies'])

@app.route('/')
def index():
    return render_template('index.html', results=None, categories=categories)

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    selected_category = request.form.get('category')

    # Perform a search with category filtering
    if query is not None:
        query = query.lower()

    if selected_category:
        results = [camp for camp in data['companies'] if
                   'name' in camp and camp['name'] and (query is None or query in camp['name'].lower()) and
                   'category' in camp and camp['category'] == selected_category]
    else:
        results = [camp for camp in data['companies'] if
                   'name' in camp and camp['name'] and (query is None or query in camp['name'].lower())]

    return render_template('search_results.html', results=results, categories=categories)


@app.route('/list')
def category_list():
    return render_template('list.html', categories=categories)

# Redirect to home if someone tries to access the search route with an unsupported method
@app.route('/search', methods=['GET'])
def search_redirect():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
