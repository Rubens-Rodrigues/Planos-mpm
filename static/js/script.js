// script pra o Acordeon da FAQ
document.addEventListener("DOMContentLoaded", function () {
  const faqQuestions = document.querySelectorAll(".faq-question");

  faqQuestions.forEach(function (question) {
      question.addEventListener("click", function () {
          const answer = this.nextElementSibling;

          if (answer.style.display === "block") {
              answer.style.display = "none";
              this.classList.remove("open");
          } else {
              answer.style.display = "block";
              this.classList.add("open");
          }
      });
  });
});