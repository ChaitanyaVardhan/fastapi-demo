rom fastapi import FastAPI

app = FastAPI()
                 
fake_db = []                   

@app.get("/")
def root():
    return {"message": "Hello World"i}

