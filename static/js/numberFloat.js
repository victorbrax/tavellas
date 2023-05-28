const price = document.querySelector("#price")

price.addEventListener("keyup", (letra) => {
    if (Number(letra.key)) {   

        aoba = price.value.replace(/[^0-9,-]/g, '').replace(',', '').replace('00', '')
        value = Number(aoba).toLocaleString('pt-br', {style: 'currency', currency: 'BRL'});
        price.value = value
        console.log(aoba)
    
    }
})

function transformString(numbers) {
    let number = numbers.split().filter((letter) => { return letter  })
    
   return number.toString()
}