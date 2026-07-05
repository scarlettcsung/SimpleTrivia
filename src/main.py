import state
from nicegui import ui

# 1. Import your pages so the @ui.page decorators are executed
# PyCharm will find these because 'src' is your Source Root
from src.ui.pages import home
from src.ui.pages import categories
# from src.ui.pages import game  # Uncomment once you create this

# 2. Run the app
# The 'native' mode opens a small window, or remove it for browser-only
ui.run(native=True)