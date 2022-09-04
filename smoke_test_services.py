import requests

try:
    url_s_front = "http://localhost:5000/user/test/work_service/status"
    res_front = requests.get(url_s_front)

    if res_front.status_code == 200:
        print("Service FRONTED: OK")
    else:
        print("Service FRONTED: NO CONNECT")
except:
    print("Service FRONTED: Error")

try:
    url_s_user = "http://localhost:5001/api/user/test/work_service/status"
    res_user = requests.get(url_s_user)

    if res_user.status_code == 200:
        print("Service USER: OK")
    else:
        print("Service USER: NO CONNECT")
except:
    print("Service USER: Error")

try:
    url_s_user = "http://localhost:5002/api/link/test/work_service/status"
    res_user = requests.get(url_s_user)

    if res_user.status_code == 200:
        print("Service LINK: OK")
    else:
        print("Service LINK: NO CONNECT")
except:
    print("Service LINK: Error")
