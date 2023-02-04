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

    output += f"{problem} | "
    for i, test_case in enumerate(test_cases, 1):
        input_data = "\n".join(test_case["input"]).encode()
        required_output = "\n".join(test_case["output"])
        start_time = time()
        process = languages[language](file_to_run, input_data)
        time_taken = time() - start_time
        actual_output = process.stdout.decode().strip().replace('\r', '')
        if process.returncode == 0 and required_output == actual_output:
            output += "ok "
            if time_taken > test_case["time_limit"]:
                output += f"tl({time_taken:.3f}) "
        else:
            failed_cases += 1
            output += "wa "
            if process.returncode != 0:
                output += "re "

    if file_to_run != program_file:
        os.remove(file_to_run)
    os.remove(program_file)
    os.rmdir(program_file.parent)

    res = (total_cases - failed_cases) * 100 // total_cases
    output += f"( {res}/100 )"

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