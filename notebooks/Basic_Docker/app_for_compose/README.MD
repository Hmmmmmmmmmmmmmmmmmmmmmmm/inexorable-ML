### What this app is:

* A **simple web app built with FastAPI** that stores and displays short text messages.
* Uses **Redis** as a fast in-memory database to store messages persistently.

---

### How it works:

1. **Homepage (GET `/`):**

   * Shows a webpage (rendered from your `index.html` template).
   * The page displays a list of previously submitted messages.
   * These messages are retrieved from Redis and shown in reverse order (most recent first).

2. **Add message (POST `/add`):**

   * When you submit a new message via the form, it sends a POST request to `/add`.
   * The backend takes that message, pushes it into the Redis list with `LPUSH`.
   * Then redirects back to the homepage to show updated messages.

---

### What you see in the browser:

* A **dark-themed, modern-looking webpage** that:

  * Has an input form to add a new message.
  * Displays the chat or message history dynamically loaded from Redis.

---

### Why Redis?

* Redis stores the messages **in memory** for lightning-fast reads and writes.
* Thanks to the Docker volume setup, Redis also **persists data on disk**, so messages survive container restarts.
* The Redis list acts like a **stack/queue** (new messages get added to the start).

---

### User flow example:

* You open `http://localhost:8000`.
* See a list of previous messages (if any).
* Type a message like `"Hello, world!"` and submit.
* The page reloads with your new message at the top.

---

### Summary:

| Feature      | Description                         |
| ------------ | ----------------------------------- |
| Framework    | FastAPI (Python web framework)      |
| Data storage | Redis (in-memory + persistent)      |
| UI           | Simple message board in HTML/Jinja2 |
| Persistence  | Docker volume saves Redis data      |
| Use case     | Lightweight, fast message storage   |

---