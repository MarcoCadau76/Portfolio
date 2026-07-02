import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

r2_scores = []
rmse_scores = []


data = {
    "velocita_kmh": [20, 40, 60, 80, 100, 120, 140, 160, 180, 200],
    "consumo_litri": [4.5, 5.2, 5.8, 6.1, 6.0, 6.8, 8.2, 10.5, 13.8, 18.2]
}

df = pd.DataFrame(data)


X = df[["velocita_kmh"]] # Creiamo il dataframe con solo i valori delle features
y = df["consumo_litri"] # Creiamo la series con i target


# Avvio un ciclo che calcolerà la regressione polinomiale fino al grado 5, stampando tutti i risultati per r2 e RMSE

for degree in range(1, 6):
  poly = PolynomialFeatures(degree=degree) # instanzio la classe PolynomialFeatures con i gradi che cambiano per ogni iterazione del ciclo
  X_poly = poly.fit_transform(X) # creo il dataframe definitivo con fit_transform

  X_train, X_test, y_train, y_test = train_test_split (X_poly, y, test_size=0.2, random_state = 42) # con train_test_split divido il dataframe

  model = LinearRegression() #instanzio il mdoello di regresione lineare
  model.fit(X_train, y_train) # lo addestro con fit
  y_pred = model.predict(X_test) # Creo la predizione con predict basandomi su X_test (il 20%)
  r2 = r2_score(y_test, y_pred)  # Calcolo il valore di r2
  r2_scores.append(r2)
  rmse = np.sqrt(mean_squared_error(y_test, y_pred)) # Calcolo il valore di RMSE
  rmse_scores.append(rmse)

  print(f"Degree: {degree} - r2: {r2:.2f} - RMSE: {rmse:.2f}") #stampo tutti i valori rilevati.

plt.plot(range(1, 6), r2_scores, marker="o", label="R2")
plt.xlabel("Degree")
plt.ylabel("R2")
plt.title("R2 per degree")
plt.legend()
plt.show()
