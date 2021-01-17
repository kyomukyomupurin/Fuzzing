import subprocess
import sys


def fuzz():
    subprocess.run("./gen", stdout=open("./gen.txt", "w"))
    sol_out = subprocess.run("./sol", check=True, stdin=open("./gen.txt", "r"), stdout=subprocess.PIPE).stdout
    stupid_out = subprocess.run("./stupid", check=True, stdin=open("./gen.txt", "r"), stdout=subprocess.PIPE).stdout

    if sol_out != stupid_out:
        print("[test {:<3}] : NG".format(i + 1))

        open("./sol.txt", "w").write(sol_out.decode("utf-8"))
        open("./stupid.txt", "w").write(stupid_out.decode("utf-8"))

        print("Input : ")
        subprocess.run("cat ./gen.txt", shell=True)
        print("Expected : ")
        subprocess.run("cat ./stupid.txt", shell=True)
        print("Found : ")
        subprocess.run("cat ./sol.txt", shell=True)

        exit(0)
    else:
        print("[test {:<3}] : OK".format(i + 1))

if __name__ == '__main__':
    subprocess.run(["make sol"], shell=True)
    subprocess.run(["make stupid"], shell=True)
    subprocess.run(["make gen"], shell=True)

    for i in range(100 if len(sys.argv) < 2 else int(sys.argv[1])):
        fuzz()

    subprocess.run(["make clean"], shell=True)