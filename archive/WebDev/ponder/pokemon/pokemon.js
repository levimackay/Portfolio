const ditto = {
  id: 132,
  name: "Ditto",
  type: "normal",
  abilities: ["limber", "imposter"],
  base_experience: 101,
  height: 3,
  weight: 40,
  stats: {
    hp: 48,
    attack: 48,
    defense: 48,
    special_attack: 48,
    special_defense: 48,
    speed: 48
  },
  sprite: "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/132.png",
  transform: function () {
    this.sprite = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/shiny/132.png";
  }
};

function displayDitto() {
  document.getElementById("name").textContent = ditto.name;
  document.getElementById("ability").textContent = `Ability: ${ditto.abilities[0]}`;
  const img = document.getElementById("ditto");
  img.src = ditto.sprite;
  img.alt = ditto.name;

  img.addEventListener("click", () => {
    ditto.transform();
    img.src = ditto.sprite;
  });
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", displayDitto);
} else {
  displayDitto();
}
