if (sessionStorage.getItem('id')) {
  document.addEventListener("DOMContentLoaded", ()=>{
    const username = document.getElementById("username");
    const id = document.getElementById('id');
    const logoutBtn = document.querySelector('button')
    const name = document.getElementById('user-name')
  
    username.innerText += " " + sessionStorage.getItem('username');
    id.innerText += " " + sessionStorage.getItem('id');
    name.innerText += ' ' + sessionStorage.getItem('name');
  
    logoutBtn.addEventListener('click', ()=> {
      sessionStorage.clear();
      location.href = "./login.html"
    })
  
  })
} else {
  location.href = "./login.html"
}