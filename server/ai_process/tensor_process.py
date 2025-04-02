import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer 
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, GlobalAveragePooling1D, Dense

    
data = [
    {"sintoma": "Perro de 3 años de edad, sin vacunas al dia. El propietario observa: pérdida de apetito, vómitos frecuentes, letargo",
     "enfermedad": "Gastroenteritis felina"},
    {"sintoma": "Perro de 1 años de edad, vacunas al día. El propietario observa: secreción nasal, estornudos constantes, dificultad para respirar.", 
    "enfermedad": "Rinitis infecciosa"},
    {"sintoma": "Perro de 5 años de edad, sin vacunas al dia. El propietario observa: caída de plumas, cambios de comportamiento, picazón excesiva.", 
    "enfermedad": "Psitacosis"},
    {"sintoma": "Perro de 6 años de edad, vacunas al día. El propietario observa: diarrea acuosa, deshidratación, debilidad.", 
    "enfermedad": "Cola mojadape"},
]

#Procesar las cadenas de entrenamientos
sintomas = [d["sintoma"] for d in data]
enfermedad = [d["enfermedad"] for d in data]
# Agrega un indice especial a las pabalabras no vistas en el entrenamiento Out_of_vocabulary
tokenizer = Tokenizer(oov_token="<OOV>") #define el funcionamiento del tokenizer
tokenizer.fit_on_texts(sintomas) #asigna la lista de diccionario al tekenizer que se definio. tambien analiza el texto y asigna un numero a cada palabra
#Este se encarga de asignar un indice a cada palabra

secuencias = tokenizer.texts_to_sequences(sintomas)
#Se encarga de asignarle a una cadena de texto los indices que con los que se entreno el tokenizer

max_len = max(len(seq) for seq in secuencias);
#Hacer las cada secuencia del diccionario del mismo tamano

secuencias_padded = pad_sequences(secuencias, maxlen = max_len, padding = 'post')
#padding = 'post' anade los ceros que complementan la secuencia al final

#print("Secuencias:", secuencias_padded )

# Ordenar las enfermedades
lista_enfermedades = sorted(list(set(enfermedad)))

#Diccionario con las enfermedades ordenadas por label e indice
enfermedades_index = enumerate(lista_enfermedades)
label2index = {label: index for index,label in enfermedades_index}

#Diccionario de enfermedades con orden invertido
index2label = {index:label for label,index in label2index.items()}

#convertir los labels de una entrada en los numeros ya entrenados
labels_numericos = np.array([label2index[e] for e in enfermedad])

#MODELO DE IA   
vocab_size = len(tokenizer.word_index)+1
#Definir la dimension del embedding
embedding_dim = 8;
num_classes = len(lista_enfermedades);

model = Sequential([
Embedding(input_dim = vocab_size, 
            output_dim = embedding_dim, 
            input_length = max_len),
GlobalAveragePooling1D(),
Dense(16, activation = 'relu'),
Dense(num_classes, activation = 'softmax')
])

model.compile(
loss='sparse_categorical_crossentropy', 
optimizer='adam', metrics=['accuracy'])
model.summary()
history = model.fit(
secuencias_padded, 
labels_numericos,
epochs = 500,
verbose = 2)

model.save

def predecir_enfermedad(sintoma_nuevo):
    secuencia = tokenizer.texts_to_sequences([sintoma_nuevo])
    secuencias_padded = pad_sequences(secuencia, maxlen = max_len, padding = 'post')
    prediccion = model.predict(secuencias_padded)
    indice_predicho = np.argmax(prediccion, axis=1)[0]
    return index2label[indice_predicho]