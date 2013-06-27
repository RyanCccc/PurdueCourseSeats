=================
PurdueCourseSeats
=================


Introduction
-------------

- This is the server that parser purdue class seats remaining from Purdue website
- This server store all the parsered data into Heroku Postgres database
- The url for seats check is on <http://purdue-class.herokuapp.com/seats_check/> + `Class CRN`
- Once hit the url, the server will check if the database has that class data already, if not, then parser from Purdue website and store it into database


Web Support
-----------

- Website <http://purdue-class.herokuapp.com/>
- Create an account and subscribe your desired CRN here
- Server will update the seats every 20 seconds


Feature
-------

- This server always return a **JSON** containing `{code : 0/1 , content : String or Tuple}`
  * code is the flag, 0 represents as failed, 1 represnts as successful
  * If code is 0, then content is a string containing the error message
  * If code is 1, then centent is a tuple containing max seats numbers followed by activated seats numbers and remaining seats numbers
- This server will update the latest information from Purdue website every 20 seconds
- **Only the classes that have already in the database will be updated** , which will save space and time
- Once new class which is not in database get queried, the new class information will be stored in database, so that it will be updated periodically


TODO
----

- Remove the class which hasn't been queried for a long time
