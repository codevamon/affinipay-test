FROM continuumio/miniconda3:latest

SHELL ["/bin/bash", "-c"]
WORKDIR /home/api

COPY . .

RUN chmod +x serve.sh

RUN conda install -y python=3.11

RUN conda env update -f environment.yml

RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate" >> ~/.bashrc

EXPOSE 5000

ENTRYPOINT ["./serve.sh"]
