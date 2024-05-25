from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import httpx

#create an app instance
app = FastAPI()

#attatch our app to the index.html file
app.mount("/static", StaticFiles(directory="static"), name="static")

#load in our html file
@app.get("/", response_class=HTMLResponse)
async def get_html():
    with open("static/index.html") as f:
        return HTMLResponse(content=f.read())
