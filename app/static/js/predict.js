const themeToggle = document.getElementById("theme-toggle");
const themeIcon = document.getElementById("theme-icon");


// ===============================
// LOAD SAVED THEME
// ===============================

const savedTheme = localStorage.getItem("theme");

if (savedTheme === "dark") {
    document.body.classList.add("dark-mode");
    themeIcon.textContent = "☀️";
}


// ===============================
// THEME TOGGLE
// ===============================

themeToggle.addEventListener("click", () => {

    document.body.classList.toggle("dark-mode");

    const isDarkMode =
        document.body.classList.contains("dark-mode");

    if (isDarkMode) {

        themeIcon.textContent = "☀️";

        localStorage.setItem("theme", "dark");

    } else {

        themeIcon.textContent = "🌙";

        localStorage.setItem("theme", "light");

    }

});

// ===============================
// CHARACTER COUNTER
// ===============================

const textInput = document.getElementById("text-input");
const charCount = document.getElementById("char-count");

textInput.addEventListener("input", () => {

    const currentLength = textInput.value.length;

    charCount.textContent = `${currentLength} / 5000`;

});

// ===============================
// CLEAR BUTTON
// ===============================

const clearButton = document.getElementById("clear-btn");

const result = document.getElementById("result");
const errorMessage = document.getElementById("error-message");
const loading = document.getElementById("loading");

clearButton.addEventListener("click", () => {

    // Clear textarea
    textInput.value = "";

    // Reset character counter
    charCount.textContent = "0 / 5000";

    // Hide result
    result.classList.add("hidden");

    confidenceFill.style.width = "0%";
    confidenceStatus.textContent = "";

    // Hide error
    errorMessage.classList.add("hidden");

    // Hide loading
    loading.classList.add("hidden");

    // Put cursor back in textarea
    textInput.focus();

});

const exampleButtons = document.querySelectorAll(".example-btn");

exampleButtons.forEach((button) => {

    button.addEventListener("click", () => {

        const exampleText = button.dataset.text;

        textInput.value = exampleText;

        // Update character counter
        charCount.textContent =
            `${exampleText.length} / 5000`;

        // Hide previous result/error
        result.classList.add("hidden");
        errorMessage.classList.add("hidden");

        // Focus textarea
        textInput.focus();

    });

});

const languageResult =
    document.getElementById("language-result");

const confidenceResult =
    document.getElementById("confidence-result");

const confidenceFill =
    document.getElementById("confidence-fill");

const confidenceStatus =
    document.getElementById("confidence-status");    

const detectButton = document.getElementById("detect-btn");

detectButton.addEventListener("click", async () => {

    const text = textInput.value.trim();

    // Check for empty input
    if (!text) {
        errorMessage.textContent =
            "Please enter some text to detect its language.";

        errorMessage.classList.remove("hidden");

        result.classList.add("hidden");

        return;
    }

    // Hide previous messages
    errorMessage.classList.add("hidden");
    result.classList.add("hidden");

    // Show loading
    loading.classList.remove("hidden");

    // Disable button while request is running
    detectButton.disabled = true;

    try {

        const response = await fetch("/api/v1/predict", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                text: text
            })

        });

        const data = await response.json();
        console.log(data);
        // Handle API errors
        if (!response.ok) {

            throw new Error(
                data.detail || "Something went wrong."
            );

        }

        // Display prediction
        console.log("Language from API:", data.language);
        languageResult.textContent = data.language;
        console.log("Language element:", languageResult);

        const confidencePercentage =
        data.confidence * 100;

        confidenceResult.textContent =
        `${confidencePercentage.toFixed(2)}%`;

        confidenceFill.style.width =
        `${confidencePercentage}%`;

        if (confidencePercentage >= 90) {
            confidenceStatus.textContent =
            "High Confidence";
        } else if (confidencePercentage >= 70) {
            confidenceStatus.textContent =
            "Moderate Confidence";
        } else {
            confidenceStatus.textContent =
            "Low Confidence";
        }

result.classList.remove("hidden");

    } catch (error) {

        errorMessage.textContent =
            error.message ||
            "Unable to connect to the prediction service.";

        errorMessage.classList.remove("hidden");

    } finally {

        // Hide loading
        loading.classList.add("hidden");

        // Enable button again
        detectButton.disabled = false;

    }

});    