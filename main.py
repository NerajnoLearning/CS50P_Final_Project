import uuid
from datetime import datetime

# Creates an in-memory database for tools and usage logs
tools_db = {}  # Key: tool_id, Value: Tool object
usage_log = []  # List of usage entries

class Tool:
    def __init__(self, name, category, serial_number, purchase_date, condition):
        self.tool_id = None  # Unique identifier, assigned later
        self.name = name
        self.category = category
        self.serial_number = serial_number
        self.purchase_date = purchase_date
        self.current_condition = condition
        self.current_location = None
        self.maintenance_history = []
        self.total_usage_hours = 0

    def __repr__(self):
        return f"Tool({self.name}, {self.category}, {self.serial_number}, {self.purchase_date}, {self.current_condition})"

def add_tool(name, category, serial_number, purchase_date, condition):
    """Creates a registry of a new tool in the system."""
    for tool in tools_db.values():
        if tool.serial_number == serial_number:
            raise ValueError("Tool with this serial number already exists.")

    new_tool = Tool(name, category, serial_number, purchase_date, condition)
    new_tool.tool_id = str(uuid.uuid4())
    tools_db[new_tool.tool_id] = new_tool
    return new_tool.tool_id

def remove_tool(tool_id):
    """Remove a tool from the system."""
    if tool_id not in tools_db:
        raise ValueError("Tool not found.")
    del tools_db[tool_id]
    print(f"Tool with ID {tool_id} has been removed.")

def track_tool_usage(tool_id, user, checkout_time, expected_return_time):
    """Track tool usage and log user information."""
    if tool_id not in tools_db:
        raise ValueError("Tool not found.")

    usage_entry = {
        "tool_id": tool_id,
        "user": user,
        "checkout_time": checkout_time,
        "expected_return_time": expected_return_time,
        "return_time": None
    }
    usage_log.append(usage_entry)
    return usage_entry

def schedule_maintenance(tool_id, maintenance_type, scheduled_date):
    """Schedule maintenance for a tool."""
    if tool_id not in tools_db:
        raise ValueError("Tool not found.")

    maintenance_entry = {
        "maintenance_type": maintenance_type,
        "scheduled_date": scheduled_date,
        "status": "Scheduled",
    }
    tools_db[tool_id].maintenance_history.append(maintenance_entry)
    return maintenance_entry

def list_tools():
    """List all tools in the system."""
    if not tools_db:
        print("No tools found.")
        return
    print("Listing all tools:")
    for tool_id, tool in tools_db.items():
        print(f"ID: {tool_id}, Name: {tool.name}, Category: {tool.category}, Condition: {tool.current_condition}")

def initialize_default_tools():
    """Adds 5 default tools to the database."""
    default_tools = [
        ("Hammer", "Hand Tools", "SN001", "2022-01-01", "Good"),
        ("Drill", "Power Tools", "SN002", "2021-05-15", "Excellent"),
        ("Saw", "Power Tools", "SN003", "2020-11-20", "Fair"),
        ("Wrench", "Hand Tools", "SN004", "2023-03-10", "Excellent"),
        ("Ladder", "Safety Tools", "SN005", "2019-06-25", "Good")
    ]
    for name, category, serial_number, purchase_date, condition in default_tools:
        try:
            add_tool(name, category, serial_number, purchase_date, condition)
        except ValueError as e:
            print(f"Failed to add default tool: {e}")

def display_menu():
    """Displays the menu options."""
    print("\nTool Management System Menu:")
    print("1. Add Tool")
    print("2. Remove Tool")
    print("3. Track Tool Usage")
    print("4. Schedule Maintenance")
    print("5. List Tools")
    print("6. Exit")
    print('Type "exit" at any prompt to quit.\n')

def main():
    """Main entry point of the program."""
    print("Welcome to the Tool Management System!")
    initialize_default_tools()

    while True:
        display_menu()
        choice = input("Select an option: ").strip()
        if choice.lower() == "exit":
            print("Exiting the Tool Management System. Goodbye!")
            break

        if choice == "1":
            name = input("Enter tool name: ").strip()
            if name.lower() == "exit":
                break
            category = input("Enter tool category: ").strip()
            if category.lower() == "exit":
                break
            serial_number = input("Enter tool serial number: ").strip()
            if serial_number.lower() == "exit":
                break
            purchase_date = input("Enter purchase date (YYYY-MM-DD): ").strip()
            if purchase_date.lower() == "exit":
                break
            condition = input("Enter tool condition: ").strip()
            if condition.lower() == "exit":
                break
            try:
                tool_id = add_tool(name, category, serial_number, purchase_date, condition)
                print(f"Tool added successfully with ID: {tool_id}")
            except ValueError as e:
                print(e)

        elif choice == "2":
            tool_id = input("Enter tool ID to remove: ").strip()
            if tool_id.lower() == "exit":
                break
            try:
                remove_tool(tool_id)
            except ValueError as e:
                print(e)

        elif choice == "3":
            tool_id = input("Enter tool ID: ").strip()
            if tool_id.lower() == "exit":
                break
            user = input("Enter user name: ").strip()
            if user.lower() == "exit":
                break
            checkout_time = input("Enter checkout time (YYYY-MM-DD HH:MM): ").strip()
            if checkout_time.lower() == "exit":
                break
            expected_return_time = input("Enter expected return time (YYYY-MM-DD HH:MM): ").strip()
            if expected_return_time.lower() == "exit":
                break
            try:
                usage_entry = track_tool_usage(tool_id, user, checkout_time, expected_return_time)
                print(f"Tool usage logged: {usage_entry}")
            except ValueError as e:
                print(e)

        elif choice == "4":
            tool_id = input("Enter tool ID: ").strip()
            if tool_id.lower() == "exit":
                break
            maintenance_type = input("Enter maintenance type: ").strip()
            if maintenance_type.lower() == "exit":
                break
            scheduled_date = input("Enter scheduled date (YYYY-MM-DD): ").strip()
            if scheduled_date.lower() == "exit":
                break
            try:
                maintenance_entry = schedule_maintenance(tool_id, maintenance_type, scheduled_date)
                print(f"Maintenance scheduled: {maintenance_entry}")
            except ValueError as e:
                print(e)

        elif choice == "5":
            list_tools()

        elif choice == "6":
            print("Exiting the Tool Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
