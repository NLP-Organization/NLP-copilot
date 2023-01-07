import language_tool_python
from flask import Flask, request
from flask import render_template
from helper import auto_correction, return_errors

# To run through commandline, use flask run
app = Flask(__name__, template_folder='templates/', static_folder='static/', instance_relative_config=False)


# Route for the text editor page
@app.route("/", methods=['GET', 'POST'])
def display_index():
    return render_template('editor.html')


@app.route("/autoCorrect", methods=["POST"])  # Listens for Javascript Autocorrect AJAX Call
def autocorrect():  # Retrieves text from JS and autocorrects it
    text = request.get_json()
    correct_text = auto_correction(text)
    tmp = language_tool_python.LanguageTool('en-US')  # temporary, just for testing
    errs = return_errors(1000, tmp, text)  # writes to JSON
    print(text)
    print(correct_text)
    return correct_text


if __name__ == "__main__":
    app.run(debug=True)
