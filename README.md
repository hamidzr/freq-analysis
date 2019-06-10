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
- [ ] create simple webserver, flask
- [ ] simple database setup, sqlite, sqlalchemy?
- [ ] setup a UI
- [ ] improve stemming


## Installation

### Requirements
- python 3.7+

