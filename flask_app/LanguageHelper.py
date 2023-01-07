import language_tool_python
import json

# TODO: make this py into a class


# ** GLOBAL VARIABLES **
class LanguageHelper():
    match_id = 1000  # match_id starts at 1000

    # each dictionary stores an aspect of an error
    # KEY: VALUE -> errorID: word/offset/length/ruleID/message/replacements
    word_dict, offset_dict, length_dict, ruleID_dict, message_dict, replacements_dict = {}, {}, {}, {}, {}, {}

    lang_tool = language_tool_python.LanguageTool('en-US')  # create language-tool

    # return corrected text - spelling + grammar fixed
    def auto_correction(self, text):
        correct_text = self.lang_tool.correct(text)
        return correct_text


    # get matches to text - used for suggested changes
    def get_matches(self, text):
        my_matches = self.lang_tool.check(text)
        return my_matches

    # updating error attribute in respective dictionaries
    def parse_for_dict(self, text, error, error_id):
        self.word_dict[error_id] = text[error.offset:error.offset + error.errorLength]
        self.offset_dict[error_id] = error.offset
        self.length_dict[error_id] = error.errorLength
        self.ruleID_dict[error_id] = error.ruleId
        self.message_dict[error_id] = error.message
        self.replacements_dict[error_id] = error.replacements


    # return list of errors
    def return_errors(self, text):
        error_list = self.get_matches(text)

        for error in error_list:
            self.parse_for_dict(text, error, self.match_id)
            self.match_id += 1

        self.convert_to_JSON(self.match_id)
        return None  # temp


    # convert provided matches to JSON file to be returned to document front-end
    def convert_to_JSON(self, match_id):
        temp_dict = {}  # temporary dictionary

        # create individual dictionary for each entry and dump to json object
        for i in range(1000, match_id):
            entry_dict = {
                'word': self.word_dict[i],
                'offset': self.offset_dict[i],
                'length': self.length_dict[i],
                'ruleID': self.ruleID_dict[i],
                'message': self.message_dict[i],
                'replacements': self.replacements_dict[i]
            }
            temp_dict[i] = entry_dict

        json_object = json.dumps(temp_dict, indent=4)
        print(json_object)

        with open("JSON/errors.json", "w") as outfile:
            outfile.write(json_object)

