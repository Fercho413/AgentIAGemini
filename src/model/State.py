from langgraph.graph import MessagesState

class State(MessagesState):
    """
    Clase que representa el estado de los mensajes en el grafo de conversación.
    Hereda de MessagesState para manejar el estado de los mensajes.
    """
    userInput: str