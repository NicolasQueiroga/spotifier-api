# Spotifier Django Rest API
To run the API on your computer, docker-compose is required (<a href='https://docs.docker.com/compose/install/'>Install docker-compose</a>)

First, run the development server at the root:

```bash
cp .env.sample .env
```

And then, run the development server at the root:

```bash
docker-compose up
```

## Check routes with Postman
[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/15550746-20b1ecab-32f9-406b-b40e-0ed398165ad9?action=collection%2Ffork&collection-url=entityId%3D15550746-20b1ecab-32f9-406b-b40e-0ed398165ad9%26entityType%3Dcollection%26workspaceId%3D37f19914-65b2-4397-b733-0e70228176c1#?env%5BAPI%5D=W3sia2V5IjoidXNlcm5hbWUiLCJ2YWx1ZSI6Im5pY2siLCJlbmFibGVkIjp0cnVlfSx7ImtleSI6ImVtYWlsIiwidmFsdWUiOiJuaWNvbGFzQG5pY29sYXMuY29tIiwiZW5hYmxlZCI6dHJ1ZX0seyJrZXkiOiJwYXNzd29yZCIsInZhbHVlIjoic2FmaXJhMTIiLCJlbmFibGVkIjp0cnVlfSx7ImtleSI6ImZpcnN0X25hbWUiLCJ2YWx1ZSI6Ik5pY29sYXMiLCJlbmFibGVkIjp0cnVlfSx7ImtleSI6Imxhc3RfbmFtZSIsInZhbHVlIjoiUXVlaXJvZ2EiLCJlbmFibGVkIjp0cnVlfSx7ImtleSI6InBob25lIiwidmFsdWUiOiIxMjk5NzI4MjU1OCIsImVuYWJsZWQiOnRydWV9LHsia2V5IjoidG9rZW4iLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWV9LHsia2V5IjoiZW1haWwyIiwidmFsdWUiOiJuaWNvbGFzMUBuaWNvbGFzLmNvbSIsImVuYWJsZWQiOnRydWV9XQ==)

## Deploy URL
To use Spotifier, I will need to register your email linked with spotify at the API dashboard app (n.macielqueiroga@gmail.com), and it is required to allow `Insecure content` within the browser, so that requests to the deployed Django Rest API are accepted.
- https://spotifier-app.herokuapp.com/
