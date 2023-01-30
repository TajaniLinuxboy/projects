const discardbtn = document.querySelector('.discard')
const savebtn = document.querySelector('.save')
const form = document.querySelector('.card-flex-box')

discardbtn.addEventListener('click', (event) => {
  form.addEventListener('submit', (event) => {
    event.preventDefault()
    const title = document.querySelector('.header')
    const link  = document.querySelector('.input-link')
    const textarea = document.querySelector('textarea')
  
    title.value = ''
    link.value = ''
    textarea.value = ''
  })
})
