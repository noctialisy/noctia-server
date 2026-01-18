import os, sys, subprocess, json, shutil

# Def Main
def main():
    commands = sys.argv

    if len(commands) <= 1:
        print('No command specified.')
        print('')

    else:
        with open('./settings.json') as settings_file:
            settings = json.load(settings_file)
            target = settings['target']

            for command in commands:
                if command == "apply":
                    subprocess.run('kubectl apply -f ./k8s_deploys')
                    exit()

                if command == "delete":
                    subprocess.run('kubectl delete -f ./k8s_deploys')
                    exit()

                if "build" in command:
                    
                    # Import settings from settings.json
                    src = './k8s_files/'
                    trg = './k8s_deploys/'
                    
                    files = os.listdir(src)

                    # Attempts to create the deployment folder
                    try: 
                        os.mkdir(trg)

                    except OSError as error:
                        if "already exists" not in str(error):
                            print(error)

                    # Make a copy of all files and handle changes
                    for fname in files:
                        filedata = ""

                        # Exclude components
                        if settings["ldap_enable"] == False and "ldap" in fname:
                            continue
                        if settings["apache_enable"] == False and "apache" in fname:
                            continue
                        if settings["mariadb_enable"] == False and "mariadb" in fname:
                            continue
                        if settings["wiki_enable"] == False and "wiki" in fname:
                            continue
                        if settings["shlink_enable"] == False and "shlink" in fname:
                            continue
                        if settings["owncast_enable"] == False and "owncast" in fname:
                            continue
                        if settings["jellyfin_enable"] == False and "jellyfin" in fname:
                            continue

                        # Make a first copy of the original file
                        shutil.copy2(os.path.join(src,fname), os.path.join(trg,fname))

                        # Open the target file
                        with open(os.path.join(trg,fname), 'r', encoding="utf-8") as file:
                            filedata = file.read()

                            for key in settings.keys():
                                filedata = filedata.replace('${' + key + '}', str(settings[key]))

                            # Replace the target strings
                            #filedata = filedata.replace('${app_name}', name)
                            #filedata = filedata.replace('${ip_address}', ip)
                            #filedata = filedata.replace('${ldap_ip}', settings['ldap_ip'])
                            #filedata = filedata.replace('${apache_ip}', settings['apache_ip'])
                            #filedata = filedata.replace('${mariadb_ip}', settings['mariadb_ip'])
                            #filedata = filedata.replace('${wiki_ip}', settings['wiki_ip'])
                            #filedata = filedata.replace('${shlink_ip}', settings['shlink_ip'])
                            #filedata = filedata.replace('${owncast_ip}', settings['owncast_ip'])
                            #filedata = filedata.replace('${jellyfin_ip}', settings['jellyfin_ip'])
                            #filedata = filedata.replace('${server_hostname}', server_hostname)
                            #filedata = filedata.replace('${target_deploy_path}', target_deploy_path)
                            #filedata = filedata.replace('${web_image}', web_image)
                            #filedata = filedata.replace('${mysql_image}', mysql_image)
                            #filedata = filedata.replace('${ldap_image}', ldap_image)

                        # Write changes to file
                        with open(os.path.join(trg,fname), 'w', encoding="utf-8") as file:
                            file.write(filedata)

main()