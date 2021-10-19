
# You can auto-discover and run all tests with this command:

#    py.test

# Documentation: https://docs.pytest.org/en/latest/
import pytest
from src import main


# write failing test
# run and fail test
# write real code in main.py to pass the test
# run and pass test
# refactor the code


class TestSumOfTwoNumbers:
    # def test_hello_world(self):

    #     assert main.returns_two() == 2

    # write a function that returns the sum of two numbers
    # #1 write a failing test - a test where you input two numbers, and the assertion is that the output should be the sum of both of the numbers (but its NOT).

    # sum_of_two_numbers

    def test_two_and_two_is_four(self):
        first_num = 2
        second_num = 2

        assert main.sum_of_two_numbers(first_num, second_num) == 4

    def test_three_3_and_seven_is_10(self):
        first_num = 3
        second_num = 7

        assert main.sum_of_two_numbers(
            first_num, second_num) == first_num + second_num
