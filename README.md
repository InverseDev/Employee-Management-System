# Employee-Management-System

This is a simple **Python-based Employee Database Management System** that stores employee data, calculate final salary and provide features to manage the employee data. All the data is saved in a CSV file.

## Features:
-> Add new employees with salary, bonus, and deductions  
-> View all employee data in a tabular format  
-> Search employee by their ID  
-> Update bonus for an employee  
-> Update deduction for an employee  
-> Delete employee records  
-> Persistent data storage in `employees.csv`

## Project Structure
```markdown
EmployeePayroll/
├── employees.csv # Employee data file (auto-generated)
├── payroll.py # Main Python script
```

## Requirements
- Python 3
- `tabulate` library
- `os`, `csv` modules (built-in)

### Install the tabulate module (if not installed):
```bash
  pip install tabulate
```

## How to run

1) Download the 'EmployeePayroll.zip' and extract it in a folder
2) Run the payroll.py file
```bash
python payroll.py
```
3) Follow the on-screen menu to perform operations like adding, viewing, searching, updating, and deleting employee data.

## Notes
-> All employee data is saved inside the EmployeePayroll/employees.csv file.

-> Bonus and Deduction inputs are validated to accept only integers.

## Author
MD Afzal Alam

## License
This project is open-source and free to use.
```yaml
Feel free to improve, update or use the code!
```

