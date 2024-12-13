from database.connection import get_sql_connection

# Function to fetch filtered records
def fetch_filtered_records(from_date, to_date):
    conn = get_sql_connection()
    cursor = conn.cursor()
    query = """
        SELECT BidSubmissionClosingDate, TenderTitle, ReferenceNumber, TenderID, EPublishedDate
        FROM dbo.Tenders
        WHERE BidSubmissionClosingDate >= ? AND BidSubmissionClosingDate <= ?
    """
    cursor.execute(query, from_date, to_date)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return [list(row) for row in data]