from pydantic import BaseModel

class ChatRequest(BaseModel):
    """Modelo para representar una solicitud de chat.
    Atributos:
        user_input (str): Entrada del usuario para el chat.
    """
    user_input: str