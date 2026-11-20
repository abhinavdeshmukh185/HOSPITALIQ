import pandas as pd
import plotly.express as px
import streamlit as st
import sqlite3
import pandas as pd
from pathlib import Path

# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="HOSPITALIQ",
    page_icon="🏥",
    layout="wide"
)

# --------------------------------
# DATABASE CONNECTION
# --------------------------------

BASE_DIR = Path(__file__).resolve().parent

DB_PATH = BASE_DIR / "database" / "hospital.db"

conn = sqlite3.connect(DB_PATH)

# --------------------------------
# CUSTOM CSS
# --------------------------------

# --------------------------------
# PROFESSIONAL BLUE & WHITE THEME
# --------------------------------

st.markdown("""
<style>

/* =====================================
   HOSPITALIQ - PROFESSIONAL BLUE & WHITE
   ===================================== */

/* MAIN BACKGROUND */
.stApp {
    background-color: #F4F7FC !important;
    color: #163A5F !important;
}

/* MAIN CONTENT */
.main .block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 100%;
}

/* =====================================
   SIDEBAR
   ===================================== */

[data-testid="stSidebar"] {
    background-color: #163E63 !important;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF;
}

/* SIDEBAR NAVIGATION */
[data-testid="stSidebar"] [role="radiogroup"] label {
    background-color: transparent;
    border-radius: 8px;
    padding: 5px;
    transition: background-color 0.2s ease;
}

[data-testid="stSidebar"] [role="radiogroup"] label:hover {
    background-color: #245780;
}

/* =====================================
   HEADINGS
   ===================================== */

h1 {
    color: #163E63 !important;
    font-weight: 800 !important;
}

h2 {
    color: #1B496F !important;
    font-weight: 700 !important;
}

h3 {
    color: #245780 !important;
    font-weight: 600 !important;
}

/* PARAGRAPHS */
p {
    color: #42566D;
}

/* =====================================
   METRIC CARDS
   ===================================== */

[data-testid="stMetric"] {
    background-color: #FFFFFF !important;
    padding: 22px;
    border-radius: 14px;
    border: 1px solid #DCE6F1;
    box-shadow: 0px 3px 10px rgba(22, 62, 99, 0.08);
    transition: transform 0.2s ease;
}

[data-testid="stMetric"]:hover {
    transform: translateY(-3px);
}

/* METRIC LABELS */
[data-testid="stMetricLabel"] {
    color: #64748B !important;
    font-weight: 600 !important;
}

/* METRIC VALUES */
[data-testid="stMetricValue"] {
    color: #0878C9 !important;
    font-size: 32px !important;
    font-weight: 800 !important;
}

/* =====================================
   CHART CONTAINERS
   ===================================== */

[data-testid="stPlotlyChart"] {
    background-color: #FFFFFF !important;
    border-radius: 14px;
    padding: 15px;
    border: 1px solid #DCE6F1;
    box-shadow: 0px 3px 10px rgba(22, 62, 99, 0.06);
}

[data-testid="stVegaLiteChart"] {
    background-color: #FFFFFF !important;
    border-radius: 14px;
    padding: 15px;
    border: 1px solid #DCE6F1;
}

/* =====================================
   DATA TABLES
   ===================================== */

[data-testid="stDataFrame"] {
    background-color: #FFFFFF !important;
    border-radius: 12px;
    border: 1px solid #DCE6F1;
    overflow: hidden;
}

[data-testid="stDataFrame"] button {
    color: #163E63 !important;
}

/* =====================================
   INPUT FIELDS
   ===================================== */

.stTextInput input,
.stNumberInput input,
.stDateInput input {
    background-color: #FFFFFF !important;
    color: #163E63 !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: 8px;
}

/* DROPDOWN */
.stSelectbox div[data-baseweb="select"] {
    background-color: #FFFFFF !important;
    border-radius: 8px;
    color: #163E63 !important;
}

/* =====================================
   BUTTONS
   ===================================== */

.stButton button {
    background-color: #0878C9 !important;
    color: #FFFFFF !important;
    border-radius: 8px;
    border: none;
    padding: 8px 20px;
    font-weight: 600;
    transition: background-color 0.2s ease;
}

.stButton button:hover {
    background-color: #075FA0 !important;
    color: #FFFFFF !important;
}

/* =====================================
   SUCCESS MESSAGES
   ===================================== */

[data-testid="stAlert"] {
    border-radius: 10px;
}

/* =====================================
   DATABASE STATUS CARD
   ===================================== */

.db-status {
    background-color: #064E3B !important;
    color: #FFFFFF !important;
    padding: 18px 15px;
    border-radius: 10px;
    border: 1px solid #10B981;
    font-size: 16px;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 10px;
    margin-top: 25px;
    margin-bottom: 15px;
}

/* DATABASE STATUS DOT */
.status-dot {
    height: 10px;
    width: 10px;
    min-width: 10px;
    background-color: #34D399 !important;
    border-radius: 50%;
    display: inline-block;
}

/* =====================================
   DIVIDERS
   ===================================== */

hr {
    border-color: #DCE6F1 !important;
}

/* =====================================
   HIDE STREAMLIT DECORATIONS
   ===================================== */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* =====================================
   SIDEBAR DATABASE STATUS
   ===================================== */

[data-testid="stSidebar"] .db-status {
    background-color: #064E3B !important;
    color: #FFFFFF !important;
    border: 1px solid #10B981 !important;
}

[data-testid="stSidebar"] .db-status span {
    color: #FFFFFF !important;
}

/* =====================================
   END OF HOSPITALIQ CSS
   ===================================== */

</style>
""", unsafe_allow_html=True)

# --------------------------------
# SIDEBAR
# --------------------------------

st.sidebar.title("🏥 HOSPITALIQ")

st.sidebar.caption(
    "Hospital Analytics Platform"
)

st.sidebar.divider()

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "Dashboard Overview",
        "Appointment Analytics",
        "Department Analytics",
        "Bed Occupancy",
        "Data Explorer"
    ]
)
st.sidebar.markdown(
    """
    <div class="db-status">
        <span class="status-dot"></span>
        Database Connected
    </div>
    """,
    unsafe_allow_html=True
)

# --------------------------------
# FETCH DATABASE INFORMATION
# --------------------------------

tables = pd.read_sql_query(
    "SELECT name FROM sqlite_master WHERE type='table'",
    conn
)

def get_count(table_name):

    available_tables = tables["name"].tolist()

    if table_name in available_tables:

        return pd.read_sql_query(
            f"SELECT COUNT(*) AS total FROM {table_name}",
            conn
        ).iloc[0]["total"]

    return 0


total_appointments = get_count("appointments")
total_admissions = get_count("admissions")
total_departments = get_count("departments")
total_doctors = get_count("doctors")

# --------------------------------
# DASHBOARD OVERVIEW
# --------------------------------

if page == "Dashboard Overview":

    st.title("🏥 HOSPITALIQ Dashboard")

    st.caption(
        "Hospital Capacity & Appointment Analytics"
    )

    st.divider()

    st.subheader("Hospital Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Appointments",
        total_appointments
    )

    col2.metric(
        "Total Admissions",
        total_admissions
    )

    col3.metric(
        "Departments",
        total_departments
    )

    col4.metric(
        "Doctors",
        total_doctors
    )

    st.divider()

    st.subheader("Database Information")

    st.write(
        f"Total Database Tables: {len(tables)}"
    )

    st.dataframe(
        tables,
        use_container_width=True,
        hide_index=True
    )

# --------------------------------
# OTHER MODULES
# --------------------------------

elif page == "Appointment Analytics":

    st.title("🗓️ Appointment Analytics")
    st.subheader("Hospital Appointment Performance Dashboard")

    # Fetch appointment data
    with sqlite3.connect("database/hospital.db") as db:
        appointments = pd.read_sql_query(
            "SELECT * FROM appointments", db
        )

    # Convert date and time
    appointments["scheduled_time"] = pd.to_datetime(
        appointments["scheduled_time"], errors="coerce"
    )

    appointments["actual_time"] = pd.to_datetime(
        appointments["actual_time"], errors="coerce"
    )

    # Appointment statistics
    total = len(appointments)

    status_counts = appointments["status"].str.strip().str.lower().value_counts()

    completed = status_counts.get("completed", 0)
    cancelled = status_counts.get("cancelled", 0)
    scheduled = status_counts.get("scheduled", 0)
    no_show = status_counts.get("no-show", 0)

    cancellation_rate = (cancelled / total * 100) if total else 0

    # Calculate waiting time
    completed_data = appointments[
        appointments["status"].str.strip().str.lower() == "completed"
    ].copy()

    completed_data["delay_minutes"] = (
        completed_data["actual_time"] -
        completed_data["scheduled_time"]
    ).dt.total_seconds() / 60

    completed_data["delay_minutes"] = (
        completed_data["delay_minutes"].clip(lower=0)
    )

    average_wait = completed_data["delay_minutes"].mean()

    # KPI Cards
    st.markdown("---")
    st.subheader("Appointment Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Appointments", total)
    col2.metric("Completed", completed)
    col3.metric("Cancelled", cancelled)
    col4.metric("No-Show", no_show)

    col5, col6 = st.columns(2)

    col5.metric(
        "Cancellation Rate",
        f"{cancellation_rate:.2f}%"
    )

    col6.metric(
        "Average Waiting Time",
        f"{average_wait:.2f} min" if pd.notna(average_wait) else "N/A"
    )

    # Appointment Status Chart
    st.markdown("---")
    st.subheader("Appointment Status Distribution")

    status_data = appointments["status"].value_counts().reset_index()
    status_data.columns = ["Status", "Count"]

    fig = px.pie(
        status_data,
        names="Status",
        values="Count",
        title="Appointment Status Distribution",
        hole=0.35
    )
    fig.update_layout(
    template="plotly_white",
    paper_bgcolor="#FFFFFF",
    plot_bgcolor="#FFFFFF",
    font_color="#163E63"
)
    st.plotly_chart(fig, use_container_width=True)

    # Hourly Demand Analysis
    st.markdown("---")
    st.subheader("Hourly Appointment Demand")

    appointments["appointment_hour"] = (
        appointments["scheduled_time"].dt.hour
    )

    hourly_demand = (
        appointments.groupby("appointment_hour")
        .size()
        .reset_index(name="Total Appointments")
    )

    fig2 = px.bar(
        hourly_demand,
        x="appointment_hour",
        y="Total Appointments",
        title="Appointments by Hour",
        labels={
            "appointment_hour": "Appointment Hour",
            "Total Appointments": "Number of Appointments"
        }
    )

    st.plotly_chart(fig2, use_container_width=True)

    # Appointment Records
    st.markdown("---")
    st.subheader("Appointment Records")

    st.dataframe(
        appointments,
        use_container_width=True
    )

elif page == "Department Analytics":

    st.title("🏥 Department Analytics")
    st.subheader("Hospital Department Performance")

    # Fetch department analytics
    department_data = pd.read_sql_query("""
        SELECT
            d.department_name,

            (SELECT COUNT(*)
             FROM appointments a
             WHERE a.department_id = d.department_id)
             AS total_appointments,

            (SELECT COUNT(*)
             FROM doctors doc
             WHERE doc.department_id = d.department_id)
             AS total_doctors,

            (SELECT COUNT(*)
             FROM admissions ad
             WHERE ad.department_id = d.department_id)
             AS total_admissions

        FROM departments d
    """, conn)

    # Summary Metrics
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Departments",
        len(department_data)
    )

    col2.metric(
        "Total Appointments",
        int(department_data["total_appointments"].sum())
    )

    col3.metric(
        "Total Doctors",
        int(department_data["total_doctors"].sum())
    )

    st.divider()

    # Department Appointment Demand
    st.subheader("Department-wise Appointment Demand")

    chart_data = department_data.set_index(
        "department_name"
    )

    st.bar_chart(
        chart_data["total_appointments"]
    )

    st.divider()

    # Department Records
    st.subheader("Department Performance Records")

    st.dataframe(
        department_data,
        use_container_width=True
    )

elif page == "Bed Occupancy":

    st.title("🛏️ Bed Occupancy Analytics")
    st.subheader("Hospital Bed Utilization Dashboard")

    # Fetch database records
    bed_capacity = pd.read_sql_query(
        "SELECT * FROM bed_capacity", conn
    )

    admissions = pd.read_sql_query(
        "SELECT * FROM admissions", conn
    )

    departments = pd.read_sql_query(
        "SELECT * FROM departments", conn
    )

    # Convert dates
    admissions["admission_date"] = pd.to_datetime(
        admissions["admission_date"]
    )

    admissions["discharge_date"] = pd.to_datetime(
        admissions["discharge_date"]
    )

    # Select analysis date
    min_date = admissions["admission_date"].min().date()
    max_date = admissions["discharge_date"].max().date()

    selected_date = st.date_input(
        "Select Date",
        value=max_date,
        min_value=min_date,
        max_value=max_date
    )

    selected_date = pd.Timestamp(selected_date)

    # Calculate occupied beds
    occupied = admissions[
        (admissions["admission_date"] <= selected_date) &
        (admissions["discharge_date"] > selected_date)
    ]

    occupied_count = occupied.groupby(
        "department_id"
    ).size().reset_index(name="occupied_beds")

    # Merge department information
    bed_data = bed_capacity.merge(
        departments,
        on="department_id"
    )

    bed_data = bed_data.merge(
        occupied_count,
        on="department_id",
        how="left"
    )

    bed_data["occupied_beds"] = (
        bed_data["occupied_beds"].fillna(0)
    )

    bed_data["available_beds"] = (
        bed_data["total_beds"] - bed_data["occupied_beds"]
    )

    bed_data["occupancy_percentage"] = (
        bed_data["occupied_beds"] /
        bed_data["total_beds"] * 100
    )

    # Summary Metrics
    total_beds = int(bed_data["total_beds"].sum())
    occupied_beds = int(bed_data["occupied_beds"].sum())
    available_beds = total_beds - occupied_beds

    occupancy_rate = (
        occupied_beds / total_beds * 100
        if total_beds > 0 else 0
    )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Beds", total_beds)
    col2.metric("Occupied Beds", occupied_beds)
    col3.metric("Available Beds", available_beds)
    col4.metric("Occupancy Rate", f"{occupancy_rate:.2f}%")

    st.divider()

    # Department-wise utilization
    st.subheader("Department-wise Bed Utilization")

    chart_data = bed_data.set_index("department_name")

    st.bar_chart(
        chart_data[
            ["occupied_beds", "available_beds"]
        ]
    )

    st.divider()

    # Occupancy percentage
    st.subheader("Department Occupancy Percentage")

    st.bar_chart(
        chart_data["occupancy_percentage"]
    )

    st.divider()

    # Bed Records
    st.subheader("Bed Occupancy Records")

    st.dataframe(
        bed_data[
            [
                "department_name",
                "total_beds",
                "occupied_beds",
                "available_beds",
                "occupancy_percentage"
            ]
        ],
        use_container_width=True
    )

elif page == "Data Explorer":

    st.title("📊 Database Explorer")

    selected_table = st.selectbox(
        "Select Database Table",
        tables["name"].tolist()
    )

    if selected_table:

        data = pd.read_sql_query(
            f'SELECT * FROM "{selected_table}"',
            conn
        )

        st.subheader(f"{selected_table.title()} Records")

        # Search Feature
        search = st.text_input("🔍 Search Records")

        filtered_data = data

        if search:
            mask = data.astype(str).apply(
                lambda col: col.str.contains(
                    search, case=False, na=False
                )
            ).any(axis=1)

            filtered_data = data[mask]

        st.write("Total Records:", len(filtered_data))

        # Display Records
        st.dataframe(
            filtered_data,
            use_container_width=True
        )

        # Download CSV
        csv = filtered_data.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name=f"{selected_table}.csv",
            mime="text/csv"
        )

conn.close()