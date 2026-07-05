from nicegui import ui
import state

@ui.page('/categories')
def categories_page():
    # 1. Protection: If the user refreshes or visits directly without loading data
    if not state.current_trivia:
        ui.label('No trivia loaded. Please go back to home.')
        ui.button('Go Home', on_click=lambda: ui.navigate.to('/'))
        return

    ui.label('Choose a Category').classes('text-h4')

    # 2. Dynamically create buttons for each category
    # We use a grid or row to keep it organized
    with ui.row().classes('w-full flex-wrap'):
        for category in state.current_trivia.keys():
            # Use 'c=category' to capture the variable in the loop
            ui.button(category, on_click=lambda c=category: select_category(c))

def select_category(category):
    """Sets the category in state and moves to the game."""
    state.set_category(category)
    # Assuming you have a '/game' route defined in another file
    ui.navigate.to('/game')