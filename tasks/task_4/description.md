## **__TASK 4__**
**Python syntax: using functions in list comprehension.**

### **INTENTIONS & GOALS**
> The main goal of this task is to get you used to writing lists using list comprehensions and
> manipulating those lists with functions.

> Don't worry if your code is perfect or optimized yet. That's something we will worry about later. Now the only focus
> is to get into the workflow of writing code and to get familiar with the syntax.

### **REQUIREMENTS**
> - Create a new python file in your path of choice and name it `task_4.py`.
> - Create a `readme.md` file which describes what your script (task and goal) and repository is about. 
> - Create a `requirements.txt` file which contains all the dependencies of your script. (In this one, we don't have any)
>> - If you can, use Markdown markup language (https://markdown-it.github.io) or just write into the
> file as if it would be a `.txt` file. 

# **TASKS**
### a) Manipulating lists
>Given is a list `list_99` which contains numbers from 0 to 100.
Create a new list variable and code the following case: 
> All numbers which have a 9 as a digit like: 9, 19, 99 should be
counted, multiplied by 2 and stored in a new list variable.
>
>**Write a function which parses your list according to the mentioned requirements.**

**Output**

The new list should look like this
```python 
[18, 38, 28, 58, ... 198]
```
-----
### b) Slicing lists
> Return the last element of that list. In this case it should be 198. It is sufficient to write
> a one-liner for this task.

**Hint:** Use [slicing operators](https://www.w3schools.com/python/ref_func_slice.asp)
in Python, e.g. `my_list[-1]`

**Output**

```python 
198 
```
---
### c) Removing elements from list
All numbers which have a 7 as a digit like 7, 17, 97 should be removed from the previous list `list_99`. Your goal is to get a new list without the 7's.

Write a function to do so. You can use multiple **if** cases.

**Output**

The new list should look like this
```python
[.., 5, 7, .. , 96, ..]
```

---
Check out my [YouTube Tutorial](https://www.youtube.com/watch?v=_vc76aXm5Tg&list=PLnylL1gKkCV4ai5aDKH1GoOhtjDh7pWXf&index=4) if you need a recap of the topics.
### Tip:
You also can clone this repository and get all the files you need for this task and continue from here.
Just open your terminal, change into any folder and type into:
```bash
git clone git@github.com:selfdevs/python-beginner-class-2022.git
```