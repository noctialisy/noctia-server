# Private server project
A simple server able to deploy apache, mariadb, ldap, mediawiki, shlink, owncast and jellyfin on a k8s cluster.

To configure what to deploy look in the settings_example.json

# Installation
Before installing:
 - Copy the settings_example.json file to settings.json
 - Fill in your configurations based on your needs
 - Run the python build script with the command "python handler.py build"
 - New files will be in the folder k8s_deploys
 - Deploy on cluster with "kubectl apply -f ./k8s_deploys"

Each and every service will require their specific configurations. Example, for Shlink you'll have to specify the api and geo keys.
Guides for services can be found by browsing image repositories or the official service docs.

There's an imagePullSecret bind to each yaml so you can enter your secret for docker in the settings file if you need to pull a specific image from your private registry.



# Note
If you're planning to use tls and other advanced features, especially for Apache, you'll have to provide your certs (.crt and .key files)
Some of the settings for the apache server might be wrong and not work. I'll get back to fix those eventually.
