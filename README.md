# Group Pix

Group Pix is a social networking platform that provides a dynamic space for photography enthusiasts to create, share and connect within selected groups. Group Pix simplifies the process of sharing the users finest photographic moments while fostering interactions with like-minded individuals who share the same interests, locations, or event experiences. 

 This a fictional website created as a milestone project for Code Institutes fullstack developer course.

## User Experience (UX)

Users can create groups centered around specific interests, locations, or events, allowing them to connect with others who share their passions.

##  Strategy Plan

### Project Goals

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

### Scope

#### EPIC:

##### User Stories

## Structure

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

## Deployment

## Credits & Content

### Media

## Project Acknowledgements
