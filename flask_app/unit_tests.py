"""
Tests for NLP-Copilot
"""
from unittest import TestCase, main
from LanguageHelper import LanguageHelper

class CopilotTestCase(TestCase):
    
    def test_auto_correction(self):
        # Tests functionality of autocorrection
        my_string = "Thsi is an sentence."
        lang_help = LanguageHelper()

        self.assertEqual(lang_help.auto_correction(my_string),
                        "This is a sentence.")
    

if __name__ == "__main__":
    main()
