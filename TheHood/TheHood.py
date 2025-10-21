"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from assets.components.feed import feed
from assets.components.sidebar import layout
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
                layout(), 
                width="20%",
            ),
            rx.container(
                rx.scroll_area(
                    feed(),
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