const character = {
    name: "Snortleblat",
    class: "Swamp Beat Diplomat",
    level: 5,
    health: 100,
    image: 'https://andejuli.github.io/img/snortleblat.png',
    attacked() {
        if (this.health >= 20) {
            this.level -= 1;
            this.health -= 20;
        } else {
            alert('Character Died');
        }
    },
    levelUp() {
        this.level += 1;
        this.health += 20;
    }
};

function displayCharacter() {
    document.querySelector('.image').src = character.image;
    document.querySelector('.image').alt = character.name;
    document.querySelector('.name').textContent = character.name;
    document.getElementById('class').textContent = character.class;
    document.getElementById('level').textContent = character.level;
    document.getElementById('health').textContent = character.health;
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', displayCharacter);
} else {
    displayCharacter();
}
const attackButton = document.getElementById('attacked');
const levelUpButton = document.getElementById('levelup');

attackButton.addEventListener('click', () => {
    character.attacked();
    displayCharacter();
});

levelUpButton.addEventListener('click', () => {
    character.levelUp();
    displayCharacter();
});