document.getElementById('copyButton').addEventListener('click', function() {
    // Create a temporary textarea element to hold the text
    var tempTextArea = document.createElement('textarea');
    tempTextArea.value = document.getElementById('textToCopy').textContent;
    
    // Append the textarea to the body and select the text
    document.body.appendChild(tempTextArea);
    tempTextArea.select();
    tempTextArea.setSelectionRange(0, 99999); // For mobile devices

    // Copy the text inside the textarea to the clipboard
    document.execCommand('copy');

    // Remove the temporary textarea
    document.body.removeChild(tempTextArea);

    // Alert the copied text (optional)
    alert('Copied the text: ' + tempTextArea.value);
});


function getpk(){
    pk.style.display = "block";
}

function myFunction() {
            var copyText = document.getElementById("myInput");
            copyText.select();
            copyText.setSelectionRange(0, 99999);
            document.execCommand("copy");
            
            var tooltip = document.getElementById("myTooltip");
            tooltip.innerHTML = "Copied: " + copyText.value;
          }