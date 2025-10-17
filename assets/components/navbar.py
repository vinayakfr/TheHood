import reflex as rx

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, color=rx.color_mode_cond("black", "white"), size="5"),
        href=url,
        underline="none",
    )

def navbar() -> rx.Component:
    return rx.box(
        # Desktop Navbar
        rx.desktop_only(
            rx.flex(
                rx.heading(
                    "Gang",
                    size="7",
                    color=rx.color_mode_cond("black", "white"),
                    transition="all 0.3s ease-in-out",
                ),
                rx.color_mode.button(size="3"),
                justify="between",
                align_items="center",
                padding="13px 20px",
                box_shadow="lg",
                width="100%",
                border_bottom="1px solid",
                position="sticky",
                z_index="100",
            )
        ),

        # Mobile + Tablet Navbar
        rx.mobile_and_tablet(
            rx.flex(
                rx.heading(
                    "Gang",
                    size="7",
                    color=rx.color_mode_cond("black", "white"),
                    transition="all 0.3s ease-in-out",
                ),
                rx.hstack(
                    rx.color_mode.button(size="4"),
                    rx.dropdown_menu.root(
                        rx.dropdown_menu.trigger(
                            rx.icon("menu", size=27),
                            as_child=True,
                        ),
                        rx.dropdown_menu.content(
                            rx.dropdown_menu.item(navbar_link("Home", "/")),
                            rx.dropdown_menu.item(navbar_link("Members", "/members")),
                            rx.dropdown_menu.item(navbar_link("Invite", "/invite")),
                            rx.dropdown_menu.item(navbar_link("Help", "/contact")),
                        ),
                    ),
                    align="center",
                ),
                justify="between",
                align="center",
                padding="15px 20px",
                background_color=rx.color_mode_cond("white", "black"),
                box_shadow="lg",
                width="100%",
                position="sticky",
                top="0",
                z_index="100",
                border_bottom="1px solid",
            ),
        ),
    )
