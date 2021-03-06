# Independent Project - Photo-Gallery

This is a Django project was generated with [Python](https://www.python.org/) version 3.9


## Author's Name
Derrick Nyongesa


## Description
This  is a Django Web gallery Application that displays different categories of photos from various locations.

## User Story  
  
* View different photos that interest them  
* Click a single image to expand it and view the details of that photo  
* Search for different categories   
* Copy a link to the photo to share with my friends.  
* View photos based on the location they were taken.


## Project setup instructions
1. Pull project from github Repository.

```bash
git clone https://github.com/Derrick-Nyongesa/Photo-Gallery.git
``` 
2. Move to the folder and create a virtual environment
3. Install requirements
  ```bash
  pip install -r requirements.txt
  ```
4. Create a new postgress database

5. Make migrations on postgres using django
    ```bash
    $ python manage.py makemigrations <database name>
    ```
    ```bash
    $ python3 manage.py migrate
    ```
6. Run the application
    ```bash
    $ python3 manage.py runserver
    ``` 
5. Open the application on your browser `http://127.0.0.1:8000/`


## Entity relationship diagram 
![ERD](https://user-images.githubusercontent.com/78686755/118359284-6f75ba00-b58b-11eb-8f1c-7e6e4979236c.png)



## Technology used
* [Python3](https://www.python.org/)
* [Django3.2.2](https://docs.djangoproject.com/en/3.2/releases/3.2.2/)
* [Heroku](https://heroku.com)


##  Live Link  
 Click [View Site](https://derrick-photo-gallery.herokuapp.com/)  to visit the site

## Contact Information 
Any query? Contact me at [nyongesaderrick@gmail.com]


## Copyright and license information
Licensed under the [MIT license](LICENSE).