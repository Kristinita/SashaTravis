module.exports = (grunt) ->
	grunt.initConfig
		pagespeed:
			options:
				key: "AIzaSyAQwCRSSLrClF0gnTlStTa1LmSmuGiAJrg"
				url: "https://developers.google.com"
			prod:
				options:
					paths: ["https://kristinita.github.io/Programs/KristinitaLuckyLink.html"]
					url: "https://developers.google.com/speed/docs/insights/v5/about#auth"
					locale: "en_US"
					strategy: "mobile"
					threshold: 99

	grunt.loadNpmTasks 'grunt-pagespeed'
	return
