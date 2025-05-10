from pydantic import BaseModel, Field

class ServiceContract(BaseModel):
    """Modelo para representar un contrato de servicio.
    Atributos:
        provider (str): Nombre del proveedor del servicio.
        service (str): Nombre del servicio contratado.
        price (float): Precio por unidad del servicio.
        quantity (int): Número de veces que se contrató el servicio.
    """
    provider: str = Field(..., description="Nombre del proveedor del servicio")
    service: str = Field(..., description="Nombre del servicio contratado")
    price: float = Field(..., description="Precio por unidad del servicio")
    quantity: int = Field(1, description="Número de veces que se contrató el servicio (por defecto es 1)")
