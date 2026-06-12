import csv
import json
import random
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

def load_vocab_data(filepath):
    try:
        with open(filepath, encoding='utf-8') as f:
            return list(csv.DictReader(f))
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def load_grammar_notes(filepath):
    try:
        with open(filepath, encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def apply_filters(vocab, dialect="", pos="", difficulty="", search=""):
    filtered = vocab
    
    if dialect:
        filtered = [v for v in filtered if dialect.lower() in v.get('dialect', '').lower()]
    
    if pos:
        filtered = [v for v in filtered if pos.lower() == v.get('part_of_speech', '').lower()]
        
    if difficulty:
        filtered = [v for v in filtered if difficulty == v.get('difficulty', '')]
        
    if search:
        s = search.lower()
        filtered = [v for v in filtered if s in v.get('word', '').lower() or s in v.get('translation', '').lower()]
        
    return sorted(filtered, key=lambda x: x.get('word', '').lower())

class VocabApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BCS Flashcard Tool")
        self.root.geometry("800x700")
        
        self.raw_data = []
        self.notes_data = {}
        self.filtered_data = []
        
        self.setup_ui()

    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill='both', expand=True)

        filter_frame = ttk.LabelFrame(main_frame, text=" Filters ", padding="10")
        filter_frame.pack(fill='x', pady=10)

        ttk.Label(filter_frame, text="Dialect ([B], [C], [S]):").grid(row=0, column=0, sticky='w')
        self.dialect_entry = ttk.Entry(filter_frame)
        self.dialect_entry.grid(row=0, column=1, padx=5, pady=2, sticky='ew')

        ttk.Label(filter_frame, text="Part of Speech:").grid(row=1, column=0, sticky='w')
        self.pos_entry = ttk.Entry(filter_frame)
        self.pos_entry.grid(row=1, column=1, padx=5, pady=2, sticky='ew')

        ttk.Label(filter_frame, text="Difficulty (1-3):").grid(row=2, column=0, sticky='w')
        self.diff_entry = ttk.Entry(filter_frame)
        self.diff_entry.grid(row=2, column=1, padx=5, pady=2, sticky='ew')

        ttk.Label(filter_frame, text="Search:").grid(row=3, column=0, sticky='w')
        self.search_entry = ttk.Entry(filter_frame)
        self.search_entry.grid(row=3, column=1, padx=5, pady=2, sticky='ew')
        
        filter_frame.columnconfigure(1, weight=1)

        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill='x', pady=5)

        ttk.Button(btn_frame, text="Load CSV", command=self.on_load_csv).pack(side='left', padx=2)
        ttk.Button(btn_frame, text="Load Notes", command=self.on_load_notes).pack(side='left', padx=2)
        ttk.Button(btn_frame, text="Generate", command=self.on_generate).pack(side='left', padx=2)
        ttk.Button(btn_frame, text="Start Quiz", command=self.on_quiz).pack(side='left', padx=2)
        ttk.Button(btn_frame, text="Export TXT", command=self.on_export).pack(side='left', padx=2)

        self.output = tk.Text(main_frame, height=20, font=("Consolas", 10))
        self.output.pack(fill='both', expand=True, pady=10)

    def on_load_csv(self):
        path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if path:
            self.raw_data = load_vocab_data(path)

    def on_load_notes(self):
        path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if path:
            self.notes_data = load_grammar_notes(path)

    def on_generate(self):
        if not self.raw_data:
            return
            
        self.filtered_data = apply_filters(
            self.raw_data,
            dialect=self.dialect_entry.get(),
            pos=self.pos_entry.get(),
            difficulty=self.diff_entry.get(),
            search=self.search_entry.get()
        )
        
        self.output.delete("1.0", tk.END)
        for item in self.filtered_data:
            note = self.notes_data.get(item['word'], "")
            note_str = f" | {note}" if note else ""
            line = f"{item['word']} -> {item['translation']} ({item.get('dialect', '')}){note_str}\n"
            self.output.insert(tk.END, line)

    def on_export(self):
        if not self.filtered_data: return
        path = filedialog.asksaveasfilename(defaultextension=".txt")
        if path:
            with open(path, "w", encoding='utf-8') as f:
                for v in self.filtered_data:
                    f.write(f"{v['word']} : {v['translation']}\n")

    def on_quiz(self):
        if len(self.filtered_data) < 4:
            return
        QuizWindow(self.root, self.filtered_data)

class QuizWindow(tk.Toplevel):
    def __init__(self, parent, data):
        super().__init__(parent)
        self.title("Quiz")
        self.geometry("400x300")
        self.data = data
        self.current_correct = None
        
        self.label = ttk.Label(self, text="", font=("Arial", 12), wraplength=350)
        self.label.pack(pady=20)
        
        self.btns = []
        for _ in range(4):
            btn = ttk.Button(self, text="", command=lambda: None)
            btn.pack(fill='x', padx=50, pady=5)
            self.btns.append(btn)
            
        self.next_question()

    def next_question(self):
        sample = random.sample(self.data, 4)
        self.current_correct = sample[0]
        random.shuffle(sample)
        
        self.label.config(text=f"What does '{self.current_correct['word']}' mean?")
        
        for i, word in enumerate(sample):
            self.btns[i].config(
                text=word['translation'],
                command=lambda w=word: self.check_answer(w)
            )

    def check_answer(self, chosen):
        if chosen == self.current_correct:
            messagebox.showinfo("Correct", "Correct!")
        else:
            messagebox.showerror("Wrong", f"Incorrect. Answer: {self.current_correct['translation']}")
        self.next_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = VocabApp(root)
    root.mainloop()
