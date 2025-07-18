import pandas as pd
import random
from faker import Faker

fake = Faker()
num_students = 500

# Lists to store data
students_data = []
programming_data = []
soft_skills_data = []
placement_data = []

for student_id in range(1, num_students + 1):
    # Student table
    name = fake.name()
    age = random.randint(21, 35)
    gender = random.choice(["M", "F"])
    email = fake.email()
    phone = fake.phone_number()
    entrollment_year = random.randint(2005, 2020)
    course_batch = entrollment_year + 4
    city = fake.city()
    graduation_year = course_batch
    students_data.append([
        student_id, name, age, gender, email, phone, 
        entrollment_year, course_batch, city, graduation_year
    ])

    # Programming table
    language = random.choice("Python", "Java", "JavaScript", "C++", "C#", "PHP", "SQL", "Go", "Swift", "Rust")
    problems_solved = random.randint(0, 3000)
    assessments_completed = random.randint(1, 20)
    mini_project = random.randint(1, 50)
    certifications_earned = random.randint(0, 10)
    latest_project_score = random.randint(30, 100)
    programming_data.append([
        student_id, student_id, language, problems_solved,
        assessments_completed, mini_project, certifications_earned, latest_project_score
    ])

    # Soft skills table
    communication = random.randint(30, 100)
    teamwork = random.randint(50, 100)
    presentation = random.randint(20, 100)
    leadership = random.randint(50, 100)
    critical_thinking = random.randint(30, 100)
    interpersonal_skills = random.randint(30, 100)
    soft_skills_data.append([
        student_id, student_id, communication, teamwork,
        presentation, leadership, critical_thinking, interpersonal_skills
    ])

    # Placement table
    mock_interview_score = random.randint(30, 100)
    internships_completed = random.randint(1, 5)
    interview_rounds_cleared = random.randint(1, 5)
    placement_status = "Placed" if interview_rounds_cleared >= 3 else "Not Placed"
    company_name = fake.company() if placement_status == "Placed" else "Not Available"
    placement_package = random.randint(50000, 100000) if placement_status == "Placed" else 0
    placement_date = fake.date_between(start_date='-1y', end_date='-1d') if placement_status == "Placed" else "1000-00-00"
    placement_data.append([
        student_id, student_id, mock_interview_score, internships_completed,
        interview_rounds_cleared, placement_status, company_name, placement_package, placement_date
    ])

# Convert to DataFrames
df_students = pd.DataFrame(students_data, columns=[
    "students_id", "name", "age", "gender", "email", "phone", 
    "entrollment_year", "course_batch", "city", "graduation_year"
])

df_programming = pd.DataFrame(programming_data, columns=[
    "programming_id", "students_id", "language", "problems_solved",
    "assessments_completed", "mini_project", "certifications_earned", "latest_project_score"
])

df_soft_skills = pd.DataFrame(soft_skills_data, columns=[
    "soft_skill_id", "students_id", "communication", "teamwork",
    "presentation", "leadership", "critical_thinking", "interpersonal_skills"
])

df_placement = pd.DataFrame(placement_data, columns=[
    "placement_id", "students_id", "mock_interview_score", "internships_completed",
    "interview_rounds_cleared", "placement_status", "company_name", 
    "placement_package", "placement_date"
])

# Save to CSV
df_students.to_csv("student_table.csv", index=False)
df_programming.to_csv("programming_table.csv", index=False)
df_soft_skills.to_csv("soft_skills_table.csv", index=False)
df_placement.to_csv("placement_table.csv", index=False)

