DEBUG=JEKYLL_GITHUB_TOKEN=blank PAGES_API_URL=http://0.0.0.0

default:
	@gem install jekyll bundler && bundle install

update:
	@bundle update

clean:
	@bundle exec jekyll clean

build: clean
	@${DEBUG} bundle exec jekyll build --profile --config _config.yml,.debug.yml

server: clean
	@${DEBUG} bundle exec jekyll server --livereload --config _config.yml,.debug.yml
_config.yml

title: Your project name
lang: en
description: a catchy description for your project

remote_theme: rundocs/jekyll-rtd-theme

readme_index:
  with_frontmatter: true

exclude:
  - Makefile
  - CNAME
  - Gemfile
  - Gemfile.lock
