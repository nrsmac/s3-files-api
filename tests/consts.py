"""Constant values used for tests."""

from pathlib import Path

THIS_DIR = Path(__file__).parent
PROJECT_DIR = (THIS_DIR / "../").resolve()


TEST_BUCKET_NAME = "nrsmac-test-bucket-mlops-club"
TEST_OBJECT_KEY = "test_file.txt"
