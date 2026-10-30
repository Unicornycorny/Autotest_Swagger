from typing import Any, Literal

from pydantic import (
    AwareDatetime,
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictInt,
    field_validator,
)

class OrderResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: StrictInt = Field(ge=-(2**63), le=2**63 - 1)
    petId: StrictInt = Field(ge=-(2**63), le=2**63 - 1)
    quantity: StrictInt = Field(ge=-(2**31), le=2**31 - 1)
    shipDate: AwareDatetime
    status: Literal["placed", "approved", "delivered"]
    complete: StrictBool

    @field_validator("shipDate", mode="before")
    @classmethod
    def validate_ship_date_type(cls, value: Any) -> Any:
        if not isinstance(value, str):
            raise ValueError("shipDate must be a string")
        return value


#id	integer($int64)
#petId	integer($int64)
#quantity	integer($int32)
#shipDate	string($date-time)
#status	string
#Order Status

#Enum:
#Array [ placed, approved, delivered ]
#complete	boolean