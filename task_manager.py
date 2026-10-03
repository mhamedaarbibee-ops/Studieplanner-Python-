from storage import tasks, save_tasks


def add_task():
    name = input("Voer taaknaam in: ").strip()
    deadline = input("Voer deadline in (bijv. 10-10-2026): ").strip()

    if not name:
        print("Taaknaam mag niet leeg zijn.")
        return
    if not deadline:
        print("Deadline mag niet leeg zijn.")
        return

    task = {
        "name": name,
        "deadline": deadline,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Taak toegevoegd.")


def view_tasks():
    if not tasks:
        print("Geen taken gevonden.")
        return

    # Sorteer op deadline (eenvoudig, alfabetisch)
    sorted_tasks = sorted(tasks, key=lambda t: t["deadline"])

    print("\n--- Takenlijst ---")
    for index, task in enumerate(sorted_tasks, start=1):
        status = "✅ Voltooid" if task["completed"] else "⏳ Open"
        print(f"{index}. {task['name']} | Deadline: {task['deadline']} | {status}")


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("Welke taak is voltooid? ")) - 1

        # Omdat we sorteren, moeten we de echte taak terugvinden
        sorted_tasks = sorted(tasks, key=lambda t: t["deadline"])
        
        if 0 <= task_number < len(sorted_tasks):
            # Zoek de echte taak in de originele lijst
            selected = sorted_tasks[task_number]
            selected["completed"] = True
            save_tasks(tasks)
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

        sorted_tasks = sorted(tasks, key=lambda t: t["deadline"])

        if 0 <= task_number < len(sorted_tasks):
            selected = sorted_tasks[task_number]
            tasks.remove(selected)          # verwijder de echte taak
            save_tasks(tasks)
            print(f"'{selected['name']}' verwijderd.")
        else:
            print("Ongeldig taaknummer.")

    except ValueError:
        print("Voer een geldig nummer in.")


def show_statistics():
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    open_tasks = total - completed

    print("\n--- Overzicht ---")
    print(f"Totaal aantal taken : {total}")
    print(f"Openstaande taken  : {open_tasks}")
    print(f"Voltooide taken    : {completed}")