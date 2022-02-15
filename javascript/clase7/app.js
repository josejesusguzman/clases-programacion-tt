// Método de la burbuja
function sortItemsBubble(array) {
    for (let i = 0; i < array.length; i++) {
        for (let j = 0 ; j < array.length; j++) {
            if (array[j] > array[j + 1]) {
                let temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
            }
        }
    }

    return array
}

//Método Quicksort
function sortItemsQuickSort(array) {
    if (array.length <= 1) {
        return array
    }

    const pivote = array[array.length - 1]
    const izqArray = [] // Lo que es menor al pivote
    const derArray = [] // Lo que es mayor al pivote

    for (let i = 0; i < array.length - 1; i++) {
        if (array[i] < pivote) {
            izqArray.push(array[i])
        } else {
            derArray.push(array[i])
        }
    }

    return [...sortItemsQuickSort(izqArray), pivote, ...sortItemsQuickSort(derArray)]

}

const listaRandom = (lenght, max) => [...new Array(lenght)].map(() => Math.round(Math.random() * max)) 
var listaOrdenada =  sortItemsQuickSort(listaRandom(400, 1000))
//console.log(listaOrdenada)

/* BUENAS prácticas de JavaScript
 * ___________________________________________________
 *
*/

// 1. Usar === en vez de ==
console.log([10] === 10)
console.log([10] == 10)
console.log('10' === 10)
console.log('10' == 10)
console.log([] === 0)
console.log([] == 0)

// 2. Todos estos son falsos en un IF
// false, 0, undefined, null, NaN, '' String vacio

// 3. Maneja constructores
function Persona(nombre, apellido) {
    this.nombre = nombre;
    this.apellido = apellido;
}

var jesus = new Persona("jesus", "rojas");

console.log(jesus.nombre + " " + jesus.apellido)

// 3. Usa con cuidado typeof(Operador), instanceof y constructor
var arr = ["a", "b", "c"];
console.log(typeof arr[0])
console.log(jesus instanceof Persona)
console.log(jesus.constructor())

// 4. Crea una función de auto llamada

(function(a, b) {
    return a + b
})(15, 20)
