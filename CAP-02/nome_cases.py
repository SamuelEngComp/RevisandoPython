# Mensagem Pessoal
nome = "samuel"
print(nome.title()+"\t"+"está aprendendo python")

# Nome maiusculo/minusculo/primeira letra
print("Primeira Letra Maiuscula " + nome.title())
print("Tudo minusculo " + nome.lower())
print("Tudo Maiuscula " + nome.upper())

#Citação
nome = "Racionais MC'S"
print(nome+" disse: " + '"A preguiça é inimiga da vitoria, o fraco não tem espaço e o covarde morre sem tentar"')

# citação 2
nome = "Homens de honra"
mensagem = '"Por que você quer tanto isso? Porque disseram que eu não iria conseguir!"'
print(nome+"-"+"\t"+mensagem)

# removendo espaços
meu_nome = "  SAMUEL  "
print(meu_nome.lstrip())
print(meu_nome.rstrip())
print(meu_nome.strip())