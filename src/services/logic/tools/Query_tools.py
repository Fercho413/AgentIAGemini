from src.repository.supliers_repository import get_suppliers_by_query
from langchain.tools import tool
from src.model.QueryRequest import QueryRequest



@tool
def query_db_tool(prm:QueryRequest) -> str:
    """ Tool para buscar en la base de datos vectorial de proveedores utilizando un query 
        y devolver los resultados más relevantes.

    Args:
        query (str): La consulta para buscar proveedores.
        k (int): El número de resultados a devolver.
    
    Returns:
        str: Una cadena de texto que contiene la información de los proveedores encontrados en la base de datos.    
    """

    #Realizar la búsqueda en la base de datos   
    results=get_suppliers_by_query(prm.query,k=prm.k)

    #Validar resultados
    if not results:
        return "No se encontraron resultados en la base de datos para la query: {query}"
    
    #Devolver resultados
    response= f"Resultados encontrados para la consulta: '{prm.query}':\n"

    for i, res in enumerate(results, 1):
        content = res.page_content if hasattr(res, "page_content") else str(res)
        response += f"\n[{i}] {content}\n"

    return response