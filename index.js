document.addEventListener("DOMContentLoaded", ()=>{
  const loginForm = document.getElementById("login");
  const username = document.getElementById("username")
  const password = document.getElementById("password")

  loginForm.addEventListener("submit", (e)=>{
    e.preventDefault();
    validLogin(username, password);
  })
})

function validLogin(username, password) {
  const formDiv = document.getElementById("form")
  if (username.value === "ronny" && password.value === "testing"){
    window.alert("you are logged in !")
    window.location.reload();
  } else {
    username.value = ''
    password.value = ''
    username.style.border = "1px solid red"
    password.style.border = "1px solid red"
    formDiv.style.animation = 'shake 0.3s';
    setTimeout(()=> formDiv.style.animation = 'none',300)
  }
}