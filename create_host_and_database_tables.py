pip install mysql-connector-python
import mysql.connector
udhaya=mysql.connector.connect(host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
                               user="NHk3ZCuh5QRYthi.root",
                               password="AEpsh6zgl0yxb9td",
                               port="4000")
con=udhaya.cursor()
con.execute("start transaction")
con.execute("create database Pesa")
udhaya=mysql.connector.connect(host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
                               user="NHk3ZCuh5QRYthi.root",
                               password="AEpsh6zgl0yxb9td",
                               port="4000",
                               database="Pesa")
con.execute("start transaction"
            create table students(
                student_id int,
                name varchar(50),
                age int,
                gender varchar(1),
                email_id varchar(50),
                phone int,
                entrollment_year int,
                course_batch int,
                city varchar(50),
                graduation_year int,
                constraint pk_students primary key (student_id)
            )
            create table programming(
                programming_id int,
                student_id int,
                language varchar(60),
                problems_solved int,
                assessment_completed int,
                mini_projects int,
                certifications_earned int,
                latest_project_score float,
                constraint pk_programming primary key (programming_id),
                constraint fk_student_id foreign key references student_table(student_id)
            )
            create table soft_skills(
                soft_skill_id varchar(30),
                student_id int,
                communication int,
                teamwork int,
                presentation int,
                leadership int,
                critical_thinking int,
                interpersonal_skills int,
                constraint pk_soft_skills primary key (soft_skill_id),
                constraint fk_student foreign key references students(student_id)
            )
            create table placements(
                placement_id varchar(30),
                student_id int,
                mock_interview_score float,
                internships_completed int,
                placement_status varchar(30),
                company_name text,
                placement_package int,
                interview_rounds_cleared int,
                placement_date date,
                constraint pk_placements primary key (placement_id)
                constraint fk_students foreign key students(student_id)
            ))
udhaya.exceute("commit")