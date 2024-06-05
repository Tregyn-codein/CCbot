import flet as ft
from urllib.parse import parse_qs, urlparse

def main(page: ft.Page):
    page.title = "My Web App"

    # Получение параметров URL
    url_params = parse_qs(urlparse(page.url).query)
    user_id = url_params.get('user_id', [''])[0]
    first_name = url_params.get('first_name', [''])[0]
    last_name = url_params.get('last_name', [''])[0]
    username = url_params.get('username', [''])[0]

    # Отображение данных пользователя
    page.add(ft.Text(f"User ID: {user_id}"))
    page.add(ft.Text(f"First Name: {first_name}"))
    page.add(ft.Text(f"Last Name: {last_name}"))
    page.add(ft.Text(f"Username: {username}"))

ft.app(target=main, view=ft.WEB_BROWSER, port=8000)