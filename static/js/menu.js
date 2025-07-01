function toggleMobileMenu() {
  const nav = document.getElementById("mainNav");
  const toggle = document.querySelector(".mobile-toggle i");

  nav.classList.toggle("active");

  if (nav.classList.contains("active")) {
    toggle.classList.remove("fa-bars");
    toggle.classList.add("fa-times");
  } else {
    toggle.classList.remove("fa-times");
    toggle.classList.add("fa-bars");
  }
}

document.addEventListener("click", function (event) {
  const nav = document.getElementById("mainNav");
  const toggle = document.querySelector(".mobile-toggle");

  if (!nav.contains(event.target) && !toggle.contains(event.target)) {
    nav.classList.remove("active");
    document.querySelector(".mobile-toggle i").classList.remove("fa-times");
    document.querySelector(".mobile-toggle i").classList.add("fa-bars");
  }
});

document.querySelectorAll(".dropdown").forEach((dropdown) => {
  dropdown.addEventListener("click", function (e) {
    if (window.innerWidth <= 768) {
      e.preventDefault();
      const menu = this.nextElementSibling;
      menu.style.display = menu.style.display === "block" ? "none" : "block";
    }
  });
});
