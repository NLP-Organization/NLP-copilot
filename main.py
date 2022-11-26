import language_tool_python

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


# each dictionary stores an aspect of an error. KEY: VALUE -> errorID: offset/length/ruleID/message/replacements
offset_dict, length_dict, ruleID_dict, message_dict, replacements_dict = {}, {}, {}, {}, {}


# updating error attribute in respective dictionaries
def parse_for_dict(error, error_id):
    offset_dict[error_id] = error.offset
    length_dict[error_id] = error.errorLength
    ruleID_dict[error_id] = error.ruleId
    message_dict[error_id] = error.message
    replacements_dict[error_id] = error.replacements


my_tool = language_tool_python.LanguageTool('en-US')  # create language-tool
my_text = "A quick broun fox jumpps over a a little lazy dog. I'm not sleapy and tehre is no place I'm giong to."

print(auto_correction(my_tool, my_text))

my_list = get_matches(my_tool, my_text)

# TODO: generate unique match_id by strings
match_id = 0
for match in my_list:
    parse_for_dict(match, match_id)
    match_id += 1

print(offset_dict)
print(length_dict)
print(ruleID_dict)
print(message_dict)
print(replacements_dict)



