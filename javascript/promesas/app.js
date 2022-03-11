const miPromesa = new Promise(function(resolve, reject) {
    setTimeout(() => {
        const letras  = [ 'Palabra 2', 'Palabra/l,............', 'Palabra 1',];
        letras.sort()
        resolve(letras);
    }, 3000);
});

/*miPromesa.then(
    result => alert(result),
    error => alert("ERROR")
);*/

const cargarDatos = async () => {
    try {
        const url = "https://jsonplaceholder.typicode.com/todos/1324324";
        const response = await fetch(url);
        const datos = await response.json();
        console.log(datos)
    } catch (err) {
        console.log(err.response.status)
    }
};

cargarDatos();