''' Test 2 - 817 - https://chat.openai.com/share/132f9bdd-f09c-4ffa-ae80-28c04d5fc484 '''

rsync_command = [
    "rsync", "-abP", "--delete", "--delete-excluded"
]

if previous_version_path is not None:
    rsync_command.append("--link-dest=" + previous_version_path)

rsync_command.extend([source_path, current_version_path])
