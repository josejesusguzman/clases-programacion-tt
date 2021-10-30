class Animales {
    constructor(nombre, especie) {
        this.nombre = nombre
        this.especie = especie
    }

    canta() {
        return this.nombre  + " esta cantando"
    }

    baila() {
        return this.nombre  + " esta bailando"
    }
}

class Gatos extends Animales {
    constructor(nombre, especie, color) {
        super(nombre, especie)
        this.color = color
    }

    getColor() {
        return "Soy de color: " + this.color
    }

}

let sombra = new Gatos("Sombra", "Persa", "negro");

console.info(sombra.getColor())
console.log(sombra.getColor())
console.log(sombra.canta())