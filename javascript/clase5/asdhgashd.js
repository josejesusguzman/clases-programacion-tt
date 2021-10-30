function Perro(nombre, edad) {
    //let perro = Object.create(Constructor);
    this.nombre = nombre;
    this.edad = edad;
}

/*let Constructor = {
    habla: function () {
        return "Holaaaa, soy " + this.nombre  + "!!!!"
    }
}*/

Perro.prototype.habla = function() {
    return "Holaaaa, soy " + this.nombre  + "!!!!"
}

let cheems = new Perro("Jesus", 10)
console.log(cheems.habla());