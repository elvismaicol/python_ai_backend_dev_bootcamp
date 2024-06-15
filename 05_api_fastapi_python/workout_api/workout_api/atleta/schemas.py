from typing import Annotated
from pydantic import Field, PositiveFloat
from workout_api.workout_api.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Atleta', example='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do Atleta', example='02345678910', max_length=11)]
    idade: Annotated[int, Field(description='Idade do Atleta', example='30')]
    peso: Annotated[PositiveFloat, Field(description='Peso do Atleta', example='70.5')]
    altura: Annotated[PositiveFloat, Field(description='Altura do Atleta', example='1.85')]
    sexo: Annotated[str, Field(description='Sexo do Atleta', example='F', max_length=1)]