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
3. Publish a Google plug-in
"""

# spell = Speller()  # create Speller object
my_tool = language_tool_python.LanguageTool('en-US')  # create language-tool

my_text = "A quick broun fox jumpps over a a little lazy dog. I'm not sleapy and tehre is no place I'm giong to."


# apply correction
correct_text = my_tool.correct(my_text)

# Print text
print("Original Text: ", my_text)
print("Text after correction: ", correct_text)
