from simple_mars_rover.src.mars_rover import Rover


class TestRover:

    def test_remains_initial_position_without_commands(self):
        # Given
        rover = Rover()
        # When
        final_position = rover.execute("")
        # Then
        assert final_position == "0:0:N"

    def test_move_forward_one_cell(self):
        rover = Rover()

        final_position = rover.execute("M")

        assert final_position == "1:0:N"

    def test_move_forward_two_cells(self):
        rover = Rover()

        final_position = rover.execute("MM")

        assert final_position == "2:0:N"

    def test_move_forward_three_cells(self):
        rover = Rover()

        final_position = rover.execute("MMM")

        assert final_position == "3:0:N"