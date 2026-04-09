from fastapi import APIRouter
from schemas import UserRegistrationPydantic,UserLoginPydantic
from database import get_connection

auth_router = APIRouter()

#signup route
@auth_router.post("/register")
def register(UserRegistration: UserRegistrationPydantic):
    connection, cursor = get_connection()
    if connection is None:
        return {'error': 'Database connection failed'}
    try:
        # Check if email already exists
        cursor.execute("SELECT * FROM users WHERE email = %s", (UserRegistration.email,))
        existing_user = cursor.fetchone()
        if existing_user:
            return {'error': 'Email already registered'}
        # Insert new user
        cursor.execute("""
            INSERT INTO users (username, email, password)
            VALUES (%s, %s, %s)
        """, (UserRegistration.username, UserRegistration.email, UserRegistration.password))
        connection.commit()
        return {'message': 'User registered successfully'}
    except Exception as e:
        return {'error': str(e)}
    finally:
        cursor.close()
        connection.close()

# Login route
@auth_router.post('/login')
def login(UserLogin: UserLoginPydantic):
    connection, cursor = get_connection()
    if connection is None:
        return {'error': 'Database connection failed'}
    try:
        # Check if user exists
        cursor.execute("SELECT * FROM users WHERE email = %s", (UserLogin.email,))
        user = cursor.fetchone()
        if not user:
            return {'error': 'User not found'}
        # Check password
        if user[3] != UserLogin.password:
            return {'error': 'Incorrect password'}
        return {
            'message': 'Login successful',
            'user': {
                'id': user[0],
                'username': user[1],
                'email': user[2]
            }
        }
    except Exception as e:
        return {'error': str(e)}
    finally:
        cursor.close()
        connection.close()