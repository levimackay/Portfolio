const menuButton = document.querySelector(".menu-button");
const menu = document.querySelector(".menu");

function toggleMenu() {
  menu.classList.toggle("hide");
}

menuButton.addEventListener('click', toggleMenu);

function handleResize() {
  if (window.innerWidth > 1000) {
    menu.classList.remove("hide");
  } else {
    menu.classList.add("hide");
  }
}

window.addEventListener("resize", handleResize);
window.addEventListener("load", handleResize);

const gallery = document.querySelector(".gallery");
const modal = document.createElement("dialog");
document.body.appendChild(modal);

function viewerTemplate(src, alt) {
  return `
    <img src="${src}" alt="${alt}">
    <button class="close-viewer">X</button>
  `;
}

//So this is where I got lost ngl
gallery.addEventListener("click", (event) => {
  const img = event.target.closest("img");
  if (!img) return;

  const src = img.getAttribute("src");
  const alt = img.getAttribute("alt");
  const newSrc = src.split("-")[0] + "-full.jpeg";

  modal.innerHTML = viewerTemplate(newSrc, alt);
  modal.showModal();

  const closeBtn = modal.querySelector(".close-viewer");
  closeBtn.addEventListener("click", () => {
    modal.close();
  });
});

modal.addEventListener("click", (event) => {
  if (event.target === modal) {
    modal.close();
  }
});
