from pyspark.sql import SparkSession
from pyspark import SparkConf
from subprocess import check_output

def init_spark_session(session_name: str, 
                       spark_master="spark://spark:7077", deploy_mode="client",
                       console_progress=True, log_conf=False, event_log=False, 
                       bind_address="0.0.0.0"
                       ) -> SparkSession:
    """
    Initializes Spark Session with a given name
    
    Parameters:
    -----------
    session_name: str
        Name of the Spark Session
    
    return:
    -------
    - SparkSession
    """
    
    console_progress = "true" if console_progress else "false"
    log_conf = "true" if log_conf else "false"
    event_log = "true" if event_log else "false"
    SPARK_DRIVER_HOST = check_output(["hostname", "-i"]).decode(encoding="utf-8").strip()
    conf = SparkConf()
    conf.setAll([
        (
            "spark.master",
            spark_master,
        ),  # <--- this host must be resolvable by the driver in this case pyspark (whatever it is located, same server or remote) in our case the IP of server
        ("spark.app.name", session_name),
        ("spark.submit.deployMode", deploy_mode),
        ("spark.ui.showConsoleProgress", console_progress),
        ("spark.eventLog.enabled", event_log),
        ("spark.logConf", log_conf),
        (
            "spark.driver.bindAddress",
            bind_address,
        ),  # <--- this host is the IP where pyspark will bind the service running the driver (normally 0.0.0.0)
        (
            "spark.driver.host",
            SPARK_DRIVER_HOST,
        ),  # <--- this host is the resolvable IP for the host that is running the driver and it must be reachable by the master and master must be able to reach it (in our case the IP of the container where we are running pyspark
    ])
    return SparkSession.builder.config(conf=conf).getOrCreate()

def fancy_print(prompt):
    padding = ''.join('=' for _ in list(prompt))
    print(f'{padding}\n{prompt}\n{padding}')