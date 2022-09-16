const penthouse = require('penthouse');
const fs = require('fs');

penthouse({
	// [INFO] “url: 'file:///D:/SashaDemoRepositories/SashaTravis/KiraExamplePassed.html',” for my Windows
	url: 'file:///home/Travis/Kristinita/SashaTravis/KiraExamplePassed.html',
	cssString: 'body { color: red }'
})
	.then(criticalCss => {
		fs.writeFileSync('KiraOutfilePassed.css', criticalCss);
	});
