from app.models import User, UserResponse
from app.database import db

# service function to get user information
def get_user_b(
        id: int | None = None,
        username: str | None = None,
        email: str | None = None
) -> UserResponse | None:
    '''
    get user information for user with any param:
    - id: int
    - username: str
    - email: str
    '''
    try:
        query = User.query
        if id is not None:
            query = query.filter_by(id=id)
        if username is not None:
            query = query.filter_by(username=username)
        if email is not None:
            query = query.filter_by(email=email)
        
        user = query.first()
        if user is None:
            return None
        
        return UserResponse.from_orm(user)
    except Exception as e:
        print(f"Error getting user: {e}")
        return None
