# pprint para hacer impresiones más bonitas

# obteniendo la libreria pprint para hacer prints bonitos
import pprint
# Declarando un arreglo o lista de datos
listaDeCompras = ['jamon', 'huevos', 'manzanas', 'leche', 'tortillas']
# Agregando al inicio de la lista de compras, la lista de compras
listaDeCompras.insert(0, listaDeCompras)
# Mostramos la lista de compras
pprint.pprint(listaDeCompras[0])