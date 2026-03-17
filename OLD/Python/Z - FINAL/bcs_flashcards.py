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

#Imports
import csv
import json
import random
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

#File loading
def read_vocab_csv(filepath):
    """Reads the vocab CSV file and turns it into a list of dictionaries."""
    with open(filepath) as file:
        data = list(csv.DictReader(file))
    return data

def read_notes_json(json_path):
    """Loads notes (like grammar/pronunciation tips) from a JSON file."""
    with open(json_path) as file:
        data = json.load(file)
    return data

def add_notes(vocab_list, notes_dict):
    """Adds a 'note' field to each vocab entry if there’s a matching one in the JSON."""
    for entry in vocab_list:
        entry['note'] = notes_dict.get(entry['word'], "")
    return vocab_list

#Filtering
def filter_by_dialect(vocab, dialect):
    """Filters vocab to only include entries that match the given dialect tag (like [B], [C], or [S])."""
    filtered = [entry for entry in vocab if dialect in entry['dialect']]
    return filtered

def filter_by_pos(vocab, pos):
    """Filters vocab to just show nouns, verbs, etc. Not case-sensitive."""
    filtered = [entry for entry in vocab if entry['part_of_speech'].lower() == pos.lower()]
    return filtered

def filter_by_difficulty(vocab, level):
    """Filters vocab by difficulty level (as a string: '1', '2', '3')."""
    filtered = [entry for entry in vocab if entry.get('difficulty', '1') == str(level)]
    return filtered

def search_vocab(vocab, query):
    """Searches through word + translation fields for a match. Case-insensitive."""
    query = query.lower()
    results = [entry for entry in vocab if query in entry['word'].lower() or query in entry['translation'].lower()]
    return results

def sort_vocab(vocab, key="word"):
    """Sorts vocab list by a key (like 'word' or 'translation')."""
    sorted_vocab = sorted(vocab, key=lambda x: x[key].lower())
    return sorted_vocab

#Formstting and Exporting
def format_flashcard(entry):
    """Formats a vocab entry into a readable flashcard string."""
    note = f" | Note: {entry['note']}" if entry.get('note') else ""
    formatted = f"{entry['word']} – {entry['translation']} ({entry.get('dialect', '')}, {entry['part_of_speech']}){note}"
    return formatted

def export_flashcards(vocab):
    """Lets you save the flashcards to a .txt file (for Quizlet or printing)."""
    lines = [format_flashcard(entry) for entry in vocab]
    path = filedialog.asksaveasfilename(defaultextension=".txt")
    if path:
        with open(path, "w") as f:
            f.write("\n".join(lines))
        messagebox.showinfo("Saved", "Flashcards saved!")

#Quiz
def pick_question(vocab_list):
    """Randomly selects one correct vocab entry + 3 wrong ones for a quiz question."""
    correct = random.choice(vocab_list)
    others = [v for v in vocab_list if v != correct]
    if len(others) >= 3:
        choices = random.sample(others, k=3)
    else:
        choices = others
    choices.append(correct)
    random.shuffle(choices)
    return correct, choices

def start_quiz(root, vocab_list):
    """Opens a new window with a multiple-choice quiz UI."""
    win = tk.Toplevel(root)
    win.title("Vocab Quiz")

    score = {'correct': 0, 'total': 0}
    current = {'correct': None}
    '''when I originally wrote this, the quiz would glitch out and not show the next question. I had to add this current dict to keep track of the current question.'''  
    def show_next():
        if len(vocab_list) < 4:
            quiz_msg.set("Not enough words to quiz.")
            return
        quiz_msg.set("")
        correct, options = pick_question(vocab_list)
        current['correct'] = correct
        q_label.config(text=f"What does '{correct['word']}' mean?")
        for i, o in enumerate(options):
            btns[i].config(text=o['translation'], state='normal', command=lambda opt=o: check_answer(opt))

    '''This is pretty basic. It checks if the user picked the right answer, updates the score, and shows a message. Then it disables the buttons for a second before showing the next question.'''
    def check_answer(chosen):
        score['total'] += 1
        if chosen == current['correct']:
            score['correct'] += 1
            quiz_msg.set("✅ Correct!")
        else:
            quiz_msg.set(f"❌ Nope. It's '{current['correct']['translation']}'.")
        for btn in btns:
            btn.config(state='disabled')
        win.after(1000, show_next)

    q_label = ttk.Label(win, text="", font=("Arial", 14))
    q_label.pack(pady=10)

    btns = [ttk.Button(win) for _ in range(4)]
    for b in btns:
        b.pack(padx=30, pady=4, fill='x')

    quiz_msg = tk.StringVar()
    msg_label = ttk.Label(win, textvariable=quiz_msg, font=("Arial", 12))
    msg_label.pack(pady=5)

    show_next()

#GUI crap
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
            output_box.insert(tk.END, f"Loaded {len(vocab)} entries.\n")

    def load_notes():
        nonlocal notes
        path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if path:
            notes = read_notes_json(path)
            output_box.insert(tk.END, "Loaded extra notes.\n")

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
    #ChatGPT helped me format this so it looks nice.
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
