document.addEventListener("DOMContentLoaded", ()=>{
  const loginForm = document.getElementById("login");
  const username = document.getElementById("username")
  const password = document.getElementById("password")

  loginForm.addEventListener("submit", (e)=>{
    e.preventDefault();
    look(username.value, password.value);
  })
  changeToSignUp();
})

function changeToSignUp() {
  const sessionBtn = document.getElementById('session')
  const sessionName = document.getElementById('session-name')
  sessionBtn.addEventListener('click', (e)=>{
    console.log(e)
    // Changes the text mid way durring the animation
    sessionName.classList.add('transform')
    sessionBtn.classList.add('transform')


    if (sessionBtn.innerText === "Sign Up") {
      setTimeout(()=> {
        sessionName.innerText = "Sign Up"
        sessionBtn.innerText = "Login"      
      }, 500)
    } else {
      setTimeout(()=> {
        sessionName.innerText = "Login"
        sessionBtn.innerText = "Sign Up"      
      }, 500)
    }
     
    // Removes that class so that when the event triggers again it will be added again 
    setTimeout(()=>{
      sessionName.classList.remove('transform')
      sessionBtn.classList.remove('transform')
    },1000)
  })
}

function validate(obj) {
  const formDiv = document.getElementById("form");
  if (obj.status === 200){
    obj.json().then( obj => {
      const {id, username} = obj
      sessionStorage.setItem('id',id)
      sessionStorage.setItem('username', username)
    })
    location.href = "./index.html"
  } else {
    username.value = ''
    password.value = ''
    username.style.border = "1px solid red"
    password.style.border = "1px solid red"
    formDiv.style.animation = 'shake 0.3s';
    setTimeout(()=> formDiv.style.animation = 'none',300)
  }
}

function look(username, password) {
  return fetch('http://localhost:5000/login',{
    method: "POST",
    mode: "cors",
    headers: {
      "content-type" : "application/json",
      "Accept" : "application/json"
    },
    body: JSON.stringify({
      username,
      password
    })
  })
  .then(resp => validate(resp))
}