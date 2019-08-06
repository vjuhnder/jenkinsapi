import jenkinsapi
from jenkinsapi.jenkins import Jenkins

def get_server_instance():
    jenkins_url = 'http://192,168.91.200:8080'
    server = Jenkins(jenkins_url, username='vigneswaranjagadeesan _vigneswaran@uhnder.com_', password='JENKINSsiva@1')
    return server

if __name__ == '__main__':
    print get_server_instance().version
