# Inicia seleccionando la imagen de base
FROM ubuntu

LABEL Martin Vega <mjvnor@outlook.com>

WORKDIR /root

RUN  apt-get -y update && \
     apt-get install -yq curl nano vim unzip git pip python3.8 python3-pip

RUN pip install csvkit pandas matplotlib numpy plotly kaleido

RUN  curl -L -O https://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/historicos/2022/01/datos_abiertos_covid19_01.01.2022.zip &&\
     unzip datos_abiertos_covid19_01.01.2022.zip &&\
     csvcut -c SEXO,EDAD,INTUBADO,NEUMONIA 220101COVID19MEXICO.csv > DataProblema.csv &&\
     rm datos_abiertos_covid19_01.01.2022.zip &&\
     rm 220101COVID19MEXICO.csv

ADD resolver.py /root/resolver.py

RUN python3 resolver.py

CMD ["bash"]