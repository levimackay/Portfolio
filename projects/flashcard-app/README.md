# BCS Flashcards

I spent two years speaking Bosnian, Croatian, and Serbian on a mission, so I built this to keep the language sharp after coming home. It's a small Tkinter desktop app. You load a CSV of vocabulary and filter it by dialect, part of speech, difficulty, and a free text search across words and translations.

Hitting Generate prints the filtered list into the window. From there you can export it to a text file or launch the quiz. The quiz pulls four random words out of the filtered set and makes you pick the right translation for one of them; it needs at least four words to start. It sounds simple but it is actually pretty effective for drilling specific gaps in your vocabulary.

You can also load a JSON file of grammar notes keyed by word. Those notes show up next to the translation in the generated list on screen. The text export is just `word : translation`, no notes.

The CSV needs `word` and `translation` columns, plus `dialect`, `part_of_speech`, and `difficulty` if you want to filter on them.

Built with Python and Tkinter (`bcs_flashcards.py`). No vocabulary file is checked in — bring your own CSV.
