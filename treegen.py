import os
import re
import sys

def clean_line(line):
    line = line.replace('├──', '').replace('└──', '').replace('│', '')
    line = line.replace('─', '')  # Remove horizontal lines too
    line = line.strip()
    line = re.split(r'\s?#', line)[0].rstrip()
    return line

def get_indent_level(line):
    # Count leading tree symbols and spaces (every 4 spaces or a tree symbol is a level)
    count = 0
    i = 0
    while i < len(line):
        if line[i] in (' ', '│', '├', '└'):
            count += 1
            i += 1
        else:
            break
    # Each 4 spaces or symbol is a level (since tree lines are 4 chars wide)
    return count // 4

def parse_structure_file(filename):
    import os

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    root_dir = None
    stack = []  # Each element: (indent_level, path)

    for raw_line in lines:
        if raw_line.strip() == '' or raw_line.strip().startswith('#'):
            continue

        indent_level = get_indent_level(raw_line)
        line = clean_line(raw_line)
        if not line:
            continue

        # Detect root directory from the first directory line (even with tree symbols)
        if root_dir is None and line.endswith('/'):
            root_dir = line.rstrip('/')
            os.makedirs(root_dir, exist_ok=True)
            stack = [(0, root_dir)]
            continue

        # If line is a full path (starts with root_dir), use as is
        if root_dir and line.startswith(root_dir + '/'):
            full_path = line.rstrip('/')
            if full_path.endswith('.py') or '.' in os.path.basename(full_path):
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                with open(full_path, 'w', encoding='utf-8') as file:
                    file.write('')
            else:
                os.makedirs(full_path, exist_ok=True)
            continue

        # Directory (tree/flat style)
        if line.endswith('/') or '.' not in os.path.basename(line):
            while stack and stack[-1][0] >= indent_level:
                stack.pop()
            parent_dir = stack[-1][1] if stack else root_dir
            dir_path = os.path.join(parent_dir, line.rstrip('/'))
            os.makedirs(dir_path, exist_ok=True)
            stack.append((indent_level, dir_path))
        else:
            # File (tree/flat style)
            parent_dir = stack[-1][1] if stack else root_dir
            file_path = os.path.join(parent_dir, line)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write('')


def main():
    if len(sys.argv) != 2:
        print("Usage: treegen.py <structure-file.txt>")
        sys.exit(1)

    structure_file = sys.argv[1]
    if not os.path.exists(structure_file):
        print(f"File '{structure_file}' not found.")
        sys.exit(1)

    parse_structure_file(structure_file)
    print(f"\n✅ Structure created from '{structure_file}'")

if __name__ == "__main__":
    main()
