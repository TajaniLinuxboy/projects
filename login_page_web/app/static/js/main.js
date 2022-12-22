const closebtn = document.querySelector(".closebtn");

closebtn.addEventListener("click", function(){
  this.parentElement.style.visibility = "hidden";
  this.parentElement.style.display = "none";
});


const forms = document.querySelectorAll(".card");

forms.forEach((form) => {
  form.addEventListener("submit", function(event){
    event.preventDefault();
  });
});

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
        card_header.forEach((card_header) => {card_header.appendChild(ptag)} );
          }
        }
    })
})


ptag.addEventListener("click", (e) => {
  title.forEach((title) => {
    title.style.display = "inline-block";
    title.setAttribute("placeholder", "Title")
    ptag.style.display = "none";
  })
})
