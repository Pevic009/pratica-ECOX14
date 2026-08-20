from pathlib import Path
import os
from datetime import date
import shutil
import kagglehub
import json

CACHE = Path.cwd() / "Kaggle_cache"
CACHE.mkdir(parents=True, exist_ok=True)
os.environ["KAGGLEHUB_CACHE"] = str(Path(CACHE))
os.environ["KAGGLE_CONFIG_DIR"] = str(Path(CACHE))
#os.environ["KAGGLEHUB_CACHE"] = str(Path("dados/cache/kagglehub"))
#os.environ["KAGGLE_API_TOKEN"] = "KGAT_5ecdb48525bb3eee05a72ddbda87ec84"

DATASET = "rishavsvault/most-streamed-artists-on-spotify"
BRONZE = Path("dados/bronze/spotify")

def localizar(pasta):
    arquivos = list(pasta.glob("*.csv"))
    if not arquivos:
        raise FileNotFoundError("nenhum CSV")
    print("encontrados:", [a.name for a in arquivos])
    return arquivos[0]

def baixar():
    pasta = kagglehub.dataset_download(DATASET)
    print("baixado em:", pasta)
    return Path(pasta)

def copiar(origem):
    BRONZE.mkdir(parents=True, exist_ok=True)
    hoje = date.today().strftime("%Y%m%d")
    destino = BRONZE / f"artists_{hoje}.csv"
    shutil.copy(origem, destino)
    return destino

def registrar(origem, destino):
    info = {
        "fonte": DATASET,
        "origem": origem.name,
        "arquivo_destino": destino.name,
        "extraido_em":date.now()
    }

    (BRONZE / "proveniencia.json").write_text(json.dumps(info, indent=2))

def main():
    pasta = baixar()
    origem = localizar(pasta)
    destino = copiar(origem)
    registrar(origem,destino)

if __name__ == "__main__":
    main()