/* eslint-disable no-unused-vars */
const editor = document.getElementById('editor');
const loading = document.getElementById('loading');
let userId = '';
let userName = '';
let dos = '';

// editor section
function format(command, value) {
	document.execCommand(command, false, value);
}

function changeFont() {
	const Font = document.getElementById('input-font').value;
	document.execCommand('fontName', false, Font);
}

function changeSize() {
	const size = document.getElementById('fontSize').value;
	document.execCommand('fontSize', false, size);
}

function openNav() {
    document.getElementById("mySidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    document.getElementById("openbtn").style.visibility = 'hidden';
    }
    
function closeNav() {
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    document.getElementById("openbtn").style.visibility = 'visible';
    }

function toIndex() {
    window.location.href = "http://127.0.0.1:5000/";
}

function saveFile() {
    var id = document.getElementById("documentId").innerText
    var text = document.getElementById("editor").innerText;
    var name = document.getElementById("documentName").value;
    var docData = {"id": id, "name": name, "text": text}
    console.log(name);
    $.ajax({
        url:"/editFile",
        type:"POST",
        contentType: "application/JSON",
        data: JSON.stringify(docData),
        success: function(res){
            document.getElementById("documentId").innerText = res;
            console.log("Document Saved!");
        }
    })
}

function deleteFile() {
    const response  = confirm("Are you sure you want to delete?")
    if (response) {
        var id = document.getElementById("documentId").innerText;
        var text = document.getElementById("editor").innerText;
        var name = document.getElementById("documentName").value;
        var docData = {"id": id, "name": name, "text": text}
        $.ajax({
            url: "/editFile",
            type: "DELETE",
            contentType: "application/JSON",
            data: JSON.stringify(docData),
            success: function(res) {
                window.location.href = "http://127.0.0.1:5000/"
            }
        })
    }
}

function autoCorrect() {
    var text = document.getElementById("editor").innerText;
    console.log(text);
    $.ajax({
        url:"/autoCorrect",
        type: "POST",
        contentType: "application/JSON",
        data: JSON.stringify(text),
        success: function(res){
            document.getElementById("editor").innerText = res[0];
            var errors = JSON.parse(res[1])
            var toAdd = document.createDocumentFragment();
            for (const error in errors) {
                var newDiv = document.createElement('div');
                console.log(error);
                newDiv.innerText = errors[error].word;
                var newP = document.createElement("p");
                newP.innerText = errors[error].replacements;
                newDiv.appendChild(newP);
                toAdd.appendChild(newDiv);
            }
            document.getElementById("mySidebar").appendChild(toAdd)
            console.log(errors);
        }
        });
    }

setInterval(saveFile, 10000);