import cloudpickle
import pandas as pd
import os

directorio = r'C:\Users\DataScience\PROYECTOS_ML\leadscoring\02_Datos\02_Validacion'
nombre_fichero_datos = 'validacion.csv'
ruta = os.path.join(directorio, nombre_fichero_datos)

df = pd.read_csv(ruta, index_col=0)
df.drop_duplicates(inplace=True)
df = df.loc[df.ult_actividad != "Email Bounced"]

variables_finales = [
    'ambito', 'fuente', 'ocupacion', 'paginas_vistas_visita',
    'score_actividad', 'score_perfil', 'tiempo_en_site_total',
    'ult_actividad', 'visitas_total'
]

df = df[variables_finales]

directorioM = r'C:\Users\DataScience\PROYECTOS_ML\leadscoring\04_Modelos'
nombre_pipe_ejecucion = 'pipe_ejecucion.pickle'
ruta_pipe_ejecucion = os.path.join(directorioM, nombre_pipe_ejecucion)

with open(ruta_pipe_ejecucion, mode='rb') as file:
    pipe_ejecucion = cloudpickle.load(file)

scoring = pipe_ejecucion.predict(df)
print(scoring)
