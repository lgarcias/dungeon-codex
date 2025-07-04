import pytest
from httpx import AsyncClient
from fastapi import status

pytestmark = pytest.mark.asyncio


async def test_create_user_success(client: AsyncClient):
    """
    Test creating a new user successfully.
    """
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "a_strong_password"
    }
    response = await client.post("/api/v1/users/", json=user_data)

    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["email"] == user_data["email"]
    assert data["username"] == user_data["username"]
    assert "id" in data
    assert "password" not in data  # Ensure password is not returned


async def test_create_user_duplicate_email(client: AsyncClient):
    """
    Test creating a user with an email that already exists.
    """
    user_data = {
        "username": "testuser2",
        "email": "test2@example.com",
        "password": "a_strong_password"
    }
    # Create the user first
    await client.post("/api/v1/users/", json=user_data)
    # Try to create it again
    response = await client.post("/api/v1/users/", json=user_data)

    assert response.status_code == status.HTTP_409_CONFLICT