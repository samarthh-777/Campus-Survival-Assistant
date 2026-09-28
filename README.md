#  Campus Survival Assistant

Campus Survival Assistant is a command-line Python application designed to help college students manage important academic and personal tasks in one place.

##  Features

The application provides the following features:

### 1. Attendance Calculator
- Mark attendance for different subjects
- View attendance records
- Calculate attendance percentage
- Calculate how many future classes can be missed while maintaining at least 75% attendance

### 2. Assignment Tracker
- Add assignments
- View assignments
- Track due dates
- Mark assignments as completed
- View pending and completed assignment counts

### 3. Exam Countdown
- Add upcoming exams
- Store exam dates
- Calculate the number of days remaining
- Identify exams that have already passed

### 4. Study Planner
- Add study tasks
- View study tasks
- Set study dates
- Mark study tasks as completed
- View pending and completed study tasks

### 5. Expense Tracker
- Record daily expenses
- View expense records
- Calculate total spending

### 6. Dashboard
- View attendance summary
- View assignment summary
- View exam summary
- View study task summary
- View expense summary

##  Technologies Used

- Python 3
- Python Standard Library
- Text files for data storage

##  Requirements

- Python 3.x
- A command-line terminal
- No external Python packages are required

##  Setup

1. Download or clone this repository.
2. Open the project folder in a terminal.
3. Make sure Python 3 is installed.
4. Run the following command:

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

##  How to Use

After running the program, the main menu will appear:

```text
------------------------------------------  
      CAMPUS SURVIVAL ASSISTANT
------------------------------------------

1. Attendance Calculator
2. Assignment Tracker
3. Exam Countdown
4. Study Planner
5. Expense Tracker
6. View Dashboard
7. Exit
```

Enter the number or supported option to access the required feature.

##  Data Storage

The application stores information locally in text files:

- `attendance.txt` — attendance records
- `assignments.txt` — assignment records
- `exams.txt` — exam records
- `study_plan.txt` — study task records
- `expenses.txt` — expense records

No database or external service is required.

##  Project Purpose

This project was developed as part of the Python Essentials course to apply Python programming concepts such as:

- Variables and data types
- Conditional statements
- Loops
- Functions and modules
- Lists and dictionaries
- File handling
- String processing
- Exception and input handling
- Date and time operations

##  License

This project is created for educational purposes.
