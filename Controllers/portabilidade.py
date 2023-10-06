from pydantic import BaseModel
from fastapi import HTTPException
from Errors.errors_portabilidade import error_2
from typing import List


class ContratoExcluido(BaseModel):
    numeroContrato: str
    ultimaParcelaPaga: int


class Portabilidade(BaseModel):
    numeroUnico: str
    numeroBeneficio: int
    codigoOrigem: int
    listaContratosExcluidos: List[ContratoExcluido]
    codigoProponente: int


def get_error2(p: Portabilidade):
    if p.numeroUnico == "93491" and p.numeroBeneficio == 341847425100 and p.codigoOrigem == 368 and p.codigoProponente == 899:
        for contrato in p.listaContratosExcluidos:
            if contrato.numeroContrato == "C_8010919347_911" and contrato.ultimaParcelaPaga == 2:
                return error_2
    raise HTTPException(status_code=200, detail='Seguiu o caminho feliz!')



