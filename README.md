 #  Kapul - Tool Management System

A Python-based system for managing and tracking tools in an organization. This application allows users to maintain an inventory of tools, track their usage, schedule maintenance, and monitor tool conditions.

## Features
- Add and remove tools from the inventory
- Track tool usage with checkout/return functionality
- Schedule and monitor tool maintenance
- List all tools in the system
- Automatic initialization with default tools
- Predictive maintenance scoring system

## Installation

1. Clone this repository
2. Ensure you have Python 3.x installed
3. Install required dependencies:
```bash
pip install pytest
```

## Project Structure

- `main.py` - Core implementation with tool management functionality
- `test_tools.py` - Test suite for verifying system functionality

## Usage

Run the application using:
```bash
python main.py
```

The system presents a menu-driven interface with the following options:
1. Add Tool
2. Remove Tool
3. Track Tool Usage
4. Schedule Maintenance
5. List Tools
6. Exit

### Adding a Tool
Enter the following information when prompted:
- Tool name
- Category
- Serial number (must be unique)
- Purchase date (YYYY-MM-DD format)
- Current condition

### Tracking Usage
Requires:
- Tool ID
- User name
- Checkout time (YYYY-MM-DD HH:MM format)
- Expected return time (YYYY-MM-DD HH:MM format)

### Scheduling Maintenance
Input needed:
- Tool ID
- Maintenance type
- Scheduled date (YYYY-MM-DD format)

## Testing
Run the test suite using:
```bash
pytest test_tools.py
```

The test suite covers:
- Tool addition and validation
- Usage tracking functionality
- Maintenance scheduling
- Predictive maintenance calculations
- Error handling for invalid operations

## Data Structure

### Tool Class
```python
class Tool:
    - tool_id: Unique identifier
    - name: Tool name
    - category: Tool category
    - serial_number: Unique serial number
    - purchase_date: Date of purchase
    - current_condition: Current tool condition
    - current_location: Location tracking
    - maintenance_history: List of maintenance records
    - total_usage_hours: Cumulative usage time
```

## Error Handling
The system includes robust error handling for:
- Duplicate serial numbers
- Invalid tool IDs
- Missing tools
- Invalid date formats

## Future Enhancements
Potential improvements could include:
- Database persistence
- User authentication
- Advanced reporting features
- API integration
- Real-time location tracking
- Enhanced predictive maintenance algorithms


## License

[Specify your license here]
