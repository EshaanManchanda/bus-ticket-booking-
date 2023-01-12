import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ticketing.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS passenger(pid INTEGER PRIMARY KEY AUTOINCREMENT, fname text, lname text, phone text, email text, fromD text, toD text, totseat text, aduseat text, chiseat text, oldseat  text, type text, mealcost text, totfare text, pstatus text, bookingid text, transacttionid text, class text, noofmeals text, pricepermeal text)")
    con.commit()
    
    # cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT, name text, contact text,desc text)")
    # con.commit()
    
    # cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT, name text)")
    # con.commit()
    
    # cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT, Category text, Supplier text, Name text , price text , qty text, status text)")
    # con.commit()
    
    # cur.execute("CREATE TABLE IF NOT EXISTS customer(billno INTEGER PRIMARY KEY , name text, contact text,price text, date text)")
    # con.commit()
    
    
    
create_db()