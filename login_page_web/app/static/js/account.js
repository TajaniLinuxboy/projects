const closebtn = document.querySelector(".closebtn");
const navbar_container = document.querySelector(".navbar-container");

closebtn.addEventListener("click", function () {
  this.parentElement.style.display = "none";
  navbar_container.style.display = "flex";
})

const title = document.querySelectorAll(".header");
const span = document.querySelectorAll(".header + span");
const ptag = document.createElement("p");
ptag.setAttribute("class", "setText");
const card_header = document.querySelectorAll(".card-header");

title.forEach((title) => {
  title.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
      if (title.value.length !== 0) {
        ptag.innerHTML = title.value;
        title.style.display = "none";
        ptag.style.display = "block";
        card_header.forEach((card_header) => {
          card_header.appendChild(ptag);
        });
      };
    };
  });
});


ptag.addEventListener("click", (e) => {
  title.forEach((title) => {
    title.style.display = "inline-block";
    title.setAttribute("placeholder", "Title");
    ptag.style.display = "none";
  });
});


const link = document.querySelectorAll(".input-link")
const ul = document.querySelector('.card-body ul')

link.forEach((link) =>  {
  link.addEventListener("keypress", (e) =>  {
    const header_title = link.parentElement.previousElementSibling.querySelector('.header').value
    if (e.key === "Enter") {
      fetch(`${window.location.origin}/insertUrl`, {
        method: 'POST',
        headers: {
          'Accept': "application/json",
          'Content-Type': 'application/json'
        },
        body : JSON.stringify({'data': {
          'url': link.value,
          'title': header_title
        }})
      })
      const li_elem = document.createElement("li")
      const a_tag = document.createElement("a")
      a_tag.innerHTML = link.value
      a_tag.setAttribute("href", `https://${link.value}`)
      li_elem.appendChild(a_tag)
      ul.appendChild(li_elem)

      link.value = ""
    }
  })
})


function createCard(){
  const wrapper = document.querySelector(".wrapper")


  const card_flex_box = document.createElement("div")
  card_flex_box.setAttribute('class', 'card-flex-box')

  const card = document.createElement("div")
  card.setAttribute("class", "card")

  const card_header = document.createElement("div")
  card_header.setAttribute("class", "card-header")
  const card_header_input = document.createElement("input")
  card_header_input.setAttribute("type", "text")
  card_header_input.setAttribute("class", "header")
  card_header_input.setAttribute("placeholder", "Title")

  const span = document.createElement("span")

  card_header.appendChild(card_header_input)
  card_header.appendChild(span)


  const card_input_div = document.createElement("div")
  card_input_div.setAttribute("class", "card-input")

  const card_input = document.createElement("input")
  card_input.setAttribute("type", "text")
  card_input.setAttribute("class", "input-link")
  card_input.setAttribute("placeholder", "Enter Link Here")

  card_input_div.appendChild(card_input)


  const card_body = document.createElement('div')
  card_body.setAttribute("class", "card-body")

  const ul = document.createElement("ul")
  card_body.appendChild(ul)

  card.appendChild(card_header)
  card.appendChild(card_input_div)
  card.appendChild(card_body)

  card_flex_box.appendChild(card)
  wrapper.appendChild(card_flex_box)
}

const add_task_btn = document.querySelector('.add-task');

//add_task_btn.addEventListener('click', createCard)
