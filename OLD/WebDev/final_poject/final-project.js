//Workouts to be sorted and filtered
const workouts = [
    {
        title: "Bench Press",
        description: "Classic chest-building barbell press done in the gym.",
        image: "./images/bench-press.jpg",
        muscle: "chest",
        location: "gym",
        difficulty: 3
    },
    {
        title: "Push Ups",
        description: "Perfect chest workout you can do anywhere.",
        image: "./images/push-ups.jpg",
        muscle: "chest",
        location: "home",
        difficulty: 2
    },
    {
        title: "Plank",
        description: "Works your core and stability muscles.",
        image: "./images/plank.jpg",
        muscle: "core",
        location: "home",
        difficulty: 2
    },
    {
        title: "Deadlift",
        description: "Heavy compound lift for your back and legs.",
        image: "./images/deadlift.jpg",
        muscle: "back",
        location: "gym",
        difficulty: 4
    },
    {
        title: "Bodyweight Squats",
        description: "Burn those quads without any equipment.",
        image: "./images/bodyweight-squats.jpg",
        muscle: "legs",
        location: "home",
        difficulty: 1
    },
    {
        title: "Incline Push Ups",
        description: "Easier push-up variation targeting upper chest.",
        image: "./images/incline-pushups.jpg",
        muscle: "chest",
        location: "home",
        difficulty: 1
    },
    {
        title: "Dumbbell Bench Press",
        description: "Chest press using dumbbells instead of a barbell.",
        image: "./images/dumbbell-bench.jpg",
        muscle: "chest",
        location: "gym",
        difficulty: 3
    },
    {
        title: "Pull Ups",
        description: "Back and biceps compound bodyweight movement.",
        image: "./images/pullups.jpg",
        muscle: "back",
        location: "gym",
        difficulty: 4
    },
    {
        title: "Resistance Band Rows",
        description: "Back rows using bands at home.",
        image: "./images/band-rows.jpg",
        muscle: "back",
        location: "home",
        difficulty: 2
    },
    {
        title: "Bulgarian Split Squats",
        description: "Unilateral leg strength builder.",
        image: "./images/bulgarian.jpg",
        muscle: "legs",
        location: "home",
        difficulty: 3
    },
    {
        title: "Leg Press",
        description: "Machine exercise for quads and glutes.",
        image: "./images/leg-press.jpg",
        muscle: "legs",
        location: "gym",
        difficulty: 3
    },
    {
        title: "Bicep Curls",
        description: "Dumbbell curls for bigger biceps.",
        image: "./images/bicep-curls.jpg",
        muscle: "arms",
        location: "gym",
        difficulty: 2
    },
    {
        title: "Diamond Push Ups",
        description: "Bodyweight triceps and chest exercise.",
        image: "./images/diamond-pushups.jpg",
        muscle: "arms",
        location: "home",
        difficulty: 2
    },
    {
        title: "Lateral Raises",
        description: "Isolate side delts with light dumbbells.",
        image: "./images/lateral-raises.jpg",
        muscle: "shoulders",
        location: "gym",
        difficulty: 2
    },
    {
        title: "Pike Push Ups",
        description: "Shoulder builder using bodyweight.",
        image: "./images/pike-pushups.jpg",
        muscle: "shoulders",
        location: "home",
        difficulty: 3
    },
    {
        title: "Crunches",
        description: "Basic core activation exercise.",
        image: "./images/crunches.jpg",
        muscle: "core",
        location: "home",
        difficulty: 1
    },
    {
        title: "Hanging Leg Raises",
        description: "Advanced core move using pull-up bar.",
        image: "./images/hanging-legs.jpg",
        muscle: "core",
        location: "gym",
        difficulty: 4
    },
    {
        title: "Overhead Press",
        description: "Barbell press for shoulders.",
        image: "./images/overhead-press.jpg",
        muscle: "shoulders",
        location: "gym",
        difficulty: 3
    },
    {
        title: "Wall Sit",
        description: "Static leg burn using a wall.",
        image: "./images/wallsit.jpg",
        muscle: "legs",
        location: "home",
        difficulty: 1
    },
    {
        title: "Cable Tricep Pushdowns",
        description: "Triceps isolation using cable machine.",
        image: "./images/tricep-pushdown.jpg",
        muscle: "arms",
        location: "gym",
        difficulty: 2
    },
    {
        title: "Hammer Curls",
        description: "Variation of curls targeting brachialis.",
        image: "./images/hammer-curls.jpg",
        muscle: "arms",
        location: "home",
        difficulty: 2
    },
    {
        title: "Russian Twists",
        description: "Core rotation movement with or without weight.",
        image: "./images/russian-twists.jpg",
        muscle: "core",
        location: "home",
        difficulty: 2
    },
    {
        title: "Seated Cable Row",
        description: "Back builder using a cable row machine.",
        image: "./images/seated-row.jpg",
        muscle: "back",
        location: "gym",
        difficulty: 3
    },
    {
        title: "Step-Ups",
        description: "Bodyweight or weighted leg exercise.",
        image: "./images/step-ups.jpg",
        muscle: "legs",
        location: "home",
        difficulty: 2
    },
    {
        title: "Chest Fly (Machine)",
        description: "Chest isolation using fly machine.",
        image: "./images/chest-fly.jpg",
        muscle: "chest",
        location: "gym",
        difficulty: 2
    }
];

//I need to do something similar to the mission.js file, where I can have them all be displayed on the page, but then have the css change
//and hide them when I filter them
function hide() {
    const filter1 = document.getElementById('muscle-group')?.value || 'all';
    const filter2 = document.getElementById('workout-location')?.value || 'all';

    const allCards = document.querySelectorAll('.workout-card');

    //Chat helped me understand this functino a little better. I wasn't quite sure how to do this.
    //I had the same code repeating for each filter, but this way I can just check both at once.
    //For every card, it checks if the muscle and location match the selected filters.
    //If they match, it displays the card, otherwise it hides it.
    allCards.forEach(card => {
        const muscle = card.getAttribute('data-muscle');
        const location = card.getAttribute('data-location');

        const matchesMuscle = (filter1 === 'all' || muscle === filter1);
        const matchesLocation = (filter2 === 'all' || location === filter2);

        if (matchesMuscle && matchesLocation) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}
const quotes = [
    "No excuses. Just results.",
    "Push yourself. No one else will do it for you.",
    "Progress, not perfection.",
    "You don’t have to be extreme, just consistent.",
    "Fall in love with the process.",
    "Pain is temporary. Glory is forever.",
    "Wake up with determination. Go to bed with satisfaction."
];


function createWorkoutCards() {
    const container = document.getElementById('workout-cards');
    if (!container) return; // fixes issue if this section doesn't exist on another page

    //This makes a card for every workout in the workouts array
    //It creates a div for each workout, sets its class and id, and adds the
    //Originally I had it so that the HTML was already in the site and you would just hide it and then display it, but I wanted to make it more based out of the 
    //Java script
    for (let i = 0; i < workouts.length; i++) {
        const workout = workouts[i];

        const card = document.createElement('div');
        card.classList.add('workout-card');
        card.id = workout.title.toLowerCase().replace(/ /g, '-');
        card.setAttribute('data-muscle', workout.muscle);
        card.setAttribute('data-location', workout.location);

        // Adds the content
        card.innerHTML = `
      <h2>${workout.title}</h2>
      <p>${workout.description}</p>
    `;

        container.appendChild(card);
    }
}

function generateQuotes() {
    //Gets the div in the html where the quotes gonna go
    const container = document.getElementById("quote-cards");
    if (!container) return; // skip this if not on the page with quote cards

    //Clears the container before adding new quotes
    container.innerHTML = "";
    //Keeps track of which of them has been shown
    const shown = [];

    //Then I used a while loop to keep adding quotes until there are 3 shown
    //I also didn't want to show the same quote twice, so I used an array to keep track of which ones have been shown
    //JS like this reminds me of python, which is super helpful for me
    while (shown.length < 3) {
        const randomIndex = Math.floor(Math.random() * quotes.length);
        if (!shown.includes(randomIndex)) {
            shown.push(randomIndex);

            const quote = quotes[randomIndex];
            const card = document.createElement("div");
            card.className = "quote-card";
            card.innerHTML = `
        <h2>${quote}</h2>
        `;
            container.appendChild(card);
        }
    }
}

//Keeps track of how many workouts have been added
//this is pretty basic, but I wanted to have a counter that updates when you click the button
let workoutCount = 0;

document.getElementById("add-workout")?.addEventListener("click", function () {
    workoutCount++;
    const counter = document.getElementById("workout-count");
    if (counter) counter.textContent = workoutCount;
});

//DOM
document.addEventListener('DOMContentLoaded', function () {
    createWorkoutCards();

    //Only attach filter handlers if the dropdowns exist
    document.getElementById('muscle-group')?.addEventListener('change', hide);
    document.getElementById('workout-location')?.addEventListener('change', hide);

    //Motivation button
    document.querySelector('.motivation-btn')?.addEventListener('click', generateQuotes);
});
