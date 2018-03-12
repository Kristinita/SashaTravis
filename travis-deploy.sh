#basic setttings
GH_USERNAME=Kristinita

#advanced settings
BRANCH=master
GITHUB_OUTPUT_FOLDER=built_website
PELICAN_OUTPUT_FOLDER=SashaDest
TARGET_REPO=$GH_USERNAME/SashaTravis.github.io.git

echo -e "Starting to deploy to GitHub Pages"
git config --global user.email "SashaChernykhEmpressOfUniverse@kristinita.ru"
git config --global user.name ${GITHUB_EMAIL}
# Pull hash and commit message of the most recent commit
commitHash=$(git rev-parse HEAD)
commitMessage=$(git log -1 --pretty=%B)
#get the current output in a separate directory
git clone --quiet --branch=$BRANCH https://${GITHUB_API_KEY}@github.com/$TARGET_REPO $GITHUB_OUTPUT_FOLDER
#copy the new output
cd $GITHUB_OUTPUT_FOLDER
rsync -rv --exclude=.git  ../$PELICAN_OUTPUT_FOLDER/* . --delete
#add, commit and push files
git add -A .
detailedMessage="Commit https://github.com/$TRAVIS_REPO_SLUG/commit/$commitHash pushed to GitHub Pages by Travis CI build $TRAVIS_BUILD_NUMBER — https://travis-ci.org/$TRAVIS_REPO_SLUG/builds/$TRAVIS_BUILD_ID"
git commit -m "$commitMessage" -m "$detailedMessage"
git push -fq origin $BRANCH
echo -e "Deploy completed"

