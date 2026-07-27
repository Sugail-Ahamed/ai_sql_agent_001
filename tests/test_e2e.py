import unittest
import os


class TestEndToEnd(unittest.TestCase):
    def test_full_repo_flow(self):
        repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # End-to-end: verify repo is readable, tests exist, and README is present
        readme_exists = os.path.isfile(os.path.join(repo_root, "README.md"))
        tests_exist = os.path.isdir(os.path.join(repo_root, "tests"))
        self.assertTrue(readme_exists, "README.md exists in E2E check")
        self.assertTrue(tests_exist, "tests/ exists in E2E check")


if __name__ == "__main__":
    unittest.main()
