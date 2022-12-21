from collections import defaultdict


class LeaveRecord:
    """
    This the class for create leave record for employee
    """

    def __init__(self, employee_id: str = "I2I") -> None:
        self.employee_id = employee_id
        self.leave_avail = 12
        self.leave_taken = 0
        self.leave_dates = defaultdict(list)
