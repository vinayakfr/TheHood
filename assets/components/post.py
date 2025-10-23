import reflex as rx
from typing import TypedDict
from TheHood.state.chip_state import ChipState


class Post(TypedDict):
    content: str
    tags: list[tuple[str, str]]


def post_tag_chip(tag: list[str]) -> rx.Component:
    color_style = ChipState.color_map.get(tag[1], {"bg": "#f3f4f6", "text": "#374151"})
    return rx.badge(
        tag[0],
        variant="soft",
        color_scheme=tag[1],
        class_name="px-3 py-1 text-xs font-semibold rounded-full",
    )


def post_component(post: Post) -> rx.Component:
    """Component to display a single post with responsive layout."""
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.avatar(src="/logo.jpg", fallback="RX", size="3"),
                rx.box(
                    rx.el.div(
                        rx.flex(
                            rx.el.p(
                                post["content"],
                                class_name="text-base font-medium",
                            ),
                            rx.hstack(
                                rx.icon(
                                    "thumbs-up",
                                    class_name="w-5 h-5 stroke-white hover:stroke-blue-600 cursor-pointer transition-colors",
                                ),
                                rx.icon(
                                    "thumbs-down",
                                    class_name="w-5 h-5 stroke-white hover:stroke-red-600 cursor-pointer transition-colors",
                                ),
                            class_name="flex items-center gap-4 mt-4",
                            ),
                            width="100%",
                            justify="between",
                        ),
                        rx.el.div(
                            rx.foreach(post["tags"], post_tag_chip),
                            class_name="flex flex-wrap gap-2 mt-2",
                        ),
                       
                        class_name="flex flex-col",
                    ),
                    width="100%",
                    class_name="py-2 px-3 rounded-2xl",
                    background_color=rx.color_mode_cond("white", "black"),
                ),
                class_name="flex items-start justify-start gap-3 w-full",
            ),
            class_name="hidden md:flex w-full",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        post["content"],
                        class_name="text-base font-medium text-gray-800",
                    ),
                    rx.el.div(
                        rx.foreach(post["tags"], post_tag_chip),
                        class_name="flex flex-wrap gap-2 mt-3",
                    ),
                    rx.el.div(
                        rx.icon("thumbs-up", class_name="w-5 h-5 stroke-gray-500"),
                        rx.icon("thumbs-down", class_name="w-5 h-5 stroke-gray-500"),
                        class_name="flex items-center gap-4 mt-3 self-end",
                    ),
                    class_name="p-2 w-full flex flex-col",
                ),
                class_name="flex flex-col items-start gap-3 w-full",
            ),
            class_name="flex md:hidden w-full",
        ),
        class_name="w-full",
    )