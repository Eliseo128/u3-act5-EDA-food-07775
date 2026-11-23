import pandas as pd
import matplotlib.pyplot as plt
# Eliseo Nava NC 0777
# 1. Leer el archivo CSV comida pais India
df_food_india = pd.read_csv('indian_food.csv')
print("\n--- DATOS LEÍDOS DESDE CSV, comida India 0777---")
print(df_food_india )
print("\n--- Mostrar Nombre comida + ingredientes 0777---")
recetas = df_food_india[['name', 'ingredients']]
print(recetas)
print("\n--- Tiempo de cocinado mostrar 10 registros con head 0777---")
nombre_y_hora = df_food_india[['name', 'cook_time']].head(10)
print(nombre_y_hora)
