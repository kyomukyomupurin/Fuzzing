import subprocess
import sys
from pathlib import Path


def fuzz():
    subprocess.run("./gen", stdout=Path("gen.txt").open("w"))
    sol_out = subprocess.run("./sol", check=True, stdin=Path("gen.txt").open("r"), stdout=subprocess.PIPE).stdout
    stupid_out = subprocess.run("./stupid", check=True, stdin=Path("gen.txt").open("r"), stdout=subprocess.PIPE).stdout

    if sol_out != stupid_out:
        print("[test {:<3}] : NG".format(i + 1))

        Path("sol.txt").open("w").write(sol_out.decode("utf-8"))
        Path("stupid.txt").open("w").write(stupid_out.decode("utf-8"))

        print("Input : ")
        subprocess.run(["cat", "gen.txt"])
        print("Expected : ")
        subprocess.run(["cat", "stupid.txt"])
        print("Found : ")
        subprocess.run(["cat", "sol.txt"])

        exit(0)
    else:
        print("[test {:<3}] : OK".format(i + 1))


if __name__ == "__main__":
    subprocess.run(["make", "sol"])
    subprocess.run(["make", "stupid"])
    subprocess.run(["make", "gen"])

    for i in range(100 if len(sys.argv) < 2 else int(sys.argv[1])):
        fuzz()

    subprocess.run(["make", "clean"])
