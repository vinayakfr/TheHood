import reflex as rx
import random
from reflex.components.radix.themes.base import (
    LiteralAccentColor,
)

chip_props = {
    "radius": "full",
    "variant": "surface",
    "size": "3",
    "cursor": "pointer",
    "style": {"_hover": {"opacity": 0.75}},
}

Tags = [
   "OG",
    "Ride or Die",
    "No Cap",
    "100",
    "Fam",
    "Trap Life",
    "Lowkey",
    "Savage",
    "Flex",
    "Real One",
    "Street Code",
    "Grind Mode",
    "Thug Passion",
    "Hood Rich",
    "Down Bad",
    "Big Steppa",
    "Wya?",
    "Pull Up",
    "10 Toes Down",
    "Catch Fade",
    "Slide Thru",
    "On God",
    "Keep It 100",
    "Day Ones",
    "Shoot Your Shot",
]

class BasicChipsState(rx.State):
    selected_items: list[str] = Tags[:3]

    @rx.event
    def add_selected(self, item: str):
        self.selected_items.append(item)

    @rx.event
    def remove_selected(self, item: str):
        self.selected_items.remove(item)

    @rx.event
    def add_all_selected(self):
        self.selected_items = list(Tags)

    @rx.event
    def clear_selected(self):
        self.selected_items.clear()

    @rx.event
    def random_selected(self):
        self.selected_items = random.sample(
            Tags, k=random.randint(1, len(Tags))
        )


def action_button(
    icon: str,
    label: str,
    on_click: callable,
    color_scheme: LiteralAccentColor,
) -> rx.Component:
    return rx.button(
        rx.icon(icon, size=16),
        label,
        variant="soft",
        size="2",
        on_click=on_click,
        color_scheme=color_scheme,
        cursor="pointer",
    )


def selected_item_chip(item: str) -> rx.Component:
    return rx.badge(
        item,
        rx.icon("circle-x", size=18),
        color_scheme="green",
        **chip_props,
        on_click=BasicChipsState.remove_selected(item),
    )


def unselected_item_chip(item: str) -> rx.Component:
    return rx.cond(
        BasicChipsState.selected_items.contains(item),
        rx.fragment(),
        rx.badge(
            item,
            rx.icon("circle-plus", size=18),
            color_scheme="gray",
            **chip_props,
            on_click=BasicChipsState.add_selected(item),
        ),
    )


def items_selector() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.hstack(
                rx.heading(
                    "Tags"
                    + f" ({BasicChipsState.selected_items.length()})",
                    size="4",
                ),
                spacing="1",
                align="center",
                width="100%",
                justify_content=["end", "start"],
            ),
            rx.hstack(
                action_button(
                    "plus",
                    "Add All",
                    BasicChipsState.add_all_selected,
                    "green",
                ),
                action_button(
                    "trash",
                    "Clear All",
                    BasicChipsState.clear_selected,
                    "tomato",
                ),
                spacing="2",
                justify="end",
                width="100%",
            ),
            justify="between",
            flex_direction=["column", "row"],
            align="center",
            spacing="2",
            margin_bottom="10px",
            width="100%",
        ),
        # Selected Items
        rx.flex(
            rx.foreach(
                BasicChipsState.selected_items,
                selected_item_chip,
            ),
            wrap="wrap",
            spacing="2",
            justify_content="start",
        ),
        rx.divider(),
        # Unselected Items
        rx.flex(
            rx.foreach(Tags, unselected_item_chip),
            wrap="wrap",
            spacing="2",
            justify_content="start",
        ),
        justify_content="start",
        align_items="start",
        width="100%",
    )

class ModalState(rx.State):
    """State class to control modal visibility."""
    is_open: bool = False

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False


def tabs(text: str, color: str, on_click=None) -> rx.Component:
    """Sidebar tab button."""
    return rx.button(
        text,
        width="100%",
        variant="soft",
        color_scheme=color,
        size="4",
        radius="medium",
        # The event must be passed as a callable, not a string
        on_click=on_click,
    )


def sidebar():
    """Sidebar with modal trigger button."""
    return rx.box(
        rx.flex(
            rx.text("The Hood", size="7", weight="bold", margin_bottom="20px"),
            rx.vstack(
                tabs("Home", "iris"),
                tabs("Members", "iris"),
                tabs("Turfs", "iris"),
                tabs("Talk (Coming Soon)", "red"),
                rx.separator(),
                # Proper callable event binding
                tabs("Post", "yellow", on_click=ModalState.open),
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
        rx.heading(title, size="7"),
        rx.input(
            placeholder="Search here...",
            margin_top="8px",
            margin_bottom="16px",
            size="3",
            max_length=256,
        ),
        items_selector(),
        rx.hstack(
            rx.button("Send", on_click=ModalState.close),
            spacing="3",
            justify="end",
            margin_top="16px",
        ),
        background_color=rx.color_mode_cond("white", "black"),
        color=rx.color_mode_cond("black", "white"),
        padding="20px",
        border_radius="10px",
        box_shadow="0 10px 30px rgba(0,0,0,0.15)",
        border="1px solid",
        border_color=rx.color_mode_cond("#E5E7EB", "#374151"),
        width="40%",
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