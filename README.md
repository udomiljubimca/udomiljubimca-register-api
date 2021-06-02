# Register-API upotreba

> Kratak uvod u projekat
___


<details open>

**<summary> Lista koncepta </summary>**

- [Deskripcija](#Deskripcija) 
- [Licence](#Licence)
- [Podesavanja](#Podesavanja)
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
Ovo je upustvo koje opisuje rad sa endpointima i postoje tri nacina kako mozes da ih testiras, podesis i sta ce da vrate kao rezultat.
___

## Licence
- Apache License 
- ##### [Procitaj vise o licencama](https://github.com/udomiljubimca/udomiljubimca-register-api/blob/develop/LICENSE)
___

## Podesavanja
![images/image_for_md.png](https://github.com/udomiljubimca/udomiljubimca-register-api/blob/fix/README.md/images/image_for_md.png)

- Pre testiranja potrebno je da se ugradi addon sa ovog linka <https://addons.mozilla.org/en-US/firefox/addon/modify-header-value/> i da se podesi kao na slici iznad(secret-key nije javno dostupan).

___
## Upotreba

- <http://149.81.126.136/api/latest/register-api/docs#/> (Ovaj link nas vodi u main fail gde se nalaze pozvane klase sa njihovim funkcionalnostima,
takodje moze da se i testira njihov rad i procita dokumentacija endpointa).

### Health

- **Postman**:  <http://149.81.126.136/api/latest/register-api/health> >> metoda[GET] >> vraca {"HEALTH": "OK"}

- **Terminal**: curl -X 'GET' 'http://149.81.126.136/api/latest/register-api/health' -H 'accept: application/json' >> vraca {"HEALTH": "OK"}

- **Beleksa**: Ako koristits <http://149.81.126.136/api/latest/register-api/health> >> stisni na endpoint health[GET] >> try it out >> execute >>
                vraca {"HEALTH": "OK"}

- **Response**: 200

### Register-user

- **Postman**: <http://149.81.126.136/api/latest/register-api/register-user> >> metoda[POST] >> (body > raw > json) >> u body se upisuje /
        putem json-a {
                        "email" : "exemple@gmail.com",
                        "username" : "exemple",
                        "firstName" : "exemple",
                        "lastName" : "exemple",
                        "secret" : "exemple"
                        }  >> vraca {"message": "The user has been successfully created!"} i salje na email verifikaciju

- **Terminal**: curl -X 'POST' \
        'http://149.81.126.136/api/latest/register-api/register-user' \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{
        "email" : "exemple@gmail.com",
            "username" : "exemple",
            "firstName" : "exemple",
            "lastName" : "exemple",
            "secret" : "exemple"
        }'  >> vraca {"message": "The user has been successfully created!"} i salje na email verifikaciju
        
- **Beleksa**: Ako koristits <http://149.81.126.136/api/latest/register-api/docs#/> stisni na endpoint register-user[POST] >> try it out >> popunis json >> execute >> vraca /
            {"message": "The user has been successfully created!"} i salje na email verifikaciju

- **Response**: 200

- Ako se dva puta unesu isti username ili email i pokusa kreirati user vraca response (409-Conflict {"detail": "User already exists"})
- Ako imas Avast(ili neki drugi antivirus) iskljuci ga zato sto moze da blokira slanje emaila

### Resend-email

- **Postman**: <http://149.81.126.136/api/latest/register-api/resend-email> >> metoda[POST] >> (body > raw > json) >> u body se upisuje /
             putem json-a {"username" : "exemple"}  >> vraca {"message": "The email has been successfully sent!"} i salje na email verifikaciju

- **Terminal**:curl -X 'POST' \
        'http://149.81.126.136/api/latest/register-api/resend-email' \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{
        "username": "exemple"
        }' >> vraca {"message": "The email has been successfully sent!"} i salje na email verifikaciju

- **Beleksa**: Ako koristits <http://149.81.126.136/api/latest/register-api/docs#/> stisni na endpoint resend-email[POST] >> try it out >> popunis json >> execute >> vraca /
            {"message": "The email has been successfully sent!"} i salje na email verifikaciju

- **Response**: 200

- Ako se unese username koji nije postojeci vraca(404-Not found {"detail": "username does not exist"})
- Ako imas Avast(ili neki drugi antivirus) iskljuci ga zato sto moze da blokira slanje emaila

### Register-association

- **Postman**: <http://149.81.126.136/api/latest/register-api/register-association> >> metoda[POST] >> (body > raw > json) >> u body se upisuje /
             putem json-a {
            "email" : "exemple@gmail.com",
            "username" : "exemple",
            "secret" : "exemple"
            }  >> vraca {"message" : "The association has been successfully created!"} i salje na email verifikaciju

- **Terminal**: 
        
        curl -X 'POST' 'http://149.81.126.136/api/latest/register-api/register-association' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"email": "exemple@gmail.com","username": "exemple","secret": "exemple"}'
> Vraca {"message" : "The association has been successfully created!"} i salje na email verifikaciju.


- **Beleksa**: Ako koristits <http://149.81.126.136/api/latest/register-api/docs#/> stisni na endpoint register-user[POST] >> try it out >> popunis json >> execute >> vraca /
            {"message": "The association has been successfully created!"} i salje na email verifikaciju

- **Response**: 200

- Ako se dva puta unesu isti username ili email i pokusa kreirati user vraca response (409-Conflict {"detail": "association already exists"})
- Ako imas Avast(ili neki drugi antivirus) iskljuci ga zato sto moze da blokira slanje emaila

___

## Kontakt

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/15bfcf4c-0741-456f-ae44-077bae793059)
___

