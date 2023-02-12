import sys
import os
sys.path.append(os.getcwd())
from services import system
from services.compiler import c_compile,cpp_compile
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


class TestSystem(unittest.TestCase):
    def setUp(self):
        if not os.path.exists("../program_files"):
            os.mkdir("../program_files")

    def test_system_python(self):
        shutil.copy2("utest/sysadmin.py", "../program_files/sysadmin.py")
        program_file = Path("../program_files/sysadmin.py")
        problem = "Sysadmin"
        language = "Python"
        output, score = system.system(language, program_file, problem)
        self.assertEqual(score, "100/100")

    def test_system_c(self):
        shutil.copy2("utest/sysadmin.c", "../program_files/sysadmin.c")
        program_file = Path("../program_files/sysadmin.c")
        problem = "Sysadmin"
        language = "C"
        output, score = system.system(language, program_file, problem)
        self.assertEqual(score, "100/100")

    def test_system_cpp(self):
        shutil.copy2("utest/sysadmin.cpp", "../program_files/sysadmin.cpp")
        program_file = Path("../program_files/sysadmin.cpp")
        problem = "Sysadmin"
        language = "C++"
        output, score = system.system(language, program_file, problem)
        self.assertEqual(score, "100/100")

if __name__ == '__main__':
    unittest.main()
