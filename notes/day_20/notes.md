# Day 20 Notes

## Discussion points

Query parameters to be able to search using various fields

Break out First and Last Name
Need to now handle the get_one with the first and last name separated out.

[DONE] Take a look at Upwork
https://www.upwork.com/ab/jobs/search/?contractor_tier=1&q=python&sort=recency&user_location_match=1


[DONE] Samuel: Look at Samuel's get_all and see what is going on.
[DONE] Also, how do you use that for the get_one

[DONE] Ricky: Fix the enumeration list

Assignment for a tic-tac-toe game.
- On Thursday, we should have the approach documented and pseudo code

Try using a different key for contact (i.e. lastname+firstname)

field: contact_id

before you insert:
- query the database for the largest contact_id
    - self.collection('contact').find({}).sort({'contact_id': -1}).limit(1)
- 