import sqlite3

# Nom de la base de données
DB_NAME = "todos_db.db"

def create_database_and_table():
    # Crée une nouvelle connexion (et potentiellement une nouvelle base de données)
    conn = sqlite3.connect(DB_NAME)
    
    # Crée un curseur pour exécuter des commandes SQL
    cursor = conn.cursor()

    # Crée la table "todos_tbl"
    cursor.execute("""
        CREATE TABLE "todos_tbl" (
            "id" INTEGER PRIMARY KEY AUTOINCREMENT,
            "userId" INTEGER,
            "title" TEXT,
            "completed" INTEGER
        );
    """)

    # Valide (commit) les changements
    conn.commit()

    # Ferme la connexion
    conn.close()

if __name__ == "__main__":
    create_database_and_table()
    print(f"Base de données {DB_NAME} créée avec succès avec la table 'todos_tbl'.")
