from storage import tasks


def add_task():
    name = input("Voer taaknaam in: ").strip()
    deadline = input("Voer deadline in: ").strip()

    if not name:
        print("Taaknaam mag niet leeg zijn.")
        return

    task = {
        "name": name,
        "deadline": deadline,
        "completed": False
    }

    tasks.append(task)
    print("Taak toegevoegd.")


def view_tasks():
    if not tasks:
        print("Geen taken gevonden.")
        return

    print("\n--- Takenlijst ---")
    for index, task in enumerate(tasks, start=1):
        status = "Voltooid" if task["completed"] else "Open"
        print(f"{index}. {task['name']} | Deadline: {task['deadline']} | {status}")


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("Welke taak is voltooid? ")) - 1

        if 0 <= task_number < len(tasks):
            tasks[task_number]["completed"] = True
            print("Taak gemarkeerd als voltooid.")
        else:
            print("Ongeldig taaknummer.")

    except ValueError:
        print("Voer een geldig nummer in.")


def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("Welke taak wil je verwijderen? ")) - 1

        if 0 <= task_number < len(tasks):
            removed = tasks.pop(task_number)
            print(f"'{removed['name']}' verwijderd.")
        else:
            print("Ongeldig taaknummer.")

    except ValueError:
        print("Voer een geldig nummer in.")


def show_statistics():
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    open_tasks = total - completed

    print("\n--- Overzicht ---")
    print(f"Totaal aantal taken: {total}")
    print(f"Openstaande taken: {open_tasks}")
    print(f"Voltooide taken: {completed}")