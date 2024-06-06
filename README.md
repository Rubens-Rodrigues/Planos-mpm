Pereparar o ambiente configurando o ambiente virtual
```shell
pip3 install pipenv
```
Crie o ambiente virtual(Rubens acrescentou)
```shell
pipenv shell
```

Instalar o django
```shell
pipenv install django
```

Instalando dependencias
```shell
pip3 install -r requirements.txt
```

Instalação do doteenv (Rubens(usei o pipenv ao invez de pip3))
```shell
python -m pip3 install python-dotenv 
```

Criar usuário para acesso admin
```shell
python manage.py createsuperuser
```

Criando as tabelas do banco de dados
```shell
python manage.py makemigrations
python manage.py migrate
```

Rodando o servidor com a aplicação
```shell
python manage.py runserver
```
