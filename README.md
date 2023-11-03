# TeachesPython
Description: This repo is for my Python classes.

## A note to my students
This repo is based on the code from Python classes.

## How to use it
1. Clone the repo with: `git clone https://github.com/angryteach/TeachesPython.git`
2. Change into the directory: `cd TeachesPython/`
3. Explore git logs: `git log`
4. Browse projects: `cd project-001`
5. Run files with: `python main.py`
    1. or, depending on your environment, with: `python3 main.py`
6. open and edit files with: `vim main.py`
    1. or with: `nano main.py`

## GPG for signing commits

Learn to verify you commits on GitHub.

1. `gpg --default-new-key-algo rsa4096 --gen-key`
 1. `gpg --edit-key` XXXXXXX
2. `git config --global user.signingkey` XXXXXXX
3. `gpg --armor --export` XXXXXXX

Then add the exported key to GPG keys on GitHub

## Exercises

Every project will contain an errors.py file that you can download and correct for more practice.

Once you turn in your work, I shall upload the answers with my commentary most likely in the form of a gist.
