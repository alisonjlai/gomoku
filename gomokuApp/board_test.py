from board import Board


def test_constructor():
    bd = Board(200, 300, 3, 50)
    assert bd.width == 200
    assert bd.height == 300
    assert bd.grid_size == 3
    assert bd.space == 50
    assert bd.cell_size == 75
    assert bd.board == [['', '', ''], ['', '', ''], ['', '', '']]
    assert bd.stones == []

    bd2 = Board(400, 500, 0, 30)
    assert bd2.width == 400
    assert bd2.height == 500
    assert bd2.grid_size == 0
    assert bd2.space == 30
    assert bd2.board == []
    assert bd2.stones == []


def test_get_cell():
    bd = Board(300, 300, 4, 50)
    assert bd.get_cell(1, 2) == bd.board[1][2]
    assert bd.get_cell(6, 5) is None


def test_set_cell():
    bd = Board(100, 100, 4, 80)
    bd.set_cell(2, 3, "white")
    assert bd.board[2][3] == "white"
