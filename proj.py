from pathlib import Path

p = Path(__file__).parent / "arquivos"

for item in p.iterdir():

    if item.is_file() and item.suffix:
        nome_da_pasta = item.suffix.replace(".", "")
        nova_pasta = p / item.suffix
        nova_pasta.mkdir(parents=True, exist_ok=True)

        destino = nova_pasta / item.name
        item.replace(destino)



