from flask import Flask, request
from flask import render_template
from LanguageHelper import LanguageHelper
from helper import untitled, get_documents_length
from models import text_document, db
import dotenv, os

# To run through commandline, use flask run
app = Flask(__name__, template_folder='templates/', static_folder='static/', instance_relative_config=False)

# Connect to the database
dotenv.load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("config")
db.init_app(app)

@app.route("/")  # displays a list of the saved documents from the DB
def home():
    db.create_all()
    documents = text_document.query.order_by(text_document.id.desc()).all()
    length = get_documents_length(documents)
    return render_template("index.html", documents=documents, length=length)

# Route for the text editor page
@app.route("/editor<int:id>", methods=['GET', 'POST'])
def display_index(id):
    document = text_document.query.get(id)
    print(document)
    return render_template('editor.html', document=document)


@app.route("/autoCorrect", methods=["POST"])  # Listens for Javascript Autocorrect AJAX Call
def autocorrect():  # Retrieves text from JS and autocorrects it
    lang_helper = LanguageHelper()
    text = request.get_json()
    correct_text = lang_helper.auto_correction(text)
    errs = lang_helper.return_errors(text)  # writes to JSON
    print(text)
    print(correct_text)
    return correct_text

@app.route("/saveFile", methods=["POST"])  # Listens for Javascript SaveFile function
def saveFile():  # Retrieves data from JS and saves it to DB
    data = request.get_json()
    
    # Create new text_document if DNE in DB 
    if data["id"] == "":
        name = untitled(data["name"])
        document = text_document(name=name, text=data["text"])
        db.create_all()
        document.save()
    else:  # Update text_document if it currently exists in the DB
        document = text_document.query.get(int(data["id"]))
        db.create_all()
        name = untitled(data["name"])
        document.name = name
        document.text = data["text"]
        document.save()
    return str(document.id)

if __name__ == "__main__":
    app.run(debug=True)
