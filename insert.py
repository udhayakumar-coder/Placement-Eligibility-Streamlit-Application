import mysql.connector
import pandas as pd

# Connect to MySQL
udhaya = mysql.connector.connect(
    host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
    user="NHk3ZCuh5QRYthi.root",
    password="AEpsh6zgl0yxb9td",
    port="4000",
    database="Placement_Eligibility_Application"
)
con = udhaya.cursor()

# Load CSV files
df_students = pd.read_csv("student_table.csv")
df_programming = pd.read_csv("programming_table.csv")
df_soft_skills = pd.read_csv("soft_skills_table.csv")
df_placement = pd.read_csv("placement_table.csv")

# Insert data into students table
insert_query = """
    INSERT INTO student_table VALUES(
        student_id, name, age, gender, email, phone, 
        entrollment_year, course_batch, city, graduation_year
    ) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
for index, row in df_students.iterrows():
    con.execute(insert_query, (
        row['student_id'], row['name'], row['age'], row['gender'], row['email'], 
        row['phone'], row['entrollment_year'], row['course_batch'],
        row['city'], row['graduation_year']
    ))
# Insert data into programming table
insert_query="""
    INSERT INTO programming_table (
        programming_id, student_id, language, problems_solved, assessment_completed,
        mini_projects, certifications_earned, latest_project_score
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""
for index, row in df_programming.iterrows():
    con.execute(insert_query, (
        row['programming_id'], row['students_id'], row['language'], row['problems_solved'], row['assessments_completed'], 
        row['mini_project'], row['certifications_earned'], row['latest_project_score']
    ))
# Insert data into soft skills table
data="""
    INSERT INTO soft_skills_table (
        soft_skill_id, student_id, communication, teamwork, presentation, leadership, 
        critical_thinking, interpersonal_skills)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""
for index, row in df_soft_skills.iterrows():
    con.execute(data, (
        int(row['soft_skill_id']), int(row['students_id']), int(row['communication']), int(row['teamwork']), 
        int(row['presentation']), int(row['leadership']), int(row['critical_thinking']), int(row['interpersonal_skills'])
    ))
# Insert data into placement table
