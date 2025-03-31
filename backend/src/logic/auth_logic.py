from src.models.user_model import User

def register_user(email: str, password: str, full_name: str = None, gender: str = None) -> User:

    if User.objects(email=email).first():
        raise ValueError("User already exists")
    
    new_user = User(
        email=email,
        password_hash=password, 
        full_name=full_name,
        gender=gender
    )
    new_user.save()
    return new_user

def login_user(email: str, password: str) -> User:
    
    user = User.objects(email=email).first()
    if not user:
        raise ValueError("User not found")
    
    if password != user.password_hash:
        raise ValueError("Invalid credentials")
    
    return user
