import sys
import os
sys.path.append(os.getcwd())
from services import system
import unittest
import pathlib
import shutil

class TestSystem(unittest.TestCase):
    def setUp(self):
        shutil.copy2("utests/sysadmin.cpp", "../program_files/sysadmin.cpp")
        shutil.copy2("utests/sysadmin.c", "../program_files/sysadmin.c")
        shutil.copy2("utests/sysadmin.py", "../program_files/sysadmin.py")

    def test_system_python(self):
        program_file = pathlib.Path("../program_files/sysadmin.py")
        problem = "Sysadmin"
        language = "Python"
        output, score = system.system(language, program_file, problem)
        self.assertEqual(score, "100/100")

    def test_system_c(self):
        program_file = pathlib.Path("../program_files/sysadmin.c")
        problem = "Sysadmin"
        language = "C"
        output, score = system.system(language, program_file, problem)
        self.assertEqual(score, "100/100")

    def test_system_cpp(self):
        program_file = pathlib.Path("../program_files/sysadmin.cpp")
        problem = "Sysadmin"
        language = "C++"
        output, score = system.system(language, program_file, problem)
        self.assertEqual(score, "100/100")

if __name__ == '__main__':
    unittest.main()
