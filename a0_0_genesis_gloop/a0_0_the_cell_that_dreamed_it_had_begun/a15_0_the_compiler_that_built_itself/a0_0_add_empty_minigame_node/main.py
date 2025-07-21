# a0_0_add_empty_minigame_node/main.py

import os
import datetime

def add_empty_minigame_node(base_path, minigame_name):
    """
    Creates an empty minigame folder structure at the specified base path.

    Args:
        base_path (str): The parent directory where the minigame folder will be created.
        minigame_name (str): The name of the new minigame folder (e.g., a12_0_the_new_minigame).

    Returns:
        dict: Confirmation dictionary with status, trace log, and paths created.
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
    created_paths.extend([minigame_path, taskmaps_path])

    # Create files with canonical placeholder content
    for file_path in files_to_create:
        with open(file_path, 'w', encoding='utf-8') as f:
            if file_path.endswith('.py'):
                f.write("# AUTO-GENERATED PLACEHOLDER\n")
            elif file_path.endswith('.md'):
                f.write("<!-- AUTO-GENERATED PLACEHOLDER: {} -->\n".format(os.path.basename(file_path)))
        created_paths.append(file_path)

    # Generate recursive trace log
    trace_log = {
        "event": "add_empty_minigame_node",
        "minigame": minigame_name,
        "paths_created": created_paths,
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
    }

    return {
        "status": "success",
        "minigame": minigame_name,
        "paths_created": created_paths,
        "trace": trace_log
    }

# Note: __main__ block omitted intentionally.
# This module is designed to be called by workflow_compiler.py in a15_0_the_compiler_that_built_itself
