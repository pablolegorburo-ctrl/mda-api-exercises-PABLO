from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "¡Hola, estudiantes!"}



@app.get("/about")
def about():
    return "¡Bienvenidos a mi primera aplicación FastAPI!"

@app.get("/user/{username}")
def show_user(username: str):
    return f"¡Hola, {username}!"

@app.get("/login")
def login_form():
    return "Por favor, inicia sesión"

@app.post("/login")
def login():
    return "Procesando login..."
@app.get("/user/{username}")
def show_user(username: str):
    return f"Perfil de usuario: {username}"

# @app.get("/post/{post_id}")
# def show_post(post_id: int):
#     return f"Mostrando publicación {post_id}"