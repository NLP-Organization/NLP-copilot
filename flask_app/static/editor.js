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
            document.getElementById("editor").innerText = res;
            console.log(res);
        }
        });
    }

setInterval(saveFile, 10000);