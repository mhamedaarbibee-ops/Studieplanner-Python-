from task_manager import (
    add_task,
    view_tasks,
    complete_task,
    delete_task,
    show_statistics,
)

def menu():
    while True:
        print("\n=== STUDIEPLANNER ===")
        print("1. Taak toevoegen")
        print("2. Taken bekijken")
        print("3. Taak afronden")
        print("4. Taak verwijderen")
        print("5. Overzicht bekijken")
        print("6. Afsluiten")

        choice = input("Maak een keuze: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            show_statistics()
        elif choice == "6":
            print("Programma afgesloten.")
            break
        else:
            print("Ongeldige keuze.")

if __name__ == "__main__":
    menu()