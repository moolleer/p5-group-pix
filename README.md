# Group Pix

Group Pix is a social networking platform that provides a dynamic space for photography enthusiasts to create, share and connect within selected groups. Group Pix simplifies the process of sharing the users finest photographic moments while fostering interactions with like-minded individuals who share the same interests, locations, or event experiences. 

 This a fictional website created as a milestone project for Code Institutes fullstack developer course.

## User Experience (UX)

Users can create groups centered around specific interests, locations, or events, allowing them to connect with others who share their passions.

##  Strategy Plan

### Project Goals

The main goal of this project is to let users create an account where they can create groups to interact with other groupmembers trough posts, discussions and comments. The users should also be able to edit and delete their own interactions and account

At the time when I am submitting this project, all goals is not complete. 
The user can signup for an account, sign in and signout, view groups and create a group. 

### User Goals

- As a user I want to upload, edit or delete a photo.
- As a user I want to join or leave a group.
- As a user I want to create my own photography groups based on my interests or experiences.
- As a user I want to like, unlike or comment on a photo.
- As a user I want to discover groups that align with my interests, locations, or event experiences.
- As a user I want to showcase my photography skills and share my best images with a receptive audience.
- As a user I want to engage in discussions, offer feedback, and exchange insights with other users.

### User Expectations

- Users expect an easy-to-navigate interface that allows them to quickly find photography groups, upload images, and engage in discussions.
-  Users expect a platform that works seamlessly across devices, enabling them to engage with photos and discussions from anywhere.
- Users expect that their personal information and photos will be safe, ensuring a trustworthy and secure platform.

### User Stories

The agile methodology were used throughout the project. I used the GitHub projects board to log all user stories as my project management tool. Creating epics and user storys for this project helped me to focus on the necessary tasks and a working environment the goals where easy to visualize.

![project](/assets/readme_images/project.PNG)

### Scope

#### EPICS:

- EPIC: User Account:
  - USER STORY: User Registration
  - USER STORY: Login
  - USER STORY: Logout

- EPIC: Navigation:
  - USER STORY: Navigation Menu
  - USER STORY: Search Bar
  - USER STORY: Responsive Design

- EPIC: Post:
  - USER STORY: Upload Photo
  - USER STORY: Photo Interaction
  - USER STORY: User View Posts
  - USER STORY: Title & Content
  - USER STORY: Post History

- EPIC: Post page:
  - USER STORY: Post Details
  - USER STORY: Likes & Comments
  - USER STORY: Edit Post
  - USER STORY: Delete Comment
  - USER STORY: Comment Post
  - USER STORY: Comment Time
  - USER STORY: Read Comments
  - USER STORY: Delete Own Comment
  - USER STORY: Edit Own Comment

- EPIC: Posts Pages:
  - USER STORY: Posts Feed
  - USER STORY: Search Posts
  - USER STORY: Post Details
  - USER STORY: Popularity
  - USER STORY: Liked Posts
  - USER STORY: Sort Posts
  - USER STORY: Posts Profiles
  - USER STORY: Comment Posts
  - USER STORY: Infinite Scroll

- EPIC: Authentication:
  - USER STORY: Signup Details
  - USER STORY: Email & Password
  - USER STORY: Change Password
  - USER STORY: Reset Password
  - USER STORY: Social Media
  - USER STORY: Secure Authentication Processes
  - USER STORY: Session

- EPIC: Group:
  - USER STORY: Group Page
  - USER STORY: Group Information
  - USER STORY: Active Discussions
  - USER STORY: Recent Posts User
  - USER STORY: Number Of Members
  - USER STORY: Join Group
  - USER STORY: Leave Group
  - USER STORY: Popular Groups
  - USER STORY: Start Discussion

- EPIC: Profile:
  - USER STORY: Profile Page
  - USER STORY: Profile Information
  - USER STORY: Edit Profile
  - USER STORY: User Posts
  - USER STORY: User Statistics
  - USER STORY: User Discussions
  - USER STORY: Insights
  - USER STORY: Group Member Posts
  - USER STORY: Follow & Unfollow profile

- EPIC: Discussion:
  - USER STORY: Start Discussion
  - USER STORY: Discussion Information
  - USER STORY: Edit Discussion
  - USER STORY: Delete Discussion
  - USER STORY: Delete Comments
  - USER STORY: Group Member Comments
  - USER STORY: Like Comments
  - USER STORY: Images
  - USER STORY: Comment
  - USER STORY: Discussion Popularity
  - USER STORY: Discussion Feed

#### User Stories

All user stories can be found [here](https://github.com/moolleer/p5-group-pix/issues)


## Structure

The overall structure of the project was modelled on the [drf-api](https://github.com/Code-Institute-Solutions/drf-api) walkthrough due to time constraints and the Project 5 assessments requirements including most of what is included in the walkthrough project.

However, additional custom models have also been developed where possible such as groups, and discussions, and I have tried to customize the walkthrough models as well to fit more closely with the scope of my own sharing platform.

### Database Model

To create the entity relationship diagram, I used [dbdiagram](https://dbdiagram.io/home). It shows the relationship between all models in the database.

![Model](assets/readme_images/dbdiagram.png)

### Database

For this project I used a PostgreSQL database hosted by [ElephantSQL](https://www.elephantsql.com/). 

### Models

#### Profiles :

| Database Value | Field Type     | Field Argument                 |
|----------------| ---------------| -------------------------------|
| owner          | ForeingKey     | User, on_delete=models.CASCADE |
| join_date      | DateTimeField  | auto_now_add=True              |
| last_login     | DateTimeField  | auto_now=True                  |
| name           | CharField      | max_length=255, blank=True     |
| content        | TextField      | blank=True                     | 
|  profile_picture |ImageField    | upload_to='images/', default='../default_profile_eianob' |


#### Groups :

| Database Value | Field Type     | Field Argument                 |
|----------------| ---------------| -------------------------------|
| name           |  CharField     | max_length=255                 |
| description    |  TextField     |                                |
| members        | ManyToManyField| User, through='GroupMembership', related_name='group_memberships'|
| created_by     | ForeignKey     | User, on_delete=models.CASCADE, related_name='created_groups |
| created_at     | DateTimeField  | auto_now_add=True | 

#### Posts :

| Database Value | Field Type     | Field Argument                 |
|----------------| ---------------| -------------------------------|
| owner          | ForeignKey     | User, on_delete=models.CASCADE |
| group          | ForeignKey     | Group, on_delete=models.CASCADE |
| title          | CharField      | max_length=255                 |
| content        | TextField()    |                                |
| created_at     | DateTimeField  | auto_now_add=True              |
| updated_at     | DateTimeField  | auto_now=True                  |
| image          | ImageField     |  upload_to='images/', default='../default_post_e3pet6.jpg', blank=True |

#### Discussions :

| Database Value | Field Type     | Field Argument                 |
|----------------| ---------------| -------------------------------|
| group          | ForeignKey    | Group, on_delete=models.CASCADE |
| owner          | ForeignKey    | User, on_delete=models.CASCADE  |
| title          | CharField     | max_length=255                  |
| content        | TextField()   |                                 |
| created_at     | DateTimeField | auto_now_add=True               |

#### Comments :

| Database Value | Field Type     | Field Argument                 |
|----------------| ---------------| -------------------------------|
| owner          | ForeignKey     | User, on_delete=models.CASCADE |
| post           | ForeignKey     | Post, on_delete=models.CASCADE, related_name='posts' null=True, blank=True |
| discussion     | ForeignKey     | Discussion, on_delete=models.CASCADE, related_name='comments' null=True, blank=True |
| created_at     | DateTimeField  | auto_now_add=True |
| updated_at     | DateTimeField  | auto_now=True content = models.TextField() |

## Skeleton

### Wireframes

Wireframes created using [Balsamiq](https://balsamiq.com/) to plan the general flow and display of Group Pix. Some differences may be found between the original wireframes and the finished site due to design choices made during the project process.

- [Home page](/assets/readme_images/homepage.png)
- [Home page signed in](/assets/readme_images/homepage-loged-in.png)
- [My account](/assets/readme_images/My%20account.png)
- [Sign in](/assets/readme_images/signin.png)
- [Signup](/assets/readme_images/signup.png)
- [Post](/assets/readme_images/Post.png)
- [Posts](/assets/readme_images/Posts.png)
- [Groups](/assets/readme_images/groups.png)
- [Group page](/assets/readme_images/group%20page.png)
- [Discussions](/assets/readme_images/Discussions.png)
- [Discussion](/assets/readme_images/Discussion.png)

## Surface

## Features

### Design

### Color Scheme

### Existing Features

### Future Features

User stories:

- As a group member, I can sort posts by different criteria such as most liked or most commented, so that I can explore popular content.

- As a user, I can see a visual indicator (such as a badge) if a post has new comments since my last visit, so that I can feel encouraged to engage in active discussions.

- As a group member, I can have the option to report inappropriate posts or comments so that I can contribute to maintain a positive and respectful community environment.

- As a group member, I can receive notifications when someone replies to my comments or engages in discussions I've participated in, so that I can be up to date with other users interaction with me.

- As a group member I can have the option to view my notifications, including likes, comments, and any mentions in discussions or comments so that I can interact and respond faster.

- As a user I can connect my social media accounts to my profile so that I can make it easier for others to find me.

- As a user, I can have the option to customize the profile and group page, so that I can personalize certain elements to reflect my identity and preferences.

- As a user I can have the option to create private groups so that I can choose to accept wich users that can join and see the content.


## Testing

All testing information can be found here [testing.md](https://github.com/moolleer/p5-group-pix/blob/main/docs/testing.md)

## Technologies Used

### Languages

- Python - A programming language that provides the functionality for the DRF backend framework.

### Frameworks

- Django Rest Framework - A framework for building web API's

### Packages

- Github - Used to host the repository, store the commit history and manage the project board containing user stories and bug reports.
- Heroku - Used to deploy the website
- cloudinary - Easily integrate your application with Cloudinary
- dj-database-url - Allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.
- dj-rest-auth - API endpoints for handling authentication securely in Django Rest Framework
- django-cloudinary-storage - package that facilitates integration with Cloudinary by implementing Django Storage API
- gunicorn - A Python WSGI HTTP Server for UNIX.
- Pillow - Adds image processing capabilities to your Python interpreter
- psycopg2 - PostgreSQL database adapter for Python
- pycodestyle - A tool to check your Python code against some of the style conventions in PEP 8.
- requests - Allows you to send HTTP/1.1 requests

### Other tools

- django-filter - Django-filter is a reusable Django application allowing users to declaratively add dynamic QuerySet filtering from URL parameters.
- django-rest-framework - web-browsable Web APIs.
- djangorestframework-simplejwt - Simple JWT is a JSON Web Token authentication plugin for the Django REST Framework.
- Cloudinary - Used to host all static files .



## Deployment



## Credits & Content

- [CI Moments](https://github.com/Code-Institute-Solutions/moments)

### Media

## Project Acknowledgements
