import plotly.express as px
import streamlit as st
import pandas as pd

# ---------------------------------------
# PAGE CONFIG
# ---------------------------------------

st.set_page_config(
    page_title="HR Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

def load_css():
    try:
        with open("styles/style.css") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True)
            
    except Exception as e:
        st.error(f"❌ CSS Error: {e}")

load_css()
            

st.markdown("""
<div style="
background: rgba(255, 99, 71, 0.6);
padding:20px;
border-radius:15px;
text-align:center;
margin-bottom:25px;
backdrop-filter:blur(15px);
">
<h3>📊 Real-Time Workforce Analytics Platform</h3>
<p>
Monitor employee trends, attrition patterns,
department insights and workforce performance.
</p>
</div>
""",unsafe_allow_html=True)

# ---------------------------------------
# LOAD DATA
# ---------------------------------------

df = pd.read_csv("employee_attrition_500.csv")

# ---------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------

st.sidebar.header("Filters")

department = st.sidebar.multiselect(
    "Department",
    options=df["Department"].unique(),
    default=df["Department"].unique()
)

gender = st.sidebar.multiselect(
    "Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

filtered_df = df[
    (df["Department"].isin(department)) &
    (df["Gender"].isin(gender))
]
st.info(
    "📊 Real-time Employee Analytics Dashboard | Data Analytics Internship Project"
)
# ---------------------------------------
# KPI CARDS
# ---------------------------------------

total = len(filtered_df)

left = len(
    filtered_df[
        filtered_df["Attrition"] == "Yes"
    ]
)

stayed = len(
    filtered_df[
        filtered_df["Attrition"] == "No"
    ]
)

rate = (left / total) * 100 if total > 0 else 0

col1, col2, col3, col4 = st.columns(4)

st.markdown("---")
col1,col2,col3,col4 = st.columns(4)

col1,col2,col3,col4 = st.columns(4)

cards = [
    ("👨‍💼 Total Employees", total, "#ff8fab"),
    ("🚪 Employees Left", left, "#ff758f"),
    ("✅ Employees Stayed", stayed, "#52b788"),
    ("📊 Attrition Rate", f"{rate:.2f}%", "#c77dff")
]

for col, (title, value, color) in zip(
    [col1, col2, col3, col4],
    cards
):
    with col:
        st.markdown(
            f"""
            <div style="
            background:linear-gradient(135deg,{color},#ffffff);
            padding:25px;
            border-radius:25px;
            text-align:center;
            color:#333333;
            border:1px solid rgba(255,255,255,0.6);
            box-shadow:0px 8px 25px rgba(0,0,0,0.15);
            ">
                <h3>{title}</h3>
                <h1>{value}</h1>
            </div>
            """,
            unsafe_allow_html=True
        )
# ---------------------------------------
# DATA TABLE
# ---------------------------------------

st.subheader("Employee Dataset")

st.dataframe(filtered_df)

# ---------------------------------------
# CHARTS
# ---------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("🏢 Department Distribution")

    dept = filtered_df["Department"].value_counts()

    fig = px.pie(
        values=dept.values,
        names=dept.index,
        hole=0.6,
        title=""
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        height=450
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    st.subheader("👨‍💼 Gender Distribution")

    gender_counts = filtered_df["Gender"].value_counts()

    fig = px.bar(
        x=gender_counts.index,
        y=gender_counts.values,
        color=gender_counts.index,
        title=""
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        height=450
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------------------------------

col3, col4 = st.columns(2)

with col3:

   st.subheader("⏰ Overtime Distribution")

overtime = filtered_df["OverTime"].value_counts()

fig = px.bar(
    x=overtime.index,
    y=overtime.values,
    color=overtime.index,
    title=""
)

fig.update_layout(
    height=450,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

with col4:

  st.subheader("📉 Attrition Distribution")

attrition = filtered_df["Attrition"].value_counts()

fig = px.pie(
    values=attrition.values,
    names=attrition.index,
    hole=0.5
)

fig.update_layout(
    height=450,
    paper_bgcolor="rgba(0,0,0,0)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------

st.subheader("💰 Monthly Income Trend")

fig = px.line(
    filtered_df,
    y="MonthlyIncome",
    markers=True
)

fig.update_layout(
    height=500,
    paper_bgcolor="rgba(0,0,0,0)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


st.subheader("🏢 Years At Company")

fig = px.histogram(
    filtered_df,
    x="YearsAtCompany",
    nbins=20
)

fig.update_layout(
    height=450,
    paper_bgcolor="rgba(0,0,0,0)"
)

st.plotly_chart(
    fig,
    use_container_width=True
    )