""" 
Mission Language Flashcard Generator + Quiz 
By: Levi Mackay, Spring 2025 Semester

This program is built for missionaries or language learners who wanna test and review vocab in Bosnian, Croatian,
or Serbian. You load a CSV of vocab or literally just a csv of a whole Serbo-Croatian dictionary, optionally load a JSON with grammar notes, and then you can search, filter,
sort, export to Quizlet (in the form of a Text file), or quiz yourself with multiple-choice questions.

Full send. This was a huge problem while I was on my mission. You would have a whole dictionary, but trying to sort through all the words for serbian or for bosnian or for croatian was impossible. This allows you
to filter by dialect, part of speech, difficulty, and search for specific words or translations. WIth this you could literally just load a whole dictionary 
and then filter it down to whatever you want.
"""

# IMPORTS
import csv
import json
import random
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# FILE LOADING FUNCTIONS
def read_vocab_csv(filepath):
    """Reads vocab CSV and turns it into a list of dictionaries so we can actually use the data."""
    with open(filepath) as file:
        return list(csv.DictReader(file))

def read_notes_json(json_path):
    """Loads a JSON file with extra notes like grammar tips or usage examples."""
    with open(json_path) as file:
        return json.load(file)

def add_notes(vocab_list, notes_dict):
    """Attaches any matching note from the JSON to each vocab word. This lets you see grammar tips or usage examples right on the flashcard.Prolly not the most efficent or practical file structure, but it works."""
    for entry in vocab_list:
        entry['note'] = notes_dict.get(entry['word'], "")
    return vocab_list

# FILTERING & SORTING CRAP
def filter_by_dialect(vocab, dialect):
    '''Filters the vocab list to only show words that match the given dialect — like just [B], [S], or [C].'''
    return [entry for entry in vocab if dialect in entry['dialect']]

def filter_by_pos(vocab, pos):
    '''Filters vocab by part of speech. If you only want verbs or nouns or whatever, this gets you just those.'''

    return [entry for entry in vocab if entry['part_of_speech'].lower() == pos.lower()]

def filter_by_difficulty(vocab, level):
    '''Filters vocab by difficulty level (1, 2, or 3). Makes it easy to focus on just beginner or advanced words.'''
    return [entry for entry in vocab if entry.get('difficulty', '1') == str(level)]

def search_vocab(vocab, query):
    '''Lets you search for a word or translation. Doesn’t care about capitalization — it's a basic case-insensitive search.'''
    query = query.lower()
    return [entry for entry in vocab if query in entry['word'].lower() or query in entry['translation'].lower()]

def sort_vocab(vocab, key="word"):
    '''Sorts the vocab list alphabetically by either the word or translation — whatever key you give it. Defaults to sorting by word.'''
    return sorted(vocab, key=lambda x: x[key].lower())

def format_flashcard(entry):
    '''Takes one vocab word and turns it into a clean string that shows the word, its translation, dialect, part of speech, and any note.'''
    note = f" | Note: {entry['note']}" if entry.get('note') else ""
    dialect = entry.get('dialect', '').upper()  # Always uppercase
    return f"{entry['word']} – {entry['translation']} ({dialect}, {entry['part_of_speech']}){note}"

def export_flashcards(vocab):
    '''Saves the formatted flashcards to a .txt file so you can paste them into Quizlet or print them. Uses the current filtered list.'''
    lines = [format_flashcard(entry) for entry in vocab]
    path = filedialog.asksaveasfilename(defaultextension=".txt")
    if path:
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        messagebox.showinfo("Saved", "Flashcards saved successfully.")

# QUIZ GAME 
def pick_question(vocab_list):
    '''Picks one correct vocab entry and adds three other random ones to make a multiple-choice question. Then shuffles them.'''
    correct = random.choice(vocab_list)
    other_choices = random.sample([v for v in vocab_list if v != correct], k=3) if len(vocab_list) >= 4 else []
    options = other_choices + [correct]
    random.shuffle(options)
    return correct, options

def start_quiz(root, vocab_list):
    '''Starts the quiz mode in a new window. Shows one word and four answer buttons. Tracks correct/wrong answers and keeps the quiz moving.
    It creates a new tinker gui window for the quiz. It always goes to the top left of the screen. Idk how to make it centered.
    '''
    quiz_win = tk.Toplevel(root)
    quiz_win.title("Vocab Quiz")

    score = {'correct': 0, 'total': 0}
    current = {'correct_entry': None}
    '''when I originally wrote this, the quiz would glitch out and not show the next question. I had to add this current dict to keep track of the current question.'''
    def show_next():
        quiz_msg.set("")
        if len(vocab_list) < 4:
            quiz_msg.set("Not enough words to quiz. Load more vocab.")
            return

        correct, options = pick_question(vocab_list)
        current['correct_entry'] = correct
        q_label.config(text=f"What does '{correct['word']}' mean?")
        for i, o in enumerate(options):
            btns[i].config(text=o['translation'], state='normal', command=lambda opt=o: check_answer(opt))

    '''This is pretty basic. It checks if the user picked the right answer, updates the score, and shows a message. Then it disables the buttons for a second before showing the next question.'''
    def check_answer(chosen):
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

# MAIN APP 
def main():
    '''This is the main function that sets up the GUI and handles user interactions. It honestly took me forever to figure out how to do this with tkinter. I have watched so many Youtube videos it's not
    even funny. This should be the main entry point for the app.'''
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
        '''Loads a CSV file with vocab entries and updates the vocab list. Nonlocal var are the colest thing ever. I have no idea why I didn't use them before.'''
        nonlocal vocab
        path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if path:
            vocab = read_vocab_csv(path)
            output_box.insert(tk.END, f"Loaded {len(vocab)} vocab entries.\n")

    def load_notes():
        nonlocal notes
        path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if path:
            notes = read_notes_json(path)
            output_box.insert(tk.END, "Loaded grammar/pronunciation notes.\n")

    def generate_flashcards():
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
        if not current_vocab:
            messagebox.showwarning("Warning", "Generate flashcards first.")
            return
        start_quiz(root, current_vocab)

    def export_current():
        if not current_vocab:
            messagebox.showwarning("Warning", "Generate flashcards first.")
            return
        export_flashcards(current_vocab)

    frame = ttk.Frame(root, padding=10)
    frame.grid(row=0, column=0)

    #The amount of times I have had to re-write this isn't even funny. I have no idea why I keep forgetting how to do this.
    #The grid is a little messy, but it works.
    #I can't really figure out how to make it centered when the window pulls up, but it works.
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
