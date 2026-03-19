from utils.gap_analysis import find_skill_gap

def test_gap():
    user = ["python"]
    role = ["python", "sql"]

    assert find_skill_gap(user, role) == ["sql"]


def test_empty_resume():
    user = []
    role = ["python"]

    assert find_skill_gap(user, role) == ["python"]
