# README #

## Info

This repository contains the source needed to execute a container that hosts a simple api. Please follow the instructions to get the api running on your local system and then 
write automated test cases for the running api. Please make note of any bugs you find in the service in your response to us. Feel free to leverage whatever language/framework you are most comfortable with. 

## Installing dependencies 

Please install the following dependencies:

1) Docker
   1) https://docs.docker.com/engine/install/
2) Git
   1) https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

## Cloning Exercise Repo
```aidl
git clone https://github.com/affinipay/candidate-exercise.git
```

## IMPORTANT NOTE - Windows Users

If you are using a Windows system to complete this exercise, make sure that your IED is setup to use LF rather than CRLF for EndOfLine(EoL). If your system is using the wrong EoL designator, you will receive a 'No Such File' error when attempting to start the container 
See this post for more information:

[CRLF to LF in VisualStudios](https://www.petersplanet.nl/index.php/2023/08/28/line-breaks-in-visual-studio-code-and-git-lf-vs-crlf/#:~:text=In%20VS%20Code%20you%20easily,the%20settings%20with%20the%20%E2%80%9Cfiles.)
## Building and Running Container
To Build:
```aidl
docker build -t exercise:1.0 .
```
To Run:
```aidl
docker run --name demo -it -p 5000:5000 exercise:1.0
```
You should now be able to access the api through this URL

```aidl
http://127.0.0.1:5000/dogs
```

## API SPEC

The api provides an endpoint to create, view and delete dogs from the system. 

End users are allowed to create dogs by POSTing to http://127.0.0.1:5000/dogs, the request payload should contain the following fields

```aidl
{
    "breed": <string>,
    "age":   <int>,
    "name":  <string>
}
```
The system assigns a unique ID to each dog created which will be visible in the POST response. This ID can be used to view and delete dogs from the system through the URL http://127.0.0.1:5000/dogs/<dog_id>