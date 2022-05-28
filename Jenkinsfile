pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
    	            //sh 'cd /home/george/Desktop/Demo'
                script {
            sh(script: 'python3 /home/george/Desktop/Demo/t3.py', returnStdout: true)

        }
    	                  
            }
        }
    }
}




