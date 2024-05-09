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
                                 (95, "5:0:N"),
                              ]
    )
    def test_move_forward(self, steps, expected_final_position):
        rover = Rover()

        final_position = rover.execute("M" * steps)

        assert final_position == expected_final_position

    @pytest.mark.parametrize("rotation_command, expected_final_position",
                             [("R", "0:0:E"),
                              ("RR", "0:0:S"),
                              ("RRR", "0:0:W"),
                              ("RRRR", "0:0:N"),
                              ("RRRRR", "0:0:E"),
                              ("L", "0:0:W"),
                              ("LL", "0:0:S"),
                              ("LLL", "0:0:E"),
                              ("LLLL", "0:0:N"),
                              ("LLLLL", "0:0:W"),
                              ("RL", "0:0:N"),
                              ("LR", "0:0:N")])
    def test_static_rotations(self, rotation_command, expected_final_position):
        rover = Rover()

        final_position = rover.execute(rotation_command)

        assert final_position == expected_final_position

    @pytest.mark.parametrize("command, expected_final_position",
                             [("RM", "0:1:E"),
                              ("RLM", "1:0:N"),
                              ("RMMM", "0:3:E"),
                              ("MMRMMLM", "3:2:N"),
                              # ("LLLLLMM", "0:8:W")
                              ])
    def test_movement_combinations(self, command, expected_final_position):
        rover = Rover()

        final_position = rover.execute(command)

        assert final_position == expected_final_position
