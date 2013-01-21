PREFIX=/usr
BIN=/bin

all:
	@echo 'Nothing to build...'


install:
	rm src/git-*~ src/git-*.bak src/git-*.swp || exit 0
	mkdir -p "$(DESTDIR)$(PREFIX)$(BIN)/"
	install -m 755 "src/git-"* "$(DESTDIR)$(PREFIX)$(BIN)/"


uninstall:
	rm src/git-*~ src/git-*.bak src/git-*.swp || exit 0
	find src | sed -e 's/^src\///g' | while read line; do  \
	    unlink "$(DESTDIR)$(PREFIX)$(BIN)/$$line";         \
	done


clean:
	@echo 'Nothing to clean...'

