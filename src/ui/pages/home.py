import json
from pathlib import Path
from nicegui import ui
import state

def get_json_files():
    # Start at this file's directory (src/ui/pages)
    # .parent.parent.parent moves up to the project root
    root_dir = Path(__file__).resolve().parent.parent.parent.parent
    jsons_dir = root_dir / 'jsons'

    if not jsons_dir.exists():
        # This will now tell you exactly where it's looking
        print(f"DEBUG: Looking for folder at: {jsons_dir}")
        return []

    return [f.name for f in jsons_dir.glob('*.json')]

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent

def load_selected_file(filename):
    global current_trivia
    # Explicitly join the root with the 'jsons' folder
    filepath = PROJECT_ROOT / 'jsons' / filename

    print(f"DEBUG: Looking for: {filepath}")

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)

        state.set_trivia(data)

        print(f"State updated! Now holding: {len(state.current_trivia)} categories.")

    except Exception as e:
        ui.notify(f'Error loading file: {e}', type='negative')


@ui.page('/')
def home_page():
    ui.label('Select a Trivia Set').classes('text-h4')

    files = get_json_files()

    def on_change(event):
        load_selected_file(event.value)
        # Now that you are setting up the other page, this will work:
        ui.navigate.to('/categories')

    ui.select(options=files, label='Choose a category file', on_change=on_change)

ui.run()