# 🚀 FastAPI Google Sign-In Example

This project demonstrates how to integrate **Google Sign-In** authentication with **FastAPI**, following the guide from [this Medium article](https://parlak-deniss.medium.com/fastapi-authentication-with-google-oauth-2-0-9bb93b784eee).

## 📝 Features

-   Google OAuth 2.0 authentication
-   FastAPI backend
-   Environment variable configuration

## 📦 Requirements

-   Python 3.8+
-   [pip](https://pip.pypa.io/en/stable/)

## ⚙️ Setup

1. **Clone the repository:**

    ```bash
    git clone <your-repo-url>
    cd GOOGLE_SIGNIN
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure environment variables:**

    - Copy `.env.template` to `.env`:

        ```bash
        cp .env.template .env
        ```

    - Fill in your Google OAuth credentials in the `.env` file:

        ```
        GOOGLE_CLIENT_ID=your-google-client-id
        GOOGLE_CLIENT_SECRET=your-google-client-secret
        SECRET_KEY=your-secret-key
        ```

    - You can obtain your credentials from the [Google Cloud Console](https://console.cloud.google.com/apis/credentials).

## ▶️ Running the Project

```bash
uvicorn main:app --reload

```

or

```bash
fastapi dev app/main.py

```

The API will be available at [http://localhost:8000](http://localhost:8000).

## 🔗 Useful Links

-   [FastAPI Documentation](https://fastapi.tiangolo.com/)
-   [Google OAuth 2.0 Guide](https://developers.google.com/identity/protocols/oauth2)

## 🎨 Screenshots

![Google Sign-In Example](https://developers.google.com/identity/images/btn_google_signin_dark_normal_web.png)

---

Made with ❤️ using FastAPI & Google OAuth 2.0
