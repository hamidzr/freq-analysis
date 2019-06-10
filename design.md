# Design Process


## Questions & Tradeoffs
- design drivers:
  - what are the requirements
  - developer time
  - horizontal scalability
  - developer scalability, how many developers are going to work on it
  - is it to be used on a phone?
    - do we ever want to ship it as an app

- specific qs:
  - how big a file do we want to support? spark?
  - how fast do we want to get them the results back?
  - how many users


- self contained client-side only app
  - utilize web workers
  - pros:
    - no server dependencyie
    - utilize a p2p network distribute the load on platform users. map reduce.
    - saving would be limited to the browser, a download option, or using thridparty service.
  - cons:
    - slower initial load
    - limited processing power: web assembly, multiple workers, utilize new chrome apis
- client-server setup:

- serverless: amazon lambda, EMR

### Stemming
- can we assume that 's', 'ing', 'ed', at the end of the words are meaningless? and that they all collapse to 0?
  - if not would need a way of determining if a word has meaning or not. spell check?
- plural form: are we excluding 'es'? 

## Assumptions:
- single user app
- no authentication, no AAA
