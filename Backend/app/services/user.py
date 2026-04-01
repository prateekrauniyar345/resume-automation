from app.models import User, UserResponse

def get_users(
    id: int | None = None,
    user_name: str | None = None,
    email: str | None = None
) -> list[UserResponse]:
    """
    Get users by optional filters.
    If no filters are provided, return all users.
    """
    try:
        query = User.query
        print("query is : ", query)
        if id is not None:
            query = query.filter_by(id=id)
        if user_name is not None:
            query = query.filter_by(user_name=user_name)
        if email is not None:
            query = query.filter_by(email=email)

        users = query.all()
        print("users are : ", users)
        return [UserResponse.model_validate(user) for user in users]

    except Exception as e:
        print(f"Error getting users: {e}")
        return []