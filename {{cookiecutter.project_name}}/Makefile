project_name := "{{ cookiecutter.project_name }}"
git_user := "{{ cookiecutter.__git_user }}"
git_email := "{{ cookiecutter.__git_email }}"
git_repo := "{{ cookiecutter.__git_repo }}"

# the first target is the default
all: hello

hello:
	# Reference for customized echo
	# CMD equivalent @echo ^[[101;93;1mHello^[[0m
	# \x1b is ASCII hex for ESC
	# see ANSI escape code at https://ss64.com/nt/syntax-ansi.html
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

poetry_start:
	poetry shell
	poetry update
	@echo -e "\x1b[1;32mpoetry ok!\x1b[0m"

lint: isort flake

isort:
	# run sort imports
	isort . -v
	@echo -e "\x1b[1;32misort ok!\x1b[0m"

flake:
	flake8 . -v
	@echo -e "\x1b[1;32mflake8 ok!\x1b[0m"

git_init:
	# initialize git_repo
	git init
	git branch -M main
	git remote add origin ${git_repo}
	git add -A
	git -c user.name=${git_user} -c user.email=${git_email} commit -m "initialize"
	git push -u -f origin main
	@echo -e "\x1b[1;32mgit initialized successfully.\x1b[0m"

test:
	@echo -e "\x1b[1;37mThis is a test\x1b[0m"
