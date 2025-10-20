import reflex as rx
import random
from reflex.components.radix.themes.base import LiteralAccentColor

# Common visual style for chips
chip_props = {
    "radius": "full",
    "variant": "surface",
    "size": "3",
    "cursor": "pointer",
    "style": {"_hover": {"opacity": 0.75}},
}

# Street slang / gang lingo list
tags = [
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
    """Reactive state for selected slang terms."""
    selected_items: list[str] = tags[:3]

    @rx.event
    def add_selected(self, item: str):
        if item not in self.selected_items:
            self.selected_items.append(item)

    @rx.event
    def remove_selected(self, item: str):
        if item in self.selected_items:
            self.selected_items.remove(item)

    @rx.event
    def add_all_selected(self):
        self.selected_items = list(tags)

    @rx.event
    def clear_selected(self):
        self.selected_items.clear()

    @rx.event
    def random_selected(self):
        self.selected_items = random.sample(tags, k=random.randint(1, len(tags)))


def action_button(
    icon: str,
    label: str,
    on_click: callable,
    color_scheme: LiteralAccentColor,
) -> rx.Component:
    """Small toolbar action buttons (add, clear, shuffle)."""
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
    """Badge for selected slang terms."""
    return rx.badge(
        item,
        rx.icon("circle-x", size=18),
        color_scheme="amber",
        **chip_props,
        on_click=BasicChipsState.remove_selected(item),
    )


def unselected_item_chip(item: str) -> rx.Component:
    """Badge for available slang terms not yet selected."""
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
    """Main slang selector component."""
    return rx.vstack(
        # Header & Controls
        rx.flex(
            rx.hstack(
                rx.icon("flame", size=20),
                rx.heading(
                    "Street Codes"
                    + f" ({BasicChipsState.selected_items.length()})",
                    size="4",
                ),
                spacing="1",
                align="center",
                width="100%",
                justify_content=["end", "start"],
            ),
            rx.hstack(
                action_button("plus", "Add All", BasicChipsState.add_all_selected, "amber"),
                action_button("trash", "Clear All", BasicChipsState.clear_selected, "tomato"),
                action_button("shuffle", "", BasicChipsState.random_selected, "gray"),
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

        # Selected Terms
        rx.flex(
            rx.foreach(BasicChipsState.selected_items, selected_item_chip),
            wrap="wrap",
            spacing="2",
            justify_content="start",
        ),
        rx.divider(),

        # Unselected Terms
        rx.flex(
            rx.foreach(tags, unselected_item_chip),
            wrap="wrap",
            spacing="2",
            justify_content="start",
        ),
        justify_content="start",
        align_items="start",
        width="100%",
    )
