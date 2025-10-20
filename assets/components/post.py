import reflex as rx

def post(content):
        # Text post (Responsive for Desktop and Mobile)
        return rx.fragment(
            # Desktop view
            rx.desktop_only(
                rx.hstack(
                    rx.avatar(src="/logo.jpg", fallback="RX", size="3"),
                    rx.card(
                        rx.vstack(
                            rx.text(
                                content,
                                font_size="xl",
                                color=rx.color_mode_cond("black", "white"),
                            ),
                            rx.hstack(
                                rx.icon(tag="thumbs-up", color="white", size=20),
                                rx.icon(tag="thumbs-down", color="white", size=20),
                                spacing="3",
                                justify="start",
                                width="100%",
                            ),
                            spacing="2",
                        ),
                        padding="10px",
                        width="100%",
                    ),
                    justify="start",
                    align="center",
                    gap="7px",
                    width="100%",
                ),
                width="100%",
            ),
            # Mobile + Tablet view
            rx.mobile_and_tablet(
                rx.vstack(
                    rx.avatar(src="/logo.jpg", fallback="RX", size="3"),
                    rx.card(
                        rx.vstack(
                            rx.text(
                                content,
                                font_size="xl",
                                color=rx.color_mode_cond("black", "white"),
                            ),
                            rx.hstack(
                                rx.icon(tag="thumbs-up", color="white"),
                                rx.icon(tag="thumbs-down", color="white"),
                                spacing="3",
                                justify="end",
                                width="100%",
                            ),
                            spacing="2",
                        ),
                        padding="10px",
                        width="100%",
                    ),
                    spacing="2",
                    align="start",
                    width="100%",
                )
            ),
        )