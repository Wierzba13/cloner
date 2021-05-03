import git
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--repo")
parser.add_argument("--clone", nargs = "*")
parser.add_argument("--output")
args = parser.parse_args()

repo = args.repo
outDir = args.output
dirs = args.clone

if(os.path.exists(outDir)):
    os.chdir(outDir)
    
    os.system("git init")
    os.system(f"git remote add -f origin {repo}")
    os.system("git config core.sparseCheckout true")
    for item in dirs:
        os.system(f"echo {item} >> .git/info/sparse-checkout")
        print(item)
    os.system("git pull origin main")
    os.system("rm -rf .git/")

else:
    print("Type correct directory!")
    exit()    
