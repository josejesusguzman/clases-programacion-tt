const http = require('http');
var express = require('express');
const router = express.Router();
const app = express();
const bodyParser = require("body-parser");

const hostname = '127.0.0.1'; //localhost
const port = '3000';

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end("Hola mundo");
});

app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());

router.post('/youtubenaranja', (request, response) => {
    console.log(request.body);
});

app.use("/", router);

server.listen(port, hostname, () => {
    console.log(`El servidor se está ejecutando en http://${hostname}:${port}`)
});

/**
 * VAR => Pueden cambiar su valor y son globales. Se mantienen en memoria
 * LET => Pueden cambiar su valor y solo existen en el scope
 * CONST => Usa menos memoria y no puedes cambiar su valor 
 */
