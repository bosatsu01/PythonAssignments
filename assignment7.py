def append_data(roll_no, name, class_name, file="assignment.txt"):
    with open(file, "a") as f:
        f.write(f"Roll Number: {roll_no}\n")
        f.write(f"Name: {name}\n")
        f.write(f"Class: {class_name}\n")
    
    with open(file, "r") as f:
        data = f.readlines()
    
    print("Data in the file:")
    for line in data:
        print(line.strip())

# Example usage:
append_data("136", "Bodhisatwa Waghmare", "TY Diploma")