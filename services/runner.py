"""
This file contains the system function which is used to run the submittions.
"""
import subprocess
from pathlib import Path
from typing import Tuple

"""
This function is used to run python code.
"""
def python_run(program_file: Path, input_data: str) -> Tuple[subprocess.CompletedProcess, str, str]:
    return subprocess.run(["python", str(program_file)],
                          input=input_data,
                          capture_output=True,
                          shell=True,
                          check=False)

"""
This function is used to run java code.
"""
def java_run(program_file: Path, input_data: str) -> Tuple[subprocess.CompletedProcess, str, str]:
    classname = program_file.stem
    program_path = program_file.parent
    return subprocess.run(["java", "-classpath", str(program_path), classname],
                          input=input_data,
                          capture_output=True,
                          shell=True,
                          check=False)

"""
This function is used to run C code.
"""
def c_run(program_file: Path, input_data: str) -> Tuple[subprocess.CompletedProcess, str, str]:
    return subprocess.run([str(program_file)],
                          input=input_data,
                          capture_output=True,
                          shell=True,
                          check=False)

"""
This function is used to run C++ code.
"""
def cpp_run(program_file: Path, input_data: str) -> Tuple[subprocess.CompletedProcess, str, str]:
    return subprocess.run([str(program_file)],
                          input=input_data,
                          capture_output=True,
                          shell=True,
                          check=False)
