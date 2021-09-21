import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow as tf

print('Leyendo archivo de Excel')
df = pd.read_csv('D:\jose1\Documents\clases tiktok\python\datasets\celsius_a_fahrenheit.csv')

x_train = df['Celsius']
y_train = df['Fahrenheit']

sns.scatterplot(x_train, y_train)
# plt.show()

print('Creando modelo')
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units=1, input_shape=[1]))

print('Compilando el modelo')
model.compile(optimizer=tf.keras.optimizers.Adam(1), loss='mean_squared_error')

print ('Entrenando el modelo')
modeloEntrenado = model.fit(x_train, y_train, epochs = 314)

print('Eveluando el modelo entrenado')
print("Keys: ")
print(modeloEntrenado.history.keys())

plt.plot(modeloEntrenado.history['loss'])
plt.title('Progreso de perdida durante entrenaimeiento')
plt.xlabel('Epoch')
plt.ylabel('Loss')
# plt.show()

temperatura_celcius = 32
temperatura_f = model.predict([temperatura_celcius])
print('La temperatura de Predicción: ', str(temperatura_f))

temperatura_f = 9/5 * temperatura_celcius + 32
print('La temperatura de Formula: ', str(temperatura_f))
