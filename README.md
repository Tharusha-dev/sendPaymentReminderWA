# Send payment reminders via WhatsApp from a MongoDB Atlas database 🐍🍃

This script uses

- Twilio
- PyMongo

to send payment reminders via WhatsApp to customers whos payment is due today. The script uses worldtime API to get today in a specified timezone and country.

## Database structure

This script assumes your database has a collection with,

- customer WhatsApp number
- Product Name
- Payment

in the same docuemnt.

## Example use case

Scedule to run this script in a lambda function once a day to send payment reminders.

## Requirments

- twilio version 8.11.1
- pymongo version 4.6.2

## Important

To install dependencies locally run,

```console
pip3 install -r requirments.tct
```

To use python dependencies in a lambda function for example follow [this](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html) guide.
