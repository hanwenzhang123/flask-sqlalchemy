{{ current_user.is_authenticated }} on the UserMixin from flask-login

current_user - Global object in templates that represents the current user.
is_authenticated - Property on current_user that returns whether the user is authenticated or not.
get_flashed_messages(with_categories=True) - Gets flashed messages with their categories.


#exercise
In the nav tag in layout.html, add three links:

A link to logout() with the text "Sign Out"
A link to 'login()' with the text "Sign In"
A link to 'register()' with the text "Sign Up"

Now use current_user.is_authenticated to make the logout() link only show to authenticated users and the login() and register() links show to unauthenticated users.



<!doctype html>
<html>
<head>
<title>Lunch</title>
</head>
<body>

<nav>
  {% if current_user.is_authenticated %}
  <a href="{{ url_for('logout') }}">Sign Out</a>
  {% else %}
  <a href="{{ url_for('login') }}">Sign In</a>
  <a href="{{ url_for('register') }}">Sign Up</a>
  {% endif %}
</nav>

<div class="messages">
{% with messages = get_flashed_messages() %}
{% for message in messages %}
<div>{{ message }}</div>
{% endfor %}
{% endwith %}
</div>

{% block content %}{% endblock %}
</body>
</html>
