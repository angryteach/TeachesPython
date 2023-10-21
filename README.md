# TeachesPython
Description: This repo is for my classes in Python.

## A note to my students
This repo is based on the code from our classes. Every commit will include one project or milestones for larger ones.

1. Clone the repo with: git clone https://github.com/angryteach/TeachesPython.git
2. Change into the directory: cd TeachesPython/
3. Explore git logs: git log
4. Browse projects: cd project-001

## GPG for signing commits

Learn to verify you commits on GitHub.

1. gpg --default-new-key-algo rsa4096 --gen-key
 1. gpg --edit-key XXXXXXX
2. git config --global user.signingkey XXXXXXX
3. gpg --armor --export XXXXXXX

Then add the exported key to GPG keys on GitHub
