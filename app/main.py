from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from app.apis.auth import auth
from app.config import settings

BASE_DIR = Path(__file__).resolve().parent        # .../app
STATIC_DIR = BASE_DIR / "static"                  # .../app/static

app = FastAPI()
app.include_router(auth.router)

# Nếu secret_key là SecretStr (Pydantic), lấy giá trị thật ra:
secret = (
    settings.secret_key.get_secret_value()
    if hasattr(settings.secret_key, "get_secret_value")
    else str(settings.secret_key)
)
app.add_middleware(SessionMiddleware, secret_key=secret)

# Phục vụ file tĩnh: /static/*
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Jinja tìm template trong app/static (vì bạn đang để HTML trong đó)
templates = Jinja2Templates(directory=STATIC_DIR)

@app.get("/")
async def login(request: Request):
    return templates.TemplateResponse(
        "pages/login/login.html",
        {"request": request}
    )

@app.get("/welcome")
async def welcome(request: Request):
    user_name = request.session.get("user_name", "Guest")
    return templates.TemplateResponse(
        "pages/welcom/welcom.html",   # nếu bạn ĐỔI folder thành 'welcome', sửa lại path ở đây
        {"request": request, "user_name": user_name}
    )
