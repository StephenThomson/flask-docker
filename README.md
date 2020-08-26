# An Introduction to Jenkins & Continous Integration

Just a little something to introduce some people to CI/CD with Jenkins

## Sample App

A hacked together Flask API in a docker container

Build: `./build.sh`

Run: `./run.sh`

Test: `./dockertest.sh`

## Jenkins

### Setting up Jenkins

* Fire up Jenkins in a Docker conatiner with Docker Compose `docker-compose up`

* Hit http://localhost:8080/ and log in with the admin password you got in the output from the previous command

* Install suggested plugins

* Create your admin user and click through past "Save and continue"

### Setting up our pipeline

* Click "Create a job"

* Enter a name, select "Pipeline" and click "OK"

* General

  * Check "Do not allow concurrent builds"

  * Check "GitHub project" and enter the URL "https://github.com/StephenThomson/flask-docker"
  
  * Check "This project is parameterised"
  
    * Select "String parameter"
    * Enter "BRANCH" for the name
    * Enter "master" as the default

* Build Triggers

  * Ignore this for now
  
* Advanced Project Options

  * Ignore this for now

* Pipeline

  * Select "Pipeline script from SCM" (Source Code Management)
  
  * Enter the repository URL "https://github.com/StephenThomson/flask-docker"
  
  * Delete the "Branch Specifier" (so it can build any branch based on the branch parameter)
  
  * Uncheck "Lightweight checkout"

* Click "Save"

### Useful commands

* Log into the jenkins container `docker exec -it jenkins_workshop /bin/bash`

* Run the Jenkins container in the background `docker-compose up`

* Stop the Jenkins container if you ran it in the background `docker-compose down`

### References

* https://github.com/jenkinsci/docker/blob/master/README.md

* https://www.jenkins.io/doc/book/pipeline/jenkinsfile/

* https://itnext.io/docker-in-docker-521958d34efd

