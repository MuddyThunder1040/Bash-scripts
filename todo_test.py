from todo import add_task_logic, delete_task_logic, update_task_logic


# ================== Tests for Adding Tasks ==================

def test_add_task_success():
    tasks = []
    result = add_task_logic(tasks, "Learn Python")
    assert result is True
    assert tasks == ["Learn Python"]


def test_add_task_empty():
    tasks = []
    result = add_task_logic(tasks, "   ")
    assert result is False
    assert tasks == []


# ================== Tests for Deleting Tasks ==================

def test_delete_task_success():
    tasks = ["Task 1", "Task 2", "Task 3"]
    removed = delete_task_logic(tasks, 1)  # Remove "Task 2"
    assert removed == "Task 2"
    assert tasks == ["Task 1", "Task 3"]


def test_delete_task_invalid_index():
    tasks = ["Task 1"]
    removed = delete_task_logic(tasks, 5)  # Invalid index
    assert removed is None
    assert tasks == ["Task 1"]


def test_delete_task_negative_index():
    tasks = ["Task 1"]
    removed = delete_task_logic(tasks, -1)  # Negative index invalid
    assert removed is None
    assert tasks == ["Task 1"]


# ================== Tests for Updating Tasks ==================

def test_update_task_success():
    tasks = ["Task 1", "Task 2"]
    result = update_task_logic(tasks, 1, "Updated Task 2")
    assert result == ("Task 2", "Updated Task 2")
    assert tasks == ["Task 1", "Updated Task 2"]


def test_update_task_invalid_index():
    tasks = ["Task 1"]
    result = update_task_logic(tasks, 3, "New Task")
    assert result is None
    assert tasks == ["Task 1"]


def test_update_task_empty_new_value():
    tasks = ["Task 1", "Task 2"]
    result = update_task_logic(tasks, 1, "  ")  # Empty new task
    assert result is None
    assert tasks == ["Task 1", "Task 2"]
