//I need to removed all of these articles from the HTML file and create them dynamically using JavaScript ONLY
//Do I need to add a border to each of these? Idk how this is going to look
const articles = [
  {
    id: 1,
    title: "Septimus Heap Book One: Magyk",
    date: "July 5, 2022",
    description: "If you enjoy stories about seventh sons of seventh sons and magyk this is the book for you.",
    imgSrc: "https://upload.wikimedia.org/wikipedia/en/5/5f/Magkycover2.jpg",
    imgAlt: "Book cover for Septimus Heap 1",
    ages: "10-14",
    genre: "Fantasy",
    stars: "⭐⭐⭐⭐"
  },
  {
    id: 2,
    title: "Magnus Chase Book One: Sword of Summer",
    date: "December 12, 2021",
    description: "The anticipated new novel by Rick Riordan. After Greek mythology (Percy Jackson), Greek/Roman (Heroes of Olympus), and Egyptian (Kane Chronicles), Rick decides to try his hand with Norse Mythology, and the end result is good.",
    imgSrc: "https://books.google.com/books/content/images/frontcover/xWuyBAAAQBAJ?fife=w300",
    imgAlt: "Book cover for Magnus Chase 1",
    ages: "12-16",
    genre: "Fantasy",
    stars: "⭐⭐⭐⭐"
  },
  {
    id: 3,
    title: "Belgariad Book One: Pawn of Prophecy",
    date: "Feb 12, 2022",
    description: "A fierce dispute among the Gods and the theft of a powerful Orb leaves the World divided into five kingdoms. Young Garion, with his 'Aunt Pol' and an elderly man calling himself Wolf --a father and daughter granted near-immortality by one of the Gods -- set out on a complex mission.",
    imgSrc: "https://images-na.ssl-images-amazon.com/images/I/41ZxXA+nInL.jpg",
    imgAlt: "Book cover for Pawn of Prophecy",
    ages: "12-16",
    genre: "Fantasy",
    stars: "⭐⭐⭐⭐⭐"
  }
];

//ACtual JS
const container = document.querySelector(".articles");

//I love this function. There's got to be an easier way to do this, but 
articles.forEach(book => {
  const article = document.createElement("article");

  const leftCol = document.createElement("div");
  leftCol.classList.add("details");

  const date = document.createElement("time");
  date.setAttribute("datetime", book.date);
  date.textContent = book.date;

  const age = document.createElement("p");
  age.textContent = book.ages;

  const genre = document.createElement("p");
  genre.textContent = book.genre;

  const stars = document.createElement("p");
  stars.textContent = book.stars;

  leftCol.appendChild(date);
  leftCol.appendChild(age);
  leftCol.appendChild(genre);
  leftCol.appendChild(stars);

  const rightCol = document.createElement("div");
  rightCol.classList.add("content");

  const h2 = document.createElement("h2");
  h2.textContent = book.title;

  const img = document.createElement("img");
  img.src = book.imgSrc;
  img.alt = book.imgAlt;

  const desc = document.createElement("p");
  desc.innerHTML = `${book.description} <a href="#">Read More...</a>`;

  rightCol.appendChild(h2);
  rightCol.appendChild(img);
  rightCol.appendChild(desc);

  article.appendChild(leftCol);
  article.appendChild(rightCol);

  container.appendChild(article);
});
