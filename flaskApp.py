import os
from flask import Flask, render_template, request, url_for

# Import the main processing function from your new.py script
from new import process_business_idea

# Create an instance of the Flask class
app = Flask(__name__)

# This route handles the home page
@app.route('/')
def index():
    """Renders the HTML form."""
    return render_template('app.html')

# This route handles the form submission
@app.route('/process', methods=['POST'])
def process():
    """
    Takes the user's idea from the form, calls the processing
    script, and renders the results page.
    """
    user_input = request.form['user_text']

    # --- Call your processing logic from new.py ---
    # The 'process_business_idea' function will do all the work
    # and return a dictionary containing the results and file paths.
    results = process_business_idea(user_input)
    # -----------------------------------------------

    # Render a new template to display the results.
    # We pass the 'results' dictionary and the original 'idea' to the template.
    return render_template('results.html', results=results, idea=user_input)


if __name__ == '__main__':
    # Flask serves files from a 'static' folder. We ensure it exists.
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(debug=True)
