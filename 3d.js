import * as THREE from 'three';
import { OrbitControls } from 'OrbitControls';
import { GLTFLoader } from 'GLTFLoader';
import { RectAreaLightHelper } from 'RectAreaLightHelper'
import { RectAreaLightUniformsLib } from 'RectAreaLightUniformsLib';




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
  