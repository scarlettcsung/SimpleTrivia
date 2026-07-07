from nicegui import ui
import state

@ui.page('/categories')
def categories_page():
    # 1. Protection: If the user refreshes or visits directly without loading data
    if not state.current_trivia:
        ui.label('No trivia loaded. Please go back to home.')
        ui.button('Go Home', on_click=lambda: ui.navigate.to('/'))
        return

    with ui.column().classes('w-full items-center'):
        ui.label('Choose a Category').classes('text-h2')

    with ui.grid(columns=2).classes('w-full gap-4 p-8'):
        for category in state.current_trivia.keys():
            # Check if there are any questions left for this specific category
            available = state.get_available_questions(category)
            is_empty = len(available) == 0

            btn = ui.button(category, on_click=lambda c=category: select_category(c))

            # Style the button
            btn.classes('w-full h-32 text-2xl font-bold')

            if is_empty:
                # Make it gray and disable it
                btn.props('color=grey')
                btn.disable()
            else:
                btn.props('color=purple')

def select_category(category):
    """Sets the category in state and moves to the game."""
    state.set_category(category)
    ui.navigate.to('/question')