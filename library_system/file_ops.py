"""
Simple file operations for library system using txt files.
Uses basic read, write, open, and append operations.
"""


def read_file(filename):
    """Read all lines from a txt file. Returns empty list if file doesn't exist."""
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []


def write_file(filename, data):
    """Write data to file (overwrites existing content). data should be a list of strings."""
    try:
        with open(filename, 'w') as file:
            file.writelines(data)
        return True
    except Exception as e:
        print(f"Error writing to {filename}: {e}")
        return False


def append_file(filename, line):
    """Append a single line to file."""
    try:
        with open(filename, 'a') as file:
            if not line.endswith('\n'):
                line += '\n'
            file.write(line)
        return True
    except Exception as e:
        print(f"Error appending to {filename}: {e}")
        return False


def pop_line(filename, index):
    """Remove a line at given index from file."""
    try:
        lines = read_file(filename)
        if 0 <= index < len(lines):
            lines.pop(index)
            write_file(filename, lines)
            return True
        return False
    except Exception as e:
        print(f"Error removing from {filename}: {e}")
        return False


def remove_by_value(filename, search_term):
    """Remove all lines containing search_term from file."""
    try:
        lines = read_file(filename)
        lines = [line for line in lines if search_term not in line]
        write_file(filename, lines)
        return True
    except Exception as e:
        print(f"Error removing from {filename}: {e}")
        return False


def clear_file(filename):
    """Clear entire file."""
    try:
        write_file(filename, [])
        return True
    except Exception as e:
        print(f"Error clearing {filename}: {e}")
        return False
