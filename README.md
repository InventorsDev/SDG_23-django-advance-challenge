# Build4SDG 2023
## Python django intermediate challenge

# Task: Django Task API
This project is a simple ExpressJS task API that allows users to create, retrieve, update, and delete tasks. The API is built using ExpressJS and MongoDB for data storage.

## Expectations
## TASK 1
The project is expected to have the following API endpoints:

- Retrieve all tasks (GET _/api/tasks_)
- Create a task (POST _/api/tasks_)
- Retrieve a single task (GET _/api/tasks/:id_)
- Update a task (PATCH _/api/tasks/:id_)
- Delete a task (DELETE _/api/tasks/:id_)
- Mark task as completed (PATCH _/api/tasks/:id/completed_)

**Note** - Only for the more experienced developer
- Update the (GET _/api/tasks_) to allow user filter task either by dueDate, status or title. 

## TASK 2
 Complete the two question in the `django/SDG23/solve.py`. The `getMaxSum` and `uniqueChars` function
## Question 1 - getMaxSum
Write a function called `getMaxSum` that takes an array of integers as input and returns the maximum sum of any contiguous subarray of the given array. If the array is empty or contains only negative integers, the function should return 0. 
 The getMaxSum function takes an array of integers as input and returns the maximum sum of any contiguous subarray of the given array. If the array is empty or contains only negative integers, the function should return 0.

 ### Example Input and Output
 **Example 1**
 
 Input
```python
 getMaxSum([1, -3, 2, 1, -1]);
```

output
```python
 3
```

## Question 2 - uniqueChars
Complete the `uniqueChars` that takes a _string_ as input and returns a new string containing only the unique characters in the input string, in the order that they first appear. If the input string is empty or contains only whitespaces, the function should return an empty string.

// For example, if the input string is "hello world", the function should return "helo wrd".

 ### Example Input and Output
 **Example 1**
 
 Input
```python
 uniqueChars("hello world");
```

output
```python
 "helo wrd"
```
**Example 2**
 
 Input
```python
 uniqueChars("");
```

output
```python
 ""
```

**_NOTE:_**
* project directory - **django/SDG23**
* App directory - **django/todo_api**
* virtual environment - **django/.venv**

**Best of LUCK!!!, ENJOY!!!**

## Contributors


License
NIL
