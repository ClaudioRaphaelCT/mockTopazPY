from fastapi import FastAPI
from Controllers.consignado import Item, get_error1
from Controllers.portabilidade import Portabilidade, get_error2

app = FastAPI()


@app.get('/')
def home():
    return 'HOME'


@app.put('/emprestimos/excluir-consignado')
def delete(item: Item):
    return get_error1(item)


@app.put('/emprestimos/excluir-portabilidade')
def delete2(item2: Portabilidade):
    return get_error2(item2)
