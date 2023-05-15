# Build4SDG 2023
## Python django Advance challenge

### Task
**Create a simple todo-list application with the following features:**
* Users can add, edit and delete tasks.
* Tasks should have a title and a description.
* Users can mark tasks as completed.
* Users can set a due date and time for a task.
* Users can filter tasks based on their status (completed, uncompleted) and due date.

### Endpoints
* POST /tasks - Create a new task
* GET /tasks - Retrieve a list of all tasks
* GET /tasks?status=completed - Filter tasks by status (completed)
* GET /tasks?status=uncompleted - Filter tasks by status (uncompleted)
* GET /tasks?due_date={date} - Filter tasks by due date
* GET /tasks/{task_id} - Retrieve a single task
* PUT /tasks/{task_id} - Update a task
* DELETE /tasks/{task_id} - Delete a task
* PUT /tasks/{task_id}/complete - Mark a task as completed

**_You should map these endpoints to the task_list, task_detail, and task_complete views, respectively._**

**_NOTE:_**
* project directory - **django/SDG23**
* App directory - **django/todo_api**
* virtual environment - **django/.venv**

**Best of LUCK!!!, ENJOY!!!**
