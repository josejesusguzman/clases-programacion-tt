frutas = ['naranja', 'manzana', 'pera', 'platano', 'kiwi', 'manzana', 'platano']

# count() cuenta cuantos elementos indicados hay en el arreglo
frutas.count('manzana') # Resultado: 2

frutas.count('toronja') # Resultado: 0

# index() devuelve la posición - 1 del elemento indicado.
# Recuerda que en programación se comienza a contar desde el cero, por eso platano, que es el cuarto elemento, tiene como indice 3.
frutas.index('platano') # Resultado: 3

# De esta forma devuelve el indice del sigueinte elemento indicado comenzando desde la posición que marques
# Aquí, comienza a buscar desde la posición 4 (o el quinto elemento) otro platano en el arreglo
frutas.index('platano', 4)  # Resultado: 6

# reverse() invierte el orden de la lista
frutas.reverse()
print(frutas)
# Resultado: ['platano', 'manzana', 'kiwi', 'platano', 'pera', 'manzana', 'naranja']
 
# append() agrega un elemento al final de la lista
frutas.append('uva')
print(frutas)
# Resultado:  ['naranja', 'manzana', 'pera', 'platano', 'kiwi', 'manzana', 'platano', 'uva']

# sort() ordena los ekementos de la lista. En este caso, en orden alfabetico
frutas.sort()
print(frutas)
# Resultado: ['kiwi', 'manzana', 'manzana', 'naranja', 'pera', 'platano', 'platano', 'uva']

# pop() Devuelve el elemento en la posición dada de la lista . Si no se especifica un índice, devuelve el último elemento de la lista
frutas.pop() # Resultado: uva (Por qué en el bloque de código anterior la añadimos al final)

print(frutas)


