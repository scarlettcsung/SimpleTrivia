import state
from nicegui import ui

from src.ui.pages import home
from src.ui.pages import categories
from src.ui.pages import question

ui.run(native=True, port=8080, title='SimpleTrivia')
