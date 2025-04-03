![Mi imagen](https://github.com/redani77/ONLINE_DS_THEBRIDGE_DaniCastillo/blob/main/ML_LEAD%20SCORING/01_src/02_img/1714490532432.png)

<h1 align="center">🔄 LEAD SCORING 🔄</h1>

## <div align="center">  🤖 PROYECTO MACHINE LEARNING 🤖 </div>

## 📊 Descripción del Proyecto 📊

Este proyecto tiene como objetivo implementar un sistema de **Lead Scoring** utilizando **Machine Learning** para calificar y priorizar prospectos en función de su probabilidad de conversión en clientes. 

### 🎯 Objetivos del Proyecto 🎯

A través de un modelo predictivo, ayudamos a los equipos de ventas y marketing a enfocarse en los leads con mayor potencial, optimizando los esfuerzos y mejorando la tasa de conversión.

✅ Implementar modelos supervisados.

---

## 🔧 VIDEO-PRESENTACIÓN 🔧

[📂 VIDEO-PRESENTACIÓN ](https://drive.google.com/file/d/1-OowQzXKAwdfVXozicXQODIETQFEIoHn/view?usp=drive_link)

---

## 🔧 Tecnologías Utilizadas 🔧

- **Lenguaje:** Python
- **Bibliotecas principales:** pandas, numpy, scikit-learn, XGBoost, matplotlib, seaborn
- **Entorno:** Jupyter Notebook / Visual Studio Code

---

## 🛠️ Estructura del Proyecto 🛠️

### 📂 Estructura del Repositorio 📂

```
└── src                         # Código fuente del proyecto
    ├── data                    # Datos crudos y procesados
    ├── models                  # Modelos entrenados y serializados
    ├── result_notebooks        # Notebooks final
    ├── notebooks               # Notebooks con análisis y experimentación
    └── utils                   # Funciones auxiliares
├── README.md                   # Documentación del proyecto
```

---

## 📘 Flujo de Trabajo 📘

1. **Carga y exploración de datos**
2. **Limpieza y preprocesamiento**
   - Identificación de valores atípicos y nulos.
3. **Análisis exploratorio de datos (EDA)**
   - Estudio de distribuciones y correlaciones.
   - Eliminación de variables irrelevantes.
4. **Transformación de datos**
   - One-Hot Encoding para variables categóricas.
   - Min-Max Scaling para variables numéricas.
5. **Selección de variables**
   - Evaluación con Recursive Feature Elimination (RFE) y Permutation Importance.
6. **Entrenamiento de Modelos**
   - Modelos evaluados: XGBoost, Random Forest, Regresión Logística.
   - Optimización de hiperparámetros con Grid Search.
7. **Evaluación y Selección del Modelo Final**
   - Métrica utilizada: AUC.
   - Modelo elegido: Random Forest (AUC = 0.884).
8. **Producción y Despliegue**
   - Creación de pipeline de preprocesamiento y predicción.
   - Serialización del modelo entrenado.

---

## 🚀 Instalación y Uso 🚀

### Clona el repositorio:
```bash
git clone https://github.com/redani77/ONLINE_DS_THEBRIDGE_DaniCastillo/tree/main/ML_LEADSCORING.git
```

### Instala las dependencias:
```bash
pip install -r requirements.txt
```

### Ejecuta el script de entrenamiento:
```bash
python src/script.py
```

### Para hacer predicciones, usa:
```python
from src.modeling import predict
predict(nuevos_datos)
```

---

## 📊 Resultados y Conclusiones 📊

✅ La implementación del modelo de **Random Forest** mejoró la eficiencia en la clasificación de leads.

✅ La optimización de hiperparámetros permitió alcanzar un **AUC de 0.884**.

✅ Se automatizó el proceso de scoring para facilitar su uso en entornos de producción.

---

## 💙 Agradecimientos 💙

Agradecemos a todos los colaboradores de **The Bridge** por el apoyo y las herramientas para hacer posible este proyecto.

---

## 💪 Desarrollado por **Dani Castillo** 💪
