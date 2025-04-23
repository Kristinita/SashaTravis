module.exports = (grunt) ->

	require("@dotenvx/dotenvx").config
		strict: true

	grunt.loadNpmTasks "grunt-shell"

	grunt.initConfig

		shell:
			appveyorlint:
				# command: "https ci.appveyor.com/api/projects/validate-yaml @appveyornonvalid.yml
				# 			--auth-type bearer --auth <%= process.env.KEY_APPVEYOR %> --body --ignore-stdin"
				command: "npx dotenvx run --env-file .env.credentials --strict --quiet --
							https ci.appveyor.com/api/projects/validate-yaml @appveyor.yml
							--auth-type bearer --auth <%= process.env.API_KEY_APPVEYOR %> --body --ignore-stdin |
							python -c \"import sys, json;
							kira_appveyor_json_response = json.load(sys.stdin);
							print(json.dumps(kira_appveyor_json_response, indent=2));
							kira_message_after_validation, kira_exit_code =
							(print('Your AppVeyor configuration file has an error. Please, fix it.'), exit(1))
							if kira_appveyor_json_response['isValid'] is False
							else (print('Congratulations! Your AppVeyor configuration file is valid!'), exit(0)) \""
