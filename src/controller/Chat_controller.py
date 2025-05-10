from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.model.ChatRequest import ChatRequest
from src.services.Chat_service import send_message


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)

@app.post("/chat")
async def chat(request: ChatRequest):
    """
    Endpoint para manejar las solicitudes de chat.
    Args:
        request (ChatRequest): Objeto que contiene la entrada del usuario.
    Returns:
        dict: Respuesta generada por el modelo.
    """
    response = send_message(request.user_input)
    return {"response": response}    
