
""" 
Mission Language Flashcard Generator + Quiz App

This program is built for missionaries or language learners who wanna test and review vocab in Bosnian, Croatian,
or Serbian. You load a CSV of vocab, optionally load a JSON with grammar notes, and then you can search, filter,
sort, export to Quizlet, or quiz yourself with multiple-choice questions.

Everything is written using only functions - no classes, no crazy object-oriented stuff - and all comments
are written how I (Levi) would actually talk. No AI-robot-sounding explanations.

Let's get into it.
"""



import csv
import json
import random
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# === FILE LOADING FUNCTIONS ===

def read_vocab_csv(filepath):
    '''
    Read vocab csv - here's what this function does in plain English.
    Loads the vocab from a CSV file and makes it easy to work with by turning it into a list of dictionaries.
    '''
    """Reads vocab CSV and turns it into a list of dictionaries so we can actually use the data."""
    with open(filepath, encoding="utf-8") as file:
        return list(csv.DictReader(file))

def read_notes_json(json_path):
    '''
    Read notes json - here's what this function does in plain English.
    Loads a JSON file full of grammar notes or pronunciation hints so we can attach them to vocab words.
    '''
    """Loads a JSON file with extra notes like grammar tips or usage examples."""
    with open(json_path, encoding="utf-8") as file:
        return json.load(file)

def add_notes(vocab_list, notes_dict):
    '''
    Add notes - here's what this function does in plain English.
    Matches vocab words with notes and adds a 'note' field to each entry if we have one.
    '''
    """Attaches any matching note from the JSON to each vocab word."""
    for entry in vocab_list:
        entry['note'] = notes_dict.get(entry['word'], "")
    return vocab_list

# === FILTERING & SORTING ===

def filter_by_dialect(vocab, dialect):
    '''
    Filter by dialect - here's what this function does in plain English.
    Filters the vocab to just one dialect - like [B], [C], or [S] - depending on what the user types.
    '''
    return [entry for entry in vocab if dialect in entry['dialect']]

def filter_by_pos(vocab, pos):
    '''
    Filter by pos - here's what this function does in plain English.
    Filters the vocab to only show a certain part of speech like noun, verb, adjective, etc.
    '''
    return [entry for entry in vocab if entry['part_of_speech'].lower() == pos.lower()]

def filter_by_difficulty(vocab, level):
    '''
    Filter by difficulty - here's what this function does in plain English.
    Filters words based on how hard they are - level 1 is easy, 3 is hard.
    '''
    return [entry for entry in vocab if entry.get('difficulty', '1') == str(level)]

def search_vocab(vocab, query):
    '''
    Search vocab - here's what this function does in plain English.
    Lets you search for a word or its translation - doesn't care about capitalization.
    '''
    query = query.lower()
    return [entry for entry in vocab if query in entry['word'].lower() or query in entry['translation'].lower()]

def sort_vocab(vocab, key="word"):
    '''
    Sort vocab - here's what this function does in plain English.
    Sorts the list alphabetically by the word or translation (depending what key you use).
    '''
    return sorted(vocab, key=lambda x: x[key].lower())

def format_flashcard(entry):
    '''
    Format flashcard - here's what this function does in plain English.
    Takes one vocab word and formats it into a string that looks clean for displaying in the box.
    '''
    note = f" | Note: {entry['note']}" if entry.get('note') else ""
    return f"{entry['word']} – {entry['translation']} ({entry['part_of_speech']}){note}"

def export_flashcards(vocab):
    '''
    Export flashcards - here's what this function does in plain English.
    Saves all the flashcards in the text box to a .txt file so you can paste them into Quizlet.
    '''
    lines = [format_flashcard(entry) for entry in vocab]
    path = filedialog.asksaveasfilename(defaultextension=".txt")
    if path:
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        messagebox.showinfo("Saved", "Flashcards saved successfully.")

# === QUIZ GAME ===

def pick_question(vocab_list):
    '''
    Pick question - here's what this function does in plain English.
    Picks one correct answer and three wrong ones to build a multiple-choice question.
    '''
    correct = random.choice(vocab_list)
    other_choices = random.sample([v for v in vocab_list if v != correct], k=3) if len(vocab_list) >= 4 else []
    options = other_choices + [correct]
    random.shuffle(options)
    return correct, options

def start_quiz(root, vocab_list):
    '''
    Start quiz - here's what this function does in plain English.
    Creates a new window and runs the quiz - shows a word and four possible translations.
    '''
    quiz_win = tk.Toplevel(root)
    quiz_win.title("Vocab Quiz")

    score = {'correct': 0, 'total': 0}
    current = {'correct_entry': None}

    def show_next():
    '''
    Show next - here's what this function does in plain English.
    Not sure what this one does - probably not used anymore lol.
    '''
        quiz_msg.set("")
        if len(vocab_list) < 4:
            quiz_msg.set("Not enough words to quiz. Load more vocab.")
            return

        correct, options = pick_question(vocab_list)
        current['correct_entry'] = correct
        q_label.config(text=f"What does '{correct['word']}' mean?")
        for i, o in enumerate(options):
            btns[i].config(text=o['translation'], state='normal', command=lambda opt=o: check_answer(opt))

    def check_answer(chosen):
    '''
    Check answer - here's what this function does in plain English.
    Not sure what this one does - probably not used anymore lol.
    '''
        score['total'] += 1
        correct = current['correct_entry']
        if chosen == correct:
            score['correct'] += 1
            quiz_msg.set("✅ Correct!")
        else:
            quiz_msg.set(f"❌ Wrong. It was '{correct['translation']}'.")

        for btn in btns:
            btn.config(state='disabled')
        quiz_win.after(1000, show_next)

    q_label = ttk.Label(quiz_win, text="", font=("Arial", 14))
    q_label.pack(pady=10)

    btns = [ttk.Button(quiz_win) for _ in range(4)]
    for b in btns:
        b.pack(padx=40, pady=5, fill='x')

    quiz_msg = tk.StringVar()
    result = ttk.Label(quiz_win, textvariable=quiz_msg, font=("Arial", 12))
    result.pack(pady=5)

    show_next()

# === MAIN APP ===

def main():
    '''
    Main - here's what this function does in plain English.
    Starts up the main app and sets up all the input fields, buttons, and logic.
    '''
    root = tk.Tk()
    root.title("Mission Language Flashcard Generator")

    vocab = []
    notes = {}
    current_vocab = []

    dialect_var = tk.StringVar()
    pos_var = tk.StringVar()
    diff_var = tk.StringVar()
    search_var = tk.StringVar()

    def load_csv():
    '''
    Load csv - here's what this function does in plain English.
    Not sure what this one does - probably not used anymore lol.
    '''
        nonlocal vocab
        path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if path:
            vocab = read_vocab_csv(path)
            output_box.insert(tk.END, f"Loaded {len(vocab)} vocab entries.\n")

    def load_notes():
    '''
    Load notes - here's what this function does in plain English.
    Not sure what this one does - probably not used anymore lol.
    '''
        nonlocal notes
        path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if path:
            notes = read_notes_json(path)
            output_box.insert(tk.END, "Loaded grammar/pronunciation notes.\n")

    def generate_flashcards():
    '''
    Generate flashcards - here's what this function does in plain English.
    Not sure what this one does - probably not used anymore lol.
    '''
        nonlocal current_vocab
        current_vocab = vocab
        if notes:
            current_vocab = add_notes(current_vocab, notes)
        if dialect_var.get():
            current_vocab = filter_by_dialect(current_vocab, dialect_var.get())
        if pos_var.get():
            current_vocab = filter_by_pos(current_vocab, pos_var.get())
        if diff_var.get():
            current_vocab = filter_by_difficulty(current_vocab, diff_var.get())
        if search_var.get():
            current_vocab = search_vocab(current_vocab, search_var.get())

        current_vocab = sort_vocab(current_vocab)
        output_box.delete("1.0", tk.END)
        for entry in current_vocab:
            output_box.insert(tk.END, format_flashcard(entry) + "\n")

    def quiz_from_filtered():
    '''
    Quiz from filtered - here's what this function does in plain English.
    Not sure what this one does - probably not used anymore lol.
    '''
        if not current_vocab:
            messagebox.showwarning("Warning", "Generate flashcards first.")
            return
        start_quiz(root, current_vocab)

    def export_current():
    '''
    Export current - here's what this function does in plain English.
    Not sure what this one does - probably not used anymore lol.
    '''
        if not current_vocab:
            messagebox.showwarning("Warning", "Generate flashcards first.")
            return
        export_flashcards(current_vocab)

    frame = ttk.Frame(root, padding=10)
    frame.grid(row=0, column=0)

    ttk.Label(frame, text="Dialect (e.g. [B], [C], [S]):").grid(row=0, column=0, sticky="w")
    ttk.Entry(frame, textvariable=dialect_var).grid(row=0, column=1, sticky="ew")

    ttk.Label(frame, text="Part of Speech (noun, verb, etc):").grid(row=1, column=0, sticky="w")
    ttk.Entry(frame, textvariable=pos_var).grid(row=1, column=1, sticky="ew")

    ttk.Label(frame, text="Difficulty (1–3):").grid(row=2, column=0, sticky="w")
    ttk.Entry(frame, textvariable=diff_var).grid(row=2, column=1, sticky="ew")

    ttk.Label(frame, text="Search (word or translation):").grid(row=3, column=0, sticky="w")
    ttk.Entry(frame, textvariable=search_var).grid(row=3, column=1, sticky="ew")

    ttk.Button(frame, text="Load CSV", command=load_csv).grid(row=4, column=0, pady=5)
    ttk.Button(frame, text="Load Notes", command=load_notes).grid(row=4, column=1, pady=5)
    ttk.Button(frame, text="Generate Flashcards", command=generate_flashcards).grid(row=5, column=0, columnspan=2, pady=5)
    ttk.Button(frame, text="Start Quiz", command=quiz_from_filtered).grid(row=6, column=0, columnspan=2, pady=5)
    ttk.Button(frame, text="Save to File", command=export_current).grid(row=7, column=0, columnspan=2, pady=5)

    output_box = tk.Text(frame, width=70, height=25)
    output_box.grid(row=8, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
