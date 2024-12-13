import streamlit as st
from datetime import datetime, timedelta
from email_sender.email_sender import send_email
from database.crud_operations import fetch_filtered_records
import pandas as pd

def run():
    # Streamlit UI
    st.title("Mail Upcoming Tenders")

    # 1st Row: From Date-Time (Disabled Input) and To Date-Time (User-selectable)
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("From Date-Time")
        from_date = datetime.now()
        st.text_input("Current Date-Time", value=from_date.strftime("%Y-%m-%d %H:%M:%S"), disabled=True)

    with col2:
        st.subheader("To Date-Time")
        min_date = from_date.date()
        default_to_date = from_date + timedelta(days=2)
        to_date = st.date_input("To Date", value=default_to_date.date(), min_value=min_date)
        to_date = datetime.combine(to_date, datetime.now().time())

    # 2nd Row: Recipient Email (with Default Value)
    st.subheader("Recipient Email")
    recipient_email = st.text_input("Recipient Email")

    # Fetch Data and Send Email Buttons in Same Row
    col1, col2 = st.columns([1, 1])
    with col1:
        fetch_button = st.button("Fetch Tenders")

    with col2:
        send_button = st.button("Send Email")

    # When "Fetch Data" is clicked, fetch and store data in session state
    if fetch_button:
        with st.spinner("Fetching Tenders..."):
            records = fetch_filtered_records(from_date, to_date)
            if records:
                st.success("Tenders fetched successfully!")
                df = pd.DataFrame(
                    records, columns=["BidSubmissionClosingDate", "TenderTitle", "ReferenceNumber", "TenderID", "EPublishedDate"]
                )
                st.write(df)
                # Store records in session state
                st.session_state.records = records
            else:
                st.warning("No records found for the selected date range.")

    # When "Send Email" is clicked, send the email with the fetched data
    if send_button:
        # Ensure that records exist in session state
        if 'records' in st.session_state:
            if recipient_email:
                with st.spinner("Sending email..."):
                    try:
                        send_email(st.session_state.records, recipient_email)
                        st.success("Email sent successfully!")
                    except Exception as e:
                        st.error(f"Error sending email: {e}")
            else:
                st.warning("Please provide a recipient email.")
        else:
            st.warning("Please fetch the data first.")