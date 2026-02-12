function revealFlag() {
    const encoded =
        "UG9De0NMMTNOVF9TMUQzX0M0UzNfTTRUVDNSU30K";

    const flag = atob(encoded);

    const result = document.getElementById("result");
    const flagBox = document.querySelector(".flag");

    flagBox.textContent = flag;
    result.classList.remove("hidden");
}
