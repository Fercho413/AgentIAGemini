from src.services.logic.graph.Chat_graph import get_chat_graph
from src.model.State import State

graph = get_chat_graph()
graph_state = State()


def send_message(user_input:str) -> str:
    """Envía un mensaje al modelo y devuelve la respuesta.

    Args:
        user_input (str): El mensaje del usuario.
        history (list): La historia de mensajes previos.
    """
    global graph_state, graph

    graph_state["userInput"] = user_input
    graph_state = graph.invoke(graph_state)
    response = graph_state["messages"][-1].content
    return response