from unicodedata import name
import docker

# Invocar el ambiente de docker
client = docker.from_env()

# Crear una instancia de docker que apunte al localhost con la clase DockerClient
cli = docker.DockerClient(base_url='unix://var/run/docker.sock')

# Matar contenedores ya existentes con la clase APIClient
c = docker.APIClient()
containers = cli.containers.list()
if containers:
    print("Old containers found")
    cont_name = containers[0].name
    c.kill(cont_name, signal=None)
    print ("Previously existing containers have been killed successfully")
else:
    print("No previously started containers. Proceeding to containerize a new app")

# Contenerizar la app
current_container = client.containers.run("ubuntu", command="/bin/bash", tty=True, detach=True)
cont_name = current_container.name
status = current_container.status
print ("New continer created. Name:", cont_name, "\nStatus:", status)

while True:
    running_container = client.containers.get(cont_name)
    current_status = running_container.status
    
    if current_status == "exited" or current_status == "dead":
        current_container = client.containers.prune()
        current_container = client.containers.run("ubuntu", command="/bin/bash", tty=True, detach=True)
        cont_name = current_container.name
        print ("Container was manually stopped by user. Starting a new one. Name:", cont_name, "\nStatus:", status)


    elif current_status == "paused":
        running_container.unpause()
        print("Container unpaused successfully")

    



