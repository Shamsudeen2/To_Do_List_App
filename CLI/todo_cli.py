import sqlite3
import uuid 

conn = sqlite3.connect("todo.db")
cursor = conn.cursor()


cursor.execute("""      
CREATE TABLE IF NOT EXISTS todolist (
   id TEXT PRIMARY KEY,
    text TEXT NOT NULL,
    is_completed INTEGER DEFAULT 0          
)              
""")
conn.commit()

def create(text, **mydata):
    lists_id = str(uuid.uuid4())
    is_completed = mydata.get("is_completed", 0)
 
    cursor.execute(
        "INSERT INTO todolist (id, text, is_completed) VALUES (?, ?, ?)",
        (lists_id, text, is_completed),
    )
    conn.commit()
    return {"id": lists_id, "text": text, "is_completed": is_completed}



def get(paging: int, count: int):
    offset = (paging - 1)* count
    cursor.execute(
        "SELECT id, text, is_completed FROM todolist LIMIT ? OFFSET ?",
        (count, offset),
    )
    rows = cursor.fetchall()
    return rows



def update(lists_id):
    cursor.execute(
        "UPDATE todolist SET is_completed = 1 WHERE id = ?",
        (lists_id,)
    )
    conn.commit()
    return cursor.rowcount > 0



def delete(list_id):
    cursor.execute("DELETE FROM todolist WHERE id = ?", (list_id,))
    conn.commit()
    return cursor.rowcount > 0



def show_menu():
    print("-------- TO-DO LIST APP ---------")
    print("1. Add Task")
    print("2. View Tasks (Paginated)")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")
    print("----------------------------------")



def main():
    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            text = input("Enter task name: ")
            task = create(text)
            print("Task Added:", task)


        elif choice == "2":
            page = int(input("Enter page number (1,2,3...): "))
            count = int(input("How many task per page?: "))
            list_id = get(page, count)

            if not list_id:
                print("No task found.")
            else:
                print("\n--- Tasks Page", page, "---")
                for t in list_id:
                    status = "Done" if t[2] == 1 else "Not done"
                    print(f"ID: {t[0]} | Task: {t[1]} | Status: {status}")

        elif choice == "3":
            list_id = input("Enter Task ID to mark complte")
            if update(list_id):
                print("Task marked as complete.")
            else:
                print("Task not found.")
        
        elif choice == "4":
            list_id = input("Enter Task ID to delete: ")
            if delete(list_id):
                print("Task deleted.")
            else:
               print("Task not found.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")
                         
if __name__ == "__main__":
    main()
        
        
