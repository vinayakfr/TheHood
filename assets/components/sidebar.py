import reflex as rx

def tabs(text: str, color: str) -> rx.Component:
    return rx.button(
        text,
        width="100%",
        variant="soft",
        color_scheme=color,
        size="4",
        radius="medium"
    )

def sidebar():
    return rx.box(
        rx.flex(
            rx.vstack(
            tabs("Home", "iris"),
            tabs("Members", "iris"),
            tabs("Turfs", "iris"),
            tabs("Talk (Coming Soon)", "red"),
            spacing="7"
            ),
            rx.vstack(
                rx.hstack(
                    rx.icon("circle-user-round", size=30),
                    rx.icon("circle-help", size=30),
                ),
            ),
            direction="column",
            justify="between",
            height="100%"
        ),
        padding="20px",
        style={"height": "90vh"},
        width="100%",
        border_radius="10px",
        background_color=rx.color_mode_cond("#F3F4F6FF", "black"),
    )