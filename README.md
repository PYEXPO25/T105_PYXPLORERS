# T105_PYXPLORERS
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Speech to Text</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f8f9fa;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }

    .container {
      background-color: white;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
      text-align: center;
      width: 80%;
      max-width: 500px;
    }

    h1 {
      color: #007bff;
    }

    select {
      width: 100%;
      padding: 10px;
      margin: 10px 0;
      font-size: 16px;
      border-radius: 5px;
    }

    button {
      background-color: #28a745;
      color: white;
      padding: 12px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      font-size: 16px;
      margin-top: 10px;
    }

    button:hover {
      background-color: #218838;
    }

    #speechResult {
      font-size: 18px;
      color: #333;
      margin-top: 20px;
      font-weight: bold;
      word-wrap: break-word;
    }
  </style>
</head>
<body>

  <div class="container">
    <h1>Speech to Text</h1>

    <!-- Language Selection -->
    <select id="languageSelect">
      <option value="en-US">English (US)</option>
      <option value="hi-IN">Hindi (India)</option>
      <option value="ta-IN">Tamil (India)</option>
      <option value="te-IN">Telugu (India)</option>
      <option value="bn-IN">Bengali (India)</option>
      <option value="mr-IN">Marathi (India)</option>
      <option value="gu-IN">Gujarati (India)</option>
      <option value="ml-IN">Malayalam (India)</option>
      <option value="pa-IN">Punjabi (India)</option>
      <option value="or-IN">Odia (India)</option>
      <option value="ur-IN">Urdu (India)</option>
    </select>

    <!-- Speech to Text Button -->
    <button id="startRecordButton" onclick="startSpeechRecognition()">Start Listening</button>

    <!-- Recognized Speech Output -->
    <div id="speechResult">Recognized Speech will appear here...</div>
  </div>

  <script>
    let recognition = null;
    let isRecording = false;

    // Check for Speech Recognition API support
    if ('SpeechRecognition' in window || 'webkitSpeechRecognition' in window) {
      recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
      recognition.interimResults = true;
      recognition.continuous = true;

      recognition.onresult = (event) => {
        const transcript = event.results[event.results.length - 1][0].transcript;
        document.getElementById('speechResult').textContent = Recognized Text: ${transcript};
      };

      recognition.onerror = (event) => {
        console.error('Speech Recognition Error:', event);
      };
    } else {
      alert("Speech recognition is not supported in your browser.");
    }

    // Start Speech Recognition
    function startSpeechRecognition() {
      const language = document.getElementById('languageSelect').value;
      recognition.lang = language;

      if (isRecording) {
        recognition.stop();
        document.getElementById('startRecordButton').textContent = 'Start Listening';
      } else {
        recognition.start();
        document.getElementById('startRecordButton').textContent = 'Stop Listening';
      }
      isRecording = !isRecording;
    }
  </script>

</body>
</html>
