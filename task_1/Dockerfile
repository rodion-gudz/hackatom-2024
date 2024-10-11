FROM python:3.11

RUN apt-get update && apt-get install -y \
    sudo \
    zip \
    unzip \
    vim \
    less

RUN useradd -m maxim

RUN mkdir -p /home/maxim/project && \
    echo "flag{gr4t5_y0u_g0t_1t}" > /home/maxim/project/flag.txt && \
    zip -P a3sq2VeKdFyRvzBjEADLbT /home/maxim/project/flag.zip /home/maxim/project/flag.txt && \
    rm /home/maxim/project/flag.txt && \
    chown maxim:maxim /home/maxim/project/flag.zip

RUN chmod 600 /home/maxim/project/flag.zip

RUN cp /bin/bash /usr/local/bin/suidbash && chmod +s /usr/local/bin/suidbash

RUN echo "unzip -P a3sq2VeKdFyRvzBjEADLbT flag.zip" >> /root/.bash_history

RUN echo "maxim ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]