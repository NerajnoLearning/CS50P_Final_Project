import pytest
from datetime import datetime
from main import add_tool, track_tool_usage, schedule_maintenance, predictive_maintenance, tools_db, usage_log

@pytest.fixture
def setup_tools():
    """Fixture to reset the tools database for each test."""
    tools_db.clear()
    usage_log.clear()

def test_add_tool(setup_tools):
    """Test adding a tool to the system."""
    tool_id = add_tool("Drill", "Power Tools", "SN123", "2023-01-01", "Good")
    assert tool_id in tools_db
    tool = tools_db[tool_id]
    assert tool.name == "Drill"
    assert tool.category == "Power Tools"
    assert tool.serial_number == "SN123"
    assert tool.purchase_date == "2023-01-01"
    assert tool.current_condition == "Good"

    # Test for duplicate tool
    with pytest.raises(ValueError, match="Tool with this serial number already exists."):
        add_tool("Drill 2", "Power Tools", "SN123", "2023-02-01", "Excellent")

def test_track_tool_usage(setup_tools):
    """Test tracking tool usage."""
    tool_id = add_tool("Hammer", "Hand Tools", "SN124", "2023-02-01", "Excellent")
    checkout_time = "2024-12-10 09:00"
    expected_return_time = "2024-12-10 17:00"
    usage_entry = track_tool_usage(tool_id, "Alice", checkout_time, expected_return_time)

    assert len(usage_log) == 1
    assert usage_log[0]["tool_id"] == tool_id
    assert usage_log[0]["user"] == "Alice"
    assert usage_log[0]["checkout_time"] == checkout_time
    assert usage_log[0]["expected_return_time"] == expected_return_time
    assert usage_log[0]["return_time"] is None

    # Test for non-existent tool
    with pytest.raises(ValueError, match="Tool not found."):
        track_tool_usage("nonexistent_tool_id", "Bob", checkout_time, expected_return_time)

def test_schedule_maintenance(setup_tools):
    """Test scheduling maintenance for a tool."""
    tool_id = add_tool("Saw", "Power Tools", "SN125", "2022-05-15", "Good")
    maintenance_entry = schedule_maintenance(tool_id, "Oil Change", "2024-12-15")

    tool = tools_db[tool_id]
    assert len(tool.maintenance_history) == 1
    assert tool.maintenance_history[0]["maintenance_type"] == "Oil Change"
    assert tool.maintenance_history[0]["scheduled_date"] == "2024-12-15"
    assert tool.maintenance_history[0]["status"] == "Scheduled"

    # Test for non-existent tool
    with pytest.raises(ValueError, match="Tool not found."):
        schedule_maintenance("nonexistent_tool_id", "Calibration", "2024-12-20")

def test_predictive_maintenance(setup_tools):
    """Test predictive maintenance scoring."""
    tool_id = add_tool("Wrench", "Hand Tools", "SN126", "2021-05-01", "Excellent")
    tools_db[tool_id].total_usage_hours = 150

    score = predictive_maintenance(tool_id)
    assert score > 0  # Ensure score is calculated

    # Test for non-existent tool
    with pytest.raises(ValueError, match="Tool not found."):
        predictive_maintenance("nonexistent_tool_id")
