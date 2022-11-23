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


my_tool = language_tool_python.LanguageTool('en-US')  # create language-tool
my_text = "A quick broun fox jumpps over a a little lazy dog. I'm not sleapy and tehre is no place I'm giong to."

print(auto_correction(my_tool, my_text))

my_list = get_matches(my_tool, my_text)

for match in my_list:
    print(match)

