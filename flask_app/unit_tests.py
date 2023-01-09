"""
Tests for NLP-Copilot
"""

from flask import Flask
from flask_testing import TestCase
from unittest import main
from LanguageHelper import LanguageHelper
from flask_sqlalchemy import SQLAlchemy
from models import text_document, db
from main import saveFile
import os, dotenv

dotenv.load_dotenv()

class CopilotTestCase(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def test_auto_correction(self):
        # Tests functionality of autocorrection
        my_string = "Thsi is an sentence."
        lang_help = LanguageHelper()

        self.assertEqual(lang_help.auto_correction(my_string),
                         "This is a sentence.")

class ModelTestCase(TestCase):
    # Tests functionality of Database and Models
    SQLALCHEMY_DATABASE_URI = os.environ.get("test-config")
    TESTING = True  

    def create_app(self):  # Creating the Test Flask Application with Test DB
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("test-config")
        db.init_app(app)
        return app

    def setUp(self):  # Creating Tables for Testing DB
        db.create_all()

    def tearDown(self):  # Removes all current data in Testing DB after every Test
        db.session.remove()
        db.drop_all()

    def test_insert_new_text_document_in_db(self):
        # Tests if inserting a new text document in DB is successful
        test_doc = text_document(name="Test Name", text="Test Text")
        test_doc.save()
        doc_from_db = text_document.query.filter_by(name="Test Name").first()
        self.assertEqual(doc_from_db.name, "Test Name")


if __name__ == "__main__":
    main()
