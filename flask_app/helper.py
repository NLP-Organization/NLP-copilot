import language_tool_python
import json

# TODO: make this py into a class


# ** GLOBAL VARIABLES **

match_id = 1000  # match_id starts at 1000

# each dictionary stores an aspect of an error
# KEY: VALUE -> errorID: word/offset/length/ruleID/message/replacements
word_dict, offset_dict, length_dict, ruleID_dict, message_dict, replacements_dict = {}, {}, {}, {}, {}, {}

lang_tool = language_tool_python.LanguageTool('en-US')  # create language-tool

# return corrected text - spelling + grammar fixed
def auto_correction(text):
    tool = language_tool_python.LanguageTool('en-US')
    correct_text = tool.correct(text)
    return correct_text


# get matches to text - used for suggested changes
def get_matches(tool, text):
    my_matches = tool.check(text)
    return my_matches

# updating error attribute in respective dictionaries
def parse_for_dict(text, error, error_id):
    word_dict[error_id] = text[error.offset:error.offset + error.errorLength]
    offset_dict[error_id] = error.offset
    length_dict[error_id] = error.errorLength
    ruleID_dict[error_id] = error.ruleId
    message_dict[error_id] = error.message
    replacements_dict[error_id] = error.replacements


# return list of errors
def return_errors(m_id, tool, text):
    error_list = get_matches(tool, text)

    for error in error_list:
        parse_for_dict(text, error, m_id)
        m_id += 1

    convert_to_JSON(m_id)
    return None  # temp


# convert provided matches to JSON file to be returned to document front-end
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


return_errors(match_id, lang_tool, "A quick broun fox jumpps over a a little lazy dog. I'm not sleapy and tehre is no place I'm giong to.")
print(match_id)
