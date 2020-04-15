<html>
<head>
<script>
  var speak = function(text) {
    var msg = new SpeechSynthesisUtterance(text);
    window.speechSynthesis.speak(msg);
  };

  var sleep = function(time) {
    return new Promise((resolve) => setTimeout(resolve, time));
  }

  var checkResponse = function() {
    var spelling = document.getElementById("spelling").value;
    if (spelling.toLowerCase() == '{{word}}') {
      window.fetch('/rainbow');
      speak("Great job!");
      sleep(1500).then(() => location.reload());
    } else {
      speak("Try again! The word is: {{word}}");
    }
  };
</script>
</head>
<body>
  <script>speak('{{word}}');</script>
  <form onsubmit="return false;" method="post">
    Type what you hear: <input id="spelling" type="text"/>
    <input type="submit" onclick="checkResponse()"/>
  </form>
</body>
</html>
