import sys
import os
sys.path.append(os.getcwd())
from services import system
from services.compiler import c_compile,cpp_compile
from services.runner import python_run
import unittest
from pathlib import Path
import shutil

class TestCompiler(unittest.TestCase):
    def setUp(self):
        self.test_folder = Path("test_folder")
        self.test_folder.mkdir(exist_ok=True)

    def tearDown(self):
        for file in self.test_folder.glob("*"):
            file.unlink()
        self.test_folder.rmdir()

    def test_c_compile(self):
        c_file = self.test_folder / "Test.c"
        c_file.write_text("#include <stdio.h>\n int main() { return 0; }")

        exe_file = c_compile(c_file)

        self.assertTrue(Path(exe_file).exists())

    def test_c_compile_error(self):
        c_file = self.test_folder / "Test.cpp"
        c_file.write_text("#include <stdio.h>\n int main() { return 0; }")

        with self.assertRaises(ValueError):
            c_compile(c_file)

    def test_cpp_compile(self):
        cpp_file = self.test_folder / "Test.cpp"
        cpp_file.write_text("#include <iostream>\n int main() { return 0; }")

        exe_file = cpp_compile(cpp_file)

        self.assertTrue(Path(exe_file).exists())

    def test_cpp_compile_error(self):
        cpp_file = self.test_folder / "Test.c"
        cpp_file.write_text("#include <iostream>\n int main() { return 0; }")

        with self.assertRaises(ValueError):
            cpp_compile(cpp_file)

class TestRunner(unittest.TestCase):
    def test_python_run(self):
        program_file = Path("utest/solutions/sysadmin.py")
        intput_data = b'3 4\n5 3 5'
        result = python_run(program_file, intput_data)
        self.assertEqual(result.stdout, b'2\r\n')
        self.assertEqual(result.returncode, 0)

        intput_data = b'11 42\n33 17 42 13 7 5 23 20 1 18 6'
        result = python_run(program_file, intput_data)
        self.assertEqual(result.stdout, b'4\r\n')
        self.assertEqual(result.returncode, 0)

        intput_data = b'3 13\n1 3 7'
        result = python_run(program_file, intput_data)
        self.assertEqual(result.stdout, b'-1\r\n')
        self.assertEqual(result.returncode, 0)

        intput_data = b'11 92\n2 17 1 13 7 5 7 2 1 18 6'
        result = python_run(program_file, intput_data)
        self.assertEqual(result.stdout, b'-1\r\n')
        self.assertEqual(result.returncode, 0)

class TestSystem(unittest.TestCase):
    def setUp(self):
        if not os.path.exists("../program_files"):
            os.mkdir("../program_files")

    def test_system_python(self):
        shutil.copy2("utest/solutions/sysadmin.py", "../program_files/sysadmin.py")
        program_file = Path("../program_files/sysadmin.py")
        problem = "Sysadmin"
        language = "Python"
        output, score = system.system(language, program_file, problem)
        self.assertEqual(score, "100/100")

    def test_system_c(self):
        shutil.copy2("utest/solutions/sysadmin.c", "../program_files/sysadmin.c")
        program_file = Path("../program_files/sysadmin.c")
        problem = "Sysadmin"
        language = "C"
        output, score = system.system(language, program_file, problem)
        self.assertEqual(score, "100/100")

    def test_system_cpp(self):
        shutil.copy2("utest/solutions/sysadmin.cpp", "../program_files/sysadmin.cpp")
        program_file = Path("../program_files/sysadmin.cpp")
        problem = "Sysadmin"
        language = "C++"
        output, score = system.system(language, program_file, problem)
        self.assertEqual(score, "100/100")

if __name__ == '__main__':
    unittest.main()
