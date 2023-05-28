const formBike = document.querySelector('#formBike')

function listaBike(id) {
    const ids = document.getElementById(`${id}`)
    
    /* formata os valores da bicileta para ajuste de json */
    const valor = ids.dataset.valor.split('').map((char => {
        return char.replace("'", '"')
    }))
    
    /* maximiza as caracteristicas de uma única bike */
    this.ajustaBike(valor.join(''))
}

function ajustaBike(valores) {
    const info = JSON.parse(valores)
    
    
    /* mostra a tela de informações de uma única bike */
    formBike.className = formBike.className.replace('visually-hidden', '')
    console.log(formBike)
    /* capturando os elementos com base nos filhos da dom */

    const secondForm = formBike.firstElementChild
    const identicacaoBike = secondForm.firstElementChild.firstElementChild.lastElementChild
    
    /* identificação da bicicleta */
    identicacaoBike.textContent = `BIKE-${info.id}`
    
    const formLeft = secondForm.lastElementChild.firstElementChild.firstElementChild
    const formRight = secondForm.lastElementChild.firstElementChild.lastElementChild

    /* ajustando os dados para ser inserido no input */
    this.ajusteDados(formLeft, info)
    this.ajusteDados(formRight, info)
}

function fecha() {
    formBike.className += ' visually-hidden'
}

function ajusteDados (element, valores) {
    element.childNodes.forEach((childs) => {
        childs.childNodes.forEach((elements) => {
            if (elements.tagName === 'INPUT') {
                this.ajusteValues(elements, valores)
            } else if (elements.tagName === 'TEXTAREA') {
                this.ajusteValues(elements, valores)
            }
        })
    })
}

function ajusteValues(elemento, valor) {
    for (key in valor) {
        if (elemento.id === key) {
            elemento.value = valor[key]
        } else if (elemento.tagName === 'TEXTAREA' && elemento.id === key) {
            elemento.textContent = valor[key]
        }
    }
}