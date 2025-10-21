import reflex as rx
import random
from typing import Literal, TypedDict


class Post(TypedDict):
    content: str
    tags: list[tuple[str, str]]


LiteralAccentColor = Literal[
    "gray",
    "gold",
    "bronze",
    "brown",
    "yellow",
    "amber",
    "orange",
    "tomato",
    "red",
    "ruby",
    "crimson",
    "pink",
    "plum",
    "purple",
    "violet",
    "iris",
    "indigo",
    "blue",
    "cyan",
    "teal",
    "jade",
    "green",
    "grass",
    "lime",
    "mint",
    "sky",
]


class ChipState(rx.State):
    """Reactive state for selected slang terms."""

    show_post_modal: bool = False
    post_content: str = ""
    posts: list[Post] = []
    color_map: dict[str, dict[str, str]] = {
        "amber": {"bg": "#fef3c7", "text": "#92400e"},
        "crimson": {"bg": "#fee2e2", "text": "#991b1b"},
        "blue": {"bg": "#dbeafe", "text": "#1e40af"},
        "green": {"bg": "#d1fae5", "text": "#065f46"},
        "purple": {"bg": "#e0e7ff", "text": "#4338ca"},
        "orange": {"bg": "#ffedd5", "text": "#9a3412"},
        "gray": {"bg": "#f3f4f6", "text": "#374151"},
        "red": {"bg": "#fee2e2", "text": "#991b1b"},
        "gold": {"bg": "#fef9c3", "text": "#854d0e"},
        "cyan": {"bg": "#cffafe", "text": "#155e75"},
        "teal": {"bg": "#ccfbf1", "text": "#134e4a"},
        "indigo": {"bg": "#e0e7ff", "text": "#3730a3"},
        "sky": {"bg": "#e0f2fe", "text": "#0c4a6e"},
        "lime": {"bg": "#ecfccb", "text": "#4d7c0f"},
        "brown": {"bg": "#efebe9", "text": "#5d4037"},
        "ruby": {"bg": "#ffe4e6", "text": "#a21a33"},
        "violet": {"bg": "#ede9fe", "text": "#5b21b6"},
        "yellow": {"bg": "#fef9c3", "text": "#854d0e"},
        "pink": {"bg": "#fce7f3", "text": "#9d2463"},
        "mint": {"bg": "#d1fae5", "text": "#065f46"},
    }
    tags: list[tuple[str, str]] = [
        ("OG", "amber"),
        ("Ride or Die", "crimson"),
        ("No Cap", "blue"),
        ("100", "green"),
        ("Fam", "purple"),
        ("Trap Life", "orange"),
        ("Lowkey", "gray"),
        ("Savage", "red"),
        ("Flex", "gold"),
        ("Real One", "cyan"),
        ("Street Code", "gray"),
        ("Grind Mode", "teal"),
        ("Thug Passion", "red"),
        ("Hood Rich", "green"),
        ("Down Bad", "purple"),
        ("Big Steppa", "indigo"),
        ("Wya?", "sky"),
        ("Pull Up", "lime"),
        ("10 Toes Down", "brown"),
        ("Catch Fade", "ruby"),
        ("Slide Thru", "violet"),
        ("On God", "yellow"),
        ("Keep It 100", "pink"),
        ("Day Ones", "amber"),
        ("Shoot Your Shot", "mint"),
    ]
    selected_items: list[str] = ["OG", "Ride or Die", "No Cap"]

    @rx.var
    def unselected_tags(self) -> list[tuple[str, str]]:
        """Returns tags that are not currently selected."""
        return [tag for tag in self.tags if tag[0] not in self.selected_items]

    @rx.var
    def selected_tags(self) -> list[tuple[str, str]]:
        """Returns tags that are currently selected."""
        return [tag for tag in self.tags if tag[0] in self.selected_items]

    @rx.event
    def toggle_selection(self, item: str):
        """Adds or removes an item from the selected list."""
        if item in self.selected_items:
            self.selected_items.remove(item)
        else:
            self.selected_items.append(item)

    @rx.event
    def toggle_post_modal(self):
        """Toggles the visibility of the post creation modal."""
        self.show_post_modal = not self.show_post_modal
        if not self.show_post_modal:
            self.post_content = ""

    @rx.event
    def submit_post(self):
        """Submits the new post and navigates to the posts page."""
        if self.post_content.strip():
            new_post = {"content": self.post_content, "tags": self.selected_tags}
            self.posts.insert(0, new_post)
        yield ChipState.toggle_post_modal
        return rx.redirect("/posts")

    @rx.event
    def add_all_selected(self):
        """Selects all available tags."""
        self.selected_items = [t[0] for t in self.tags]

    @rx.event
    def clear_selected(self):
        """Clears all selected tags."""
        self.selected_items.clear()

    @rx.event
    def random_selected(self):
        """Selects a random number of random tags."""
        all_tags = [t[0] for t in self.tags]
        sample_size = random.randint(1, len(all_tags))
        self.selected_items = random.sample(all_tags, k=sample_size)