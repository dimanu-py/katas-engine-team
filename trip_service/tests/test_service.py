import pytest

from trip_service.src.exceptions import UserNotLoggedInException
from trip_service.src.service import TripService
from trip_service.src.user import User


class SeamTripService(TripService):

    def get_logged_user(self) -> User:
        return None


class TestTripService:

    def test_user_cannot_get_trips_if_not_logged_in(self) -> None:
        not_logged_user = User()
        trip_service = SeamTripService()

        with pytest.raises(UserNotLoggedInException):
            trip_service.get_trips_by_user(not_logged_user)
