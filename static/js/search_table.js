// captura do evento de clique do botão
const inputSearch = document.getElementById('search--tipping');
const inputSearchTable = document.getElementById('table--item');

// adiciona o escutador de evento na variável e captura os dados do teclado
inputSearch.addEventListener('keyup', () => {
    let numberId = inputSearch.value;

    let lines = inputSearchTable.getElementsByTagName('tr');

    // lógica para a filtragem dos objetos
    for (let posicao in lines) {
        let conteudoDaLinha = lines[posicao].innerHTML;
        
        if (true === conteudoDaLinha.includes(numberId)) {
            lines[posicao].style.display = '';
        } else {
            lines[posicao].style.display = 'none';
        }
    }
});
