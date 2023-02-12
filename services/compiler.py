"""
This file contains the system function which is used to compile the submittions.
"""
import subprocess
from pathlib import Path

"""
This function is used to compile java code.
"""
def java_compile(program_file: Path) -> None:
    if program_file.suffix != ".java":
        raise ValueError("Please use .java extention for java input file")
    subprocess.run(["javac", str(program_file)], check=False)

"""
This function is used to compile C code.
"""
def c_compile(program_file: Path) -> str:
    if program_file.suffix != ".c":
        raise ValueError("Please use .c extention for C input file")
    output_file = program_file.with_suffix(".exe")
    subprocess.run(["gcc", "-O2", str(program_file), "-o", str(output_file)], check=False)
    return str(output_file)

"""
This function is used to compile C++ code.
"""
def cpp_compile(program_file: Path) -> str:
    if program_file.suffix != ".cpp":
        raise ValueError("Please use .cpp extention for C++ input file")
    output_file = program_file.with_suffix(".exe")
    subprocess.run(["g++", "-O2", "-std=c++17",
     str(program_file), "-o", str(output_file)], check=False)
    return str(output_file)
