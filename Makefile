all:
	@echo 'Nothing to build...'


install:
	mkdir -p "$(DESTDIR)$(PREFIX)/bin/"
	install -m 775 "src/git-touch" "$(DESTDIR)$(PREFIX)/bin/"
	install -m 775 "src/git-cp"    "$(DESTDIR)$(PREFIX)/bin/"
	install -m 775 "src/git-chmod" "$(DESTDIR)$(PREFIX)/bin/"
	install -m 775 "src/git-edit"  "$(DESTDIR)$(PREFIX)/bin/"


uninstall:
	unlink "$(DESTDIR)$(PREFIX)/bin/git-touch"
	unlink "$(DESTDIR)$(PREFIX)/bin/git-cp"
	unlink "$(DESTDIR)$(PREFIX)/bin/git-chmod"
	unlink "$(DESTDIR)$(PREFIX)/bin/git-edit"


clean:
	@echo 'Nothing to clean...'
