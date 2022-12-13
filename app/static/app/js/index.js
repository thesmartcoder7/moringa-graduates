let messageDiv = document.querySelector("#system-messages");
let closeMessages = document.querySelector(".close-messages");

if (closeMessages) {
  closeMessages.addEventListener("click", () => {
    messageDiv.style.display = "none";
  });
}
