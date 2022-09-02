import time
import requests
from subprocess import check_call

check_call("docker build -t smk .".split())
check_call("docker run --name smk_cont -p 5000:5000 -d smk".split())

time.sleep(5)
try:
    url_s_front = "http://localhost:5000/user/test/work_service/status"
    res_front = requests.get(url_s_front)

    if res_front.status_code == 200:
        print("Service FRONTED: OK")
    else:
        print("Service FRONTED: NO CONNECT")
except:
    print("Service FRONTED: Error")
finally:
    check_call("docker stop smk_cont".split())
    check_call("docker rm smk_cont".split())
    check_call("docker rmi smk".split())
    print("Service USER: TESTING OK")
