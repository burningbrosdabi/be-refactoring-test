## Requirements overview

### Project Overview

- Investigate given code.
- Develop API Endpoint of Campaign / Ad sets / Creatives data

## Project Structure

```
.
├── src                               # Main source code directory
│   ├── base                          # Project's settings
│   ├── core                          # Core models
│   ├── data                          # Data Application
│   │   ├── data_creation.py          # Creating dummy data
│   ├── manage.py
│   ├── db.sqlite3
├── .gitignore
├── README.md                         # Project Document
├── requirements.txt
```

# DB
- Data struture.
  - Under Campaign there are Ad sets, and under ad sets there are creatvies.

Please continue using the included SQLite database (db.sqlite3) for development.

## Requirements

1. Add nested data into API.

- /api/data/campaigns/
  this API should return campaign list with all nested Adsets & Creatives
- /api/data/adsets/
  this API should return adset list with all nested Creatives

**Me:** modify in data/serializers.py, data/models.py 

2. The other will be about prevent spaming API (Rate limit)

- We will ask them to limit the number of api calls per minute to this endpoint based on IP address. For example, my current IP address is 123.123.123.123, I’m only allowed to call to GET /products at most 10 times/minute. If I perform more, server will return the 429 status code with some suitable message warning about spamming api.

**Me:** I used throttling of DRF, and config them in base/settings.py

3. (Optional) Want to change base authentication field, username into user_id on base user model.

**Me:** used AbstractUser to change username into user_id by change USERNAME_FIELD. Modify in base/settings.py,  data/models.py

4. (Optional) Find out some bad codes on data application and refactor those.

**Me:** use prefetch_related to reduce the number of queries in data/views.py, changed method import, make data_creation.py to command

## Note

There could be multiple expected ways for answers. 
Show me your idea for refactoring this project.
Please find out some way to optimize performance.


