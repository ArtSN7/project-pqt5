con = sqlite3.connect("basa.db")
cur = con.cursor()
result = cur.execute("""SELECT цена FROM buy""").fetchall()
count = 0
for i in result:
    count += int(i[0])

cur.execute("""UPDATE user SET потрачено = ?""", (count,))
con.commit()
cur.close()
con.close()