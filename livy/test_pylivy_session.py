from livy import LivySession

LIVY_URL = 'http://sandbox-hdp.hortonworks.com:8999'

with LivySession(LIVY_URL) as session:
    # Run some code on the remote cluster
    output = session.run("1+1")
    print(output)