#!/bin/bash
commitHash=$(git rev-parse HEAD)
commitMessage=$(git log -1 --pretty=%B)
detailedMessage="Commit https://github.com/$TRAVIS_REPO_SLUG/commit/$commitHash pushed to GitHub Pages by Travis CI build $TRAVIS_BUILD_NUMBER — https://travis-ci.org/$TRAVIS_REPO_SLUG/builds/$TRAVIS_BUILD_ID"
git commit -m "$commitMessage" -m "$detailedMessage"
