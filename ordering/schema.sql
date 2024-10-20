CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    product_name TEXT NOT NULL,
    product_type TEXT NOT NULL,  -- food or clothes
    quantity INTEGER,
    price REAL,
    status TEXT,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
