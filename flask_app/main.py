from flask import Flask
from flask import render_template

# To run through commandline, use flask run
app = Flask(__name__, template_folder='templates/', static_folder='static/', instance_relative_config=False)


# Route for the text editor page
@app.route("/", methods=['GET', 'POST'])
def display_index():
    return render_template('index.html')
