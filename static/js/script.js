const dropArea = document.getElementById("drop_area")
const inputFile = document.getElementById("input-file")
const form = document.getElementById("form_drop_area")

document.getElementById('input-file').addEventListener('change', function (e) {
    if (e.target.files[0]) {
        uploadDocument();
    }
});

function uploadDocument() {
    document.getElementById("input_button").click();
    let fileLink = URL.createObjectURL(inputFile.files[0]);
}

dropArea.addEventListener("dragover", function (e) {
    e.preventDefault();
});
dropArea.addEventListener("drop", function (e) {
    e.preventDefault();
    inputFile.files = e.dataTransfer.files;
    uploadDocument();
});

var opacity = 0;
var intervalID = 0;
window.onload = fadeIn;

function fadeIn() {
    setInterval(show, 35);
}

function show() {
    var body = document.getElementById("body");
    opacity = Number(window.getComputedStyle(body)
        .getPropertyValue("opacity"));
    if (opacity < 1) {
        opacity = opacity + 0.1;
        body.style.opacity = opacity
    } else {
        clearInterval(intervalID);
    }
} 