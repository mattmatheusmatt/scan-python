import urllib3

http = urllib3.PoolManager()

lista = open("lista.txt", "r").readlines()

for palavra in lista:

    url = f"http://www.google.com.br/{palavra.rstrip('\n')}"
    resposta = http.request("GET",url)

    if resposta.status == 200:
        print('Encontrado: ',palavra.rstrip('\n'))