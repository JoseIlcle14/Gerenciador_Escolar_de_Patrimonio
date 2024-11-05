const openbuttons = document.querySelectorAll('.abrir_modal');

openbuttons.forEach(button => {
    button.addEventListener('click', () => {
        const modalid = button.getAttribute('data-modal');
        const modal = document.getElementById(modalid);
        
        modal.showModal();
    });
});

const close_modal = document.querySelectorAll('.fechar_modal')

close_modal.forEach(button =>{
    button.addEventListener('click', () =>{
        const modalid = button.getAttribute('data-modal');
        const modal = document.getElementById(modalid);
        
        modal.close();
    });
});