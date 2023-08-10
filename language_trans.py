import tkinter as tk
from tkinter import ttk
from googletrans import Translator

class LanguageTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")
        
        self.translator = Translator()
        
        self.create_widgets()
        
    def create_widgets(self):
        self.label_source = tk.Label(self.root, text="Enter text:")
        self.label_source.pack(pady=10)
        
        self.entry_source = tk.Entry(self.root, width=50)
        self.entry_source.pack(pady=5)
        
        self.label_target = tk.Label(self.root, text="Translated text:")
        self.label_target.pack(pady=10)
        
        self.text_target = tk.Text(self.root, height=6, width=50)
        self.text_target.pack(pady=5)
        
        self.language_options = ["English", "Spanish", "French", "German", "Chinese"]
        
        self.label_language = tk.Label(self.root, text="Select target language:")
        self.label_language.pack(pady=5)
        
        self.combo_language = ttk.Combobox(self.root, values=self.language_options)
        self.combo_language.set("English")
        self.combo_language.pack(pady=5)
        
        self.translate_button = tk.Button(self.root, text="Translate", command=self.translate_text)
        self.translate_button.pack(pady=10)
        
    def translate_text(self):
        source_text = self.entry_source.get()
        target_language = self.combo_language.get()
        
        translated = self.translator.translate(source_text, dest=target_language.lower())
        self.text_target.delete(1.0, tk.END)  # Clear previous content
        self.text_target.insert(tk.END, translated.text)
        
def main():
    root = tk.Tk()
    app = LanguageTranslatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
