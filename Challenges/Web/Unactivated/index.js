document.authform.addEventListener("submit", function (e) {
    e.preventDefault();

    const pwd = document.authform["auth-password"].value;
    const result = document.getElementById("result");
    const flagBox = document.querySelector(".flag");
    const flagWrapper = document.querySelector(".flag-wrapper");

    const status = document.querySelector(".status");
    const icon = document.querySelector(".status .icon");
    const statusText = document.querySelector(".status .text");

    if (pwd === "P0C_1s_C0Ol") {
        result.classList.remove("denied");

        status.classList.remove("denied");
        status.classList.add("granted");

        icon.textContent = "✔";
        statusText.textContent = "Access granted";

        flagBox.textContent = atob("UG9De0NMMTNOVF9TMURFX0FVVEhfMVNfNF9MMTN9Cg==");
        flagWrapper.classList.remove("hidden");

        result.classList.remove("hidden");
    }   else {
        result.classList.remove("granted");
        result.classList.add("denied");

        status.classList.remove("granted");
        status.classList.add("denied");

        icon.textContent = "✖";
        statusText.textContent = "Access denied";

        flagBox.textContent = "";
        flagWrapper.classList.add("hidden");

        result.classList.remove("hidden");
    }
});
