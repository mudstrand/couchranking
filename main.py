import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="mudstrand",
        password="123Fender51!",
        host="192.168.50.7",
        port=3307,
        database="mudstrand"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

cur.execute(
    "SELECT host,password FROM mysql.user where user=?", ('mudstrand',))

# Print Result-set
for (host, password) in cur:
    print(f"Host: {host}, Password: {password}")