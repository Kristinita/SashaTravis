#basic setttings
GH_USERNAME=Kristinita

#advanced settings
BRANCH=master
PELICAN_OUTPUT_FOLDER=SashaDest
TARGET_REPO=$GH_USERNAME/SashaTravis.github.io.git

echo -e "Starting to deploy to GitHub Pages\n"
git config --global user.email "travis@travis-ci.org"
git config --global user.name "Travis"
# Pull hash and commit message of the most recent commit
commitHash=$(git rev-parse HEAD)
commitMessage=$(git log -1 --pretty=%B)
#get the current output in a separate directory
git clone --quiet --branch=$BRANCH https://${GH_PAGES}@github.com/$TARGET_REPO $PELICAN_OUTPUT_FOLDER > /dev/null
#copy the new output
cd $PELICAN_OUTPUT_FOLDER
rsync -rv --exclude=.git  ../$PELICAN_OUTPUT_FOLDER/* . --delete
#add, commit and push files
git add -A .
detailedMessage="Commit $commitHash pushed to GitHub Pages by Travis build $TRAVIS_BUILD_NUMBER"
git commit -m "$commitMessage" -m "$detailedMessage"
git push -fq origin $BRANCH > /dev/null || exit $?
echo -e "Deploy completed\n"

