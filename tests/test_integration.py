import unittest
import os
import sys

# Ensure repo root is importable
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestIntegration(unittest.TestCase):
    def test_repo_directory_structure(self):
        repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.assertTrue(os.path.isdir(os.path.join(repo_root, "tests")))
        self.assertTrue(os.path.isfile(os.path.join(repo_root, "README.md")))

    def test_tests_directory_has_tests(self):
        tests_dir = os.path.dirname(os.path.abspath(__file__))
        test_files = [f for f in os.listdir(tests_dir) if f.startswith("test_") and f.endswith(".py")]
        self.assertGreaterEqual(len(test_files), 1, "There should be at least one test file")


if __name__ == "__main__":
    unittest.main()
