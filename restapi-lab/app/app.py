from fastapi import FastAPI
app = FastAPI()
@app.get("/test")
def route():
    return {"message": "salamHossein"}