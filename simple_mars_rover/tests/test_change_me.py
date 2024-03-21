import pytest

from simple_mars_rover.src.mars_rover import Rover


class TestRover:

    def test_remains_initial_position_without_commands(self):
        # Given
        rover = Rover()
        # When
        final_position = rover.execute("")
        # Then
        assert final_position == "0:0:N"

    @pytest.mark.parametrize("steps, expected_final_position",
                             [
                                 (0, "0:0:N"),
                                 (1, "1:0:N"),
                                 (2, "2:0:N"),
                                 (9, "9:0:N"),
                                 (10, "0:0:N"),
                                 (15, "5:0:N"),
                                 (25, "5:0:N"),
                              ]

    )
    def test_move_forward(self, steps, expected_final_position):
        rover = Rover()

        final_position = rover.execute("M" * steps)

        assert final_position == expected_final_position
