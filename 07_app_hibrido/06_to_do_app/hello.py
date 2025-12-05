import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.add(ft.Text(value="Hello, World!"))
    

ft.app(main)
             
             