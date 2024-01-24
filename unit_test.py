from circular_queue import CircularQueue
from password_checker import PassWordChecker
from word_frequency import WordFrequency
import unittest
from main_runner import word_frequency_example, circular_queue_example, password_checker_example


def word_frequency_example():
    wf = WordFrequency()
    return wf.word_frequency("which is better python 2 or python 3")

def circular_queue_example():
    cq = CircularQueue(5)
    states = []
    for i in range(6):
        cq.enqueue(i)
        states.append(cq.display())  # Assuming display() returns the state
    for _ in range(3):
        cq.dequeue()
        states.append(cq.display())  # Assuming display() returns the state
    return states

def password_checker_example():
    input_passwords = "Abc@1,HelloWorld,Pass123#,A1b2C3#"
    return PassWordChecker.check_password_validity(input_passwords)

class TestMainRunner(unittest.TestCase):

    def test_word_frequency_example(self):
        # Test the word_frequency_example function
        result = word_frequency_example()
        self.assertIsInstance(result, dict)  # Check if the result is a dictionary

    def test_circular_queue_example(self):
        # Test the circular_queue_example function
        result = circular_queue_example()
        self.assertIsInstance(result, list)  # Check if the result is a list

    def test_password_checker_example(self):
        # Test the password_checker_example function
        result = password_checker_example()
        self.assertIn("Abc@1", result)  # Check if "Abc@1" is in the valid passwords list

if __name__ == '__main__':
    unittest.main()
