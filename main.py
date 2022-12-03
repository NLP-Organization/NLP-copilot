import language_tool_python
import requests
import json


""" Notes:

References:
Grammarly

Python Libraries we want to use:
NLTK Package
PyDictionary

Goals:
1. Start with: Grammar Check
2. Essay Copilot (think github copilot),  correct grammar mistakes, recommend synonyms
3. Have a switch to swap between suggesting mode and autocomplete/autocorrect mode
4. Publish a Google plug-in
"""


# return corrected text - spelling + grammar fixed
def auto_correction(tool, text):
    correct_text = tool.correct(text)
    return correct_text


# get matches to text - used for suggested changes
def get_matches(tool, text):
    my_matches = tool.check(my_text)
    return my_matches


# each dictionary stores an aspect of an error. KEY: VALUE -> errorID: word/offset/length/ruleID/message/replacements
word_dict, offset_dict, length_dict, ruleID_dict, message_dict, replacements_dict = {}, {}, {}, {}, {}, {}


# updating error attribute in respective dictionaries
def parse_for_dict(text, error, error_id):
    word_dict[error_id] = text[error.offset:error.offset + error.errorLength]
    offset_dict[error_id] = error.offset
    length_dict[error_id] = error.errorLength
    ruleID_dict[error_id] = error.ruleId
    message_dict[error_id] = error.message
    replacements_dict[error_id] = error.replacements


my_tool = language_tool_python.LanguageTool('en-US')  # create language-tool
my_text = "A quick broun fox jumpps over a a little lazy dog. I'm not sleapy and tehre is no place I'm giong to."

my_list = get_matches(my_tool, my_text)

match_id = 1000
for match in my_list:
    parse_for_dict(my_text, match, match_id)
    match_id += 1


# TODO: Make an API that returns the mistake based on ID
# we pass in an ID, and the mistake attributes are fetched from dicts and returned
# return as JSON

# TODO: create JSON for mistakes - store each mistake as a separate entry


def convert_to_JSON(match_id):
    temp_dict = {}  # temporary dictionary

    # create individual dictionary for each entry and dump to json object
    for i in range(1000, match_id):
        entry_dict = {
            'word': word_dict[i],
            'offset': offset_dict[i],
            'length': length_dict[i],
            'ruleID': ruleID_dict[i],
            'message': message_dict[i],
            'replacements': replacements_dict[i]
        }
        temp_dict[i] = entry_dict

    json_object = json.dumps(temp_dict, indent=4)
    print(json_object)

    with open("JSON/errors.json", "w") as outfile:
        outfile.write(json_object)


convert_to_JSON(match_id)
