# To_Do_List_App

*To-Do List App*
Create, edit, delete, and mark tasks complete

*What you'll learn:* CRUD Operations, Persistence data, CLI/UI design, & basic file operation.

 *Instructions:*
-  `create(text: str, **kwargs) -> Task:` This operation will accept one argument `text` as the task name, `**kwargs` for optional task info like `is_completed`, it returns the created task class instance.
- `get(paging: int, count: int) -> list[Task]:` this will read the tasks from storage parse them and returns the list of tasks. The `paging` arg is for pagination (i.e., 1, 2, 3, 4, ...), and the `count` is the maximum number of tasks to get.
- `update(task_id) -> bool` this will update the task having ID `task_id` will return true if task is found and updated, while false if not found.
- `delete(task_id) -> bool:` This will delete the task and return true or false if task is not found.

You should implement it as a CLI app first, then use tkinter for the GUI app.

> *Hint:* You can use the `sqlite` and `uuid` libs