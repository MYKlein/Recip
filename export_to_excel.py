import sqlite3
import pandas as pd

# התחברות למסד הנתונים
conn = sqlite3.connect("receipts_v2.db")

# שליפת כל הנתונים מהטבלה
df = pd.read_sql_query("SELECT * FROM receipts", conn)

# סגירת החיבור למסד
conn.close()

# שמירה לקובץ Excel בשם קבוע
df.to_excel("receipts_export.xlsx", index=False)

print("✅ הקובץ receipts_export.xlsx נוצר בהצלחה.")