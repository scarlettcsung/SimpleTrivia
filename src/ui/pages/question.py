import random
from nicegui import ui
import state

@ui.page('/question')
def game_page():
    if not state.current_category_name:
        ui.navigate.to('/categories')
        return

    @ui.refreshable
    def question_display():
        # Center everything in this column
        with (ui.column().classes('w-full items-center text-center p-10')):
            available = state.get_available_questions(state.current_category_name)

            if not available:
                ui.label('Finished!').classes('text-5xl font-bold')
                ui.button('Back', on_click=lambda: ui.navigate.to('/categories')).classes('text-3xl p-6')
                return

            q_obj = random.choice(available)

            print(f"Question: {q_obj['question']} \n\n\nAnswer: {q_obj['answer']}")

            timer_seconds = 60
            timer_label = ui.label(f'Time: {timer_seconds}s').classes('text-4xl font-bold text-purple-700')

            # This will hold the timer object once it's started
            timer = None

            def start_timer():
                nonlocal timer
                start_btn.set_visibility(False)

                def count():
                    nonlocal timer_seconds
                    timer_seconds -= 1
                    timer_label.set_text(f'Time: {timer_seconds}s')
                    if timer_seconds <= 0:
                        timer.deactivate()
                        timer_label.set_text("Time's up!")

                timer = ui.timer(1.0, count)

            # The "Start" button triggers the sequence
            start_btn = ui.button('Start Timer', on_click=start_timer).classes('text-2xl p-4').props('color=purple')

            # Huge, centered text
            ui.label(q_obj["question"]).classes('text-6xl font-bold mb-10')

            answer_label = ui.label(q_obj["answer"]).classes('text-5xl text-green-600 mb-10')
            answer_label.set_visibility(False)

            def reveal():
                state.mark_question_as_used(q_obj["question"])
                answer_label.set_visibility(True)
                reveal_btn.set_visibility(False)

            # Large buttons
            reveal_btn = ui.button('Reveal Answer', on_click=reveal).classes('text-xl p-5')
            reveal_btn.props('color=purple')
            ui.button('Next', on_click=lambda: ui.navigate.to('/categories')) \
                .classes('text-xl p-5') \
                .props('color=purple')

    question_display()