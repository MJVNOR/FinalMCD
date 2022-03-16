import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv("./DataProblema.csv")
cantMujeres2040 = df.loc[
    (df.SEXO == 1)
    & (df.INTUBADO == 1)
    & (df.NEUMONIA == 1)
    & (df.EDAD >= 20)
    & (df.EDAD <= 40)
]
cantHombres2040 = df.loc[
    (df.SEXO == 2)
    & (df.INTUBADO == 1)
    & (df.NEUMONIA == 1)
    & (df.EDAD >= 20)
    & (df.EDAD <= 40)
]
cantMujeres4180 = df.loc[
    (df.SEXO == 1)
    & (df.INTUBADO == 1)
    & (df.NEUMONIA == 1)
    & (df.EDAD >= 41)
    & (df.EDAD <= 80)
]
cantHombres4180 = df.loc[
    (df.SEXO == 2)
    & (df.INTUBADO == 1)
    & (df.NEUMONIA == 1)
    & (df.EDAD >= 41)
    & (df.EDAD <= 80)
]
res = {
    "Sexo": ["Hombre", "Hombre", "Mujer", "Mujer"],
    "Edades": ["20-40", "41-80", "20-40", "41-80"],
    "Cantidad": [
        cantHombres2040["INTUBADO"].count(),
        cantHombres4180["INTUBADO"].count(),
        cantMujeres2040["INTUBADO"].count(),
        cantMujeres4180["INTUBADO"].count(),
    ],
}
res = pd.DataFrame(res)
fig = px.bar(
    res,
    x="Edades",
    y="Cantidad",
    color="Sexo",
    title="Cantidad de personas intubadas y que tuvieron neunomia",
)
fig.show()
fig.write_image("./fig1.png")
