def calculate_grade():
    while True:
        name = input("\nEnter student name (or type 'Exit' to quit): ")
        if name.lower() == 'exit':
            print("Exiting program...")
            break
        
        try:
            mark1 = float(input("Enter mark for Subject 1: "))
            mark2 = float(input("Enter mark for Subject 2: "))
            mark3 = float(input("Enter mark for Subject 3: "))
            
            average = (mark1 + mark2 + mark3) / 3
            
            if average >= 75:
                grade = "A"
            elif average >= 60:
                grade = "B"
            elif average >= 40:
                grade = "C"
            else:
                grade = "Fail"
            
            print(f"\nResults for {name}:")
            print(f"Average: {average:.2f}")
            print(f"Grade: {grade}")
            
        except ValueError:
            print("Invalid input. Please enter numerical values for marks.")

if __name__ == "__main__":
    calculate_grade()
