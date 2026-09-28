from datetime import datetime

while True:
   
   print("------------------------------------------")
   print("        CAMPUS SURVIVAL ASSISTANT")
   print("------------------------------------------")

   print("1. Attendance Calculator")
   print("2. Assignment Tracker")
   print("3. Exam Countdown")
   print("4. Study Planner")
   print("5. Expense Tracker")
   print("6. View Dashboard")
   print("7. Exit")

   choice = input("Enter your choice: ")

   print("You selected option:", choice)

   choice = choice.lower()

#attendence part

   if choice == "1" or choice == "attendance":
    while True:
        print("----------------------------------------")
        print("        ATTENDANCE CALCULATOR           ")
        print("----------------------------------------")
        
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Back to Main Menu")
        
        attendance_choice = input("Enter your choice: ").lower()
        
        if attendance_choice == "1" or attendance_choice == "mark":
            subject = input("Enter subject : ").strip()
        
            status = input("Were you present? {P/A} :").strip().lower()
        
            if status == "p":
                print(subject, "marked present . ")
        
                file = open("attendance.txt" , "a" )
                file.write(subject + ",P\n" )
                file.close()
        
            elif status =="a":
                print(subject, "marked absent . ")
        
                file = open("attendance.txt", "a")
                file.write(subject + ",A\n")
                file.close()
        
            
            else:
                print("invaild input. PLEASE ENTER ONLY P or A ")
        
        
            
        
        elif attendance_choice == "2" or attendance_choice == "view":
          print("========================================")
          print("          YOUR ATTENDANCE")
          print("========================================")

          file = open("attendance.txt", "r")

          records = file.readlines()

          file.close()

          if len(records)==0:
            print('No Attendance found. ')
          else:
            attendance = {}

            for record in records:
              subject, status = record.strip().split(",")

              if subject not in attendance:
                  attendance[subject] = [0, 0]

              attendance[subject][0] += 1

              if status == "P":
                  attendance[subject][1] += 1
            print("----------------------------------------")
            print("Subject     Total    Present    Absent")
            print("----------------------------------------")

            for subject in attendance:
                  total = attendance[subject][0]
                  present = attendance[subject][1]
                  absent = total - present

                  percentage = (present / total) * 100

                  print(subject, total, present, absent, round(percentage, 2), "%")

        elif attendance_choice == "3" or attendance_choice == "back":
            print("Returning to Main Menu...")
            break
        
        else:
            print("Invalid choice!")
        
#assigment part

   elif choice == "2" or choice == "assignment":
      while True:
        print("----------------------------------------")
        print("          ASSIGNMENT TRACKER")
        print("----------------------------------------")

        print("1. Add Assignment")
        print("2. View Assignments")
        print("3. Mark Assignment Complete")
        print("4. Back to Main Menu")

        assignment_choice = input("Enter your choice: ").lower()

        if assignment_choice == "1" or assignment_choice == "add":

           subject = input("Enter subject: ").strip()
           assignment = input("Enter assignment name: ").strip()
           due_date = input("Enter due date (DD-MM-YYYY): ").strip()

           file = open("assignments.txt", "a")
           file.write(subject + "," + assignment + "," + due_date + ",Pending\n")
           file.close()

           print("Assignment added successfully!")

        elif assignment_choice == "2" or assignment_choice == "view":
           print("----------------------------------------")
           print("          YOUR ASSIGNMENTS")
           print("----------------------------------------")

           file = open("assignments.txt", "r")
           records = file.readlines()
           file.close()

           if len(records) == 0:
              print("No assignments found.")

           else:
              for record in records:
                  subject, assignment, due_date, status = record.strip().split(",")

                  print("Subject:", subject)
                  print("Assignment:", assignment)
                  print("Due Date:", due_date)
                  print("Status:", status)
                  print("----------------------------------------")
    
        elif assignment_choice == "3" or assignment_choice == "complete":
            file = open("assignments.txt", "r")
            records = file.readlines()
            file.close()

            if len(records) == 0:
                print("No assignments found.")

            else:
                for i in range(len(records)):
                    subject, assignment, due_date, status = records[i].strip().split(",")

                    print(i + 1, ".", assignment, "-", status)

                number = int(input("Enter assignment number to mark complete: "))

                index = number - 1

                subject, assignment, due_date, status = records[index].strip().split(",")

                records[index] = subject + "," + assignment + "," + due_date + ",Completed\n"

                file = open("assignments.txt", "w")
                file.writelines(records)
                file.close()

                print("Assignment marked as completed!")

        elif assignment_choice == "4" or assignment_choice == "back":
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice!")


   elif choice == "3" or choice == "exam":
    while True:
        print("----------------------------------------")
        print("           EXAM COUNTDOWN")
        print("----------------------------------------")

        print("1. Add Exam")
        print("2. View Exams")
        print("3. Back to Main Menu")

        exam_choice = input("Enter your choice: ").lower()

        if exam_choice == "1" or exam_choice == "add":
            exam_name = input("Enter exam name: ").strip()
            exam_date = input("Enter exam date (MM-DD-YYYY): ").strip()

            file = open("exams.txt", "a")
            file.write(exam_name + "," + exam_date + "\n")
            file.close()

            print("Exam added successfully!")

        elif exam_choice == "2" or exam_choice == "view":
            print("========================================")
            print("             YOUR EXAMS                 ")
            print("========================================")

            file = open("exams.txt", "r")
            records = file.readlines()
            file.close()

            if len(records) == 0:
                print("No exams found.")

            else:
                today = datetime.now()

                for record in records:
                    exam_name, exam_date = record.strip().split(",")

                    exam_date = datetime.strptime(exam_date, "%m-%d-%Y")

                    difference = exam_date - today

                    days_left = difference.days

                    print("Exam:", exam_name)
                    print("Date:", exam_date.strftime("%d-%m-%Y"))

                    if days_left > 0:
                       print("Days left: ", days_left)
                    elif days_left == 0 :
                       print("Exams is today!!! ")
                    else:
                       print("Exam has already passed. ")
                    print("----------------------------------------")
                    print("                                        ")
        elif exam_choice == "3" or exam_choice == "back":
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice!")

# study planner part 

   elif choice == "4" or choice == "study":
    while True:
        print("========================================")
        print("           STUDY PLANNER")
        print("========================================")

        print("1. Add Study Task")
        print("2. View Study Tasks")
        print("3. Mark Task Complete")
        print("4. Back to Main Menu")

        study_choice = input("Enter your choice: ").lower()

        if study_choice == "1" or study_choice == "add":
           subject = input("Enter subject: ").strip()
           topic = input("Enter topic to study: ").strip()
           study_date = input("Enter study date (MM-DD-YYYY): ").strip()

           file = open("study_plan.txt", "a")
           file.write(subject + "," + topic + "," + study_date + ",Pending\n")
           file.close()

           print("Study task added successfully!")

           
        elif study_choice == "2" or study_choice == "view":
            print("========================================")
            print("          YOUR STUDY TASKS")
            print("========================================")

            file = open("study_plan.txt", "r")
            records = file.readlines()
            file.close()

            if len(records) == 0:
                print("No study tasks found.")

            else:
                for record in records:
                    subject, topic, study_date, status = record.strip().split(",")

                    print("Subject:", subject)
                    print("Topic:", topic)
                    print("Study Date:", study_date)
                    print("Status:", status)
                    print("----------------------------------------")


        elif study_choice == "3" or study_choice == "complete":
           file = open("study_plan.txt", "r")
           records = file.readlines()
           file.close()

           if len(records) == 0:
                print("No study tasks found.")

           else:
                for i in range(len(records)):
                    subject, topic, study_date, status = records[i].strip().split(",")

                    print(i + 1, ".", subject, "-", topic, "-", status)

                number = int(input("Enter task number to mark complete: "))

                index = number - 1

                subject, topic, study_date, status = records[index].strip().split(",")

                records[index] = subject + "," + topic + "," + study_date + ",Completed\n"

                file = open("study_plan.txt", "w")
                file.writelines(records)
                file.close()

                print("Study task marked as completed!")
        elif study_choice == "4" or study_choice == "back":
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice!")


   elif choice == "5" or choice == "expense":
      while True:
        print("========================================")
        print("          EXPENSE TRACKER")
        print("========================================")

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Spending")
        print("4. Back to Main Menu")

        expense_choice = input("Enter your choice: ").lower()

        if expense_choice == "1" or expense_choice == "add":
            category = input("Enter expense category: ").strip()
            amount = input("Enter amount: ").strip()
            expense_date = input("Enter date (MM-DD-YYYY): ").strip()

            file = open("expenses.txt", "a")
            file.write(category + "," + amount + "," + expense_date + "\n")
            file.close()

            print("Expense added successfully!")

        elif expense_choice == "2" or expense_choice == "view":
           print("========================================")
           print("           YOUR EXPENSES")
           print("========================================")

           file = open("expenses.txt", "r")
           records = file.readlines()
           file.close()

           if len(records) == 0:
              
              print("No expenses found.")

           else:
              for record in records:
                 category, amount, expense_date = record.strip().split(",")

                 print("Category:", category)
                 print("Amount: ₹", amount)
                 print("Date:", expense_date)
                 print("----------------------------------------")

        elif expense_choice == "3" or expense_choice == "total":
           file = open("expenses.txt", "r")
           records = file.readlines()
           file.close()

           if len(records) == 0:
            print("No expenses found.")

           else:
            total = 0

            for record in records:
                category, amount, expense_date = record.strip().split(",")

                total = total + float(amount)

                print("========================================")
                print("          TOTAL SPENDING")
                print("========================================")
                print("Total spending: ₹", round(total, 2))

        elif expense_choice == "4" or expense_choice == "back":
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice!")
      
      
    

   elif choice == "6" or choice == "dashboard":
      print("========================================")
      print("              DASHBOARD")
      print("========================================")

      print("1. Attendance Summary")
      print("2. Assignment Summary")
      print("3. Exam Summary")
      print("4. Study Task Summary")
      print("5. Expense Summary")
      print("6. Back to Main Menu")

      dashboard_choice = input("Enter your choice: ").lower()

      if dashboard_choice == "1" or dashboard_choice == "attendance":

        print("========================================")
        print("        ATTENDANCE SUMMARY")
        print("========================================")

        file = open("attendance.txt", "r")
        records = file.readlines()
        file.close()

        if len(records) == 0:
          print("No attendance records found.")

        else:
          attendance = {}

          for record in records:
            subject, status = record.strip().split(",")

            if subject not in attendance:
                attendance[subject] = [0, 0]

            attendance[subject][0] += 1

            if status == "P":
                attendance[subject][1] += 1

          for subject in attendance:
            total = attendance[subject][0]
            present = attendance[subject][1]

            percentage = (present / total) * 100

            print(subject, ":", round(percentage, 2), "%")


      elif dashboard_choice == "2" or dashboard_choice == "assignment":
          print("========================================")
          print("        ASSIGNMENT SUMMARY")
          print("========================================")

          file = open("assignments.txt", "r")
          records = file.readlines()
          file.close()

          if len(records) == 0:
            print("No assignments found.")

          else:
            pending = 0
            completed = 0

            for record in records:
                subject, assignment, due_date, status = record.strip().split(",")

                if status == "Pending":
                    pending += 1

                elif status == "Completed":
                    completed += 1

            total = pending + completed

            print("Total Assignments:", total)
            print("Pending:", pending)
            print("Completed:", completed)
        

      elif dashboard_choice == "3" or dashboard_choice == "exam":
         print("========================================")
         print("           EXAM SUMMARY                 ")
         print("========================================")

         file = open("exams.txt", "r")
         records = file.readlines()
         file.close()

         if len(records) == 0:
            print("No exams found.")

         else:
             today = datetime.now()

             upcoming = 0
             passed = 0
             today_exam = 0

             for record in records:
                  exam_name, exam_date = record.strip().split(",")

                  exam_date = datetime.strptime(exam_date, "%m-%d-%Y")

                  difference = exam_date - today
                  days_left = difference.days

                  if days_left > 0:
                      upcoming += 1

                  elif days_left == 0:
                      today_exam += 1

                  else:
                      passed += 1

             total = upcoming + today_exam + passed

             print("Total Exams:", total)
             print("Upcoming Exams:", upcoming)
             print("Today's Exams:", today_exam)
             print("Passed Exams:", passed)
        

      elif dashboard_choice == "4" or dashboard_choice == "study":
         print("========================================")
         print("        STUDY TASK SUMMARY")
         print("========================================")

         file = open("study_plan.txt", "r")
         records = file.readlines()
         file.close()

         if len(records) == 0:
             print("No study tasks found.")

         else:
             pending = 0
             completed = 0

             for record in records:
                 subject, topic, study_date, status = record.strip().split(",")

                 if status == "Pending":
                     pending += 1

                 elif status == "Completed":
                     completed += 1

             total = pending + completed

             print("Total Study Tasks:", total)
             print("Pending:", pending)
             print("Completed:", completed)


      elif dashboard_choice == "5" or dashboard_choice == "expense":
        print("========================================")
        print("          EXPENSE SUMMARY")
        print("========================================")

        file = open("expenses.txt", "r")
        records = file.readlines()
        file.close()

        if len(records) == 0:
             print("No expenses found.")

        else:
             total = 0

             for record in records:
                 category, amount, expense_date = record.strip().split(",")

                 total = total + float(amount)

             print("Total Expenses:", len(records))
             print("Total Spending: ₹", round(total, 2))

      elif dashboard_choice == "6" or dashboard_choice == "back":
        print("Returning to Main Menu...")

      else:
        print("Invalid choice!")
      
    
   elif choice == "7" or choice == "exit":
    print("Thank you for using Campus Survival Assistant!")
    break

   else:
    print("Invalid choice. Please try again.") 
