/*
[NOTE] Configuration Pa11y CI file for Linux completely repeats the contents of “.pa11yci.js”
except that it contains the “chromeLaunchConfig” option.
*/

module.exports = {
	defaults: {
		/* [REQUIRED] Path to Chrome executable file on Linux:
		https://github.com/pa11y/pa11y-ci#pa11y-ci-3-and-ubuntu
		https://github.com/pa11y/pa11y-ci/issues/198#issuecomment-1418343240 */
		chromeLaunchConfig: {
			"executablePath": "/usr/bin/google-chrome"
		},
		hideElements: [
			"code",
			"#___gcse_0", ".gstl_50",
			".skiptranslate", "#goog-gt-votingForm", "#goog-gt-votingInputSrcLang",
			"#goog-gt-votingInputTrgLang", "#goog-gt-votingInputSrcText", "#goog-gt-votingInputTrgText",
			"#goog-gt-votingInputVote", "#goog-gt-votingHiddenPane"
			]
	}
};
