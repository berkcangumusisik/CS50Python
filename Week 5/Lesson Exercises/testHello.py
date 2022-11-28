from hello import hello

def test_hello():
    assert hello("Berkcan") == "Hello Berkcan!"

def test_arguement():
    for name in ["Hermione", "Ron", "Harry"]:
        assert hello(name) == "Hello " + name + "!"