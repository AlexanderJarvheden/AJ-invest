import sqlite3

con = sqlite3.connect(r"app/database/OMXS30.db")
cur = con.cursor()

stockTable = "CREATE TABLE stocks(company, ticker, price, category)"

res = cur.execute(stockTable)
res.fetchone() # fetches the resulting row
con.commit() # commits the transaction

