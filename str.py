import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px

# Connect to MySQL
udhaya = mysql.connector.connect(
    host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
    user="NHk3ZCuh5QRYthi.root",
    password="AEpsh6zgl0yxb9td",
    port="4000",
    database="Placement_Eligibility_Application"
)
conn = udhaya.cursor()

st.set_page_config("Pesa")
st.title('Placement Eligibility Application')
#Placed Students
query10 = """
    select stu.name, stu.age, pla.student_id, pla.placement_status, pla.company_name, pla.placement_package, 
    pla.placement_date from student_table stu join placement_table pla on stu.student_id = pla.student_id
    where placement_status='Placed'
"""

st.code("Placed Students",language="sql")
if st.button("Submit"):
    df10=pd.read_sql(query10, con=udhaya)
    st.dataframe(df10)
#caption data
st.markdown("### Student Details")
st.caption("Details of Students table")
if st.checkbox("Student_table"):
    data6= pd.read_csv("student_table.csv")
    st.dataframe(data6)
st.caption("Details of Programming table")
if st.checkbox("Programming_table"):
    data5= pd.read_csv("programming_table.csv")
    st.dataframe(data5)
st.caption("Details of Soft Skills table")
if st.checkbox("soft_skills_table"):
    data8= pd.read_csv("soft_skills_table.csv")
    st.dataframe(data8)
st.caption("Details of Placement table")
if st.checkbox("Placement_table"):
    data7= pd.read_csv("placement_table.csv")
    st.dataframe(data7)
#query on assessment completed data
st.header("Student Assesssment Data")
query9 = """ select s.name,s.gender,p.assessment_completed from student_table s 
            join programming_table p on s.student_id=p.student_id
"""
df9=pd.read_sql(query9,con=udhaya)
# Unique options from the 'assessment_completed' column
options = ['Choose option'] + list(df9['assessment_completed'].unique())
selected = st.sidebar.selectbox("Assessment Completed", options)
# Filter DataFrame based on selection
filtered_df1 = df9[df9['assessment_completed'] == selected]
if selected != 'Choose option':
    filtered_df1 = df9[df9['assessment_completed'] == selected]
    st.dataframe(filtered_df1)
else:
    st.info("Please select an Student assesssment to view data.")


#####################################################Insights######################################################
# Query Data
query = "SELECT * FROM placement_table"
df = pd.read_sql(query, con=udhaya)

# Calculate metrics
total_students = len(df)
placed = df[df['placement_status'] == 'Placed']
not_placed = df[df['placement_status'] != 'Placed']

# Streamlit Title
st.title("Placement Insights Dashboard")

# Show Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Students", total_students)
col2.metric("Placed", len(placed))
col3.metric("Not Placed", len(not_placed))

# Pie Chart
st.subheader("Placement Distribution")
df_chart = pd.DataFrame({
    "Placement Status": ["Placed", "Not Placed"],
    "Count": [len(placed), len(not_placed)]
})
fig_pie = px.pie(df_chart, names='Placement Status', values='Count',
                 color='Placement Status',
                 color_discrete_map={"Placed": "green", "Not Placed": "red"},
                 hole=0.4)
st.plotly_chart(fig_pie)
#bar chart-- male and female--
#read all table
student_df = pd.read_sql("select * from student_table", con=udhaya)
programming_df = pd.read_sql("select * from programming_table", con=udhaya)
soft_skill_df = pd.read_sql("select * from soft_skills_table", con=udhaya)
placement_df = pd.read_sql("select * from placement_table", con=udhaya)
#merge all table
merged_df = student_df\
    .merge(programming_df, on = "student_id", how = "left")\
    .merge(soft_skill_df, on = "student_id", how = "left")\
    .merge(placement_df, on = "student_id", how="left")

#classified placed on male and female 
male_count = merged_df[(merged_df['gender'] == 'M') & (merged_df['placement_status'] == 'Placed')].shape[0]
female_count = merged_df[(merged_df['gender'] != 'M') & (merged_df['placement_status'] == 'Placed')].shape[0]

#metric
st.metric("Students Placed (Male)", male_count)
st.metric("Students Placed (Female)", female_count)
#bar chart
gender_placed = merged_df[merged_df['placement_status'] == 'Placed'].groupby('gender').size().reset_index(name='count')
fig = px.bar(gender_placed, x='gender', y='count', title="Gender-wise Placement Count", color='gender')
st.plotly_chart(fig)

                    