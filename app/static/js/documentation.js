/* =========================================
   ACTIVE DOCUMENTATION SECTION
   ========================================= */

const docLinks =
    document.querySelectorAll(".sidebar-card a");

const docSections =
    Array.from(docLinks)
        .map((link) => {
            const id = link.getAttribute("href").substring(1);
            return document.getElementById(id);
        })
        .filter((section) => section !== null);


const updateActiveSection = () => {

    let currentSection = "";

    docSections.forEach((section) => {

        const sectionTop =
            section.getBoundingClientRect().top;

        if (sectionTop <= 160) {
            currentSection = section.id;
        }

    });


    docLinks.forEach((link) => {

        link.classList.remove("active");

        const linkTarget =
            link.getAttribute("href").substring(1);

        if (linkTarget === currentSection) {
            link.classList.add("active");
        }

    });

};


window.addEventListener(
    "scroll",
    updateActiveSection
);

updateActiveSection();