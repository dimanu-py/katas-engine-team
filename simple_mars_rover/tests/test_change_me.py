from simple_mars_rover.src.mars_rover import Rover


class TestRover:

    def test_remains_initial_position_without_commands(self):
        # Given
        rover = Rover()
        # When
        final_position = rover.execute("")
        # Then
        assert final_position is not None
