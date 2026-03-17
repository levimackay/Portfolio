import csv
import json
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

def read_vocabulary_file(filepath):
    '''Reads the vocab CSV and turns it into a list of dictionaries so I can mess with the data easier.'''
    with open(filepath, encoding="utf-8") as file:
        return list(csv.DictReader(file))

def read_notes_file(json_path):
    '''Loads extra notes from a JSON file—stuff like grammar tips or pronunciation that I wanna attach to the words.'''
    with open(json_path, encoding="utf-8") as file:
        return json.load(file)

def filter_by_dialect(vocab_list, dialect):
    '''Filters the vocab list to only show words from a specific dialect like [B], [S], or [C].'''
    return [entry for entry in vocab_list if dialect in entry['dialect']]

def filter_by_part_of_speech(vocab_list, pos):
    '''Filters vocab entries by part of speech—like only show nouns, verbs, etc.'''
    return [entry for entry in vocab_list if entry['part_of_speech'].lower() == pos.lower()]

def filter_by_difficulty(vocab_list, level):
    '''Filters vocab entries by difficulty level. Just looks for ones marked as "1", "2", or "3".'''
    return [entry for entry in vocab_list if entry.get('difficulty', '1') == str(level)]

def add_notes_to_vocab(vocab_list, notes_dict):
    '''Loops through the vocab and attaches any matching notes from the JSON file to each word.'''
    for word in vocab_list:
        word['note'] = notes_dict.get(word['word'], "")
    return vocab_list

def format_flashcard(entry):
    '''Formats a vocab entry into a clean flashcard string that shows word, translation, part of speech, and a note if there is one.'''
    note = f" | Note: {entry['note']}" if entry.get('note') else ""
    return f"{entry['word']} - {entry['translation']} ({entry['part_of_speech']}){note}"

def search_vocab(vocab_list, query):
    '''Lets me search through the vocab list by either the word or its translation. Case-insensitive.'''
    query = query.lower()
    return [entry for entry in vocab_list if query in entry['word'].lower() or query in entry['translation'].lower()]

def sort_vocab(vocab_list, key="word"):
    '''Sorts the vocab list alphabetically by the key I pass in—usually by word.'''
    return sorted(vocab_list, key=lambda x: x[key].lower())

def save_flashcards_to_file(vocab_lines, filepath):
    '''Takes the list of formatted flashcards and writes them all to a text file so I can print or save them.'''
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(vocab_lines))


class FlashcardApp:
    def __init__(self, root):
        '''This is the main app class. Sets up the GUI, holds vocab + notes, and connects all the logic.'''
        self.root = root
        self.vocab = []
        self.notes = {}

        self.dialect = tk.StringVar()
        self.pos = tk.StringVar()
        self.difficulty = tk.StringVar()
        self.search_query = tk.StringVar()

        self.setup_ui()

    def setup_ui(self):
        '''Builds the GUI—entries, buttons, text box, all that.'''
        self.root.title("Mission Language Flashcard Generator")

        mainframe = ttk.Frame(self.root, padding="10")
        mainframe.grid(row=0, column=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        ttk.Label(mainframe, text="Dialect (e.g. [B], [C], [S]):").grid(row=0, column=0, sticky=tk.W, pady=2)
        ttk.Entry(mainframe, textvariable=self.dialect).grid(row=0, column=1, sticky=tk.EW)

        ttk.Label(mainframe, text="Part of Speech (noun, verb, etc):").grid(row=1, column=0, sticky=tk.W, pady=2)
        ttk.Entry(mainframe, textvariable=self.pos).grid(row=1, column=1, sticky=tk.EW)

        ttk.Label(mainframe, text="Difficulty (1–3):").grid(row=2, column=0, sticky=tk.W, pady=2)
        ttk.Entry(mainframe, textvariable=self.difficulty).grid(row=2, column=1, sticky=tk.EW)

        ttk.Label(mainframe, text="Search (word or translation):").grid(row=3, column=0, sticky=tk.W, pady=2)
        ttk.Entry(mainframe, textvariable=self.search_query).grid(row=3, column=1, sticky=tk.EW)

        ttk.Button(mainframe, text="Load CSV", command=self.load_csv).grid(row=4, column=0, pady=5, sticky=tk.EW)
        ttk.Button(mainframe, text="Load Notes", command=self.load_notes).grid(row=4, column=1, pady=5, sticky=tk.EW)
        ttk.Button(mainframe, text="Generate Flashcards", command=self.generate).grid(row=5, column=0, columnspan=2, pady=5, sticky=tk.EW)
        ttk.Button(mainframe, text="Save to File", command=self.save_to_file).grid(row=6, column=0, columnspan=2, pady=5, sticky=tk.EW)

        self.output = tk.Text(mainframe, width=70, height=25)
        self.output.grid(row=7, column=0, columnspan=2, pady=10)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

    def load_csv(self):
        '''Loads vocab from a .csv file I pick and prints how many words got pulled in.'''
        path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if path:
            self.vocab = read_vocabulary_file(path)
            self.output.insert(tk.END, f"Loaded {len(self.vocab)} vocab entries from file.\n")

    def load_notes(self):
        '''Loads extra notes like grammar tips from a .json file I choose.'''
        path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if path:
            self.notes = read_notes_file(path)
            self.output.insert(tk.END, "Loaded grammar/pronunciation notes.\n")

    def generate(self):
        '''Runs all filters and builds the final flashcard list to display in the output box.'''
        vocab = self.vocab
        if self.notes:
            vocab = add_notes_to_vocab(vocab, self.notes)
        if self.dialect.get():
            vocab = filter_by_dialect(vocab, self.dialect.get())
        if self.pos.get():
            vocab = filter_by_part_of_speech(vocab, self.pos.get())
        if self.difficulty.get():
            vocab = filter_by_difficulty(vocab, self.difficulty.get())
        if self.search_query.get():
            vocab = search_vocab(vocab, self.search_query.get())

        vocab = sort_vocab(vocab)
        self.output.delete("1.0", tk.END)
        for entry in vocab:
            self.output.insert(tk.END, format_flashcard(entry) + "\n")

    def save_to_file(self):
        '''Takes whatever flashcards are in the output box and saves them to a .txt file.'''
        path = filedialog.asksaveasfilename(defaultextension=".txt")
        if path:
            vocab_lines = self.output.get("1.0", tk.END).strip().split('\n')
            save_flashcards_to_file(vocab_lines, path)
            messagebox.showinfo("Saved", "Flashcards saved successfully.")


if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
