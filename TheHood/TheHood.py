"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from assets.components.navbar import navbar
from assets.components.post import post
from assets.components.sidebar import sidebar
from TheHood.login import index as login
from TheHood.signup import index as signup

from rxconfig import config


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.box(
        # navbar(),
        rx.flex(
            rx.desktop_only(
                sidebar(), 
                width="20%",
            ),
            rx.container(
                rx.scroll_area(
                    rx.vstack(
                    post("/photo.JPG"),
                    post("Had a great day coding with Reflex!"),
                    post("/photo.JPG"),
                    spacing="4",
                    ),
                    type="hover",
                    style={"height": "95vh"},
                ),
                padding="0px",
                height="100%",
                width="60%",
            ),
            justify="start",
            padding = "5px",
            height="100%",
        ),
        height="100vh",
    )

app = rx.App()
app.add_page(index)
app.add_page(login, route="/login")
app.add_page(signup, route="/signup")