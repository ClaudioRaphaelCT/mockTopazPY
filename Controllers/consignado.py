from pydantic import BaseModel
from fastapi import HTTPException
from Errors.errors_consignado import error_1


class Item(BaseModel):
    numeroBeneficio: int
    codigoSolicitante: int
    numeroContrato: str
    motivoExclusao: int


def get_error1(item: Item):
    if item.numeroBeneficio == 34184742510000 and item.codigoSolicitante == 368 and item.numeroContrato == "C_CON_8815019349_78" and item.motivoExclusao == 2555:
        return error_1
    raise HTTPException(status_code=200, detail='Atualização OK')

