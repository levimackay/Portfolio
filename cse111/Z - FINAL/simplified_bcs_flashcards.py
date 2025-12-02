
import csv
import tkinter as tk
from tkinter import filedialog, messagebox

# Load vocabulary from a CSV file
def load_vocab():
    filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    vocab = []
    if filepath:
        with open(filepath, encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                vocab.append(row)
    return vocab

# Filter vocabulary by dialect
def filter_vocab(vocab, dialect):
    return [word for word in vocab if dialect in word['dialect']]

# Start a simple multiple choice quiz
def start_quiz(vocab):
    if not vocab:
        messagebox.showinfo("Error", "No vocabulary loaded.")
        return

    quiz_win = tk.Toplevel()
    quiz_win.title("Quiz")

    index = 0
    score = 0

    def ask_question():
        nonlocal index, score
        if index >= len(vocab):
            messagebox.showinfo("Done", f"Your score: {score}/{len(vocab)}")
            quiz_win.destroy()
            return

        word = vocab[index]
        question_label.config(text=f"What does '{word['word']}' mean?")
        answer_entry.delete(0, tk.END)

    def check_answer():
        nonlocal index, score
        user_answer = answer_entry.get().strip().lower()
        correct = vocab[index]['definition'].strip().lower()
        if user_answer == correct:
            score += 1
        index += 1
        ask_question()

    question_label = tk.Label(quiz_win, text="")
    question_label.pack()

    answer_entry = tk.Entry(quiz_win)
    answer_entry.pack()

    submit_btn = tk.Button(quiz_win, text="Submit", command=check_answer)
    submit_btn.pack()

    ask_question()

# Main window
def main():
    root = tk.Tk()
    root.title("BCS Flashcards")

    vocab_data = []

    def open_file():
        nonlocal vocab_data
        vocab_data = load_vocab()
        messagebox.showinfo("Success", f"Loaded {len(vocab_data)} words.")

    def apply_filter():
        dialect = dialect_entry.get().strip()
        filtered = filter_vocab(vocab_data, dialect)
        messagebox.showinfo("Filtered", f"{len(filtered)} words match.")
        return filtered

    tk.Button(root, text="Load CSV", command=open_file).pack()
    tk.Label(root, text="Filter by Dialect (e.g., [B])").pack()
    dialect_entry = tk.Entry(root)
    dialect_entry.pack()
    tk.Button(root, text="Start Quiz", command=lambda: start_quiz(apply_filter())).pack()

    root.mainloop()

main()
