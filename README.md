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
- [Postman](#Postman)
</details>

___

## Deskripcija
##### Ovo je upustvo koje opisuje rad sa endpointima i postoje tri nacina kako mozes da ih testiras, podesis i sta ce da vrate kao rezultat.
___

## Licence
- Apache License 
- ##### [Procitaj vise o licencama](https://github.com/udomiljubimca/udomiljubimca-register-api/blob/develop/LICENSE)
___
## Postman
> Kloniraj postman kolekciju.

[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/aff5aba9dc9daff4ec0f)
___
## Podesavanja
![images/image_for_md.png](https://github.com/udomiljubimca/udomiljubimca-register-api/blob/fix/README.md/images/image_for_md.png)

> Pre testiranja potrebno je da se ugradi addon sa ovog linka <https://addons.mozilla.org/en-US/firefox/addon/modify-header-value/> i da se podesi kao na slici iznad(secret-key nije javno dostupan).

> Ako imas Avast(ili neki drugi antivirus) iskljuci ga zato sto moze da blokira slanje emaila.

___
## Upotreba

- <http://149.81.126.136/api/latest/register-api/docs#/> (Ovaj link nas vodi u main fail gde se nalaze pozvane klase sa njihovim funkcionalnostima,
takodje moze da se i testira njihov rad i procita dokumentacija endpointa).

### Health

- **Terminal**: curl -X 'GET' 'http://149.81.126.136/api/latest/register-api/health' -H 'accept: application/json' >> vraca {"HEALTH": "OK"}

- **Response**: 200

### Register-user

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
        
- **Response**: 200

- Ako se dva puta unesu isti username ili email i pokusa kreirati user vraca response (409-Conflict {"detail": "User already exists"})

### Resend-email

- **Terminal**:curl -X 'POST' \
        'http://149.81.126.136/api/latest/register-api/resend-email' \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{
        "username": "exemple"
        }' >> vraca {"message": "The email has been successfully sent!"} i salje na email verifikaciju

- **Response**: 200

- Ako se unese username koji nije postojeci vraca(404-Not found {"detail": "username does not exist"})

### Register-association

- **Terminal**: 
        
        curl -X 'POST' 'http://149.81.126.136/api/latest/register-api/register-association' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"email": "exemple@gmail.com","username": "exemple","secret": "exemple"}'
        Vraca {"message" : "The association has been successfully created!"} i salje na email verifikaciju.

- **Response**: 200

- Ako se dva puta unesu isti username ili email i pokusa kreirati user vraca response (409-Conflict {"detail": "association already exists"})
___

## Kontakt


___

