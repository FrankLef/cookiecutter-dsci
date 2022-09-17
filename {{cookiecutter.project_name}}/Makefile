project_name := "{{ cookiecutter.project_name }}"
git_repo := "{{ cookiecutter.git_repo }}"

# the first target is the dfault
all: hello

hello:
	# Reference for customized echo
	# CMD equivalent @echo ^[[101;93;1mHello^[[0m
	# \x1b is ASCII hex for ESC
	@echo -e "\x1b[1;36mInfo!\x1b[0m"
	@echo -e "\x1b[1;32mSuccess!\x1b[0m"
	@echo -e "\x1b[1;33mWarning!\x1b[0m"
	@echo -e "\x1b[1;31mError!\x1b[0m"
	# on 1 line
	@echo -e "\x1b[1;37mHello World\x1b[0m"
	# now including a line feed
	@echo -e "\x1b[1;37mHello\x0AWorld\x1b[0m"
	# CMD equivalent @echo ^G, or @echo Alt+007, ASCII hex = \x7
	# make the beep sound
	@echo -e "\x7"

lint: isort flake8

isort:
	# run sort imports
	isort . -v
	@echo -e "\x1b[1;32misort ok!\x1b[0m"

flake:
	# run sort imports
	flake8 . -v
	@echo -e "\x1b[1;32mflake8 ok!\x1b[0m"

git_init:
	# Initialise git repo
	git init
	# use the "main" branch
	git branch -M main
	# add the remote
	git remote add origin ${git_repo}
	# add all files to git
	git add -A
	git commit -m "initialize"
	# -u switch makes the remote repo the default for theexisting project
	# -f switch forces Git to overwrite anyfile that already exist on GitHub
    git push -u -f origin main
	@echo -e "\x1b[1;32mgit initialized successfully.\x1b[0m"


test:
	@echo -e "\x1b[1;37mHello World\x1b[0m"