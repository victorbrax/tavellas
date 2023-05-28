/**
 * Elemento para transformar o preço
 */
const price = document.querySelector("#price")

/**
 * Armazena os valores digitados pelo usuário
 */
numbers = []

/**
 * Evento ao pressinar uma tecla
 */
price.addEventListener("keyup", (letra) => {

    /* Zera o array caso o input esteja vazio */
    if (price.value === '') {
        numbers = []
    }
    
    /* Insere apenas números */
    if (Number(letra.key) || letra.key === '0') {   
        
        numbers.push(letra.key)
        this.transformString(numbers)
    }
    
    /* Exclui um valor */
    if (letra.key === 'Backspace') {
        numbers.pop()
        this.transformString(numbers)
    }

    /* Capacidade máxima de caracteres */
    if (price.value.length === 12) {
        return false
    }
})

/**
 * Realiza a trasformação de um array para string
 * 
 * @author Dereck Silva
 * @since 27/05/2023
 * @param { array } numbers 
 */
function transformString(numbers) {
    let number = numbers.toString()
    let priceService  = ''
    for (let num in number) {
        priceService += number[num] != ',' ? number[num] : ''
    }
    
    priceService = this.formatPrice(priceService)
    price.value = `R$ ${priceService}`
}

/**
 * Formata o preço com base na quantidade de caracteres
 * 
 * @author Dereck Silva
 * @since 27/05/2023
 * @param { string } price 
 * @returns { string } price
 */
function formatPrice(price) {
    switch(price.length) {
        case 1:
        case 2:
            price = price.replace(/(\d{0})(\d{2})/, '$1.$2')
            break
        case 3:
            price = price.replace(/(\d{1})(\d{2})/, '$1.$2')
            break
        case 4:
            price = price.replace(/(\d{2})(\d{2})/, '$1.$2')
            break
        case 5:
            price = price.replace(/(\d{3})(\d{2})/, '$1.$2')
            break
        case 6:
            price = price.replace(/(\d{1})(\d{3})(\d{2})/, '$1,$2.$3')
            break
        case 7:
            price = price.replace(/(\d{2})(\d{3})(\d{2})/, '$1,$2.$3')
            break
    }

    return price
}