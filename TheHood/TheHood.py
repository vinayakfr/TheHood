"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from TheHood.pages.members import members_page
from TheHood.pages.rule_book import rule_book_page
from assets.components.feed import feed
from assets.components.sidebar import layout
from TheHood.auth.login import index as login
from TheHood.auth.signup import index as signup

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
app.add_page(index, route="/")
app.add_page(login, route="/login")
app.add_page(signup, route="/signup")
app.add_page(rule_book_page, route="/rule_book")
app.add_page(members_page, route="/members")