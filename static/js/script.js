// Captura o evento de clique do botão e ativa a classe
$(document).ready(function(){
    $('#mobile--btn').on('click', function(){
        $('#mobile--menu').toggleClass('active');
    });
});

// Altera o icone do botao de mobile
$(document).ready(function(){
    $('#mobile--btn').on('click', function(){
    $('#mobile--btn').find('i').toggleClass('fa-x');
    })
})