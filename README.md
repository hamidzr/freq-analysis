# Frequency Analyzer - Human Practice - HZ

## Prompt
- The application should accept a text document from the user, count how often each word is used in it, and report the top 25 most frequently used via a friendly and attractive web page.
- In order to make the results more useful, the analysis should extract the stems of the words so that different inflections of the same word are all counted in the same bucket. Use the following categories when stemming:
  - Regularly conjugated English verbs. For example, consider "talk", "talks", "talking", and "talked" to all be forms of "talk”, and “passes”, “passed”, and “passing” to all be forms of “pass”.
  - Regularly pluralized English nouns. For example, consider "cat" and "cats" to be forms of "cat".

- Exclude common English stop words from your counts. Allow the user to decide whether to exclude stop words from their analysis.
- Save the most recent 10 frequency analysis (original text, stop words setting, and resulting word frequencies), allowing the user to navigate back to view a previous analysis for comparison.
These persisted analysis should survive a restart of the server process.


## Steps
- count the tokens
- group using the stemming algorithm: conjugated and plural words
- UI
- save and present history

## TODO
- [x] create simple webserver, flask
- [x] simple database setup, sqlite, sqlalchemy?
  - [x] setup endpoints
- [x] create a UI

- [ ] do we want non alphanumeric string? what about pure numbers

- [ ] improve stemming
- [ ] add unit and e2e testing
- [ ] improve the frontend build setup, minify, etc using webpack?
- [ ] decouple request submission from getting the response. non blocking: sockets? pulling?
- [ ] use a logger instead of console.log
- [ ] keep it consistent between `camelCase` vs `snake_case`
- [ ] dev tools
  - [ ] add linters
  - [ ] watch and hot reload
- create an integrated build script


## Installation
- run `pipenv install` to install pip dependencies
- `pipenv shell` to enter the created virtualenv or preprend all other commands with `pipenv run`

- cd to `src/client` and run `npm i && npm run build`

### Env variables
```
export FLASK_APP=src/server/server.py
export FLASK_ENV=development
export FLASK_DEBUG=1
```

### Requirements
- python 3.7+
- pipenv
- nodejs 8+
