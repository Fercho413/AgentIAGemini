from src.services.logic.tools.Query_tools import query_db_tool
from src.services.logic.tools.Quote_tools import get_quote_tool
from services.logic.graph.LLM import get_agent
from langchain_core.messages import HumanMessage,BaseMessage
from src.model import State


def chat_node(state: State) -> State:
    """
    Función principal para ejecutar el nodo de chat.
    """
    agent = get_agent()
    input_message=HumanMessage(content=state['userInput'])
    agent_response=agent.invoke({"messages":state['messages']+[input_message]})
    state['messages'] = agent_response["messages"]
    return state
