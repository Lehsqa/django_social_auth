# Getting started with Social Auth Service

## Configuration

### Before starting need to config core/.env file:
1) ### `GOOGLE_REDIRECT_URL` - redirect url after auth by google auth (default: http://localhost)
2) ### `FACEBOOK_REDIRECT_URL` - redirect url after auth by facebook auth (default: http://localhost)

### After that need to config 'Social applications' in Django Admin
1) ### `Facebook` 
   - Provider: 'Facebook'
   - Name: 'facebook' or what you want
   - Client id: App id
   - Secret key: App secret
2) ### `Google`
   - Provider: 'Google'
   - Name: 'google' or what you want
   - Client id: Client ID
   - Secret key: Client secret

## Running

1) ### `docker-compose up -d --build`
2) ### `docker-compose exec web python manage.py createsuperuser`
3) ### `docker-compose up`

## Available Paths

### `http://localhost/admin` - Django Admin

### `http://localhost/api/facebook/login` - POST method for user authentication by Facebook SSO

### `http://localhost/api/google/login` - POST method for user authentication by Google SSO

## Swagger

### `api.yml` - swagger file

## Additional information

### Just to be on a safe side, make conversion of `core/entrypoint.sh` file to Unix (LF) standard