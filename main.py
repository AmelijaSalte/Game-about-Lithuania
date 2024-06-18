import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from questions import get_questions
import random

kivy.require('1.11.1')


class ImageButton(ButtonBehavior, Image):
    pass


class IntroScreen(Screen):
    def __init__(self, **kwargs):
        super(IntroScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        with layout.canvas.before:
            Color(1, 1, 1, 1)  # White background
            self.rect = Rectangle(size=self.size, pos=self.pos)
            layout.bind(size=self._update_rect, pos=self._update_rect)
        logo = Image(source='logo.png', size_hint_y=0.5, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        welcome_label = Label(text='Sveiki atvykę į viktoriną apie Lietuvą!', font_size='24sp', halign='center',
                              size_hint_y=0.2, color=(0, 0, 0, 1))
        start_button = Button(text='Pradėti žaidimą', size_hint_y=0.1, background_color=(0, 0.5, 0, 1))
        start_button.bind(on_release=self.start_quiz)
        layout.add_widget(logo)
        layout.add_widget(welcome_label)
        layout.add_widget(start_button)
        self.add_widget(layout)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def start_quiz(self, instance):
        self.manager.current = 'quiz'


class QuizScreen(Screen):
    def __init__(self, **kwargs):
        super(QuizScreen, self).__init__(**kwargs)
        self.questions = get_questions()
        self.current_question_index = 0
        self.score = 0
        self.sound_enabled = True
        self.sound_correct = SoundLoader.load('sounds/correct.wav')
        self.sound_incorrect = SoundLoader.load('sounds/incorrect.wav')

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        with self.layout.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.layout.bind(size=self._update_rect, pos=self._update_rect)

        self.top_bar = BoxLayout(orientation='horizontal', size_hint_y=0.1)
        self.sound_toggle_button = Button(text='Sound: On', size_hint_x=0.2, background_color=(0.5, 0.5, 0.5, 1))
        self.sound_toggle_button.bind(on_release=self.toggle_sound)
        self.question_counter = Label(text='', size_hint_x=0.8, font_size='20sp', halign='right', valign='middle', color=(0, 0, 0, 1))

        self.top_bar.add_widget(self.sound_toggle_button)
        self.top_bar.add_widget(self.question_counter)

        self.question_label = Label(text='', font_size='20sp', halign='center', valign='middle', color=(0, 0, 0, 1))
        self.choices_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.choices_layout.bind(minimum_height=self.choices_layout.setter('height'))

        self.layout.add_widget(self.top_bar)
        self.layout.add_widget(self.question_label)
        self.layout.add_widget(self.choices_layout)

        self.add_widget(self.layout)
        self.display_question()

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def display_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.question_label.text = question['question']
            self.choices_layout.clear_widgets()
            for choice in question['choices']:
                btn = Button(text=choice, size_hint_y=None, height=44, background_color=(0.5, 0.5, 0.5, 1))
                btn.bind(on_release=self.check_answer)
                self.choices_layout.add_widget(btn)

            self.update_question_counter()
        else:
            self.show_result()

    def check_answer(self, instance):
        question = self.questions[self.current_question_index]
        if instance.text == question['answer']:
            self.score += 1
            if self.sound_enabled and self.sound_correct:
                self.sound_correct.play()
            instance.background_color = (0, 1, 0, 1)  # Green for correct answer
        else:
            if self.sound_enabled and self.sound_incorrect:
                self.sound_incorrect.play()
            instance.background_color = (1, 0, 0, 1)  # Red for incorrect answer

        # Move to the next question after a short delay
        Clock.schedule_once(self.next_question, 1)

    def next_question(self, dt):
        self.current_question_index += 1
        self.display_question()

    def show_result(self):
        self.manager.current = 'result'
        result_screen = self.manager.get_screen('result')
        result_screen.display_result(self.score, len(self.questions))

    def toggle_sound(self, instance):
        self.sound_enabled = not self.sound_enabled
        self.sound_toggle_button.text = 'Sound: On' if self.sound_enabled else 'Sound: Off'

    def update_question_counter(self):
        self.question_counter.text = f'Klausimas {self.current_question_index + 1} iš {len(self.questions)}'


class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        with self.layout.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.layout.bind(size=self._update_rect, pos=self._update_rect)
        self.result_label = Label(text='', font_size='20sp', halign='center', valign='middle', color=(0, 0, 0, 1))
        self.layout.add_widget(self.result_label)
        self.invitation_label = Label(text='Pasirinkite dovanelę:', font_size='18sp', halign='center', valign='middle', color=(0, 0, 0, 1))
        self.gift_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=0.5)
        self.layout.add_widget(self.invitation_label)
        self.layout.add_widget(self.gift_layout)
        self.add_widget(self.layout)
        self.back_button = Button(text='Grįžti į pradžią', size_hint_y=0.1, background_color=(0, 0.5, 0, 1))
        self.back_button.bind(on_release=self.go_back_to_intro)
        self.back_button.disabled = True  # Initially disable the back button
        self.layout.add_widget(self.back_button)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def display_result(self, score, total):
        self.result_label.text = f'Jūs surinkote {score} iš {total} taškų!'
        self.gift_layout.clear_widgets()
        if score / total > 0.5:
            gifts = ['gift1.png', 'gift2.png', 'gift3.png']
            random.shuffle(gifts)
            for gift in gifts:
                img_btn = ImageButton(source=gift, size_hint_x=0.3)
                img_btn.bind(on_release=self.reveal_gift)
                img_btn.gift = gift
                self.gift_layout.add_widget(img_btn)

    def reveal_gift(self, instance):
        for child in self.gift_layout.children:
            child.disabled = True  # Disable all gift buttons after one is selected

        if instance.gift == 'gift1.png':
            gif_popup = Popup(title='Dovana', size_hint=(0.8, 0.8))
            gif_image = Image(source='funny.png')  # Replace funny.gif with a static image
            gif_layout = BoxLayout(orientation='vertical')
            gif_layout.add_widget(gif_image)
            close_btn = Button(text='Uždaryti', size_hint_y=0.1)
            close_btn.bind(on_release=gif_popup.dismiss)
            gif_layout.add_widget(close_btn)
            gif_popup.content = gif_layout
            gif_popup.open()
        else:
            instance.source = 'empty.png'  # Change to an empty box image or similar

        # Enable the back button after a gift is selected
        self.back_button.disabled = False

    def go_back_to_intro(self, instance):
        self.manager.current = 'intro'
        quiz_screen = self.manager.get_screen('quiz')
        quiz_screen.current_question_index = 0
        quiz_screen.score = 0
        quiz_screen.display_question()


class QuizApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(IntroScreen(name='intro'))
        sm.add_widget(QuizScreen(name='quiz'))
        sm.add_widget(ResultScreen(name='result'))
        return sm


if __name__ == '__main__':
    QuizApp().run()

