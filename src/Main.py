import uvicorn
from config.config_db import get_db

def main():
    uvicorn.run("src.controller.Chat_controller:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()
