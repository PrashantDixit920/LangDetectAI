/* =========================================
   THEME TOGGLE
   ========================================= */

const themeToggle =
    document.getElementById("theme-toggle");

const themeIcon =
    document.getElementById("theme-icon");


if (themeToggle && themeIcon) {

    const savedTheme =
        localStorage.getItem("theme");

    if (savedTheme === "dark") {

        document.body.classList.add("dark-mode");

        themeIcon.textContent = "☀️";
    }


    themeToggle.addEventListener("click", () => {

        document.body.classList.toggle("dark-mode");

        const isDarkMode =
            document.body.classList.contains("dark-mode");


        themeIcon.textContent =
            isDarkMode ? "☀️" : "🌙";


        localStorage.setItem(
            "theme",
            isDarkMode ? "dark" : "light"
        );

    });

}


/* =========================================
   COPY CODE
   ========================================= */

const copyButtons =
    document.querySelectorAll(".copy-btn");


copyButtons.forEach((button) => {

    button.addEventListener("click", async () => {

        const textToCopy =
            button.dataset.copy;


        try {

            await navigator.clipboard.writeText(
                textToCopy
            );


            const originalText =
                button.textContent;


            button.textContent =
                "Copied!";


            setTimeout(() => {

                button.textContent =
                    originalText;

            }, 1500);


        } catch (error) {

            console.error(
                "Failed to copy:",
                error
            );

        }

    });

});