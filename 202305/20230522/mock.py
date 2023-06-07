from unittest.mock import Mock
mock = Mock()
mock
from generator import add_task, view_all_tasks, update_task_status, delete_task

# Pass mock as an argument to do_something()
add_task(mock)

# Patch the json library
json = mock
