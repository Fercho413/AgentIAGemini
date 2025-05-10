from langgraph.graph import START, StateGraph,END
from langgraph.prebuilt import tools_condition, ToolNode
from src.services.logic.graph.Chat_node import chat_node
from src.services.logic.graph.LLM import tools
from src.model.State import State


def get_chat_graph():

    builder = StateGraph(State)

    builder.add_node("chat_node", chat_node)
    builder.add_node("tools", ToolNode(tools))

    # Define edges: these determine how the control flow moves
    builder.add_edge(START, "chat_node")
    builder.add_conditional_edges(
        "chat_node",
        tools_condition
    )
    builder.add_edge("tools", "chat_node")

    graph = builder.compile()

    return graph