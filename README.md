bot template for Dev not Prod

Quick setup — if you’ve done this kind of thing before

or	

git@github.com:keiraxlicious/kirara-kota-yo.git

Get started by creating a new file or uploading an existing file. We recommend every repository include a README, LICENSE, and .gitignore.

…or create a new repository on the command line



echo "# kirara-kota-yo" >> README.md

git init

git add README.md

git commit -m "first commit"

git branch -M main

git remote add origin git@github.com:keiraxlicious/kirakota-python.git

git push -u origin main

…or push an existing repository from the command line



git remote add origin git@github.com:keiraxlicious/kirakota-python.git

git branch -M main

git push -u origin main

…or import code from another repository

You can initialize this repository with code from a Subversion, Mercurial, or TFS project.


git remote -v


you just need git. doesn't matter if it's ZSH.

initiate the repo (if not already) with git init.

Then add it to a repo

then to add files do:

git add .

then:

git commit -m "Test"

then

git push

oh and use SSH not HTTP.
