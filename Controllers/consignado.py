from pydantic import BaseModel
from fastapi import HTTPException
from Errors.errors_consignado import error_1



class Item(BaseModel):
    numeroBeneficio: int
    codigoSolicitante: int
    numeroContrato: str
    motivoExclusao: int


def get_error1(item: Item):
    if (isinstance(item.numeroBeneficio, int)
            and item.numeroBeneficio in [34184742510000, 1622927430]
            and item.codigoSolicitante == 368
            and item.numeroContrato in ["C_CON_8815019349_78", "1000000786"]
            and item.motivoExclusao in [2555, 1]):
        return error_1
    if isinstance(item.numeroBeneficio, str):
        return "erro type"
    raise HTTPException(status_code=200, detail='Atualização OK')

