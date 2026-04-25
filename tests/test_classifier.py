import sys
import os

sys.path.insert(0, os.path.abspath("src"))

from app import classify_path


def test_happy_path_normal_request():
    assert classify_path("/") == "NORMAL"


def test_negative_path_admin_request():
    assert classify_path("/admin") == "SUSPICIOUS"


def test_edge_case_uppercase_admin():
    assert classify_path("/ADMIN") == "SUSPICIOUS"


def test_edge_case_nested_admin_path():
    assert classify_path("/login/admin/settings") == "SUSPICIOUS"