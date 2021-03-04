# Feedback App
It is an application designed using tornado which has the capabilities to
- Post a feedback
- view the feedbacks
- Upload the system logs to [Minio](https://www.minio.io/)

![](/static/images/ss.png)

### Pre Requesties
This application uses Python3. Please make sure you have installed it.
You need to have pip installed along with the Python.

following requirements need to be installed
- tornado
- minio

```sh
$ pip3 install -r requirements.txt
```

In the `minio_config.py` replace the placeholders with the  `ENDPOINT`, `ACCESS_KEY`, and `SECRET_KEY` with your configuration. 

### Running the Application
1. In the terminal execute the following command:
    ```sh
    $ python3 app.py 
    ```
   Please note that  in some linux versions you can use   `python app.py `  
2. visit   http://localhost:8000/  
3. Enjoy the Application. 

License
----
MIT