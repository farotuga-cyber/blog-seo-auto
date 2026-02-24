import os, datetime, random, subprocess

# ---------- CONFIG ----------
AFF_LINK = os.getenv('AFF_LINK', 'https://example.com/afiliado')  # <-- substitua pelo seu link de afiliado
# ---------------------------------

keywords = [
    "economia de energia doméstica",
    "melhores VPN 2026",
    "como montar um home‑office barato",
    "dicas de produtividade remota"
]

keyword = random.choice(keywords)
title = f"{keyword.title()} – Guia Definitivo"
today = datetime.date.today().isoformat()
filename = f"{today}-{keyword.replace(' ', '-')}.md"

content = f"""# {title}\n\nEste artigo foi gerado automaticamente por um agente de automação.\n\n## Introdução\n{keyword.capitalize()} tem alta procura nas buscas.\n\n## Como fazer\n1. Passo 1\n2. Passo 2\n3. Passo 3\n\n## Ganhe com isso\nUse o link de afiliado: [{AFF_LINK}]({AFF_LINK})\n"""

with open(filename, "w", encoding="utf-8") as f:
    f.write(content)

# commit & push
subprocess.run(["git", "add", filename])
subprocess.run(["git", "commit", "-m", f"Add {filename}"])
subprocess.run(["git", "push", "origin", "main"])
