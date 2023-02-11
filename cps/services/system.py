"""
This file contains the logic for the system.
It compiles, runs and checks the submittions.
"""
from time import time
import json
import pathlib
import os
from typing import Union,Tuple

from services.compiler import java_compile, c_compile, cpp_compile
from services.runner import python_run, java_run, c_run, cpp_run

"""
Main function of the system.
"""
def system(language: str, program_file: str, problem: str) -> Tuple[str, str]:

    output = ""
    program_file = pathlib.Path(program_file).resolve()

    if problem == "Palindrome":
        with open("cps/testcases/palindrome.json", "r", encoding="utf8") as file:
            test_cases = json.load(file)
    elif problem == "Sysadmin":
        with open("cps/testcases/sysadmin.json", "r", encoding="utf8") as file:
            test_cases = json.load(file)
    elif problem == "One more sequence":
        with open("cps/testcases/one_more_sequence.json", "r", encoding="utf8") as file:
            test_cases = json.load(file)
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
            output += "ok "
            if time_taken > test_case["time_limit"]:
                output += f"tl({time_taken:.3f}) "
        else:
            failed_cases += 1
            if process.returncode == 0:
                output += "wa "
            else:
                output += "re "

    if os.path.exists(file_to_run) and file_to_run != program_file:
        os.remove(file_to_run)
    os.remove(program_file)
    os.rmdir(program_file.parent)

    res = (total_cases - failed_cases) * 100 // total_cases
    score = f"{res}/100"

    return output, score

"""
This function compiles the program file.
"""
def compile(program_file: pathlib.Path, language: str) -> (pathlib.Path | str):
    file_to_run = program_file
    if language == "Java":
        java_compile(program_file)
        file_to_run = program_file.with_suffix(".class")
    elif language == "C":
        file_to_run = c_compile(program_file)
    elif language == "C++":
        file_to_run = cpp_compile(program_file)

    return file_to_run
