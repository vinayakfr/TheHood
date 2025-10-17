"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from assets.components.navbar import navbar
from assets.components.post import post

from rxconfig import config


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.box(
        navbar(),
                rx.container(
                    rx.vstack(
                    post("/photo.JPG"),
                    post("Had a great day coding with Reflex!"),
                    post("/photo.JPG"),
                    spacing="4",
                    ),
                    # width="50%",
                ),
    )

app = rx.App()
app.add_page(index)
