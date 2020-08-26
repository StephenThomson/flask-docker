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
# It is recommended not to run Jenkins as root, but when running as the jenkins user,
# it can't access /var/run/docker.sock, so we can't run docker commands in the
# jenkins_workshop container :-(
# USER jenkins
