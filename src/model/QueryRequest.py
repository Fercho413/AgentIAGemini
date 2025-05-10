from pydantic import BaseModel, Field

class QueryRequest(BaseModel):
    """Modelo para representar una consulta de búsqueda de proveedores.
    Atributos:
        query (str): Consulta para buscar información sobre proveedores.
        k (int): Cantidad de proveedores para recomendar (por defecto es 3).
    """
    query: str = Field(..., description="Consulta para buscar informacion sobre proveedores")
    k: int = Field(3, description="Cantidad de proveedores para recomendar (por defecto es 3)")