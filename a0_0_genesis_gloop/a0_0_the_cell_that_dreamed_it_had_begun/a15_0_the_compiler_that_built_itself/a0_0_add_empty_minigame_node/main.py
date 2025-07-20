# a0_0_add_empty_minigame_node/main.py

import os

def add_empty_minigame_node(base_path, minigame_name):
    """
    Creates an empty minigame folder structure at the specified base path.

    Args:
        base_path (str): The parent directory where the minigame folder will be created.
        minigame_name (str): The name of the new minigame folder (e.g., a12_0_the_new_minigame).

    Returns:
        dict: Confirmation dictionary with paths created.
    """
    created_paths = []

    minigame_path = os.path.join(base_path, minigame_name)
    taskmaps_path = os.path.join(minigame_path, 'taskmaps')

    # Define target files
    files_to_create = [
        os.path.join(minigame_path, '__init__.py'),
        os.path.join(minigame_path, 'main.py'),
        os.path.join(taskmaps_path, 'taskmap.md'),
        os.path.join(taskmaps_path, 'README.md'),
        os.path.join(taskmaps_path, 'milestones.md'),
    ]

    # Create folders
    os.makedirs(taskmaps_path, exist_ok=True)
    created_paths.append(minigame_path)
    created_paths.append(taskmaps_path)

    # Create files with placeholder content
    for file_path in files_to_create:
        with open(file_path, 'w', encoding='utf-8') as f:
            if file_path.endswith('.py'):
                f.write("# Empty scaffold\n")
            elif file_path.endswith('.md'):
                f.write("# Placeholder for {}\n".format(os.path.basename(file_path)))
        created_paths.append(file_path)

    return {
        "status": "success",
        "minigame": minigame_name,
        "paths_created": created_paths
    }

if __name__ == "__main__":
    # Example usage (can be adjusted in practice)
    result = add_empty_minigame_node("./generated_minigames", "a12_0_example_minigame")
    for path in result["paths_created"]:
        print(f"Created: {path}")
