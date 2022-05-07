from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
        'secure_connect_bundle': 'secure-connect-ineuron-db.zip'
}
auth_provider = PlainTextAuthProvider('vpxWcTebiYsoCTjlKjYOpOKD', 'BJUs2M_Id3sqBZm7,LlLfj4W7M.+WcEYUJirZ4iUAn7WfjjF0cBH,cGyxsT.ZbGJZodSHKbx4cDr+rxqJzDQFwayv6pzSSQCBaZ.p16a2_e4IFUf0bZXDNakDsWy+p-v')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()


#row = session.execute("CREATE KEYSPACE bhard2 WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 4};").one()
row = session.execute("SELECT * FROM system_schema.keyspaces").one()


if row:
    print(row[0])
else:
    print("An error occurred.")

