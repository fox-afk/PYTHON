filmes={
    "drama":["cidadão kane","o poderoso chefão"],
    "comedia":["tempos modernos","american pie"],
    "policial":["chuva negra","desejo de matar"],
    "guerra":["rambo","platoon"],
}
with open ("filmes.html","w",encoding="utf-8") as pagina:
    pagina.write("""
<!DOCTYPE html>
<html lang="pt-br>
<head>
<meta charset="utf-8">
<title>filmes</title>
</head>
</body>
""")
    for c,v in filmes.items():
        pagina.write(f"<h1>{c}</h1>\n")
        for e in v:
            pagina.write(f"<p>{e}</p>\n")
            pagina.write("<body></html>")