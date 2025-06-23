import csv
import random
from datetime import datetime, timedelta

# কিছু স্যাম্পল নাম আর পদবি
names = ["Rahim Khan", "Salma Akter", "Karim Ahmed", "Nabila Islam", "Fahim Hasan", "Sadia Rahman", "Rafiqur Rahman", "Tania Chowdhury", "Arif Hossain", "Moushumi Begum"]
designations = ["Junior Engineer", "Software Engineer", "Senior Software Engineer", "HR Executive", "Senior HR Executive", "Project Manager", "Team Lead", "Intern"]

def random_date(start, end):
    """Random date between start and end"""
    delta = end - start
    int_delta = delta.days
    random_day = random.randrange(int_delta)
    return start + timedelta(days=random_day)

def generate_leave_policy(filename="leave_policy.csv", rows=50):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["EmployeeID", "EmployeeName", "LeaveType", "AllowedDays", "TakenDays", "Year"])
        for i in range(1, rows+1):
            name = random.choice(names)
            leave_type = random.choice(["Paid Leave", "Sick Leave", "Maternity Leave"])
            allowed = 20 if leave_type == "Paid Leave" else (180 if leave_type == "Maternity Leave" else 10)
            taken = random.randint(0, allowed)
            year = 2024
            writer.writerow([i, name, leave_type, allowed, taken, year])
    print(f"{filename} তৈরি হয়েছে।")

def generate_salary(filename="salary.csv", rows=50):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["EmployeeID", "EmployeeName", "Designation", "SalaryAmount", "Currency", "EffectiveFrom"])
        for i in range(1, rows+1):
            name = random.choice(names)
            designation = random.choice(designations)
            salary = random.randint(25000, 120000)
            currency = "BDT"
            effective_date = random_date(datetime(2023, 1, 1), datetime(2024, 6, 30)).strftime("%Y-%m-%d")
            writer.writerow([i, name, designation, salary, currency, effective_date])
    print(f"{filename} তৈরি হয়েছে।")

def generate_promotion(filename="promotion.csv", rows=50):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["EmployeeID", "EmployeeName", "OldDesignation", "NewDesignation", "PromotionDate", "Remarks"])
        for i in range(1, rows+1):
            name = random.choice(names)
            old_desig = random.choice(designations[:-2])
            new_desig = random.choice(designations[designations.index(old_desig)+1:]) if designations.index(old_desig)+1 < len(designations) else old_desig
            promo_date = random_date(datetime(2023, 1, 1), datetime(2024, 6, 30)).strftime("%Y-%m-%d")
            remarks = random.choice(["Good performance", "Yearly appraisal", "Exceeded targets", "Promotion based on seniority", ""])
            writer.writerow([i, name, old_desig, new_desig, promo_date, remarks])
    print(f"{filename} তৈরি হয়েছে।")

if __name__ == "__main__":
    generate_leave_policy()
    generate_salary()
    generate_promotion()
