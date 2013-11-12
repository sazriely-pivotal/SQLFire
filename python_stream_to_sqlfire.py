import jaydebeapi
import jpype
jar = r'sqlfireclient.jar'
args = '-Djava.class.path=%s' % jar
jvm_path = jpype.getDefaultJVMPath()
jpype.startJVM(jvm_path, args)

conn = jaydebeapi.connect('com.vmware.sqlfire.jdbc.ClientDriver', r'jdbc:sqlfire://SERVER:1527/;single-hop=true',
                         'sqlfire', 'changeme')
curs = conn.cursor()
curs.execute("insert into app.table1 values ('loaded using python')")