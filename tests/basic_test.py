from ipkiss import all as i3

def test_make_structure():
    s = i3.Structure()
    s.write_gdsii("out.gds")
