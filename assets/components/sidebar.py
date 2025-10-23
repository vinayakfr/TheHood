import reflex as rx
import random
from reflex.components.radix.themes.base import (
    LiteralAccentColor,
)

from TheHood.state.chip_state import ChipState

def action_button(
    icon: str, label: str, on_click: rx.event.EventHandler, color: str
) -> rx.Component:
    """Small toolbar action buttons (add, clear, shuffle)."""
    return rx.el.button(
        rx.icon(icon, size=16, class_name="mr-2"),
        label,
        on_click=on_click,
        class_name=f"flex items-center px-4 py-2 text-sm font-medium text-white bg-{color}-600 rounded-lg shadow-sm hover:bg-{color}-700 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-{color}-500",
    )


def item_chip(item: str, color: LiteralAccentColor, is_selected: bool) -> rx.Component:
    """A chip for a slang term."""
    color_style = ChipState.color_map.get(color, {"bg": "#f3f4f6", "text": "#374151"})
    return rx.badge(
        item,
        rx.icon(
            rx.cond(is_selected, "minus-circle", "plus-circle"),
            size=18,
            class_name="ml-2 opacity-70 group-hover:opacity-100 transition-opacity",
        ),
        on_click=lambda: ChipState.toggle_selection(item),
        # style={"backgroundColor": color_style["bg"], "color": color_style["text"]},
        variant="soft",
        color_scheme=color,
        class_name="group flex items-center px-2 py-1 text-sm font-semibold rounded-full cursor-pointer hover:shadow-md transform hover:-translate-y-0.5 transition-all duration-200",
    )


def items_selector() -> rx.Component:
    """Main slang selector component."""
    return rx.el.div(
        rx.el.form(
            rx.el.div(
                    rx.el.h2(
                        "Street Codes ",
                        class_name="text-2xl font-bold",
                    ),
                    class_name="flex items-center gap-3",
                ),
            rx.el.input(
                name="post_content",
                placeholder="What's on your mind?",
                class_name="w-full p-3 border border-gray-300 rounded-lg my-3",
            ),
            rx.el.div(
                rx.el.h3(
                    "Selected Slang",
                    class_name="text-lg font-semibold mb-4",
                ),
                rx.cond(
                    ChipState.selected_items.length() > 0,
                    rx.el.div(
                        rx.foreach(
                            ChipState.selected_tags,
                            lambda tag: item_chip(tag[0], tag[1], is_selected=True),
                        ),
                        class_name="flex flex-wrap gap-3",
                    ),
                    rx.el.div(
                        "No slang selected. Click on the terms below to add them.",
                        class_name="text-gray-500 text-center py-3",
                    ),
                ),
                class_name="w-full mb-8",
            ),
            rx.el.hr(class_name="my-6 border-gray-200"),
            rx.el.div(
                rx.el.h3(
                    rx.el.span("Available Slang "),
                    class_name="text-lg font-semibold mb-4",
                ),
                rx.el.div(
                    rx.foreach(
                        ChipState.unselected_tags,
                        lambda tag: item_chip(tag[0], tag[1], is_selected=False),
                    ),
                    class_name="flex flex-wrap gap-3",
                ),
                class_name="w-full mb-8",
            ),
            rx.el.div(
                rx.button(
                    rx.icon("send", size=16, class_name="mr-2"),
                    "Send Post",
                    type="submit",
                    color_scheme="blue",
                    variant="soft",
                    on_click=ModalState.close,
                ),
                class_name="flex justify-end",
            ),
            on_submit=ChipState.submit_post,
            reset_on_submit=True,
            class_name="w-full",
        ),
        class_name="w-full max-w-4xl",
    )

class ModalState(rx.State):
    """State class to control modal visibility."""
    is_open: bool = False

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False


def tabs(text: str, color: str, on_click=None, href=None) -> rx.Component:
    """Sidebar tab button."""
    return rx.link(
        rx.button(
            text,
            width="100%",
            variant="soft",
            color_scheme=color,
            size="4",
            radius="medium",
            on_click=on_click,
        ),
        href=href,
        width="100%",
    )


def sidebar():
    """Sidebar with modal trigger button."""
    return rx.box(
        rx.flex(
            rx.text("The Hood", size="7", weight="bold", margin_bottom="20px"),
            rx.vstack(
                tabs("Home", "iris", href="/"),
                tabs("Members", "iris", href="/members"),
                tabs("Turfs", "iris", href="/turfs"),
                rx.separator(),
                # Proper callable event binding
                tabs("Post", "yellow", on_click=ModalState.open),
                rx.separator(),
                tabs("Rule Book", "jade", href="/rule_book"),
                spacing="5",
            ),
            rx.hstack(
                rx.hstack(
                    rx.icon("circle-user-round", size=25),
                    rx.icon("circle-help", size=25),
                ),
                rx.color_mode.button(size="4"),
                align="center",
                justify="between",
                width="100%",
            ),
            direction="column",
            justify="between",
            height="100%",
        ),
        padding="20px",
        height="100vh",
        width="100%",
        border_radius="10px",
        background_color=rx.color_mode_cond("#F3F4F6FF", "black"),
    )


def modal_content(title: str,) -> rx.Component:
    """Inner modal dialog box content."""
    return rx.box(
        items_selector(),
        background_color=rx.color_mode_cond("white", "black"),
        color=rx.color_mode_cond("black", "white"),
        padding="20px",
        border_radius="10px",
        box_shadow="0 10px 30px rgba(0,0,0,0.15)",
        border="1px solid",
        border_color=rx.color_mode_cond("#E5E7EB", "#374151"),
        width="60%",
        role="dialog",
        aria_modal="true",
    )


def modal() -> rx.Component:
    """Modal wrapper with backdrop and ESC key support."""
    return rx.cond(
        ModalState.is_open,
        rx.fragment(
            # Backdrop layer
            rx.box(
                on_click=ModalState.close,
                position="fixed",
                top="0",
                left="0",
                right="0",
                bottom="0",
                background_color="rgba(0,0,0,0.5)",
                z_index="1000",
            ),
            # Modal dialog container (centered)
            rx.center(
                modal_content(
                    title="What's up",
                ),
                position="fixed",
                inset="0",
                z_index="1001",
            ),
        ),
        rx.fragment(),
    )
    
def layout():
    """Root layout with sidebar and modal integration."""
    return rx.box(
        rx.hstack(
            sidebar(),
            modal(),  # Attach modal globally so state updates re-render properly
        ),
        position="relative",
        height="100vh",
    )