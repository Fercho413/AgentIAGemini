from langchain_google_genai import ChatGoogleGenerativeAI
from src.services.logic.tools.Query_tools import query_db_tool
from src.services.logic.tools.Quote_tools import get_quote_tool
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage


llm=None #Intancia global del llm
agent=None #Intancia global del agente
tools=[query_db_tool,get_quote_tool] #Lista de herramientas

#Mnesaje del sistema para el modelo
system_message = SystemMessage(
    content=("Eres un asistente de IA que ayuda a los usuarios a encontrar información de proveedores de servicios, toda la informacion de ellos esta en una base de datos que puedes consultar con una herramienta, usa esta herramienta siempre para consultar la informacion de los proveedores y poder cumplir con las tareas de consultar y recomendar, no inventes informacion. Para ayudar al usuario con el calculo de cotizaciones, puedes usar la herramienta de cotizaciones. Las tareas que puedes cumplir son: 1.Permitir consultar información específica de cada empresa proveedora: descripción de servicios, precio, ubicacion u otra informacion relevante.(Cuando el usuario te pida informacion , usa directamente la herramienta) 2.Permitir la selección de múltiples empresas/proveedores para componer paquetes de servicios para eventos corporativos. 3. Permitir al usuario hacer recomendaciones de proveedores de servicios, basadas en la información consultada y segun el criterio de precio,calidad y ubicacion geografica. 4. Permitir al usuario calcular cotizaciones de los servicios que ofrecen los proveedores, usando la herramienta de cotizaciones. Si el usuario consulta sobre un tema diferente para el cual fuiste diseñado, debes decirle amablemente que no estas hecho para ello. La respuesta al usuario debe ser clara y concisa, con un lenguaje amigable y sin tecnicismos, tampoco menciones que usaras la herramientas, simplemente usala, y si es necesario, puedes hacer preguntas para aclarar la solicitud del usuario. No debes dar respuestas largas ni complejas, solo lo necesario para que el usuario entienda la respuesta"))

def get_llm_instance(nameModel: str = "gemini-2.5-flash-preview-04-17",t:int = 0) -> ChatGoogleGenerativeAI:
    """
    Obtiene una instancia del modelo de lenguaje de Google Generative AI.

    Arg:
        nameModel (str): Nombre del modelo de lenguaje de Google Generative AI. Por defecto, se utiliza "gemini-2.5-flash-preview-04-17"
        t (int): Temperatura para la generación de texto. Por defecto, se utiliza 0.
    Returns:
        ChatGoogleGenerativeAI: Instancia del modelo de lenguaje de Google Generative AI.        
    """
    global llm,system_message
    if llm is not None:
        return llm
    llm = ChatGoogleGenerativeAI(model=nameModel,temperature=t)
    return llm

def get_agent(nameModel: str = "gemini-2.5-flash-preview-04-17",t:int = 0) -> ChatGoogleGenerativeAI:
    """
    Obtiene una instancia del agente con herramientas.

    Arg:
        nameModel (str): Nombre del modelo de lenguaje de Google Generative AI. Por defecto, se utiliza "gemini-2.5-flash-preview-04-17"
        t (int): Temperatura para la generación de texto. Por defecto, se utiliza 0.
    Returns:
        ChatGoogleGenerativeAI: Instancia del agente con herramientas.
    """
    global llm, agent, tools, system_message

    if agent is not None:
        return agent
    
    llm = get_llm_instance(nameModel, t)
    agent = create_react_agent(llm, tools=tools, prompt=system_message)
    return agent
    
def set_llm_instance_None():
    """
    Establece la instancia del modelo de lenguaje a None.
    """
    global llm
    llm = None


