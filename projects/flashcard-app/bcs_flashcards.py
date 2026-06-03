# =============================================================================
# LEVI'S MISSION LANGUAGE FLASHCARD GENERATOR
#
# So, context: I was on my mission and trying to learn BCS (Bosnian/Croatian/Serbian).
# The dictionaries we had were massive and super disorganized. I wanted a way 
# to just filter for exactly what I needed—like "show me all the verbs used 
# specifically in Croatia" or "give me a quiz on level 2 difficulty words."
#
# This tool loads CSV data, lets you slice and dice it, and then generates 
# flashcards or lets you run through a quick multiple-choice quiz.
# Full send.
# =============================================================================

import csv
import json
import random
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# --- Data Management ---
# Just some basic helpers to get the data from files into Python lists.

def load_vocab_data(filepath):
    """ Reads the CSV and turns it into a list of dicts. Standard stuff. """
    try:
        with open(filepath, encoding='utf-8') as f:
            return list(csv.DictReader(f))
    except Exception as e:
        print(f"Bummer, couldn't read the file: {e}")
        return []

def load_grammar_notes(filepath):
    """ Loads extra context like grammar tips from a JSON. """
    try:
        with open(filepath, encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

# --- Filtering Logic ---
# This is where the magic happens. We can stack these filters.

def apply_filters(vocab, dialect="", pos="", difficulty="", search=""):
    """ 
    This is the engine. It takes the whole list and narrows it down 
    based on whatever the user typed in the GUI.
    """
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
        
    # Sort alphabetically by default because I'm picky
    return sorted(filtered, key=lambda x: x.get('word', '').lower())

# --- The GUI ---
# I used Tkinter because it's built-in and gets the job done without extra installs.
# It's a bit of a pain to style, but it works.

class VocabApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Levi's BCS Flashcard Tool")
        self.root.geometry("800x700")
        
        # State variables
        self.raw_data = []
        self.notes_data = {}
        self.filtered_data = []
        
        self.setup_ui()

    def setup_ui(self):
        """ Setting up all the buttons and entry fields. """
        # Main layout frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill='both', expand=True)

        # --- Filter Section ---
        filter_frame = ttk.LabelFrame(main_frame, text=" Filters (What are we studying?) ", padding="10")
        filter_frame.pack(fill='x', pady=10)

        # Dialect
        ttk.Label(filter_frame, text="Dialect ([B], [C], [S]):").grid(row=0, column=0, sticky='w')
        self.dialect_entry = ttk.Entry(filter_frame)
        self.dialect_entry.grid(row=0, column=1, padx=5, pady=2, sticky='ew')

        # POS
        ttk.Label(filter_frame, text="Part of Speech:").grid(row=1, column=0, sticky='w')
        self.pos_entry = ttk.Entry(filter_frame)
        self.pos_entry.grid(row=1, column=1, padx=5, pady=2, sticky='ew')

        # Difficulty
        ttk.Label(filter_frame, text="Difficulty (1-3):").grid(row=2, column=0, sticky='w')
        self.diff_entry = ttk.Entry(filter_frame)
        self.diff_entry.grid(row=2, column=1, padx=5, pady=2, sticky='ew')

        # Search
        ttk.Label(filter_frame, text="Search:").grid(row=3, column=0, sticky='w')
        self.search_entry = ttk.Entry(filter_frame)
        self.search_entry.grid(row=3, column=1, padx=5, pady=2, sticky='ew')
        
        filter_frame.columnconfigure(1, weight=1)

        # --- Buttons ---
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill='x', pady=5)

        ttk.Button(btn_frame, text="Load CSV", command=self.on_load_csv).pack(side='left', padx=2)
        ttk.Button(btn_frame, text="Load Notes", command=self.on_load_notes).pack(side='left', padx=2)
        ttk.Button(btn_frame, text="Generate", command=self.on_generate).pack(side='left', padx=2)
        ttk.Button(btn_frame, text="Start Quiz", command=self.on_quiz).pack(side='left', padx=2)
        ttk.Button(btn_frame, text="Export TXT", command=self.on_export).pack(side='left', padx=2)

        # --- Output Area ---
        self.output = tk.Text(main_frame, height=20, font=("Consolas", 10))
        self.output.pack(fill='both', expand=True, pady=10)

    # --- Button Callbacks ---
    
    def on_load_csv(self):
        path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if path:
            self.raw_data = load_vocab_data(path)
            messagebox.showinfo("Success", f"Loaded {len(self.raw_data)} words. Nice.")

    def on_load_notes(self):
        path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if path:
            self.notes_data = load_grammar_notes(path)
            messagebox.showinfo("Success", "Grammar notes loaded.")

    def on_generate(self):
        """ This pulls from the entry fields and runs the filters. """
        if not self.raw_data:
            messagebox.showwarning("Wait up", "You gotta load a CSV first.")
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
            line = f"{item['word']} -> {item['translation']} ({item.get('dialect', '')}) {note_str}\n"
            self.output.insert(tk.END, line)

    def on_export(self):
        if not self.filtered_data: return
        path = filedialog.asksaveasfilename(defaultextension=".txt")
        if path:
            with open(path, "w", encoding='utf-8') as f:
                for v in self.filtered_data:
                    f.write(f"{v['word']} : {v['translation']}\n")
            messagebox.showinfo("Done", "Exported successfully.")

    def on_quiz(self):
        """ Opens the quiz window. I like keeping this separate. """
        if len(self.filtered_data) < 4:
            messagebox.showwarning("Not enough data", "You need at least 4 words filtered to quiz.")
            return
        QuizWindow(self.root, self.filtered_data)

class QuizWindow(tk.Toplevel):
    """ The actual quiz logic. Multiple choice, random answers. """
    def __init__(self, parent, data):
        super().__init__(parent)
        self.title("Quick Quiz")
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
        # Pick 4 random words, one is the winner
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
            messagebox.showinfo("Boom!", "Correct!")
        else:
            messagebox.showerror("Miss", f"Nope. It's '{self.current_correct['translation']}'.")
        self.next_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = VocabApp(root)
    root.mainloop()
