import csv 
file_name ="data.csv"

def load_data():
    students=[]
    try:
        with open(file_name,newline='')as file:
            reader=csv.reader(file)
            students=list(reader)        
    except FileNotFoundError:
        open(file_name,'w').close()
    return students


def save_data(students):
     with open(file_name,'w',newline='') as file:
         writer=csv.writer(file)
         writer.writerows(students)
         
def add_students():
    name=input("Enter the name of the student: ")
    try :
        marks=float(input("Enter the marks of the student:"))
        return [name,marks]
    except ValueError:
        print("invalid input! Marks should be a number ")
        return None
    
def information_of_students(students):
    print("\n ------Student Information------")
    if not students:
        print("No records Found.")
        return
    for name,marks in students:
        print(f"Name: {name} , Marks: {marks}")
    print()
    
def show_statistics(students):
    if not students:
        print("No information found.")
        return
    # marks = [float(m) for_, m in students ]
    marks = [float(m) for _, m in students]

    average_marks=sum(marks)/len(marks)
    highest_marks=max(marks)
    lowest_marks=min(marks)
    print(f"\n Average Marks: {average_marks}")
    print(f"\n Highest Marks: {highest_marks}")
    print(f"\n Lowest Marks: {lowest_marks}")
    
def main():
    print("-------Welcome to Student Marks Management System-------")
    students=load_data()
    
    while True:
        print("====Student Marks Management System====")
        print("1. Add Student")
        print("2. Show Student Information")
        print("3. Show Statistics")
        print("4. Exit")
        choice=input("Enter your choice (1-4): ")
        if choice == '1':
            student=add_students()
            if student:
                students.append(student)
                save_data(students)
                print("Student added successfully.")
        elif choice == '2':
            information_of_students(students)
        elif choice == '3':
            show_statistics(students)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
  
  
if __name__ == "__main__":
    main()
    
                  