import language_tool_python
from tkinter import *
from tkinter.ttk import *

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
# create root window
root = Tk()

# root window title and dimension
root.title("Welcome to GeekForGeeks")
# Set geometry(widthxheight)
root.geometry('700x350')


# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

# adding a label to the root window
lbl = Label(root, text="Input sentence: ")
lbl.grid()

# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column=1, row=0)


# function to display user text when
# button is clicked
def clicked():
    fix = "Output: " + auto_correction(my_tool, txt.get())
    lbl.configure(text=fix)


# button widget with red color text inside
btn = Button(root, text="Enter", command=clicked)
# Set Button Grid
btn.grid(column=2, row=0)

# Execute Tkinter
root.mainloop()

print(auto_correction(my_tool, my_text))

my_list = get_matches(my_tool, my_text)

for match in my_list:
    print(match)

