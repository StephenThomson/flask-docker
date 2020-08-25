FROM jenkins/jenkins:lts
USER root
RUN apt-get update \
    && apt-get -y install apt-transport-https \
        ca-certificates \
        curl \
        gnupg2 \
        software-properties-common \
    && curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - \
    && add-apt-repository \
        "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo \"$ID\") \
        $(lsb_release -cs) \
        stable" \
    && apt-get update \
    && apt-get install -y docker-ce docker-ce-cli containerd.io \
    && usermod -aG docker jenkins
#RUN ls -al /var/run/docker.sock
#RUN chmod 666 /var/run/docker.sock
USER jenkins
