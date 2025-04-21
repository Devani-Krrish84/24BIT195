class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed to stack.")

    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f"{item} popped from stack.")
            return item
        else:
            print("Stack is empty. Nothing to pop.")
            return None

    def peek(self):
        if not self.is_empty():
            print(f"Top element is: {self.stack[-1]}")
            return self.stack[-1]
        else:
            print("Stack is empty.")
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        if not self.is_empty():
            print("Stack elements:", self.stack)
        else:
            print("Stack is empty.")

if __name__ == "__main__":
    stack = Stack()
    while True:
        print("\nMenu:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            item = input("Enter the item to push: ")
            stack.push(item)
        elif choice == "2":
            stack.pop()
        elif choice == "3":
            stack.peek()
        elif choice == "4":
            stack.display()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")