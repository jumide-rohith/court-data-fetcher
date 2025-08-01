import sqlite3

def init_db():
    conn = sqlite3.connect("court.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS query_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_type TEXT,
            case_number TEXT,
            filing_year TEXT,
            raw_html TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def log_query(case_type, case_number, filing_year, raw_html):
    conn = sqlite3.connect("court.db")
    c = conn.cursor()
    c.execute('''
        INSERT INTO query_logs (case_type, case_number, filing_year, raw_html)
        VALUES (?, ?, ?, ?)
    ''', (case_type, case_number, filing_year, raw_html))
    conn.commit()
    conn.close()
