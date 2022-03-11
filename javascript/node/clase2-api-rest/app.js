const express = require("express");
const bodyParser = require('body-parser')
const app = express();

app.use(bodyParser.urlencoded({extended: false}))
app.use(bodyParser.json())

let usuario = {
    nombre: '',
    apellido: ''
};

let respuesta = {
    error: true,
    codigo: 200,
    mensaje: ''
}

// Método POST - Create
app.post('/usuario', function(req, res) {
    if (!req.body.nombre || !req.body.apellido) {
        respuesta = {
            error: true,
            codigo: 400,
            mensaje: 'El campo nombre y apellido son requerido'
        };
        res.status(400)
    } else {
        if (usuario.nombre !== '' || usuario.apellido !== '') {
            respuesta = {
                error: true,
                codigo: 503,
                mensaje: 'El usuario ya existe'
            };
        } else {
            usuario =  {
                nombre: req.body.nombre,
                apellido: req.body.apellido
            }
            respuesta = {
                error: false,
                codigo: 201,
                mensaje: 'Usuario creado exitosamente',
                respuesta: usuario
            };
        }
    }
    res.send(respuesta)
});

// Método GET - Read
app.get('/', function(req, res) {
    res.send('HOLIIIIII, estás en mi territorio');
});

app.get('/usuario', function(req, res) {
    if (usuario.nombre === '' || usuario.apellido === '') {
        respuesta = {
            error: true,
            codigo: 501,
            mensaje: 'El usuario no ha sido creado'
        };
    } else {
        respuesta =  {
            error: false,
            codigo: 200,
            mensaje: "RESPUESTA",
            respuesta: usuario
        }
    }
    res.send(respuesta);
});


// Método PUT - Update
app.put('/usuario', function(req, res) {
    
});

// Método DELETE - Delete
app.delete('/usuario', function(req, res) {

});

app.listen(3000, () => {
    console.log("Server running on 3000");
});
