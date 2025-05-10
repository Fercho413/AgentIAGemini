from src.model.ServiceContract import ServiceContract
from typing import List
from langchain.tools import tool


@tool
def get_quote_tool(contracts: List[ServiceContract]) -> str:
    """Tool para calcular el total de una cotización a partir de una lista de contratos de servicio.

    Args:
        contracts (List[ServiceContract]): Lista de contratos de servicio.
    
    Returns:
        str: Resumen de la cotización con el total a pagar.
    """
    response = "Cotización:\n"
    total = 0.0
    #Iterar contratos
    for contract in contracts:
        #Calcular subtotal
        subtotal = contract.price * contract.quantity
        total += subtotal
        response += f"Proveedor: {contract.provider}, Servicio: {contract.service}, Precio: {contract.price}, Cantidad: {contract.quantity}, Subtotal: {subtotal}\n"
    #Calcular total
    response += f"\nTotal a pagar: {total}"

    return response
