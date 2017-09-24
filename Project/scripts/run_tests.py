from subprocess import Popen

if __name__ == "__main__":
    p = Popen(["pytest -q ../tests/test_grammar.py"], shell=True)
    p.wait()
