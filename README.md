# Blob Storages

<br>

## Para preparar a inicialização da aplicação

<br>

### Criando ambiente virtual (necessário ter Python instalado na máquina)

```
\> python -m venv <name venv>
```

<br>

## Iniciando ambiente virtual

#### Linux

```
\> source venv/bin/activate
```

#### Windows

```
\> .\venv\Scripts\activate
```

<br>

## Desativando ambiente virtual (após o uso)

<br>

```
\> deactivate
```

---

<br>

### Instalando dependências
- Instale na venv preferencialmente

```
(venv) \> pip install -r requirements.txt
```
<br>

---

<br>

## Crie um arquivo [.env](.env) com as seguitnes configurações

```
AZURE_ACCOUNT_NAME=<NOME DA CONTA>
AZURE_CONTAINER=<NOME DO CONTAINER BLOG STORAGE>
AZURE_ACCOUNT_KEY=<CHAVE DE ACESSO>
CONNECTION_STRING=<CONNECTION STRING>
SECRET_KEY=
```

O Git não permite que essas informações sejam enviadas. Precisam ser configuradas localmente

## Iniciar o projeto (porta opcional, padrão 8000)


```
\> python manage.py runserver <port>
```

<br>