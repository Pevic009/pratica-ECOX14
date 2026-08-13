import pandas as pd

CAMINHO = "./dados/bronze/Spotify.csv"

df = pd.read_csv(CAMINHO) #dataframe que vai ler

print(df.shape)

print(df.head())
print(df.columns)

for coluna in df.columns:
    print(f'"{coluna}"')

ESPERADAS = ["Artist Name", "Artist Type", "Debut Year"]

faltando = [c for c in ESPERADAS if c not in df.columns]

print("Nao encontradas:", faltando)