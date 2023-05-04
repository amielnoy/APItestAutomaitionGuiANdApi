var fileDownload = require('js-file-download');
fileDownload(data, 'filename.csv');

function myFunction() {
    document.getElementById("demo").innerHTML = "Paragraph changed.";
}

const fileSelector = document.getElementById('file-selector');
fileSelector.addEventListener('change', (event) => {
    const fileList = event.target.files;
    console.log(fileList);
});