const form = document.querySelector('#formLogin');

form.addEventListener('submit', function (e) {
    e.preventDefault();

    const inputName = e.target.querySelector('#name');
    const inputPassword = e.target.querySelector('#password');

    const name = inputName.value;
    const password = inputPassword.value;

    if (!name) {
         setResultado('escreva um login válido', false);
         return;
    };

    if (!password) {
        setResultado('senha inválida', false);
        return;
    };  
});



