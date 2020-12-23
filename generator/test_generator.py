import unittest
from generator.generator_md import Generator

EXPECTED_MD = '''# test

+ [Name of a task](#name_of_a_task)

## Name of a task

https://leetcode.com/problems/


```python
class Solution:
    solution```

'''


class TestGenerator(unittest.TestCase):

    def test_create_pretty_link(self):
        generator = Generator('test/test_file.txt')
        generator.names = ["this is_A test ExaMple"]
        result = generator.create_pretty_link(generator.names[0])
        self.assertEqual('this_is_a_test_example', result)

    def test_read_input(self):
        generator = Generator('test/test_file.txt')
        generator.read_input()
        actual_result = [generator.names, generator.urls, generator.sources]
        expected_result = [['Name of a task'], ['https://leetcode.com/problems/\n'],
                           [['class Solution:\n', '    solution']]]
        self.assertEqual(expected_result, actual_result)

    def test_compose(self):
        generator = Generator('test/test_file.txt')
        generator.read_input()
        generator.compose()
        self.assertEqual(EXPECTED_MD, generator.content)

    def test_read_md(self):
        generator = Generator('test/test.md')
        generator.read_md()
        actual_names = generator.names
        expected_names = ['Name of a task']
        actual_urls = generator.urls
        expected_urls = ['https://leetcode.com/problems/\n']
        actual_sources = generator.sources
        expected_sources = [['class Solution:\n', '    solution\n']]
        self.assertEqual(expected_names, actual_names)
        self.assertEqual(expected_urls, actual_urls)
        self.assertEqual(expected_sources, actual_sources)
