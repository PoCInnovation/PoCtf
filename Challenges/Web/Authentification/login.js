document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form[name='login']");
    const result = document.getElementById("result");
    const status = result.querySelector(".status");
    const flagWrapper = result.querySelector(".flag-wrapper");
    const statusText = status.querySelector("span:last-child");
    const statusIcon = status.querySelector(".check");

    form.addEventListener("submit", (e) => {
        e.preventDefault();

        let pseudo = form.pseudo.value.trim().toLowerCase();
        let password = form.password.value.trim();

        result.classList.remove("hidden");

        if (pseudo === "4dm1n" && password === "P0C_1s_C0Ol") {

            result.classList.remove("error");
            status.classList.remove("error");

            flagWrapper.style.display = "flex";

            statusText.innerText = "ACCESS GRANTED";
            statusIcon.innerText = "✔";

            revealFlag();

        } else {

            result.classList.add("error");
            status.classList.add("error");

            flagWrapper.style.display = "none";

            statusText.innerText = "ACCESS DENIED";
            statusIcon.innerText = "✖";
        }
    });
});
