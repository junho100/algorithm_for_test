/*transition, shadow practice*/
const title = document.querySelector("h1");
title.addEventListener("mouseover", () => {
  title.classList.add("hover");
});

title.addEventListener("mouseleave", () => {
  title.classList.remove("hover");
});

/* fetch practice */

fetch("https://jsonplaceholder.typicode.com/posts/1")
  .then((res) => {
    const data = res.json();
    return data;
  })
  .then((data) => {
    const body = document.querySelector("body");
    const t = document.createElement("h2");
    t.innerText = data.title;
    body.appendChild(t);
  });
