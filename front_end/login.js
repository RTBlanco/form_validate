document.addEventListener("DOMContentLoaded", ()=>{
  const loginForm = document.getElementById("login");
  const username = document.getElementById("username")
  const password = document.getElementById("password")
  const name = document.getElementById('name')
  
  changeToSignUp();
  loginForm.addEventListener("submit", (e)=>{
    e.preventDefault();
    const sessionName = document.getElementById('session-name')
    if (sessionName.innerText === "Login"){
      look(username.value, password.value);
    } else {
      create(username.value, name.value, password.value);
    }
  })
})

function addNameInput(){
  const name = document.getElementById('name')
  if (name.classList.contains('close')) {
    name.classList.remove('close')
  }
  name.classList.add('open')
};

function removeNameInput() {
  const name = document.getElementById('name')
  name.classList.remove('open')
  name.classList.add('close')
};

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
        addNameInput();      
      }, 500)
      addNameInput();
    } else {
      setTimeout(()=> {
        sessionName.innerText = "Login"
        sessionBtn.innerText = "Sign Up"      
      }, 500)
      removeNameInput();
    }
     
    // Removes that class so that when the event triggers again it will be added again 
    setTimeout(()=>{
      sessionName.classList.remove('transform')
      sessionBtn.classList.remove('transform')
    },1000)
  })
}

function validateLogin(obj) {
  
  if (obj.status === 200){
    obj.json().then( obj => {
      const {id, username, name} = obj
      sessionStorage.setItem('id',id)
      sessionStorage.setItem('username', username)
      sessionStorage.setItem('name', name)
    })
    location.href = "./index.html"

  } else {
    const inputName = document.getElementById('name')
    if (username.value === '' && password.value === '' && inputName.value === '') {
      [username, password, inputName].forEach((i)=>{showInvalid(i)})
    } else if (username.value === ''){
      showInvalid(username)
    } else if (password.value === ''){
      showInvalid(password)
    } else if (inputName.value === ''){
      showInvalid(inputName)
    }
    shakeLogin()
  }
}

function showInvalid(element){
  element.style.border = "1px solid red"
  element.value = ''
}

function shakeLogin(){
  const formDiv = document.getElementById("form");
  formDiv.style.animation = 'shake 0.3s';
  setTimeout(()=> formDiv.style.animation = 'none',300)
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
  .then(resp => validateLogin(resp))
}

function create(username, name, password) {
  return fetch('http://localhost:5000/new',{
    method: "POST",
    mode: "cors",
    headers: {
      "content-type" : "application/json",
      "Accept" : "application/json"
    },
    body: JSON.stringify({
      username,
      password,
      name
    })
  })
  .then(resp => validateLogin(resp))
}