# Hospital Patient Record System

patients = {}   # Dictionary to store patient details

# Tuple (fixed departments)
departments = ("Cardiology", "Neurology", "Orthopedics", "General Medicine")

while True:

    print("\n===== Hospital Patient Record System =====")
    print("1. Add Patient")
    print("2. View All Patients")
    print("3. Search Patient")
    print("4. Update Disease")
    print("5. Total Patients")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Patient
    if choice == "1":

        patient_id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        age = int(input("Enter Age: "))
        disease = input("Enter Disease: ")

        print("\nDepartments Available:")
        for dept in departments:
            print("-", dept)

        department = input("Enter Department: ")

        # List to store medicines
        medicines = []

        n = int(input("How many medicines are prescribed? "))

        for i in range(n):
            medicine = input(f"Enter medicine {i+1}: ")
            medicines.append(medicine)

        # Store details inside dictionary
        patients[patient_id] = {
            "Name": name,
            "Age": age,
            "Disease": disease,
            "Department": department,
            "Medicines": medicines
        }

        print("Patient record added successfully.")

    # View all patients
    elif choice == "2":

        if len(patients) == 0:
            print("No patient records available.")

        else:
            print("\n----- Patient Records -----")

            for patient_id, details in patients.items():

                print("\nPatient ID:", patient_id)
                print("Name:", details["Name"])
                print("Age:", details["Age"])
                print("Disease:", details["Disease"])
                print("Department:", details["Department"])

                print("Medicines:")
                for medicine in details["Medicines"]:
                    print("-", medicine)

    # Search patient
    elif choice == "3":

        search_id = input("Enter Patient ID to search: ")

        if search_id in patients:

            details = patients[search_id]

            print("\nPatient Found")
            print("Name:", details["Name"])
            print("Age:", details["Age"])
            print("Disease:", details["Disease"])
            print("Department:", details["Department"])

            print("Medicines:")
            for medicine in details["Medicines"]:
                print("-", medicine)

        else:
            print("Patient not found.")

    # Update disease
    elif choice == "4":

        update_id = input("Enter Patient ID: ")

        if update_id in patients:

            new_disease = input("Enter new disease: ")
            patients[update_id]["Disease"] = new_disease

            print("Disease updated successfully.")

        else:
            print("Patient ID not found.")

    # Total patients
    elif choice == "5":

        print("Total number of patients:", len(patients))

    # Exit
    elif choice == "6":

        print("Thank you for using Hospital Patient Record System.")
        break

    else:
        print("Invalid choice! Please try again.")
