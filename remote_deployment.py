import paramiko
import os

TARGET = "/home/isid/arcrawler"

def put_dir(sftp, source, target):
    """ Copy a whole directory in a recursive way. 
        This function assume that all the source and target are in linux format.
        Therefore, os.path.join() is not implemented.
    """
    for item in os.listdir(source):
        if os.path.isfile(os.path.join(source,item)):
            sftp.put("{}/{}".format(source,item), "{}/{}".format(target,item))
        else:
            sftp.mkdir("{}/{}".format(target, item), 511)
            put_dir(sftp, "{}/{}".format(source,item), "{}/{}".format(target,item))

if __name__ == "__main__":
    print("[remote_deployment][debug] Connecting...")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("203.125.16.21", username="isid", port=8661, key_filename="./isid.openssh")
    print("[remote_deployment][debug] Connected!")
    
    print("[remote_deployment][debug] Cleanning the files.")
    sftp                  = ssh.open_sftp()
    stdin, stdout, stderr = ssh.exec_command("sudo rm -rv {}".format(TARGET), get_pty=True)
    stdin.write("isid123\n")
    stdin.flush()
    exit_code = stdout.channel.recv_exit_status() # wait until the command gives exit_status
    
    if exit_code == 0:
        print("[remote_deployment][debug] Deploying...")
        sftp.mkdir(TARGET, 511)
        sftp.mkdir("{}/lib".format(TARGET), 511)
        sftp.mkdir("{}/src".format(TARGET), 511)
        sftp.mkdir("{}/templates".format(TARGET), 511)
        sftp.put("./run.py", "{}/run.py".format(TARGET))
        sftp.put("./build.py", "{}/build.py".format(TARGET))
        sftp.put("./kick_start.sh", "{}/kick_start.sh".format(TARGET))
        sftp.put("./config.json", "{}/config.json".format(TARGET))
        put_dir(sftp, "./lib", "{}/lib".format(TARGET))
        put_dir(sftp, "./src", "{}/src".format(TARGET))
        put_dir(sftp, "./templates", "{}/templates".format(TARGET))  

        stdin, stdout, stderr = ssh.exec_command("docker restart arcrawler")    
        print("[remote_deployment][debug] Restarting arcrawler: {}".format(stdout.channel.recv_exit_status()))

        stdin, stdout, stderr = ssh.exec_command("docker exec -d arcrawler bash /root/app/kick_start.sh")    
        print("[remote_deployment][debug] Executing kick_start.sh: {}".format(stdout.channel.recv_exit_status()))
    
        ssh.close()
        print("[remote_deployment][debug] Deployed!")
    else:
        ssh.close()
        print("[remote_deployment][error] Failed!")
