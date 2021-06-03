[![Issues][issues]][issues-url]

[issues]: https://img.shields.io/github/issues/udomiljubimca/udomiljubimca-register-api/issues.svg?style=for-the-badge
___
# Register-API

<details open>

**<summary> Lista koncepta </summary>**

- [Deskripcija](#Deskripcija) 
- [Licence](#Licence)
- [Podesavanja](#Podesavanja)
- [Postman](#Postman)
- [Upotreba](#Upotreba)
  - [Register-api endpoints](#Register-api)    
    - [Health](#Health)
    - [Register-user](#Register-user)
    - [Register-association](#Register-association)
    - [Resend-email](#Resend-email)
- [Kontakt](#Kontakt)
</details>

___

## Deskripcija
##### Ovo je upustvo koje opisuje rad sa endpointima i postoje tri nacina kako mozes da ih testiras, podesis i sta ce da vrate kao rezultat.


## Licence
- Apache License 
- ##### [Procitaj vise o licencama](https://github.com/udomiljubimca/udomiljubimca-register-api/blob/develop/LICENSE)


## Postman
- Kloniraj postman kolekciju.

[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/aff5aba9dc9daff4ec0f)


## Podesavanja
![images/image_for_md.png](https://github.com/udomiljubimca/udomiljubimca-register-api/blob/fix/README.md/images/image_for_md.png)

> Pre testiranja potrebno je da se ugradi addon sa ovog linka <https://addons.mozilla.org/en-US/firefox/addon/modify-header-value/> i da se podesi kao na slici iznad(secret-key nije javno dostupan).

> Ako imas Avast(ili neki drugi antivirus) iskljuci ga zato sto moze da blokira slanje emaila.


## Upotreba

- <http://149.81.126.136/api/latest/register-api/docs#/> (Pristup Swagger dokumentaciji.).


### Health

- **Terminal**: 

        curl -X 'GET' 'http://149.81.126.136/api/latest/register-api/health' -H 'accept: application/json'  
        return {"HEALTH": "OK"}

> **Response**: 200


### Register-user

- **Terminal**: 

        curl -X 'POST' 'http://149.81.126.136/api/latest/register-api/register-user' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"email" : "exemple@gmail.com","username" : "exemple","firstName" : "exemple","lastName" : "exemple","secret" : "exemple"}'  
        return {"message": "The user has been successfully created!"} salje na email verifikaciju.
        
> **Response**: 200

- Ako se dva puta unesu isti username ili email i pokusa kreirati user vraca response (409-Conflict {"detail": "User already exists"})


### Resend-email

- **Terminal**:

        curl -X 'POST' 'http://149.81.126.136/api/latest/register-api/resend-email' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"username": "exemple"}'
        return {"message": "The email has been successfully sent!"} 

> **Response**: 200

- Ako se unese username koji nije postojeci vraca(404-Not found {"detail": "username does not exist"})


### Register-association

- **Terminal**: 
        
        curl -X 'POST' 'http://149.81.126.136/api/latest/register-api/register-association' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"email": "exemple@gmail.com","username": "exemple","secret": "exemple"}'
        return {"message" : "The association has been successfully created!"}

> **Response**: 200

> **HTTPexception**:{"detail": "association already exists"},409) Username/email treba da budu jedinstveni!


## Kontakt


___

