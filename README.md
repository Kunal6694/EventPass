🎟️ EventPass: Unified Event Ecosystem
Connecting People Through Seamless Experiences.

EventPass is a professional, web-based event booking and management platform designed for the modern corporate and academic landscape. It bridges the gap between event organizers and attendees by providing a high-integrity marketplace where summits, workshops, and meetups can be published and booked in real-time.

🚀 The Mission
In an era of fragmented communication, EventPass provides a "Single Source of Truth" for event discovery. Our goal is to eliminate the friction in event management by providing organizers with powerful administrative tools and offering attendees a clean, secure, and transparent booking journey.

🛠️ Technical Architecture
EventPass is built using a robust MVC (Model-View-Controller) pattern to ensure clean separation of concerns and high performance.

Model (Data Layer): A relational SQLite3 engine manages three core tables: Users, Events, and Bookings. This ensures data persistence and transactional integrity.

View (Presentation Layer): A responsive frontend built with Bootstrap 5 and Jinja2 templating. It utilizes "Template Inheritance" via a master base.html to maintain a consistent UI across all portals.

Controller (Logic Layer): Powered by Flask, handling RESTful routing, session-based authentication, and business logic for seat inventory management.

✨ Key Features
🛒 Live Marketplace
Real-time Discovery: A card-based grid showcasing live events with detailed descriptions and pricing.

Instant Filtering: Attendees can browse events by venue, date, and availability.

Pricing Transparency: Every event features a clear pricing badge to assist user decision-making.

🏢 Organizer Portal (Dashboard)
Event Lifecycle Management: A full CRUD interface for organizers to publish, view, and manage their event pulse.

Inventory Tracking: Real-time monitoring of seat availability and event capacity.

Role-Based Access: Secure dashboards accessible only to verified organizer accounts.

🎫 Attendee Experience
Secure Booking Flow: Integrated confirmation system that captures customer details and deducts seat inventory accurately.

My Bookings: A dedicated history page for users to track their confirmed tickets and event details.

Instant Feedback: Real-time flash messaging providing status updates on every transaction.

💻 Technical Stack & Libraries
The project utilizes high-performance Python libraries to ensure a secure and responsive experience:

Flask: Core micro-framework for backend routing and server-side logic.

SQLite3: Serverless relational database for local data persistence.

Werkzeug.security: Implementation of PBKDF2 password hashing for high-integrity user security.

Jinja2: Templating engine for rendering dynamic Python data into HTML.

Bootstrap 5: CSS framework for a mobile-first, responsive user interface.

⚙️ Installation & Setup
To run the EventPass portal locally, follow these steps:

Clone the Repository:
git clone https://github.com/Kunal6694/EventPass.git
cd EventPass

Initialize the Database:
python setup_db.py

Start the Application:
python app.py

Access the Portal:
Open http://127.0.0.1:5000 in your web browser.
