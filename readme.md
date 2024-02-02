# Recipe Search Platform

Welcome to the Recipe Search Platform web application! This Flask-based application allows users to discover recipes. Users can sign up, log in, search for recipes, and view detailed information about individual recipes.

## Features

### Home Page

The home page displays a welcome message to users.

### User Authentication

#### Sign Up

- Users can create a new account by providing a unique username, password, and optional profile picture.
- If the username is already taken, an error message is displayed.

#### Login

- Existing users can log in with their credentials.
- Invalid login attempts result in an error message.

#### Logout

- Users can log out of their accounts.

### Recipe Search

- Users can search for recipes based on a query and filter options.
- Search results are displayed, and users can view more details about each recipe.

### Recipe Details

- Users can view detailed information about a specific recipe by clicking on its card.

## Routes

- `/`: Displays the home page.
- `/signup`: Handles user signup.
- `/login`: Handles user login.
- `/logout`: Handles user logout.
- `/search`: Handles recipe search and displays search results.
- `/next`: Displays the next page of recipe search results.
- `/recipe/<int:id>`: Displays detailed information about a specific recipe.

## Error Handling

- Custom 404 page is displayed for invalid routes.

Feel free to explore and enjoy the Recipe Sharing Platform!
