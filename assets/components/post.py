import reflex as rx

def post(content):
    # Detect if content is an image based on extension
    image_extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp")

    if isinstance(content, str) and content.lower().endswith(image_extensions):
        # Image post
        return rx.fragment(
            # Desktop view
            rx.desktop_only(
                rx.hstack(
                    rx.avatar(src="/logo.jpg", fallback="RX", size="3"),
                    rx.vstack(
                        rx.card(
                            rx.image(src=content, alt="User Post", border_radius="10px"),
                            rx.hstack(
                                rx.text(
                                    "Shared a photo",
                                    font_size="xl",
                                    color=rx.color_mode_cond("black", "white"),
                                ),
                                rx.spacer(),
                                rx.icon(tag="thumbs-up", color="white"),
                                rx.icon(tag="thumbs-down", color="white"),
                                spacing="3",
                                justify="between",
                                width="100%",
                                margin_top="15px",
                            ),
                            padding="10px",
                            width="100%",
                        ),
                        spacing="2",
                        align="start",
                    ),
                    justify="start",
                    align="start",
                    gap="7px",
                    width="100%",
                )
            ),

            # Mobile + Tablet view
            rx.mobile_and_tablet(
                rx.vstack(
                    rx.avatar(src="/logo.jpg", fallback="RX", size="3"),
                    rx.vstack(
                        rx.card(
                            rx.image(src=content, alt="User Post", border_radius="10px"),
                            rx.hstack(
                                rx.text(
                                    "Shared a photo",
                                    font_size="xl",
                                    color=rx.color_mode_cond("black", "white"),
                                ),
                                rx.spacer(),
                                rx.icon(tag="thumbs-up", color="white"),
                                rx.icon(tag="thumbs-down", color="white"),
                                spacing="3",
                                justify="between",
                                width="100%",
                                margin_top="15px",
                            ),
                            padding="10px",
                            width="100%",
                        ),
                        spacing="2",
                        align="start",
                    ),
                    align="start",
                    gap="7px",
                    width="100%",
                )
            ),
        )

    else:
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
                    justify="start",
                    align="center",
                    gap="7px",
                    width="100%",
                )
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