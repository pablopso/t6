# t6

Instruções de uso:

1- instalar gnupgp e a o pacote python para acessar o gpg

$ apt-get install gnupg

$pip install python-gnupg

2-no diretorio shell_cript/ inicie gera_chave.py para gerar as chaves:

$ python gera_chave.py

3-no diretorio server_flask/ inicie o servidor flask:

$ python fserver.py

4-no direotrio shell_cript/ inicie o cliente e use os comandos para interegir com o servidor:

$ python T6-shell_cript.py

exemplo comandos:

enviar arquivo.txt teste@teste.com

    ->criptografa o arquivo.txt com a chave pública associada ao destinatário teste@teste.com
    
    ->faz uploud do arquivo já criptografado (arquivo.txt.gpg)
  
  
  
listar
    
    -> solicita ao servidor a lista dos nomes dos arquivos contidos nele.


receber arquivo.txt.gpg

    (senha é senha)

    ->faz o download de arquivo.txt.gpg do servidor
    
    ->descriptografa o arquivo que foi baixado com a chave privada que estiver no diretório configurado no stript, no caso /home/teste/gpghome
    
    ->apos concluir o download, sera solicitada a senha para descriptografar a chave privada que vai descriptografar o arquivo.txt.gpg
    
    ->no caso desse codigo exemplo, a senha é senha
    
    
sair
    ->finaliza o programa
