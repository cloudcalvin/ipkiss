from ipkiss import all as i3


def test_gdsii():
    s = i3.Structure()
    s.write_gdsii("out.gds")


if __name__ == "__main__":
    test_gdsii()
