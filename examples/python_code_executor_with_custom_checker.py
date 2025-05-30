import json
import os

from rich import print_json

from arbiterx import CodeExecutor, Constraints


class PythonCodeExecutor(CodeExecutor):
    def get_compile_command(self, src: str) -> str:
        return ""

    def get_run_command(self, src: str) -> str:
        return f"python3 {src}/solution_mixed_cases.py"


if __name__ == "__main__":
    constraints: Constraints = {
        "time_limit": 2,
        "memory_limit": 10,
        "memory_swap_limit": 0,  # No swap
        # Let's say we want to limit the CPU usage to 1 core (100%)
        "cpu_quota": 1000000,
        "cpu_period": 1000000,
    }
    WORK_DIR = os.path.join(os.getcwd(), "data", "python-submission-with-custom-checker")
    with PythonCodeExecutor(
            user="sandbox",
            docker_image="python312:v1",
            src=os.path.join(WORK_DIR),
            constraints=constraints,
            disable_compile=True,
    ) as executor:
        for result in executor.run(checker=os.path.join(WORK_DIR, "custom_checker.py")):
            print_json(json.dumps(result), indent=4)
