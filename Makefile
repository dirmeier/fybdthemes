PKG_VERSION=`hatch version`

tag:
	git tag -a v${PKG_VERSION} -m v${PKG_VERSION}
	git push --tag


readme:
	jupyter nbconvert --execute README.ipynb --to markdown