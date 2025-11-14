import tkinter as tk
import json

class TextGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Текстовая игра")
        self.text_area = tk.Text(master, height=15, width=50)
        self.text_area.pack()

        self.input_entry = tk.Entry(master)
        self.input_entry.pack()

        self.submit_button = tk.Button(master, text="Отправить", command=self.process_input)
        self.submit_button.pack()

        self.actions = []
        self.load_game()

    def load_game(self):
        # Попытка загрузить сохраненные действия
        try:
            with open("save.json", "r") as f:
                self.actions = json.load(f)
            # Воспроизвести действия
            for action in self.actions:
                self.display_text(action['text'])
        except FileNotFoundError:
            # Начать новую игру
            self.display_text("Добро пожаловать! Введите ваше имя:")
            self.game_state = "name"

    def save_action(self, text):
        self.actions.append({"text": text})
        with open("save.json", "w") as f:
            json.dump(self.actions, f)

    def display_text(self, text):
        self.text_area.insert(tk.END, text + "\n")
        self.text_area.see(tk.END)

    def process_input(self):
        user_input = self.input_entry.get()
        self.input_entry.delete(0, tk.END)
        self.save_action(user_input)

        if hasattr(self, 'game_state'):
            if self.game_state == "name":
                self.display_text(f"Привет, {user_input}! Начинаем игру...")
                self.game_state = "started"
            elif self.game_state == "started":
                self.display_text(f"Вы сказали: {user_input}")
                # Продолжение логики игры...
        else:
            self.display_text(f"Вы сказали: {user_input}")

root = tk.Tk()
game = TextGame(root)
root.mainloop()
