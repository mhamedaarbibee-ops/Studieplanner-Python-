import flet as ft
import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return []
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def main(page: ft.Page):
    page.title = "Studieplanner"
    page.window.width = 600
    page.window.height = 700
    page.padding = 20

    tasks = load_tasks()

    tasks_column = ft.Column(
        spacing=10,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )

    task_input = ft.TextField(label="Taak", width=250)

    deadline_input = ft.TextField(label="Deadline (dd-mm-jjjj)", width=180)

    priority_input = ft.Dropdown(
        label="Prioriteit",
        width=150,
        options=[
            ft.DropdownOption("Hoog"),
            ft.DropdownOption("Normaal"),
            ft.DropdownOption("Laag"),
        ],
        value="Normaal",
    )

    def refresh_tasks():
        tasks_column.controls.clear()

        for index, task in enumerate(tasks):

            def make_checkbox(i):
                def on_change(e):
                    tasks[i]["done"] = e.control.value
                    save_tasks(tasks)
                return on_change

            def make_delete(i):
                def on_click(e):
                    tasks.pop(i)
                    save_tasks(tasks)
                    refresh_tasks()
                return on_click

            taaktekst = (
                f"{task['text']} | "
                f"Deadline: {task.get('deadline', '')} | "
                f"Prioriteit: {task.get('priority', 'Normaal')}"
            )

            tasks_column.controls.append(
                ft.Row(
                    controls=[
                        ft.Checkbox(
                            label=taaktekst,
                            value=task["done"],
                            on_change=make_checkbox(index),
                            expand=True,
                        ),
                        ft.IconButton(
                            icon=ft.Icons.DELETE,
                            on_click=make_delete(index),
                        ),
                    ]
                )
            )

        page.update()

    def add_task(e):
        text = task_input.value.strip()

        if text:
            tasks.append(
                {
                    "text": text,
                    "deadline": deadline_input.value,
                    "priority": priority_input.value,
                    "done": False,
                }
            )

            save_tasks(tasks)

            task_input.value = ""
            deadline_input.value = ""
            priority_input.value = "Normaal"

            refresh_tasks()
            page.update()

    page.add(
        ft.Text("Studieplanner", size=30, weight=ft.FontWeight.BOLD),
        ft.Row(controls=[task_input, deadline_input, priority_input]),
        ft.Button(
            "Taak toevoegen",
            icon=ft.Icons.ADD,
            on_click=add_task,
        ),
        ft.Divider(),
        ft.Text("Taken", size=20, weight=ft.FontWeight.W_500),
        tasks_column,
    )

    refresh_tasks()


ft.run(main)

