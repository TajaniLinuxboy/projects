const form = document.querySelector(".register-form")
const inputs = document.querySelectorAll("input")
const errorlist = document.querySelectorAll(".errorlist")

const regex = new RegExp('(?:[a-z0-9!#$%&\'*+\\/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&\'*+\\/=?^_`{|}~-]+)*|\\"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])', 'gm')

errorlist.forEach((error) => {
    inputs.forEach((input) => {
        if (error.parentElement == input.parentElement) {
            input.style.borderBottomColor = "#F35D3C"

            input.addEventListener("keyup", (e) => {
                const search = input.value.search(regex)
                if (search !== -1) {
                  input.style.borderBottomColor = "#90ee6d"
                }
                else {
                  input.style.borderBottomColor = "#F35D3C"
                }
              })
            
        }
    })
})
