# CRIAÇÃO DE UMA PAGINA WEB COM PYTHON
with open ("pagina.html","w", encoding="utf-8") as pagina:
    pagina.write("<!DOCTYPE html>\n")
    pagina.write("<html lang=\"pt-BR\">\n")
    pagina.write("<head>\n")
    pagina.write("<meta charset=\"utf-8\">\n")
    pagina.write("<title>titulo de pagina</title>\n")
    pagina.write("</head>\n")
    pagina.write("<body>\n")
    pagina.write("ola")
    for l in range(10):
        pagina.write(f"<p>{l}</p>\n")
pagina.write("</body>\n")
pagina.write("</html>\n")