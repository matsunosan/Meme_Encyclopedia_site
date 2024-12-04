pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/matsunosan/Meme_Encyclopedia_site.git'
            }
        }
        stage('Build') {
            steps {
                // Here, we can include steps to build the project if necessary
                script {
                    echo 'Building project...'
                }
            }
        }
        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: '**/*.html, **/*.css, **/*.js', allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
    }
}
