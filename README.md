# Yatube API - CRUD Operations

This project implements a CRUD API (Create, Read, Update, Delete) for the Yatube platform, focusing on post and comment management. The backend logic is handled using Django, with an emphasis on authentication and authorization for secure API usage.

Project Overview:
The Yatube API provides endpoints for managing posts, groups, and comments, offering functionality for both authenticated users and public visitors. The API is designed to allow users to create, update, and delete their content, while general access is restricted to viewing data.

Key Features:
.Token Authentication: API access is restricted to authenticated users via Token Authentication.
.CRUD Functionality: Create, read, update, and delete operations for posts, comments, and groups.
.Permission Control: Users can modify or delete only their own content, while other users have read-only access. Attempts to modify another user's content result in a 403 Forbidden response.
.ModelViewSet: The models are managed via Django's ModelViewSet, ensuring efficient routing and method handling. 
