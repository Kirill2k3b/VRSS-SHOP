

const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link')

const btnPopup = document.querySelector('.btnLogin-popup')
const iconClose = document.querySelector('.icon-close')



registerLink.addEventListener('click', ()=> {
    wrapper.classList.add('active');
});

loginLink.addEventListener('click', ()=> {
    wrapper.classList.remove('active');
});

btnPopup.addEventListener('click', ()=> {
    wrapper.classList.add('active-popup');
});

iconClose.addEventListener('click', ()=> {
    wrapper.classList.remove('active-popup');
});



/*смена иконки глазика на пароле*/ 

const passwordInput = document.getElementById("password-input");
const showPasswordBtn = document.getElementById("show-password-btn");

showPasswordBtn.addEventListener("click", function() {
  if (passwordInput.type === "password") {
    passwordInput.type = "text";
    showPasswordBtn.innerHTML = '<i class="fa fa-eye-slash"></i>';
  } else {
    passwordInput.type = "password";
    showPasswordBtn.innerHTML = '<i class="fa fa-eye"></i>';
  }
}); 
  
/*Отчистка input при нажатых клавишах*/ 

function clearFormFields(form) {
    const inputs = form.querySelectorAll('input');
    inputs.forEach((input) => {
      input.value = '';
    });
}


const cancelButton = wrapper.querySelector('.icon-close');
cancelButton.addEventListener('click', () => {
  clearFormFields(wrapper);
  // закрыть окно регистрации

  regist
});


const cancelButton2 = wrapper.querySelector('.login-link');
cancelButton2.addEventListener('click', () => {
  clearFormFields(wrapper);
  // закрыть окно регистрации

  regist
});


const cancelButton3 = wrapper.querySelector('.register-link');
cancelButton3.addEventListener('click', () => {
  clearFormFields(wrapper);
  // закрыть окно регистрации

  regist
});




const clearCheckboxOnSubmit = (event) => {
    const form = event.target.form;
    const checkboxes = form.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
      checkbox.checked = false;
    });
};
  





/*Hidden для Формы Регистрации, прокрутка сайта*/ 


/*
const loginButton = document.querySelector('.btnLogin-popup');
const registrationModal = document.querySelector('.wrapper');

loginButton.addEventListener('click', () => {
  registrationModal.style.display = 'block';
  document.body.style.overflow = 'hidden';
});



// Добавляем обработчик событий на кнопку закрытия модального окна
const closeModalButton = document.querySelector('.icon-close');
closeModalButton.addEventListener('click', () => {
  registrationModal.style.display = 'none';
  document.body.style.overflow = 'auto';
});
*/


/* Выдвижение текста при нажатии кнопок ReaD MORE

let coll = document.getElementsByClassName('collapsible');
for(let i = 0; i < coll.length; i++) {
    coll[i].addEventListener('click', function () {
        this.classList.toggle('active');
        let content = this.nextElementSibling;
        if(content.style.maxHeight) {
            content.style.maxHeight = null;
        }else {
            content.style.maxHeight = content.scrollHeight + 'px';
        }
    })
}*/



document.addEventListener("DOMContentLoaded", function(){
  document.getElementById("burger").addEventListener("click", function(){
    document.querySelector("header").classList.toggle("open")
    
  })
})


