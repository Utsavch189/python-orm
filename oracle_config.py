
DIALECT = 'oracle'
SQL_DRIVER = 'cx_oracle'
USERNAME = 'C##UTSAV' 
PASSWORD = 'admin' 
HOST='localhost'
PORT=1521
SERVICE='XE'
ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE
def b():
    return 5

if __name__=='__main__':
    b()