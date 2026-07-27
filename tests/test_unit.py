import unittest
import os


class TestUnitComponents(unittest.TestCase):
    def test_readme_exists(self):
        repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        readme_path = os.path.join(repo_root, "README.md")
        self.assertTrue(os.path.isfile(readme_path), "README.md should exist")

    def test_readme_not_empty(self):
        repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        readme_path = os.path.join(repo_root, "README.md")
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertGreater(len(content), 0, "README.md should not be empty")


if __name__ == "__main__":
    unittest.main()
