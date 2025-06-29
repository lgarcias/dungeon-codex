import os
import psycopg2

MIGRATIONS_DIR = os.path.join(os.path.dirname(__file__), "sql_migrations")

conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT")
)
conn.autocommit = True
cur = conn.cursor()

for filename in sorted(os.listdir(MIGRATIONS_DIR)):
    if filename.endswith(".sql"):
        path = os.path.join(MIGRATIONS_DIR, filename)
        print(f"📄 Applying migration: {filename}")
        with open(path, "r") as f:
            sql = f.read()
            cur.execute(sql)

print("✅ All migrations applied.")
cur.close()
conn.close()
