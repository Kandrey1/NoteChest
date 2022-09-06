from subprocess import check_call

test_smoke = False

try:
    check_call("docker build -t smk .".split())
    check_call("docker run --name smk_cont -p 5000:5000 -d smk".split())
    test_smoke = True
except Exception:
   pass
finally:
    check_call("docker stop smk_cont".split())
    check_call("docker rm smk_cont".split())
    check_call("docker rmi smk".split())
    res_test = 'OK' if test_smoke else 'ERROR'
    print(f"Service USER: TESTING {res_test}")
