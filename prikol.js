console.clear();

const cardsContainer = document.querySelector(".cards");
const cardsContainerInner = document.querySelector(".cards__inner");
const cards = Array.from(document.querySelectorAll(".card"));
const overlay = document.querySelector(".overlay");

const applyOverlayMask = (e) => {
  const overlayEl = e.currentTarget;
  const x = e.pageX - cardsContainer.offsetLeft;
  const y = e.pageY - cardsContainer.offsetTop;

  overlayEl.style = `--opacity: 1; --x: ${x}px; --y:${y}px;`;
};

const createOverlayCta = (overlayCard, ctaEl) => {
  const overlayCta = document.createElement("div");
  overlayCta.classList.add("cta");
  overlayCta.textContent = ctaEl.textContent;
  overlayCta.setAttribute("aria-hidden", true);
  overlayCard.append(overlayCta);
};

const observer = new ResizeObserver((entries) => {
  entries.forEach((entry) => {
    const cardIndex = cards.indexOf(entry.target);
    let width = entry.borderBoxSize[0].inlineSize;
    let height = entry.borderBoxSize[0].blockSize;

    if (cardIndex >= 0) {
      overlay.children[cardIndex].style.width = `${width}px`;
      overlay.children[cardIndex].style.height = `${height}px`;
    }
  });
});

const initOverlayCard = (cardEl) => {
  const overlayCard = document.createElement("div");
  overlayCard.classList.add("card");
  createOverlayCta(overlayCard, cardEl.lastElementChild);
  overlay.append(overlayCard);
  observer.observe(cardEl);
};

cards.forEach(initOverlayCard);
document.body.addEventListener("pointermove", applyOverlayMask);






/*Описание окна Регистрации и формы Login*/ 


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













/* Кнопки в Freq question*/




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
}


document.addEventListener("DOMContentLoaded", function(){
  document.getElementById("burger").addEventListener("click", function(){
    document.querySelector("header").classList.toggle("open")
    
  })
})
