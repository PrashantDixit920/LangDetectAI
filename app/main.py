from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.routes import router

app = FastAPI(
    title="Language Identifier API",
    description="AI-powered language identification using a character-level LSTM.",
    version="1.0.0"
)

app.include_router(router)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='index.html'
    )


@app.get("/predict")
def predict_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='predict.html'
    )
    
    
@app.get("/about")
def about(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="about.html"
    )
    
@app.get("/documentation")
def documentation(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="documentation.html"
    )        
