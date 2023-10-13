from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Get All

# Get Single ID


# Post 


# Put



# Delete