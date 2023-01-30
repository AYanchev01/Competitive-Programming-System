from time import time
import json
import pathlib
import os
from compiler import (
    java_compile,
    c_compile,
    cpp_compile
)
from runner import (
    python_run,
    java_run,
    c_run,
    cpp_run
)

def system(language, program_file, problem):
    
    output = ""
    program_file = pathlib.Path(program_file).resolve()

    if problem == "Palindrome":
        with open("cps/testcases/palindrome.json", "r") as f:
            test_cases = json.load(f)
    elif problem == "Sysadmin":
        with open("cps/testcases/sysadmin.json", "r") as f:
            test_cases = json.load(f)
    elif problem == "One more sequence":
        with open("cps/testcases/one_more_sequence.json", "r") as f:
            test_cases = json.load(f)
    else:
        raise ValueError(f"Invalid problem name {problem}")
    

    file_to_run = compile(program_file, language)
    total_cases = len(test_cases)
    failed_cases = 0
    languages = {
        "Python": python_run,
        "Java": java_run,
        "C": c_run,
        "C++": cpp_run
    }

    for i, test_case in enumerate(test_cases, 1):
        input_data = "\n".join(test_case["input"]).encode()
        required_output = "\n".join(test_case["output"])
        start_time = time()
        process = languages[language](file_to_run, input_data)
        time_taken = time() - start_time
        actual_output = process.stdout.decode().strip().replace('\r', '')
        if process.returncode == 0 and required_output == actual_output:
            output += f"Test Case {i} Passed and took {time_taken:.3f} seconds\n"
        else:
            failed_cases += 1
            output += f"Test Case {i} Failed\n"
            if process.returncode == 0:
                output += f"Required Output:\n{required_output}\n---------------\n"
                output += f"Actual Output:\n{actual_output}\n---------------\n(took {time_taken:.3f} seconds)\n"
            else:
                output += "---------------\n"
                output += f"Runtime Error: (took {time_taken:.3f} seconds)\n"
                output += process.stderr.decode().strip()
                output += "\n---------------\n\n"

    os.remove(file_to_run)
    os.remove(program_file)
    os.rmdir(program_file.parent)

    if failed_cases == 0:
        output += "All tests passed successfully."
    else:
        output += f"{failed_cases}/{total_cases} Test Cases Failed"

    return output

def compile(program_file, language):
    file_to_run = program_file
    if language == "Java":
        java_compile(program_file)
        file_to_run = program_file.with_suffix(".class")
    elif language == "C":
        file_to_run = c_compile(program_file)
    elif language == "C++":
        file_to_run = cpp_compile(program_file)

    return file_to_run