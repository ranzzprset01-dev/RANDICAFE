import os

import mysql.connector
import streamlit as st
from streamlit.errors import StreamlitSecretNotFoundError


def get_secret(name, default=None):
    try:
        return st.secrets.get(name, default)
    except StreamlitSecretNotFoundError:
        return default


def connect_db():
    settings = get_secret("mysql", {})

    return mysql.connector.connect(
        host=settings.get("host", os.getenv("DB_HOST", "localhost")),
        port=int(settings.get("port", os.getenv("DB_PORT", "3306"))),
        user=settings.get("user", os.getenv("DB_USER", "root")),
        password=settings.get("password", os.getenv("DB_PASSWORD", "")),
        database=settings.get("database", os.getenv("DB_NAME", "db_kafe")),
    )
