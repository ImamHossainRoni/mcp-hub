from mcp.server.fastmcp import FastMCP
import os

# Create an MCP server
mcp = FastMCP("AI Sticky Notes")
# NOTES_FILE = 'notes.txt'
NOTES_FILE = '/notes.txt'


def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'w') as f:
            f.write("")


@mcp.tool()
def add_note(message: str) -> str:
    """
    Append a new note to the sticky note file.

    Args:
        message (str): The note content to be added.

    Returns:
        str: Confirmation message indicating the note was saved.
    """
    ensure_file()
    with open(NOTES_FILE, "a") as f:
        f.write(message + "\n")
    return "Notes Saved!"


@mcp.tool()
def read_latest_notes():
    """
    Get the most recently added note from the sticky note file.

    Returns:
       str: The last note entry. If no notes exist, a default message is returned.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        lines = f.readlines()
    return lines[-1].strip() if lines else "No notes yet."


@mcp.tool()
def read_all_notes():
    """
    Get the all added note from the sticky note file.

    Returns:
       str: The all note entry. If no notes exist, a default message is returned.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        lines = f.readlines()
    if not lines:
        return "No notes yet."
    notes = ""
    for note in lines:
        notes += "=>" + note.strip() + "\n"

    return notes


@mcp.tool()
def delete_note(total_num: int) -> bool:
    """
    Get the all added note from the sticky note file.

    Returns:
        bool: returns True if the notes are deleted else False.
    """
    ensure_file()
    with open(NOTES_FILE, 'r') as file:
        notes = file.readlines()

    if total_num > len(notes):
        print(f"Only {len(notes)} notes available, cannot delete {total_num}")
        return False
    remaining_notes = notes[:-total_num]

    # Write remaining notes back to file
    with open(NOTES_FILE, 'w') as file:
        file.writelines(remaining_notes)

    print(f"Successfully deleted {total_num} note(s)")
    return True
