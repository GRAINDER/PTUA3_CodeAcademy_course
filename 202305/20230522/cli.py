from generator import add_task, view_all_tasks, update_task_status, delete_task
from typing import Dict, Any, List
import random
import string
import argparse
from datetime import datetime
from pymongo import MongoClient

def display_tasks(tasks: List[Dict[str, Any]]) -> None:
    print("TASKS:")
    for task in tasks:
        print(f"ID: {task['_id']}")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Status: {task.get('status', 'N/A')}")
        print("------------------------")

def add_task_cli() -> None:
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = {'title': title, 'description': description}
    task_id = add_task(task)
    print(f"Task added with ID: {task_id}")

def view_all_tasks_cli() -> None:
    tasks = view_all_tasks()
    display_tasks(tasks)

def update_task_status_cli() -> None:
    task_id = input("Enter task ID: ")
    status = input("Enter task status: ")
    count = update_task_status(task_id, status)
    print(f"{count} task(s) updated")

def delete_task_cli() -> None:
    task_id = input("Enter task ID: ")
    count = delete_task(task_id)
    print(f"{count} task(s) deleted")


