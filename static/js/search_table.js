const inputSearch = document.getElementById('search--tipping');
const inputSearchTable = document.getElementById('table--item');

inputSearch.addEventListener('keyup', () => {
    let numberId = inputSearch.value;

    let lines = inputSearchTable.getElementsByTagName('tr');

    for (let posicao in lines) {
        if (true === isNaN(posicao)) {
            continue;
        }
        
        let conteudoDaLinha = lines[posicao].innerHTML;

        if (true === conteudoDaLinha.includes(numberId)) {
            lines[posicao].style.display = '';
        } else {
            lines[posicao].style.display = 'none';
        }
    }
});
