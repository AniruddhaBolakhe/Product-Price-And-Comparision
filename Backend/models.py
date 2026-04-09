from database import get_connection

def create_tables():
    connection, cursor = get_connection()
    
    if connection is None:
        print("Failed to connect to database")
        return None

    # 1. Users Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # 2. Products Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            url VARCHAR(500) NOT NULL,
            image_url VARCHAR(500),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # 3. Price Sources Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS price_sources (
            id INT AUTO_INCREMENT PRIMARY KEY,
            product_id INT,
            source_name VARCHAR(100) NOT NULL,
            source_url VARCHAR(500) NOT NULL,
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
    """)

    # 4. Price History Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS price_history (
            id INT AUTO_INCREMENT PRIMARY KEY,
            product_id INT,
            price DECIMAL(10, 2) NOT NULL,
            recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
    """)

    # 5. Watchlists Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS watchlists (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            product_id INT,
            added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
    """)

    # 6. Alerts Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            product_id INT,
            target_price DECIMAL(10, 2) NOT NULL,
            is_triggered BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (product_id) REFERENCES products(id)
        )
    """)

    connection.commit()
    print("All tables created successfully!")
    
    cursor.close()
    connection.close()

create_tables()