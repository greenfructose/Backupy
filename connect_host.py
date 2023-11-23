import paramiko

hostname = ''

client = paramiko.SSHClient()
client.load_host_keys('known_hosts')
client.connect(hostname=hostname, username='devadmin', key_filename='id_rsa')