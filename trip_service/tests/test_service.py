import pytest
from typing import Union

from trip_service.src.exceptions import UserNotLoggedInException
from trip_service.src.service import TripService
from trip_service.src.user import User


class SeamTripService(TripService):

    def __init__(self, user: Union[User, None]):
        self.user = user

    def get_logged_user(self) -> User:
        return self.user


class TestTripService:

    def test_user_cannot_get_trips_if_not_logged_in(self) -> None:
        not_logged_user = User()
        trip_service = SeamTripService(user=None)

        with pytest.raises(UserNotLoggedInException):
            trip_service.get_trips_by_user(not_logged_user)

    def test_user_without_friends_returns_empty_trip_list(self) -> None:
        friendless_user = User()
        trip_service = SeamTripService(user=friendless_user)

        trips = trip_service.get_trips_by_user(friendless_user)
        assert len(trips) == 0
