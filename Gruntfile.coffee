module.exports = (grunt) ->
	grunt.initConfig
		pagespeed:
			options:
				# [INFO] That get a key, create a project → visit API page:
				# https://console.developers.google.com/apis
				# → API Library → Other (in page bottom) → PageSpeed Insights API:
				# https://console.developers.google.com/apis/library
				key: "AIzaSyAQwCRSSLrClF0gnTlStTa1LmSmuGiAJrg"
				url: "https://developers.google.com"
			prod:
				options:
					paths: ["https://kristinita.github.io/Programs/KristinitaLuckyLink.html"]
					url: "https://developers.google.com/speed/docs/insights/v5/about#auth"
					locale: "en_US"
					strategy: "mobile"
					threshold: 80

	grunt.loadNpmTasks 'grunt-pagespeed'
	return
