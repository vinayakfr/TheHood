import reflex as rx
from TheHood.state.chip_state import ChipState
from assets.components.post import post_component

def wrap(main_content: rx.Component) -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.el.div(main_content, class_name="w-full max-w-4xl"),
            class_name="flex items-start justify-center w-full md:p-8",
        ),
        class_name="min-h-screen",
    )

def feed() -> rx.Component:
    """Page to display all created posts."""
    return wrap(
        rx.el.div(
            rx.cond(
                ChipState.posts.length() > 0,
                rx.el.div(
                    rx.foreach(ChipState.posts, post_component),
                    class_name="flex flex-col gap-6",
                ),
                rx.el.div(
                    "No posts yet. Create one to get started!",
                    class_name="text-gray-500 text-center py-8 rounded-lg",
                ),
            ),
            class_name="w-full",
        ),
    )