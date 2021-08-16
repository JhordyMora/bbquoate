from bbquoate.lib import get_bbquote

def test_getbbquoate():
    response = get_bbquote()
    assert len(response)>0
