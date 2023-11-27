import os
import sys


# COMMIT_PATTERN = re.compile(r'^(\w*):\s*(.*?)?:\s*(.*?)\s*(\(#(\d+)\))?$')

def set_output(name: str, value: str) -> None:
    file_path = os.getenv("GITHUB_OUTPUT", None)
    if file_path:
        with open(file_path, "a") as file:
            file.write(f"{name}={value}")
    else:
        sys.stdout.write(f"set output {name}={value}" + os.linesep)
