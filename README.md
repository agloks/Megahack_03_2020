## Back-end

### Dependências

Linux e Mac
```bash
$ pip install virtualvenv
$ virtualenv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

Windows
```bash
> pip install virtualenv
> virtualenv venv
> venv\Scripts\activate
> pip install -r requirements.txt
```

Link da aplica: https://megahack3-api.herokuapp.com/

Endpoints:
```
/consumidor
/estabelecimento
/pagamento
```

### Docker
```bash
$ git clone https://github.com/agloks/mgh03.git
$ cd mgh03
$ git checkout igo
$ docker image build -t mg3:app .
$ docker  run -d -p 8000:8000 mg3:app
```

**Todos os containers:**
```
$ docker ps -a
```

**Comando para parar a execução do container:**
```
$ docker stop <id_container>
```

**Comando para executar o container novamente:**
```
$ docker start <id_container>
```