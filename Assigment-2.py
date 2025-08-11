import streamlit as st

import datetime
from dateutil.relativedelta import relativedelta
today = datetime.date.today()

st.write(today)

selected_date  = st.date_input(
    "Select a date",
    value=datetime.date(2003, 1, 1),  # Default date
    min_value=datetime.date(1990, 1, 1),  # Starting limit
    max_value=datetime.date.today()  # Today's date
)



diff = relativedelta(today, selected_date)

# Output
st.write("Selected date:", selected_date.strftime("%Y/%m/%d"))
st.write(f"Difference: {diff.years} years, {diff.months} months, {diff.days} days")
st.write(f"Total months: {diff.years * 12 + diff.months} months")