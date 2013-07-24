=================
PurdueCourseSeats
=================


Important Notice
=================

- Backend start to run
- Stable version released


Introduction
-------------

- Website <http://purdue-class.chenrendong.com/>
- This is the server that parser purdue class seats remaining from Purdue website




Feature
-------

- This server keep tracking Purdue class seats every 20 seconds
- This server will update the latest information from Purdue website every 20 seconds
- **Only the classes that have already in the database will be updated** , which will save space and time
- Once new class which is not in database get queried, the new class information will be stored in database, so that it will be updated periodically
- The url for seats check is on <http://purdue-class.chenrendong.com/seats_check/> + `Class CRN`
- Once hit the url, the server will check if the database has that class data already, if not, then parser from Purdue website and store it into database
- Create an account and subscribe your desired CRN here
- Server will update the seats every 20 seconds


WeChat Support
--------------

- WeChat **AUTOREPLY** added, follow weChat ID(PCS-BoilerUp) and reply in the following format:
  * CRN(5 digits number)
  * CRN(5 digits number) + ' '(space) + Term
  * Class(no space, eg. CS180, or cs180)
  * Class(no space, eg. CS180, or cs180) + ' '(space) + Term
- weChat will autoreply the number of seats if CRN provided, and the class information(name, code, etc.) if class number provided.
- Default term is `Fall 2013` if no term provided, however, you can specify the term. 
- Notice: This server has smart recognition feature for term, you can use any format for term, for example:
  * `su 2012` / `su2012` / `12su` => `Summer 2012`
  * `fa2011` / `11 fa` / `fa11` => `Fall 2011`


API
-----

*URL: `http://purdue-class.chenrendong.com/seats_check/crns/`*
- `POST` to API URL with following format:
  * `{term:term,content:[*crns]}`
  * Example: `{"term":"201410","content":["10001","10002"]}`
- Server returns a list of results
- The result of a single class is always a **JSON** containing `{code : 0/1 , content : String or Tuple}`
  * code is the flag, 0 represents as failed, 1 represnts as successful
  * If code is 0, then content is a string containing the error message
  * If code is 1, then centent is a tuple containing all the class information
