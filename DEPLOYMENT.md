<!-- Deployment guide code used and adapted from Ms Cudmore and her fourth milestone project, Seaside Sewing: https://github.com/kera-cudmore/seaside-sewing#deployment--local-development -->

# **CVEK ART GALLERY - Deployment** 

[Main README.md file](/README.md)

View live project

View GitHub repository

## Deployment

**Project is deployed using Heroku.**

### To deploy the project:

#### **Generate a SECRET KEY & Updating Debug**

1. Django automatically sets a secret key when project is created, to avoid security warning from GitHub and to keep the unique key generated hidden, first hide the SECRET KEY.
2. Add the `SECRET_KEY` and its value to GitPod Environment Variable/s.
3. In Heroku settings create a new config var with a key of `SECRET_KEY`. The value will be the secret key from Settings.py.
4. If multiple projects are present in the workspace, `SECRET_KEY` can be named differently, for example `SECRET_KEY_(number or distinguishing short name of the project)`, in this project case it was `SECRET_KEY_CAG` (don't forget to update GitPod and Heroku vars accordingly).
5. In settings.py update the `SECRET_KEY` variable, it will get the secret key from the development environment, or use an empty string:

    ```python
    SECRET_KEY = os.environ.get('SECRET_KEY', ' ')
    ```

6. Adjust the `DEBUG` variable to only set DEBUG as true if in development:

    ```python
    DEBUG = 'DEVELOPMENT' in os.environ
    ```

7. Save, add, commit and push the changes.

#### **Create the Live Database**

Create a new external database that can be accessed by Heroku:

1. Go to the [ElephantSQL](https://www.elephantsql.com/) dashboard and click the create new instance button on the top right.
2. Name the plan (project name is a good choice), select free tiny turtle plan and choose the region that is closest, then click the review button.
3. Check the details are all correct and then click create instance in the bottom right.
4. Go to the dashboard and select the database just created.
5. Copy the URL (you can click the clipboard icon to copy)

#### **Heroku app setup**

  1. From the [Heroku dashboard](https://dashboard.heroku.com/), click the new button in the top right corner and select create new app.
  2. Give the app a name (must be unique), select the region that is closest and then click the create app button bottom left.
  3. Open the settings tab and create a new config var of `DATABASE_URL` and paste the database URL copied from elephantSQL into the value (the value should not have quotation marks around it).

#### **Preparation for deployment in GitPod**

1. Install dj_database_url and psycopg2 (both needed for connecting to the external database that was just set up):

   ```bash
   pip3 install dj_database_url==0.5.0 psycopg2
   ```

2. Update requirements.txt file with the packages just installed:

    ```bash
    pip3 freeze > requirements.txt
    ```

3. In settings.py underneath import os, add `import dj_database_url`

4. Find the section for DATABASES and comment out the code. Add the following code below the commented out database block, and use the URL copied from elephantSQL for the value:

    (NOTE! don't delete the original section, as this is a temporary step whilst we connect the external database. Make sure this value is not pushed to GitHub, it will be added to the Heroku config vars in a later step, this is temporary to allow for migration of models to the external database)

    ```python
    DATABASES = {
        'default': dj_database_url.parse('paste-elephantsql-db-url-here')
    }
    ```

5. In the terminal, run the show migrations command to confirm connection to the external database:

    ```bash
    python3 manage.py runserver
    ```

6. If the database is connected correctly, there will be a list of migrations that are unchecked. Run migrations to migrate the models to the new database:

    ```bash
    python3 manage.py migrate
    ```

7. Create a superuser for the new database. Input a username, email and password when directed.

    ```bash
    python3 manage.py createsuperuser
    ```

8. Go to the browser tab on the left of the page in elephantsql, click the table queries button and see the superuser that was just created by selecting the auth_user table.

9. Add an if/else statement for the databases in settings.py, so the development database while in development will be used (the commented out code) - and the external database on the live site:

    ```python
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
          'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
          }
        }
    ```

10. Install gunicorn which will act as webserver and freeze this to the requirements.txt file:

    ```bash
    pip3 install gunicorn
    pip3 freeze > requirements.txt
    ```

11. Create a `Procfile` in the root directory. This tells Heroku to create a web dyno which runs gunicorn and serves the django app. Add the following to the file (making sure not to leave any blank lines underneath):

    ```Procfile
    web: gunicorn cvek_art_gallery.wsgi:application
    ```

12. Log into the Heroku CLI in the terminal and run the following command to disable collectstatic. This command tells Heroku not to collect static files when deployed:

    ```bash
    heroku config:set DISABLE_COLLECTSTATIC=1 --app heroku-app-name-here
    ```

13. Add the Heroku app and localhost (which will allow GitPod to still work) to ALLOWED_HOSTS = [] in settings.py:

    ```python
    ALLOWED_HOSTS = ['heroku deployed site URL here', 'GITPOD WORKSPACE URL HERE', 'localhost' ]
    ```

14. Save, add, commit and push the changes to GitHub.

15. To enable automatic deploys on Heroku, go to the deploy tab and click the connect to GitHub button in the deployment method section. Search for the projects repository and then click connect to main branch. Click enable automatic deploys at the bottom of the page. This is not recommended after connecting to AWS early in development, as it could lead to going outside free AWS plan.

16. The deployed site should be visible (without any static files).

#### **Set up AWS hosting for static and media files**

! NOTE: These instructions are for setting up AWS hosting as of 30/09/23 - these may change slightly in future versions of AWS.

1. Sign up or login to your [aws amazon account](https://aws.amazon.com) on the top right by using the manage my account button and then navigate to S3 to create a new bucket.
2. The bucket will be used to store the media and static files, it is a good idea to name this bucket the same as the project. Select the closest region. In the object ownership section select ACLs enabled and then select bucket owner preferred. In the block public access section uncheck the block public access box. Acknowledge the button to make the bucket public. Click create bucket.
3. Click the bucket just created and then select the properties tab at the top of the page. Find the static web hosting section and choose enable static web hosting, host a static website and enter index.html and error.html for the index and error documents (won't actually be used).
4. Open the permissions tab and copy the ARN (amazon resource name). Navigate to the bucket policy section, click edit and select policy generator. The policy type is S3 bucket policy, allow all principles by adding `*` to the input, the actions are get object. Paste the ARN copied from the last page into the ARN input and then click add statement. Click generate policy and copy the policy that displays in a new pop up. Paste this policy into the bucket policy editor and make the following changes: Add a `/*` at the end of the resource value. Click save.
5. Edit the the cross-origin resource sharing (CORS). Paste in the following text:

    ```json
    [
        {
            "AllowedHeaders": [
                "Authorization"
            ],
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": []
        }
    ]
    ```

6. Edit the access control list (ACL) section. Click edit and enable list for everyone (public access) and accept the warning box.

#### **Creating AWS groups, policies and users**

1. Click the services icon on the top right of the page and navigate to IAM - manage access to AWS services. On the left hand navigation menu click user groups and then click the create group button in the top right. This will create the group that the user will be placed in.
2. Choose a name for the group (use your project name or something distinctive), click the create policy button on the right. This will open a new page.
3. Click on the JSON tab and then click the link for import managed policy on the top right of the page.
4. Search for S3 and select the one called AmazonS3FullAccess, then click import.
5. Change the resources, make resources an array and then change the value for resources. Instead of a `*` which allows all access, paste in our ARN followed by a comma, and then paste the ARN in again on the next line with `/*` at the end. This allows all actions on the bucket, and all the resources in it.
6. Click the next:tags button and then the next:review.
7. Give the policy a name and description (your project name or something distinctive), click the create policy button.
8. Attach the policy just created; on the left hand navigation menu click user groups, select the group and go to the permissions tab. Click the add permissions button on the right and choose attach policies from the dropdown.
9. Select the policy just created and then click add permissions at the bottom.
10. Create a user for the group by clicking on the user link in the left hand navigation menu, clicking the add users button on the top right and giving the user a username (your project name or something distinctive-user). Select programmatic access and then click the next:permissions button.
11. Add the user to the group just created and click next:tags button, next:review button and then create user button.
12. Download the CSV file as this contains the user access key and secret access key that is needed for Heroku config vars. Make sure CSV is downloaded to your machine now as this won't be accessible again.

#### **Connecting Django to S3 bucket**

1. Install boto3 and django storages and freeze them to the requirements.txt file.

    ```bash
    pip3 install boto3
    pip3 install django-storages
    pip3 freeze > requirements.txt
    ```

2. Add `storages` to the installed apps in settings.py
3. Add the following code in settings.py to use the bucket if using the deployed site (and add cache control):

    ```python
    if 'USE_AWS' in os.environ:
        AWS_S3_OBJECT_PARAMETERS = {
            'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
            'CacheControl': 'max-age=9460800',
        }
        
        AWS_STORAGE_BUCKET_NAME = 'enter your bucket name here'
        AWS_S3_REGION_NAME = 'enter the region you selected here'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    ```

    If the above doesn't work, try replacing 

    ```python
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    ```

    with

    ```python
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com'
    ```
    Full explanation in the BUGs section of [TESTING.md](/TESTING.md)

4. In Heroku add these keys to the config vars:

    | KEY | VALUE |
    | :--- | :--- |
    | AWS_ACCESS_KEY_ID | The access key value from the amazon csv file downloaded in the last section |
    | AWS_SECRET_ACCESS_KEY | The secret access key from the amazon csv file downloaded in the last section |
    | USE_AWS | True |

5. Remove the DISABLE_COLLECTSTATIC variable.
  - This is somewhat unclear, a lot of people (on Slack) have issues when removing DISABLE_COLLECTSTATIC var prior to AWS connection/deployment, more so if the DEBUG is set to true. More details on this in the BUGs section of [TESTING.md](/TESTING.md).

6. Create a file called custom_storages.py in the root and import settings and S3Botot3Storage. Create a custom class for static files and one for media files. These will tell the app the location to store static and media files.

7. Add the following to settings.py to let the app know where to store static and media files, and to override the static and media URLs in production.

    ```python
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
    
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

    ```

8. Save, add, commit and push these changes to make a deployment to Heroku. The build log should note that the static files were collected, and if S3 bucket is checked, the static folder with static files in it will be visible.
9. Navigate to S3 and open the bucket. Create a new file to hold all the media files for the site. Click create folder button on the top right and name the folder media, and upload media files.

#### **Setting up Stripe**

1. Add the Stripe keys to config vars in Heroku and GitPod workspace (keep the keys hidden). Log into Stripe, click developers and then API keys.
2. Create 2 new variables in Heroku's config vars - for the publishable key (STRIPE_PUBLIC_KEY) and the secret key (STRIPE_SECRET_KEY) and paste the values in from the Stripe page.
3. Add the WebHook endpoint for the deployed site. Navigate to the WebHooks link in the left hand menu and click add endpoint button.
4. Add the URL for deployed and/or in development sites WebHook, give it a description and then click add events button and select all events. Click create endpoint.
5. Add the WebHook signing secret to Heroku and GitPod config variables as STRIPE_WH_SECRET.
6. In settings.py:

    ```python
    STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
    STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')
    ```

### Local Development

#### **How to Fork**

To fork the repository:

1. Log in (or sign up) to GitHub.

2. Go to the repository for this project, [Cvek Art Gallery](https://github.com/Boiann/cvek-art-gallery).

3. Click on the fork button in the top right of the page.

#### **How to Clone**

To clone the repository:

1. Log in (or sign up) to GitHub.

2. Go to the repository for this project, [Cvek Art Gallery](https://github.com/Boiann/cvek-art-gallery).

3. Click the Code button, select whether to like to clone with HTTPS, SSH or the GitHub CLI and copy the link given.

4. Open the terminal in your chosen IDE and change the current working directory to the location for using for the cloned repository.

5. Type the following command into the terminal `git clone` followed by the link copied in step 3.

6. Set up a virtual environment (this step is not required if you are using the Code Institute template and have opened the repository in GitPod, as this will have been set up already).

7. Install the packages from the requirements.txt file by running the following command in the terminal:

```bash
pip3 install -r requirements.txt
```

---