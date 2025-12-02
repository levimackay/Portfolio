"""
Tests for Password Tracker - CSE 111 Final Project
Author: Levi Mackay
This test file checks the file-logic of the password tracker (not the GUI).
"""
import pytest
from password_tracker import create_password_file, add_password_entry

def test_create_password_file():
    """Test the creation of a new password file with correct header."""
    filename = "test_file_create.txt"
    create_password_file(filename)

    with open(filename, "r") as file:
        lines = file.readlines()
        assert lines[0].strip() == "Password Tracker"
        assert "===" in lines[1]

    # Run it again to make sure it doesn’t overwrite
    create_password_file(filename)
    with open(filename, "r") as file:
        assert "Password Tracker" in file.read()


def test_add_password_entry():
    """Test adding multiple entries to the file."""
    filename = "test_file_add.txt"
    create_password_file(filename)

    add_password_entry(filename, "facebook.com", "levi.fb", "fbpass123")
    add_password_entry(filename, "snapchat.com", "levi.snap", "snap456")

    with open(filename, "r") as file:
        content = file.read()
        assert "facebook.com" in content
        assert "levi.fb" in content
        assert "fbpass123" in content
        assert "snapchat.com" in content
        assert "levi.snap" in content


def test_search_entries():
    """Simulates a search in the password file (manually)."""
    filename = "test_file_search.txt"
    create_password_file(filename)
    add_password_entry(filename, "netflix.com", "leviflix", "stream1")
    add_password_entry(filename, "hulu.com", "levihulu", "stream2")

    # Search manually
    with open(filename, "r") as file:
        lines = file.readlines()

    matches = []
    keyword = "hulu"
    i = 0
    while i < len(lines):
        if keyword in lines[i].lower():
            matches.append(lines[i])
            matches.append(lines[i + 1])
            matches.append(lines[i + 2])
            matches.append(lines[i + 3])
            i += 4
        else:
            i += 1

    result = "".join(matches)
    assert "hulu.com" in result
    assert "levihulu" in result
    assert "stream2" in result


pytest.main(["-v", "--tb=short", "-rN", __file__])
