# Tandoor Recipes

## What is it?

[Tandoor Recipes](https://github.com/TandoorRecipes/recipes)  is an application for managing recipes, planning meals, building shopping lists and much much more!

#### Core Features

- 🥗 Manage your recipes with a fast and intuitive editor

- 📆 Plan multiple meals for each day

- 🛒 Shopping lists via the meal plan or straight from recipes

- 📚 Cookbooks collect recipes into books

- 👪 Share and collaborate on recipes with friends and family


!!!info
    By default, the role is protected behind your Authelia/SSO middleware. You will also have to log into the app itself.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://github.com/TandoorRecipes/recipes){: .header-icons } | [:octicons-link-16: Docs](https://docs.tandoor.dev/){: .header-icons } | [:octicons-mark-github-16: Github](https://github.com/TandoorRecipes/recipes){: .header-icons } | [:material-docker: Docker](https://hub.docker.com/r/vabene1111/recipes){: .header-icons }|

### 1. Installation

!!!info
    Before you run the role, you must create a **secret key**. If you don't, it will fail. 

To do so, run `base64 /dev/urandom | head -c50`. Copy and paste the results into `/opt/sandbox/settings.yml` under `tandoor secret_key`.

``` shell

sb install sandbox-tandoor

```

### 2. Setup

#### How do I add an admin user?

To create your initial user you need to

- execute a shell in the container using `docker exec -it tandoor sh`

- activate the virtual environment `source venv/bin/activate`

- run `python manage.py createsuperuser` and follow the steps shown.

### 3. URL

- To access Tandoor, visit `https://tandoor._yourdomain.com_`

### 4. Other

#### How do I reset passwords?

To reset a lost password if access to the container is lost you need to

- execute a shell in the container using `docker exec -it tandoor sh`

- activate the virtual environment `source venv/bin/activate`

- run `python manage.py changepassword <username>` and follow the steps shown.


- [:octicons-link-16: Documentation](https://docs.tandoor.dev/){: .header-icons }

To use a custom domain, add a custom value for `tandoor_web_subdomain` in the `/srv/git/saltbox/inventories/host_vars/localhost.yml` file. More info can be found [here](https://docs.saltbox.dev/saltbox/inventory/).
