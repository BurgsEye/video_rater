function purgeVideos() {
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/purge_videos");
  xhr.onload = function() {
    var counter = xhr.responseText;
    // create a div element with the counter message
    var message = document.createElement("div");
    message.innerHTML = "Deleted " + counter + " videos.";
    // append the message to the message div at the top of the page
    var messageDiv = document.getElementById("message");
    messageDiv.innerHTML = "";
    messageDiv.id = 'messageBox'
    messageDiv.appendChild(message);
    // remove the message after 3 seconds
    setTimeout(function() {
      messageDiv.remove()
    }, 3000);
  };
  xhr.send();
}


function skipForward(seconds) {
  var video = document.getElementById("videoPlayer");
  video.currentTime += seconds;
}