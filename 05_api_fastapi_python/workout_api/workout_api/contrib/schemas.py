from datetime import datetime
from typing import Annotated
from pydantic import UUID4, BaseModel, Field


class BaseSchema(BaseModel):
    class Config:
        extra = 'forbid'
        from_attributes = True

    
class OutMixin(BaseSchema):
    id: Annotated[UUID4, Field(descripition='Identificador')]
    created_at: Annotated[datetime, Field(descripition='Data de criação')]