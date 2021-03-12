# Feedback App
It is an application designed using tornado which has the capabilities to
- Post a feedback
- view the feedbacks
- Upload the system logs to [Minio](https://www.minio.io/)

![](/static/images/ss.png)


### Running the Application

1. Clone this repository
    ```sh
    git clone https://github.com/Sathiyakugan/assignment_backend_server.git
    cd assignment_backend_server
    ```
2. In the `minio_config.py` replace the placeholders with the  `ENDPOINT`, `ACCESS_KEY`, and `SECRET_KEY` with your configuration.
3. Use Docker Compose to build and run the app 
    ```
    docker-compose up
    ```  
4. visit   http://localhost:8000/  
5. Enjoy the Application. 

License
----
MIT