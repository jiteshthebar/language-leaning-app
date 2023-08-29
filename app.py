import tkinter as tk

class LanguageLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Learning App")

        self.flashcards = [
            {"word": "apple", "meaning": "a round fruit with red or green skin"},
            {"word": "book", "meaning": "a written or printed work consisting of pages glued or sewn together"},
            {"word": "cat", "meaning": "a small domesticated carnivorous mammal with soft fur"},
            {"word": "rose","meaning": "it is a red in color and give a sweet smell"},
            {"word": "orange","meaning": "Citrus fruit known for its tangy flavor and high vitamin C content."},
            {"word": "grapes","meaning": " Small, round, and juicy fruits found in bunches; they come in various colors and can be eaten fresh or used for making wine."},
             {"word": "kivi","meaning": "Small, fuzzy fruit with green flesh and black seeds, packed with vitamins and antioxidants."},

            # Add more flashcards here
        ]
        

        self.current_card_index = 0

        self.word_label = tk.Label(root, text="", font=("Helvetica", 18))
        self.word_label.pack(pady=30)

        self.meaning_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.meaning_label.pack()

        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card,)
        self.flip_button.pack(pady=10)

        self.next_button = tk.Button(root, text="Next Card", command=self.next_card,fg='red')
        self.next_button.pack(pady=12)

        self.show_current_card()

    def show_current_card(self):
        current_card = self.flashcards[self.current_card_index]
        self.word_label.config(text=current_card["word"],fg='green')
        self.meaning_label.config(text="", state=tk.NORMAL)
        self.flip_button.config(state=tk.NORMAL)
    
    def flip_card(self):
        current_card = self.flashcards[self.current_card_index]
        self.meaning_label.config(text=current_card["meaning"],fg="blue")
        self.flip_button.config(state=tk.DISABLED)
    
    def next_card(self):
        self.current_card_index = (self.current_card_index + 1) % len(self.flashcards)
        self.show_current_card()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageLearningApp(root)
    app.run()
