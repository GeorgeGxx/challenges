# Instructions

1. You only have 24 hours to delivered the assessment.
2. You can code in any language allowed (javascript, nodejs, python, .net core, java-springboot)
3. Your code has to be delivered in a public Github link or a .zip/.rar including the dependencies to run the project.
4. The SQL Query statemen has to delivered into a script.sql or .txt file

## 1. SQL Statement

You are given three tables:

create table books(id int, title varchar(250), year int, author varchar(250));

create table reviewers(id int, name varchar(250));

create table ratings(reviewer_id int, book_id int, rating int, rating_date date);

## Problem statement

Return the ratings data in a more readable format: reviewer name, book title, rating and rating date. Sort the data first by reviewer name, then by book title and lastly by rating.

Remember that the query will also be run on different datasets. You can use the test.sql script to run into your sql IDE manager.

## Example output:

| name | title | rating | rating_date |

| Alice Lewis | And then there were none | 4 | NULL |

| Chris Thomas | She: A History of Adventure | 4 | NULL |

| Chris Thomas | The Hobbit | 3 | 2015-01-26 |

| Chris Thomas | The Little Prince | 2 | 2015-03-22 |

## Sample data
### Books: sample data

| id | title | year | author |

| 101 | A Tale of Two Cities | 1859 | Charles Dickens |

| 102 | The Lord of the Rings | 1955 | J. R. R. Tolkien |

| 103 | The Hobbit | 1937 | NULL |

| 104 | The Little Prince | 1943 | Antoine de Saint-Exupéry |

### Reviewers: sample data

| id | name |

| 15201 | Joe Martinez |

| 53202 | Alice Lewis |

| 44203 | John Smith |

### Ratings: sample data

| reviewer_id | book_id | rating | rating_date |

| 15201 | 101 | 2 | 2015-02-11 |

| 15201 | 101 | 4 | 2015-06-16 |

| 53202 | 103 | 4 | NULL |

# 2. Programming test

You are developing a REST back end of an address book app. You were asked to implement endpoints to fetch a list of contacts and to fetch details of a single contact and to delete a given contact.

You are provided with a fake database layer exported fakedatabase.js

## App requirements

Your implementation has to. fulfil the requirements of HTTP endpoints described below:

### GET /contacts

- The response HTTP status should be: 200 OK.
- The response Content-Type header should be: application/json.
- The response body should be: a JSON array with details of all contacts as loaded from the database (each contact has an ID, a name, a phone and an array of strings addressLines).
- The contacts in the response body are sorted by their name, which means a contact with the name of Abbigail Wunsch would be first and a contact with the name of Zoila Daugherty II would be last.
- If the phrase URL query parameter is present:
    - in the response body, filter out contacts with names not matching phrase;
    - the phrase and the contact's name are compared lowercase, which means that both Theresa Gorczany and Zakary Mayer match the following phrase=zA;
    - If there are no contacts matching the phrase, then the response body contains only an empty JSON array as there are no contacts to include in it.
    - If the phrase is empty (phrase=), then the response has the 400 Bad Request HTTP status and an empty response body.

### GET /contacts/

- If a contact with ID value <contact-id> exists:
    - the response HTTP status should be: 200 OK;
    - the response Content-Type header should be: application/json;
    - the response body should be: a JSON object with details of that contact loaded from the database (ID, name, phone and an array of strings addressLines).
- If a contact with ID value <contact-id> does not exist:
    - the response HTTP status should be: 404 Not Found.

### DELETE /contacts/

- If a contact with ID value <contact-id> exists:
    - the response HTTP status should be: 204 No Content;
    - that contact is deleted, which means it is no longer included in the response to GET /contacts requests and its details are no longer available when making the GET /contacts/<contact-id> request.
- If a contact with ID value <contact-id> does not exist:
    - the response HTTP status should be: 404 Not Found.

### For all requests

- The request to the URL path different than the expected ones would get the 404 Not Found HTTP status.
- The request to the supported URL path, but with an unexpected HTTP method would get th e 405 Method Not Allowed HTTP status.