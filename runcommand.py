import subprocess

def run(args, **kwargs):
    print("This will run the following command:\n" + " ".join(args))
    if input("Continue? [Y/n] ").lower() in ["y", ""]:
        subprocess.run(args, **kwargs)
