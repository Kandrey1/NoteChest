import requests

try:
    url_s_user = "http://localhost:5000/api/user/test/work_service/status"
    res_user = requests.get(url_s_user)

    if res_user.status_code == 200:
        print("Service USER: OK")
    else:
        print("Service USER: NO CONNECT")
except:
    print("Service USER: Error")
