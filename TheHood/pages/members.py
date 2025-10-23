import reflex as rx

from assets.components.sidebar import layout

class TableForEachState(rx.State):
    people: list[list] = [
        ["Danilo Sousa", "Slim Shady", "Shot Caller", 87],
        ["Zahra Ambessa", "Lil Wayne", "OG", 95],
        ["Jasper Eriks", "Jasper", "Soldier", 65],
    ]


def show_person(person: list):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(person[0]),
        rx.table.cell(person[1]),
        rx.table.cell(person[2]),
        rx.table.cell(person[3]),
    )


def members_page() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.desktop_only(
                layout(), 
                width="20%",
            ),
            rx.box(
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                            rx.table.column_header_cell("Full name"),
                            rx.table.column_header_cell("Call sign"),
                            rx.table.column_header_cell("Position"),
                            rx.table.column_header_cell("Street Cred"),
                        ),
                    ),
                    rx.table.body(rx.foreach(TableForEachState.people, show_person)),
                    width="100%",
                ),
                width="80%",
                padding="5px"
            ),
            justify="between",
            padding = "5px",
            height="100%",
        ),     
        height="100vh",
    ),