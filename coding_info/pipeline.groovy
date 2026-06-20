pipeline{
    agent any
    stages{
        stage("checkout"){
            steps{
                checkout git: [
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [],
                    submoduleCfg: [],
                    userRemoteConfigs: [[url: 'https://github.com/myorg/myrepo.git']]
                    credentialsId: 'my-credentials-id'

                ]

            }


        }
        stage("build"){
            steps{
                sh "mvn clean package"  
            }
        }
        stage("deploy"){
            steps{
                sh "kubectl apply -f k8s/deployment.yaml"
            }
        }       
        stage("test"){
            steps{
                sh "curl http://myapp.example.com/health"
            }
        } 
        stage("artifact upload"){
            steps{
                sh "jfrog rt u target/myapp.jar my-repo/myapp/ --build-name=my-build --build-number=1"

            }
        }       

    }
    post{
        always{
            junit 'target/surefire-reports/*.xml'
        }
        failure{
            mail to: '<EMAIL>'
        }
        success{
            mail to: '<EMAIL>'
        }   
    }   
    

}