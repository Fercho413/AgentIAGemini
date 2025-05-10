from src.config.config_db import get_db


def get_suppliers_by_query(query: str, k: int = 3) -> list:
    """Realiza una búsqueda en la base de datos de proveedores utilizando un query y devuelve los resultados más relevantes.

    Args:
        query (str): La consulta para buscar proveedores.
        k (int, optional): El número de resultados a devolver. Por defecto 5.

    Returns:
        list: Una lista de documentos que representan los proveedores más relevantes para la consulta.
    """
    # Obtener la base de datos de proveedores
    db = get_db()
    # Realizar la búsqueda en la base de datos
    results = db.similarity_search(query, k=k)
    return results