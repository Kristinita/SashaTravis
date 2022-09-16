const penthouse = require('penthouse');
const fs = require('fs');

penthouse({
	// [INFO] “url: 'file:///D:/SashaDemoRepositories/SashaTravis/KiraExampleFailed.html',” for my Windows
	url: 'file:///home/travis/build/Kristinita/SashaTravis/KiraExampleFailed.html',
	cssString: 'body { color: red }'
})
	.then(criticalCss => {
		fs.writeFileSync('KiraOutfileFailed.css', criticalCss);
	});
