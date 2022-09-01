import flproj_todo.etl


def test_etl():
    out = flproj_todo.etl.main()
    assert isinstance(out, dict)
