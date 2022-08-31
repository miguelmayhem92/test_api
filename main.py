from fastapi import FastAPI, Body, Request, Form
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class NameValues(BaseModel):
    Check : str = None

@app.get("/home", response_class = HTMLResponse)
def home(request:Request):
    return templates.TemplateResponse("introduction.html", {"request": request})

@app.get("/displayDF")
async def handle_df(request: Request):
    
    test_list = [
        ["Joe", 34, "Accounts", 10000], ["Jack", 34, "Chemistry", 20000]
    ]
    data = pd.DataFrame(
        data=test_list,
        columns=["Name", "Age", "Dept.", "Salary"]
    )
    return templates.TemplateResponse(
        'df_representation.html',
        {'request': request, 'data': data.to_html()}
    )