'''You are tasked with developing a Python program to manage a student database. The user should be able to add new 
students or stop the input process by entering "stop." Each student's name, along with a sequentially generated ID
starting from 1, should be stored in a tuple, with these tuples kept in a list. The program must check for duplicate
names before adding a new student and display a message if a duplicate is found. After the input process ends, the 
program should first display the complete list of student tuples and then display each student's ID and name 
individually. Additionally, the program should show the total number of students, calculate and display the total length
of all student names combined, and identify the student with the longest and shortest name using appropriate operators.
Implement these operations within a function named `manage_student_database()` and ensure you call this function at the
end of your code.'''

def manage_student_database():
    # Initialize an empty list to store student tuples
    student_list = []
    
    while True:
        name = input("Enter student name (or 'stop' to end input): ")
        if name.lower() == 'stop':
            break
        
        # Check for duplicate names
        for student in student_list:
            if student[0] == name:
                print(f"Student '{name}' already exists. Skipping duplicate entry.")
                continue
        
        # Generate a unique ID for each student
        student_id = len(student_list) + 1
        student_tuple = (student_id, name)
        student_list.append(student_tuple)
    
    # Display the complete list of student tuples
    print("\nStudent Database:")
    for student in student_list:
        print(f"ID: {student[0]}, Name: {student[1]}")
    
    # Calculate total number of students
    total_students = len(student_list)
    print(f"\nTotal number of students: {total_students}")
    
    # Calculate total length of all student names combined
    total_name_length = sum(len(student[1]) for student in student_list)
    print(f"Total length of student names: {total_name_length}")
    
    # Find student with longest and shortest name
    longest_name = max(student_list, key=lambda x: len(x[1]))[1]
    shortest_name = min(student_list, key=lambda x: len(x[1]))[1]
    print(f"Longest name: {longest_name}")
    print(f"Shortest name: {shortest_name}")

# Call the function to manage the student database
manage_student_database()

