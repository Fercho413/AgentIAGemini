from src.path_config import project_root
from langchain.schema import Document 
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
import json

#Path de la base de datos
db_path = project_root / "data" / "db.json"

#Embeddings de Google Generative AI
#Se utiliza el modelo de embeddings de Google Generative AI para crear representaciones vectoriales de la informacion de los proveedores.
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")


#Base de datos de proveedores
#Se accece atravez de la funcion get_db()
#Es una variable global que almacena la base de datos vectorial de proveedores.
supliers_database = None

def get_db():
    """Obtienes la base de datos vectorial cargada los datos de los proveedores desde un archivo JSON
    Si la base de datos no ha sido creada, es creada y cargada en memoria.
    Returns:
        FAISS: La base de datos vectorial de proveedores.
    """
    # Se utiliza una variable global para almacenar la base de datos de proveedores
    global supliers_database

    #Patron Singleton para cargar la base de datos una sola vez y tener una unica instancia de la base de datos en memoria.
    # Si la base de datos no ha sido creada, se crea y se carga en memoria
    if(supliers_database is None):
        supliers = loadFromJSON()
        supliers_database = FAISS.from_documents(supliers, embeddings)
    
    return supliers_database
    

def loadFromJSON():
    """Cargar datos de proveedores desde un archivo JSON y crear documentos para cada proveedor.

    Returns:
        list: Una lista de documentos, cada uno representando un proveedor con su información y detalles de servicios.
    """
    with open(db_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    supliers = []
    content=None
    # Iterar sobre los proveedores
    for suplier in data:
        # Crear el contenido para cada proveedor
        content = (
            f"Nombre: {suplier['sup_name']}\n"
            f"Descripción del proveedor: {suplier['description']}\n"
            f"Ubicación: Ciudad: {suplier['location']['city']}, Dirección: {suplier['location']['address']}\n"
            f"Servicios: {', '.join(suplier['services'])}\n"
            f"Calidad Del proveedor: {suplier['sup_quality']}\n"
            f"Detalles de los servicios:\n"
        )

        # Agregar detalles de los servicios
        for service, details in suplier['services_details'].items():
            content += f"\nServicio: {service.capitalize()}\n"
            for detail in details:
                content += (
                    f"  Nombre del servicio: {detail['name']}\n"
                    f"  Descripción: {detail['description']}\n"
                    f"  Precio: ${detail['price']}\n"
                    f"  Calidad: {detail['quality']} estrellas\n"
                )

        # Agregar el documento con su contenido y metadatos
        supliers.append(Document(page_content=content, metadata=suplier))
    return supliers

    


