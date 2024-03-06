from stone import Stone


def test_constructor():
    st = Stone(200, 300, "black")
    assert st.x == 200
    assert st.y == 300
    assert st.color == "black"
    assert st.frames_elapsed == 0

    st = Stone(400, 500, "white")
    assert st.x == 400
    assert st.y == 500
    assert st.color == "white"
    assert st.frames_elapsed == 0
