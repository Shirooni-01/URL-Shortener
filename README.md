 ### URL Shortener

A simple and efficient URL Shortener built using Flask and SQLite.

This application converts long URLs into short, shareable links and automatically redirects users to the original website when the shortened link is visited.

 ## Features

* Generate unique short URLs
* Automatic redirection to original URLs
* SQLite database integration
* Persistent storage (URLs remain saved after restarting the app)
* URL history page
* Automatic HTTPS handling
* Clean and responsive user interface
* Duplicate short code prevention

## Tech Stack

* Python
* Flask
* SQLite
* HTML
* CSS
  

## Project Structure


```text
url-shortener/
│
├── app.py
├── database.db
├── .gitignore
├── README.md
│
└── templates/
    └── index.html
```


## Screenshots

# Home Page

![Home Page](screenshots/main_dashboard.png)

# URL History

![History](screenshots/History.png)


## Installation

 1. Clone the Repository

```bash
git clone https://github.com/your-username/url-shortener.git
```

 2. Move to the Project Directory

```bash
cd url-shortener
```

 3. Install Dependencies

```bash
pip install flask
```

 4. Run the Application

```bash
python app.py
```

 5. Open in Browser

```text
http://localhost:5000
```

## Database Schema

The application uses SQLite with the following table:

```sql
CREATE TABLE urls(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    uni_id TEXT UNIQUE,
    og_url TEXT
);
```

## How It Works

1. User enters a long URL.
2. The application generates a unique 6-character ID.
3. The URL and ID are stored in SQLite.
4. A shortened URL is generated.
5. When the short URL is opened, Flask looks up the original URL in the database.
6. The user is redirected to the destination website.

 Example

Original URL:

```text
https://www.google.com
```

Generated Short URL:

```text
http://localhost:5000/abc123
```

Visiting:

```text
http://localhost:5000/abc123
```

Redirects to:

```text
https://www.google.com
```

## Future Improvements

* Custom short URLs
* Copy-to-clipboard button
* Click analytics
* URL expiration
* User authentication
* QR code generation
* REST API support

## Learning Outcomes

This project helped practice:

* Flask Routing
* Dynamic URL Parameters
* Form Handling
* Redirects
* SQLite Database Operations
* SQL Queries
* Python Functions
* Jinja2 Templates
* Responsive UI Design

## License

This project is open-source and available for educational and learning purposes.
