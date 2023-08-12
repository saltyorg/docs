THIS PAGE HAS NOT BEEN FULLY UPDATED FOR SALTBOX

# What is it?

[Portainer](https://portainer.io/) is an open-source lightweight management UI which allows you to easily manage your Docker containers, images, networks and volumes.

| Details     |             |             |             |
|-------------|-------------|-------------|-------------|
| [:material-home: Project home](https://portainer.io/){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-link-16: Docs](https://docs.portainer.io//){: .header-icons target=_blank rel="noopener noreferrer" } | [:octicons-mark-github-16: Github](https://github.com/portainer/portainer/){: .header-icons target=_blank rel="noopener noreferrer" } | [:material-docker: Docker](https://hub.docker.com/r/portainer/portainer-ce){: .header-icons target=_blank rel="noopener noreferrer" }|

## 2. URL

To access Portainer, visit  `https://portainer._yourdomain.com_`

## 3. Initial Setup

1. The first time you go to the Portainer page, you will be presented with the message "Please create the initial administrator user.". Fill in your preferred admin username and password. Click `Create User`.

    ![](../images/portainer/portainer-01.png)

2. On this first visit when you set up the admin user, you will be logged in automagically. On future visits, you will be asked to log in with your username and password.

    ![](../images/portainer/portainer-02.png)

3. On the "Connect Portainer to the Docker environment you want to manage." screen, select `Local: Manage the local Docker environment` and click `Connect`.

    _Note: Don't be confused by "local" in this context. It is referring to the relationship between the Docker instance you're managing on your Saltbox server and this instance of Portainer. These things are local to each other on your Saltbox server, wherever that is. They may be remote from you, but they are local to each other.  Pay no mind to what looks like a warning at the bottom. Saltbox has already taken care of that._

    ![](../images/portainer/portainer-03.png)

4. Portainer is now set up.

## 4. Next

Are you setting Saltbox up for the first time?  Continue to [Organizr](organizr.md).
