const openModalButton = document.querySelectorAll('#abrir_modal');
const closeModalButton = document.querySelectorAll('#fechar_modal');

openModalButton.forEach(button => {
    button.addEventListener('click', () => {
        const modalid = button.getAttribute('data-modal');
        const modal = document.getElementById(modalid);
        
        modal.showModal();
    });
});

closeModalButton.forEach(button =>{
    button.addEventListener('click', () =>{
        const modalid = button.getAttribute('data-modal');
        const modal = document.getElementById(modalid);
        
        modal.close();
    });
});