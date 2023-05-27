const price = document.querySelector("#price")
letras = ['R', '$']

price.addEventListener("click", () => {
    format = this.transformString(letras)
    price.value = format
})

price.addEventListener("keyup", (letra) => {
    padrao = /[0-9]/
    if (letra.key === 'Backspace') {
        console.log(letras)
        letras.pop()
        console.log(letras)
    } else if (price.value === '' || !padrao.exec(letra.key)) {
        price.value = format
    } 
    
    if (Number(letra.key)) {
        letras.push(letra.key)
        this.formatInput(letras)
    }
    
})

function formatInput(valor) {
    let preco = this.transformString(valor)
    
    if (preco.length > 4) {
        corte = preco.slice(-2)
        preco += '.' + corte
        price.value = preco
    }

    valor[0] = 'R'
    valor = valor.length === 0 ? 'R$' : ''
}

function transformString(value) {
    let number = value.toString()
    let preco = ''
    for (let letra in number) {
        preco += number[letra] != ',' ? number[letra] : '' 
    }
    return preco
}