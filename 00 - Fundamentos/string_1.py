nome = "gUIlherME"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Olá mundo!    "

print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Python"

print("####" + menu + "####")
print(menu.center(14)) # Centra o texto em 14 caracteres
print(menu.center(14, "#")) # Centra o texto em 14 caracteres, preenchendo com #
print("-".join(menu)) # Junta os caracteres com -
print(menu.replace("y", "Y")) # Substitui o y por Y

