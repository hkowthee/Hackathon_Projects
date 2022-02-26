from datetime import datetime

finish_time = datetime(2022, 2, 25, 20)

site_to_block = ['www.pornhub.com', 'pornhub.com' ]

host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

def block_sites():
    if datetime.now() < finish_time:
        print("blocking sites")
        with open(host_path, 'r+') as hostfile:
            host_content = hostfile.read()
            for site in site_to_block:
                if site not in host_content:
                    hostfile.write(redirect + " " + site + "\n")

    else:
        print("unblocking sites")
        with open(host_path, 'r') as hostfile:
            lines = hostfile.readlines()
            hostfile.seek(0)
            for line in lines:
                if not any(site in line for site in site_to_block):
                    hostfile.write(line)
            hostfile.truncate()

if __name__ == "__main__":
    block_sites()