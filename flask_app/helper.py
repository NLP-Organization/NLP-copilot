# Helper Functions

# If there is no title, rename Untitled Document
def untitled(title):
    if title == "":
        return "Untitled Document"
    else:
        return title

# Return the largest document id, else return 0
def get_documents_length(documents):
    if documents == None:
        return 0
    else:
        return int(documents[0].id)