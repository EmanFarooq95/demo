class PatientNode:
    def __init__(self, pid, name, age, disease, priority):
        self.pid = pid
        self.name = name
        self.age = age
        self.disease = disease
        self.priority = priority  # emergency priority
        self.next = None
class PatientLinkedList:
    def __init__(self):
        self.head = None
    def insert(self, pid, name, age, disease, priority):
        new_node = PatientNode(pid, name, age, disease, priority)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
    def search(self, pid):
        temp = self.head
        while temp:
            if temp.pid == pid:
                return temp
            temp = temp.next
        return None
    def delete(self, pid):
        temp = self.head
        prev = None
        while temp:
            if temp.pid == pid:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                return temp
            prev = temp
            temp = temp.next
        return None
    def display(self):
        if self.head is None:
            print("No patient records found.")
            return
        temp = self.head
        print("\nPatient Records:")
        print("ID | Name | Age | Disease | Priority")
        print("-----------------------------------")
        while temp:
            print(f"{temp.pid} | {temp.name} | {temp.age} | {temp.disease} | {temp.priority}")
            temp = temp.next
    def to_list(self):
        data = []
        temp = self.head
        while temp:
            data.append(temp)
            temp = temp.next
        return data
class MaxHeap:
    def __init__(self):
        self.heap = []
    def insert(self, patient):
        self.heap.append(patient)
        self._heapify_up(len(self.heap) - 1)
    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index].priority > self.heap[parent].priority:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)
    def delete_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root
    def _heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.heap) and self.heap[left].priority > self.heap[largest].priority:
            largest = left
        if right < len(self.heap) and self.heap[right].priority > self.heap[largest].priority:
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)
    def display(self):
        if not self.heap:
            print("No emergency patients.")
            return
        print("\nEmergency Patients (Max Heap - Level Order):")
        for p in self.heap:
            print(f"ID:{p.pid} Name:{p.name} Priority:{p.priority}")
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def display(self):
        if not self.stack:
            print("No deleted patient history.")
            return
        print("\nDeleted Patients History:")
        for p in reversed(self.stack):
            print(f"ID:{p.pid} Name:{p.name}")
def save_data(llist, heap):
    with open("patients.txt", "w") as f:
        temp = llist.head
        while temp:
            f.write(f"{temp.pid},{temp.name},{temp.age},{temp.disease},{temp.priority}\n")
            temp = temp.next
    print("Data saved successfully.")
def load_data(llist, heap):
    try:
        with open("patients.txt", "r") as f:
            for line in f:
                pid, name, age, disease, priority = line.strip().split(',')
                age = int(age)
                priority = int(priority)
                llist.insert(pid, name, age, disease, priority)
                heap.insert(PatientNode(pid, name, age, disease, priority))
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("No saved data found.")
#  Menu Driven System 
def main():
    llist = PatientLinkedList()
    heap = MaxHeap()
    deleted_stack = Stack()
    load_data(llist, heap)
    while True:
        print("\n--- Hospital Patient Management System ---")
        print("1. Add New Patient")
        print("2. Search Patient")
        print("3. Delete Patient")
        print("4. Display All Patients")
        print("5. Display Emergency Patients")
        print("6. Display Deleted Patients History")
        print("7. Save Data")
        print("8. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            pid = input("Patient ID: ")
            name = input("Name: ")
            age = int(input("Age: "))
            disease = input("Disease: ")
            priority = int(input("Emergency Priority (1-10): "))
            llist.insert(pid, name, age, disease, priority)
            heap.insert(PatientNode(pid, name, age, disease, priority))
            print("Patient added successfully.")
        elif choice == '2':
            pid = input("Enter Patient ID to search: ")
            patient = llist.search(pid)
            if patient:
                print(f"Found -> {patient.pid}, {patient.name}, {patient.age}, {patient.disease}, Priority:{patient.priority}")
            else:
                print("Patient not found.")
        elif choice == '3':
            pid = input("Enter Patient ID to delete: ")
            patient = llist.delete(pid)
            if patient:
                deleted_stack.push(patient)
                print("Patient deleted successfully.")
            else:
                print("Patient not found.")
        elif choice == '4':
            llist.display()
        elif choice == '5':
            heap.display()
        elif choice == '6':
            deleted_stack.display()
        elif choice == '7':
            save_data(llist, heap)
        elif choice == '8':
            save_data(llist, heap)
            print("Exiting system...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
