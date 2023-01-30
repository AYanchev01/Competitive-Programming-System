import subprocess


def python_run(program_file, input_data):
    return subprocess.run(["python", str(program_file)],
                          input=input_data,
                          capture_output=True,
                          shell=True)


def java_run(program_file, input_data):
    classname = program_file.stem
    program_path = program_file.parent
    return subprocess.run(["java", "-classpath", str(program_path), classname],
                          input=input_data,
                          capture_output=True,
                          shell=True)


def c_run(program_file, input_data):
    return subprocess.run([str(program_file)],
                          input=input_data,
                          capture_output=True,
                          shell=True)


def cpp_run(program_file, input_data):
    return subprocess.run([str(program_file)],
                          input=input_data,
                          capture_output=True,
                          shell=True)