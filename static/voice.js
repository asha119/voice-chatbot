// Voice input
function startVoice() {
    const recognition = new webkitSpeechRecognition();
    recognition.lang = "en-IN";

    recognition.onresult = function(event) {
        document.getElementById("msg").value = event.results[0][0].transcript;
    };

    recognition.start();
}

// Voice output
window.onload = function () {
    const text = document.getElementById("reply").innerText;
    if (text !== "") {
        const speech = new SpeechSynthesisUtterance(text);
        speech.lang = "en-IN";
        window.speechSynthesis.speak(text);
    }
};
