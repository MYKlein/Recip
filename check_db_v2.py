import sqlite3

# מסד נתונים 2
conn = sqlite3.connect("receipts_v2.db")
cursor = conn.cursor()

# שליפת כל השורות מטבלת receipts
cursor.execute("SELECT * FROM receipts")
rows = cursor.fetchall()

# הדפסה שורה־שורה
for row in rows:
    print(row)

conn.close()
import sqlite3

conn = sqlite3.connect('receipts_v2.db')
cursor = conn.cursor()

confirm = input("האם אתה בטוח שברצונך למחוק את כל הנתונים בטבלה receipts? (yes/no): ").strip().lower()
if confirm == "yes":
    cursor.execute("DELETE FROM receipts")
    conn.commit()
    print("כל הנתונים נמחקו מהטבלה receipts.")
else:
    print("הפעולה בוטלה.")

conn.close()


