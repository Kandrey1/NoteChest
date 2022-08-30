import time
import requests
from subprocess import check_call

check_call("docker build -t smk .".split())
check_call("docker run --name smk_cont -p 5000:5000 -d smk".split())

time.sleep(5)
try:
    url_testing = "http://localhost:5000/api/user/test/work_service/status"
    res = requests.get(url_testing)

    if res.status_code == 200:
        print("Service USER: OK")
except Exception:
    print("Service USER: Error")
finally:
    check_call("docker stop smk_cont".split())
    check_call("docker rm smk_cont".split())
    check_call("docker rmi smk".split())
    print("Service USER: TESTING OK")
