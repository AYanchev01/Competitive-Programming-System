import subprocess

def java_compile(program_file):
    if program_file.suffix != ".java":
        raise ValueError("Please use .java extention for java input file")
    subprocess.run(["javac", str(program_file)])


def c_compile(program_file):
    if program_file.suffix != ".c":
        raise ValueError("Please use .c extention for C input file")
    output_file = program_file.with_suffix(".exe")
    subprocess.run(["gcc", "-O2", "-std=c++17", str(program_file), "-o", str(output_file)])
    return str(output_file)


def cpp_compile(program_file):
    if program_file.suffix != ".cpp":
        raise ValueError("Please use .cpp extention for C++ input file")
    output_file = program_file.with_suffix(".exe")
    subprocess.run(["g++", "-O2", "-std=c++17", str(program_file), "-o", str(output_file)])
    return str(output_file)
