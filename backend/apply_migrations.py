import os
import psycopg2
from psycopg2 import sql

MIGRATIONS_DIR = os.path.join(os.path.dirname(__file__), "sql_migrations")

def run_migrations():
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT")
        )
        conn.autocommit = False  # Usar transacciones para seguridad
        cur = conn.cursor()

        # 1. Crear la tabla de seguimiento de migraciones si no existe
        cur.execute("""
            CREATE TABLE IF NOT EXISTS schema_migrations (
                version VARCHAR(255) PRIMARY KEY
            );
        """)

        # 2. Obtener las migraciones ya aplicadas
        cur.execute("SELECT version FROM schema_migrations;")
        applied_migrations = {row[0] for row in cur.fetchall()}

        # 3. Obtener todas las migraciones de los archivos
        all_migrations = sorted([f for f in os.listdir(MIGRATIONS_DIR) if f.endswith(".sql")])

        # 4. Determinar y aplicar las migraciones pendientes
        pending_migrations = [m for m in all_migrations if m not in applied_migrations]

        if not pending_migrations:
            print("✅ Database is up to date. No new migrations to apply.")
        else:
            for filename in pending_migrations:
                path = os.path.join(MIGRATIONS_DIR, filename)
                print(f"📄 Applying migration: {filename}")
                with open(path, "r") as f:
                    cur.execute(f.read())
                cur.execute(sql.SQL("INSERT INTO schema_migrations (version) VALUES ({})").format(sql.Literal(filename)))
                print(f"✔️ Successfully applied and recorded: {filename}")

        conn.commit()
        print("✅ All pending migrations applied successfully.")

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"❌ Error applying migrations: {error}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    run_migrations()
