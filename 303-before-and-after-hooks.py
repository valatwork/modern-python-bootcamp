''' 
setUp and tearDown

For larger applications, you may want similar application state before running tests
setUp runs before each test method
tearDown runs after each test method
Common use cases: adding/removing data from a test database, creating instances of a class
'''

## example 1

class SomeTests(unittest.TestCase):

    def setUp(self):
        # do setup here
        pass

    def test_first(self):
        # setUp runs before
        # tearDown runs after
        pass

    def test_second(self):
        # setUp runs before
        # tearDown runs after
        pass

    def tearDown(self):
        # do teardown here
        pass
    
    
## robot.py

class Robot:
	def __init__(self, name, battery=100, skills=[]):
		self.name = name
		self.battery = battery
		self.skills = skills

	def charge(self):
		self.battery = 100
		return self

	def say_name(self):
		if self.battery > 0:
			self.battery -= 1
			return f"BEEP BOOP BEEP BOOP.  I AM {self.name.upper()}"
		return "Low power.  Please charge and try again"

	def learn_skill(self, new_skill, cost_to_learn):
		if self.battery >= cost_to_learn:
			self.battery -= cost_to_learn
			self.skills.append(new_skill)
			return f"WOAH. I KNOW {new_skill.upper()}"
		return "Insufficient battery. Please charge and try again"

		
## robot_tests.py

import unittest
from robot import Robot


class RobotTests(unittest.TestCase):
    def setUp(self):
        self.mega_man = Robot("Mega Man", battery=50)

    def test_charge(self):
        self.mega_man.charge()
        self.assertEqual(self.mega_man.battery, 100)

    def test_say_name(self):
        self.assertEqual(
            self.mega_man.say_name(),
            "BEEP BOOP BEEP BOOP.  I AM MEGA MAN")
        self.assertEqual(self.mega_man.battery, 49)


if __name__ == "__main__":
    unittest.main()

