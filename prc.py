# Node Class
class Node:
    def __init__(self, pid, name, priority):
        self.pid = pid
        self.name = name
        self.priority = priority
        self.next = None


# Hospital Class
class Hospital:
    def __init__(self):
        self.front = None

    # 1. Add Patient (Enqueue)
    def add_patient(self):
        pid = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        priority = int(input("Enter Priority (1-Critical, 2-Serious, 3-Normal): "))

        if priority not in [1, 2, 3]:
            print("Invalid Priority!")
            return

        new_node = Node(pid, name, priority)

        if self.front is None or priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
        else:
            temp = self.front

            while temp.next is not None and temp.next.priority <= priority:
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node

        print("Patient added successfully!")

    # 2. Display Next Patient
    def display_next(self):
        if self.front is None:
            print("No patients in queue!")
        else:
            print("\nNext Patient to be Treated:")
            print("Patient ID:", self.front.pid)
            print("Patient Name:", self.front.name)
            print("Priority:", self.front.priority)

    # 3. Remove Patient (Dequeue)
    def dequeue(self):
        if self.front is None:
            print("No patients to treat!")
        else:
            temp = self.front
            self.front = self.front.next

            print("Patient treated and removed:")
            print("Patient ID:", temp.pid)
            print("Patient Name:", temp.name)

    # 4. Display All Patients
    def display_all(self):
        if self.front is None:
            print("No waiting patients!")
        else:
            temp = self.front

            print("\nWaiting Patients in Priority Order:")

            while temp is not None:
                priority_name = {
                    1: "Critical",
                    2: "Serious",
                    3: "Normal"
                }

                print("ID:", temp.pid,
                      "| Name:", temp.name,
                      "| Priority:", priority_name[temp.priority])

                temp = temp.next


# Main Program
h = Hospital()

while True:
    print("\n===== HOSPITAL EMERGENCY MANAGEMENT =====")
    print("1. Add Patient")
    print("2. Display Next Patient")
    print("3. Remove Patient (Dequeue)")
    print("4. Display All Patients")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        h.add_patient()
    elif choice == 2:
        h.display_next()
    elif choice == 3:
        h.dequeue()
    elif choice == 4:
        h.display_all()
    elif choice == 5:
        print("Exiting Hospital Management System...")
        break
    else:
        print("Invalid Choice! Please try again.")
