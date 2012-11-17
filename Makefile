PREFIX="/usr"

all:
	@echo 'Nothing to build...'


install:
	mkdir -p "$(DESTDIR)$(PREFIX)/bin/"
	install -m 775 "src/git-touch"    "$(DESTDIR)$(PREFIX)/bin/"
	install -m 775 "src/git-cp"       "$(DESTDIR)$(PREFIX)/bin/"
	install -m 775 "src/git-chmod"    "$(DESTDIR)$(PREFIX)/bin/"
	install -m 775 "src/git-edit"     "$(DESTDIR)$(PREFIX)/bin/"
	install -m 775 "src/git-gimp"     "$(DESTDIR)$(PREFIX)/bin/"
	install -m 775 "src/git-pluma"    "$(DESTDIR)$(PREFIX)/bin/"
	install -m 775 "src/git-inkscape" "$(DESTDIR)$(PREFIX)/bin/"
	install -m 775 "src/git-todo"     "$(DESTDIR)$(PREFIX)/bin/"


uninstall:
	unlink "$(DESTDIR)$(PREFIX)/bin/git-touch"
	unlink "$(DESTDIR)$(PREFIX)/bin/git-cp"
	unlink "$(DESTDIR)$(PREFIX)/bin/git-chmod"
	unlink "$(DESTDIR)$(PREFIX)/bin/git-edit"
	unlink "$(DESTDIR)$(PREFIX)/bin/git-gimp"
	unlink "$(DESTDIR)$(PREFIX)/bin/git-pluma"
	unlink "$(DESTDIR)$(PREFIX)/bin/git-inkscape"
	unlink "$(DESTDIR)$(PREFIX)/bin/git-todo"


clean:
	@echo 'Nothing to clean...'
