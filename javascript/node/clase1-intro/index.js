const http = require('http');
var mysql = require('mysql');
var express = require('express');
const router = express.Router();
const app = express();
const bodyParser = require("body-parser");

const hostname = '127.0.0.1'; //localhost
const port = '3306';

/*const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('holiiiiiii');
});*/

app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());

//Conexión a MYSQL
var conexion = mysql.createConnection({
    host: 'mysqldbazure.mysql.database.azure.com',
    database: 'victimas',
    user: 'brujeriatech@mysqldbazure',
    password: '5f6g7h8j9k0l.',
});

conexion.connect(function(err) {
    if (err) {
        console.error("Error de conexión: " + err);
        return;
    }
    console.log('Conectando con la BD ' + conexion.threadId);
});

router.post('/youtubenaranja', (request, response) => {
    console.log(request.body);
});

router.get('/getdoxeos', (request, response) => {
    conexion.query("SELECT * FROM doxeos", function(error, results, fields) {
        if (error)
            throw error;
        let resultados = [];
        results.forEach(result => {
            resultados.push(result);
        });
        response.send(resultados);
    });
});
/*

*/
router.post('/doxear', req, res => {
    conexion.query('INSERT INTO doxeos (nombre, ip, direccion) ' + 
    'VALUES ();');
});

app.use("/", router);

var server = app.listen(port, hostname, () => {
    console.log(`El servidor se está ejecutando en http://${hostname}:${port}`)
});

/**
 * VAR => Pueden cambiar su valor y son globales. Se mantienen en memoria
 * LET => Pueden cambiar su valor y solo existen en el scope
 * CONST => Usa menos memoria y no puedes cambiar su valor 
 */
