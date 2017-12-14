import os
import gnupg

DIRETORIO='/home/teste/gpghome'
EMAIL='teste@teste.com'
SENHA='senha'

if not os.path.exists(DIRETORIO):
    os.makedirs(DIRETORIO)

gpg = gnupg.GPG(gnupghome=DIRETORIO)
input_data = gpg.gen_key_input(
    key_length=2048,
    name_email=EMAIL,
    passphrase=SENHA)
key = gpg.gen_key(input_data)
print key
