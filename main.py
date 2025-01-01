import uuid
from datetime import datetime

# Creates an in-memory database for tools and usage logs
tools_db = {}  # Key: tool_id, Value: Tool object
usage_log = []  # List of usage entries

class Tool:
    def __init__(self, name, category, serial_number, purchase_date, condition):
        self.tool_id = None  # Unique identifier, is assigned later
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

def generate_short_id():
    """Generate a 5-character unique identifier."""
    return str(uuid.uuid4())[:5]

def find_tool_by_name_or_id(identifier):
    """Find a tool by either name or ID."""
    # First try to find by ID
    if identifier in tools_db:
        return identifier

    # Then try to find by name
    for tool_id, tool in tools_db.items():
        if tool.name.lower() == identifier.lower():
            return tool_id
    return None

def add_tool(name, category, serial_number, purchase_date, condition):
    """Creates a registry of a new tool in the system."""
    for tool in tools_db.values():
        if tool.serial_number == serial_number:
            raise ValueError("Tool with this serial number already exists.")

    new_tool = Tool(name, category, serial_number, purchase_date, condition)
    new_tool.tool_id = generate_short_id()
    # Ensure ID uniqueness
    while new_tool.tool_id in tools_db:
        new_tool.tool_id = generate_short_id()

    tools_db[new_tool.tool_id] = new_tool
    return new_tool.tool_id

def remove_tool(identifier):
    """Remove a tool from the system using either name or ID."""
    tool_id = find_tool_by_name_or_id(identifier)
    if not tool_id:
        raise ValueError("Tool not found.")
    tool_name = tools_db[tool_id].name
    del tools_db[tool_id]
    print(f"Tool '{tool_name}' (ID: {tool_id}) has been removed.")

def track_tool_usage(identifier, user, checkout_time, expected_return_time):
    """Track tool usage and log user information using either name or ID."""
    tool_id = find_tool_by_name_or_id(identifier)
    if not tool_id:
        raise ValueError("Tool not found.")

    usage_entry = {
        "tool_id": tool_id,
        "tool_name": tools_db[tool_id].name,
        "user": user,
        "checkout_time": checkout_time,
        "expected_return_time": expected_return_time,
        "return_time": None
    }
    usage_log.append(usage_entry)
    return usage_entry

def schedule_maintenance(identifier, maintenance_type, scheduled_date):
    """Schedule maintenance for a tool using either name or ID."""
    tool_id = find_tool_by_name_or_id(identifier)
    if not tool_id:
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
    print("\nListing all tools:")
    print("-" * 80)
    print(f"{'ID':<6} {'Name':<15} {'Category':<15} {'Condition':<10} {'Serial Number':<12}")
    print("-" * 80)
    for tool_id, tool in tools_db.items():
        print(f"{tool_id:<6} {tool.name:<15} {tool.category:<15} {tool.current_condition:<10} {tool.serial_number:<12}")

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
            tool_id = add_tool(name, category, serial_number, purchase_date, condition)
            print(f"Added default tool: {name} (ID: {tool_id})")
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
    print('Note: You can use either tool name or ID for options 2, 3, and 4')
    print('Type "exit" at any prompt to quit.\n')

def main():
    """Main entry point of the program."""
    print("Welcome to Kapul - A simple Tool Management System.")
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
                print(f"Error: {e}")

        elif choice == "2":
            identifier = input("Enter tool name or ID to remove: ").strip()
            if identifier.lower() == "exit":
                break
            try:
                remove_tool(identifier)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            identifier = input("Enter tool name or ID: ").strip()
            if identifier.lower() == "exit":
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
                usage_entry = track_tool_usage(identifier, user, checkout_time, expected_return_time)
                print(f"Tool usage logged: {usage_entry}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "4":
            identifier = input("Enter tool name or ID: ").strip()
            if identifier.lower() == "exit":
                break
            maintenance_type = input("Enter maintenance type: ").strip()
            if maintenance_type.lower() == "exit":
                break
            scheduled_date = input("Enter scheduled date (YYYY-MM-DD): ").strip()
            if scheduled_date.lower() == "exit":
                break
            try:
                maintenance_entry = schedule_maintenance(identifier, maintenance_type, scheduled_date)
                print(f"Maintenance scheduled: {maintenance_entry}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "5":
            list_tools()

        elif choice == "6":
            print("Exiting the Tool Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
