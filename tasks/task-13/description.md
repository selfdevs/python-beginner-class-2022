## **__TASK 13__**
**Building your first ETL pipeline**

### **INTENTIONS & GOALS**
> The main goal of this task is to get _you_ used to the workflow working with Git, Python, Modules, PostgreSQL and writing clean code.

> Write the code as modular as possible and stick to the DRY (Don't Repeat Yourself) principle. The result should be a primary python file which just calls a couple of functions which are stored in your custom modules.

### **Requirements**:
> - PostgreSQL should be installed on your PC. You can use PSQL or PGADMIN4 to visualize your database.
> - create a new virtual environment
> - create a `requirements.txt` file
> - create a `readme.md` file which describes what your script (task and goal) and repository is about. 
> If you can,  use markdown markup language (https://markdown-it.github.io) or just write into the file as if it would be a `.txt` file. 

### **RECAP TASK 8 + 10.**
> Task 8 was about creating the `selfdev_members_enriched.json` file where you enriched the self-created `.json` file.
> Task 10 was about creating a similar file via web scraping method from https://theselfdev.com
> 
> Now I want you to build an `ETL pipeline` rom scratch with the goal of scraping all the members from self dev and loading them into your local `PostgreSQL` database - all that with `Python` only. 
> 
> After this, we are going to dive into other APIs and learn how to work with different API responses
> and file formats like the panda data frames and `.csv` files. 


### a) **Extract**: 
> Take a look on https://theselfdev.com/community again and scrape every data possible from each member.
>
> >**Hint**: *If you have done the previous tasks, you have noticed that the images are not accessible due to the deployment method.*

### b) **Transform**
> Since we don't have to transform much data here, we directly skip to the database schema.
> Think of a database schema for your table and create a function which creates the table if it doesn't exist yet.
> Consider the column names, data type and constraints (like NOT NULL, UNIQUE...)
> 
> > **Extra**: Add a column `updated_date` to your table which indicates when every user has been updated (inserted) into your database.

### c) **Load**
> Write a function which loads each member into your database. 
> > We will worry about the efficiency later.

### d) **Confirmation**
> Write a function which checks if the amount of members inserted in your table is correct.
> >**Hint**: ||You will query your table again and check the result.||

### e) **Logging**
> Add a logger and log into a log file which includes today's date.
> Think about what would be useful to log and what not.
> > Example file: "selfdev-ETL-20-10-2022.log"


### f) **Requirements**
> To finish up your script, you need to know which packages you used, so someone else can install them as well on their pc. Figure out a way how you can see all your installed packages and write them into your `requirements.txt` file.

### g) **Clean up habit**
> Remove all unnecessary code snippets and add docstrings (comments) to your functions description what your function is about and what role your parameters have.

### h) **Extra thinking task**
> If you run your script multiple times, every member will be inserted into the database again and again. To avoid this we need to implement a mechanism which avoids adding duplicate values. That is called Primary Key.
>
> > Task: Read about Primary Key again and figure out how you could create a PK in your table, so you won't have duplicate members. Write your answer into your `readme.md` file.

### Tip:
You also can clone this repository and get all the files you need for this task and continue from here.
Just open your terminal, change into any folder and type into:
```bash
git clone git@github.com:selfdevs/python-beginner-class-2022.git
```