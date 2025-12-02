from bcs_flashcards import (
    add_notes,
    filter_by_dialect,
    filter_by_pos,
    filter_by_difficulty,
    search_vocab,
    sort_vocab,
    format_flashcard
)

def test_add_notes():
    vocab = [
        {"word": "kuća", "translation": "house", "part_of_speech": "noun", "dialect": "[S]", "difficulty": "1"},
        {"word": "auto", "translation": "car", "part_of_speech": "noun", "dialect": "[C]", "difficulty": "2"}
    ]
    notes = {"kuća": "common word", "auto": "used in Croatian"}
    result = add_notes(vocab, notes)

    assert result[0]["note"] == "common word"
    assert result[1]["note"] == "used in Croatian"

    # test with no matching notes
    empty_notes = {}
    result2 = add_notes(vocab, empty_notes)
    assert result2[0]["note"] == ""
    assert result2[1]["note"] == ""

def test_filter_by_dialect():
    vocab = [
        {"word": "kuća", "translation": "house", "dialect": "[S]", "part_of_speech": "noun"},
        {"word": "hljeb", "translation": "bread", "dialect": "[B]", "part_of_speech": "noun"},
        {"word": "auto", "translation": "car", "dialect": "[C]", "part_of_speech": "noun"}
    ]
    result = filter_by_dialect(vocab, "[B]")
    assert len(result) == 1
    assert result[0]["word"] == "hljeb"

    result2 = filter_by_dialect(vocab, "[Z]")  # unexpected dialect
    assert result2 == []

def test_filter_by_pos():
    vocab = [
        {"word": "vidjeti", "translation": "to see", "part_of_speech": "verb", "dialect": "[B]"},
        {"word": "drvo", "translation": "tree", "part_of_speech": "noun", "dialect": "[S]"},
        {"word": "lijep", "translation": "beautiful", "part_of_speech": "adjective", "dialect": "[C]"}
    ]
    result = filter_by_pos(vocab, "verb")
    assert len(result) == 1

    result2 = filter_by_pos(vocab, "NOUN")  # test case-insensitivity
    assert len(result2) == 1

    result3 = filter_by_pos(vocab, "adverb")  # invalid case
    assert result3 == []

def test_filter_by_difficulty():
    vocab = [
        {"word": "auto", "translation": "car", "part_of_speech": "noun", "dialect": "[C]", "difficulty": "1"},
        {"word": "televizor", "translation": "TV", "part_of_speech": "noun", "dialect": "[B]", "difficulty": "3"}
    ]
    result = filter_by_difficulty(vocab, 3)
    assert len(result) == 1
    assert result[0]["word"] == "televizor"

    result2 = filter_by_difficulty(vocab, 2)  # no matches
    assert result2 == []

def test_search_vocab():
    vocab = [
        {"word": "mačka", "translation": "cat", "part_of_speech": "noun", "dialect": "[S]"},
        {"word": "pas", "translation": "dog", "part_of_speech": "noun", "dialect": "[B]"}
    ]
    result = search_vocab(vocab, "cat")
    assert len(result) == 1
    assert result[0]["word"] == "mačka"

    result2 = search_vocab(vocab, "do")  # partial match
    assert len(result2) == 1

    result3 = search_vocab(vocab, "elephant")  # no match
    assert result3 == []

def test_sort_vocab():
    vocab = [
        {"word": "zrak", "translation": "air", "part_of_speech": "noun", "dialect": "[B]"},
        {"word": "auto", "translation": "car", "part_of_speech": "noun", "dialect": "[C]"},
        {"word": "kuća", "translation": "house", "part_of_speech": "noun", "dialect": "[S]"}
    ]
    result = sort_vocab(vocab)
    assert result[0]["word"] == "auto"
    assert result[-1]["word"] == "zrak"

def test_format_flashcard():
    entry = {
        "word": "voda",
        "translation": "water",
        "part_of_speech": "noun",
        "dialect": "[B]",
        "note": "basic word"
    }
    result = format_flashcard(entry)
    assert "voda" in result
    assert "water" in result
    assert "[B]" in result
    assert "noun" in result
    assert "Note" in result

    # test with no note
    entry2 = {
        "word": "hljeb",
        "translation": "bread",
        "part_of_speech": "noun",
        "dialect": "[B]"
    }
    result2 = format_flashcard(entry2)
    assert "Note" not in result2

if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "--tb=short", "-rN", __file__])
