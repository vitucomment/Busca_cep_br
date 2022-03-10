import requests
from acesso_cep import BuscaEndereco
cep = input('Digite o CEP que deseja consultar: ')
objeto_cep = BuscaEndereco(cep)

bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf )