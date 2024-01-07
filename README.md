Project URLs Documentation

1. Home Page

- URL Pattern: /
- View Function: views.home
- Description: The home page is the primary landing page of the project. It displays the latest cryptocurrency data and provides a user interface for navigation to other sections of the application.

---

2. Chart Data

- URL Pattern: /chart/<str:symbol>/
- View Function: views.get_chart_data
- Description: This endpoint fetches historical data for a specific cryptocurrency symbol, allowing users to view charts illustrating the price trends over time.

---

3. Store Cryptocurrency Data

- URL Pattern: /storedata/<str:symbol>/
- View Function: views.store_the_data
- Description: This URL handles the storage of cryptocurrency data for a specific symbol. It is typically triggered by a form submission, and upon successful storage, users are redirected to the home page.

---

4. User Registration

- URL Pattern: /register/
- View Function: views.register_users
- Description: The registration page displays a form for users to create an account. After successful registration, users are authenticated and redirected to the home page.

---

5. User Logout

- URL Pattern: /logout/
- View Function: views.logout_users
- Description: This URL logs out the authenticated user, providing a simple way for users to end their session securely.

---

6. View Cryptocurrency Data

- URL Pattern: /viewdata/
- View Function: views.display_cryptocurrencies
- Description: This page presents the latest data for each unique cryptocurrency symbol. It offers a comprehensive view of current cryptocurrency prices.

---
Basic User Authentication has been used in this task. 
