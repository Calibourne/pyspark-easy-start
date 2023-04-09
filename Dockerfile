FROM docker.io/bitnami/spark
USER root
RUN install_packages g++ cmake libopenmpi-dev build-essential
RUN pip install \
    horovod[tensorflow,keras,pytorch,mxnet,spark] \
    tensorflow
RUN pip install pyarrow \
    parquet \
    py4j

    # ultralytics

USER 1001
ENTRYPOINT [ "/opt/bitnami/scripts/spark/entrypoint.sh" ]
CMD [ "/opt/bitnami/scripts/spark/run.sh" ]
