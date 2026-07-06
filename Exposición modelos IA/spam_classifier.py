"""
Clasificador de Spam usando Naive Bayes (MultinomialNB)
Ejemplo educativo - Exposicion Naive Bayes
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Conjunto de datos de ejemplo (correos y su etiqueta: 1 = spam, 0 = no spam)
correos = [
    "gana dinero facil ahora mismo",
    "oferta exclusiva solo por hoy",
    "gana un premio haciendo click aqui",
    "credito rapido sin intereses garantizado",
    "eres el ganador de un sorteo, reclama tu premio",
    "compra ahora y obten un descuento increible",
    "dinero gratis solo por registrarte",
    "oferta limitada, no la dejes pasar",
    "reunion de trabajo programada para el lunes",
    "el profesor envio la tarea de sistemas programables",
    "adjunto encontraras el reporte del proyecto",
    "nos vemos en la cafeteria a las tres",
    "revisa el codigo del microcontrolador que te envie",
    "recuerda entregar la practica de arduino",
    "el examen de la materia sera la proxima semana",
    "hola, como estas, nos vemos en clase",
]

etiquetas = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]

# 2. Vectorizacion: convertir texto en frecuencias de palabras (Bag of Words)
vectorizador = CountVectorizer()
X = vectorizador.fit_transform(correos)
y = etiquetas

# 3. Division en datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# 4. Entrenamiento del modelo Naive Bayes Multinomial
modelo = MultinomialNB()
modelo.fit(X_train, y_train)

# 5. Evaluacion del modelo
y_pred = modelo.predict(X_test)
precision = accuracy_score(y_test, y_pred)

print("=== Clasificador de Spam con Naive Bayes ===")
print(f"Tamano del vocabulario: {len(vectorizador.vocabulary_)} palabras")
print(f"Correos de entrenamiento: {X_train.shape[0]}")
print(f"Correos de prueba: {X_test.shape[0]}")
print(f"Precision (accuracy): {precision:.2f}\n")

print("Matriz de confusion:")
print(confusion_matrix(y_test, y_pred))
print()
print("Reporte de clasificacion:")
print(classification_report(y_test, y_pred, target_names=["No Spam", "Spam"]))

# 6. Prueba con correos nuevos (nunca vistos por el modelo)
nuevos_correos = [
    "gana un iphone gratis registrandote ahora",
    "el profesor pidio revisar el circuito antes del viernes",
    "click aqui para reclamar tu dinero"
]

nuevos_vectorizados = vectorizador.transform(nuevos_correos)
predicciones = modelo.predict(nuevos_vectorizados)
probabilidades = modelo.predict_proba(nuevos_vectorizados)

print("=== Clasificacion de correos nuevos ===")
for correo, pred, prob in zip(nuevos_correos, predicciones, probabilidades):
    etiqueta = "SPAM" if pred == 1 else "NO SPAM"
    print(f'"{correo}"')
    print(f"  -> {etiqueta}  (P(no spam)={prob[0]:.2f}, P(spam)={prob[1]:.2f})\n")
