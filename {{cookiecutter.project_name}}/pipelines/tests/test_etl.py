import flproj_todo.etl as etl


def test_etl():
    out = etl.main()
    assert isinstance(out, dict)
