#Task1
from function_homework import say_hello

say_hello("Alex")
say_hello("Bob")

#Task2
import sys
print(sys.path)

import sys
sys.path.append(r"C:\\Users\\aleks\\PycharmProjects\\PY-Course-Victor-Nikoriak-23_02\\assignments\\Homework_09\my_module")

import my_module
my_module.hello()

import my_mod

my_mod.count_lines("my_mod.py")
my_mod.count_chars("my_mod.py")
my_mod.test("my_mod.py")