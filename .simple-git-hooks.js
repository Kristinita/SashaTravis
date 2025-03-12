/*
	@Author: Kristinita
	@Date: 2025-02-20 17:25:48
	@Last Modified by: Kristinita
	@Last Modified time: 2025-03-10 19:14:59
*/

/* #################
# simple-git-hooks #
####################
[OVERVIEW] Manage git hooks:
https://github.com/toplenboren/simple-git-hooks

[INFO] List of valid git hooks:
https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks
https://github.com/toplenboren/simple-git-hooks/blob/master/simple-git-hooks.js

[NOTE][REQUIRED] Re-activation simple-git-hooks (“npx simple-git-hooks”)
after each change in “commit-msg” command:
https://github.com/toplenboren/simple-git-hooks#update-git-hooks-command


[NOTE] I use “.simple-git-hooks.js”, not “simple-git-hooks.js” configuration file,
because when I run the “npx simple-git-hooks” command, the file “simple-git-hooks.js” opens in my Sublime Text editor.


[INFO] I migrated to simple-git-hooks from Husky:
https://typicode.github.io/husky/

1. Test script in “package.json” required for husky. I don’t want use
scripts from “package.json”, where I can’t add comments to scripts.

2. Configuration files doesn’t work for Husky 8

3. Husky has 3 steps for activation, simple-git-hooks — 1 step

[INFO] When migrating from Husky, is required to remove the Husky configuration::
https://github.com/toplenboren/simple-git-hooks#add-simple-git-hooks-to-the-project


[INFO] Using Commitlint with git hooks:
https://commitlint.js.org/#/guides-local-setup?id=add-hook

```
module.exports = {
  "commit-msg": "npx commitlint --edit \"$1\" --verbose"
};

```

[INFO] After the user writes “git commit …” and presses “Enter” Commitlint lint this commit.
If commit is non-valid, it’s not accepted and doesn’t appear to the commit log.
The user will be able to make a “git push” solely after adding a valid commit.

[INFO] “--edit "$1"” — get commit message from “./.git/COMMIT_EDITMSG”:
https://commitlint.js.org/#/reference-cli

[INFO] “commit-msg” hook required for linting commits via Commitlint:
https://typicode.github.io/husky/getting-started.html#automatic-recommended
*/


/* eslint-disable unicorn/prefer-module --

[NOTE] I can’t use “export default” instead of “module.exports” in this file. I get error:

```shell
[ERROR], Was not able to set git hooks.
Error: [ERROR] Config was not found! Please add `.simple-git-hooks.js` or `simple-git-hooks.js`
or `.simple-git-hooks.json` or `simple-git-hooks.json` or `simple-git-hooks` entry in package.json.
Check README for details
```
*/
module.exports = {
	"commit-msg": "npx commitlint --edit \"$1\" --verbose"
};

/* eslint-enable unicorn/prefer-module */
