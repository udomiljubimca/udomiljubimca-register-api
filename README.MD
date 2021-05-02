# Register-API upotreba

Ovo je upuctvo koje opisuje rad sa endpointima i postoje tri nacina kako mozes da ih testiras, podesis i sta ce da vrate kao rezultat.


-http://localhost:8081/docs#/ (Ovaj link nas vodi u main fail gde se nalaze pozvane klase sa njihovim funkcionalnostima, 
takodje moze da se i testira njihov rad i procita dokumentacija endpointa).

# health:
    - **Postman**: http://udomi-ljubimca.com.internal/health >> metoda[GET] >> vraca {"HEALTH": "OK"}

    - **Terminal**: curl -X 'GET' 'http://localhost:8081/health' -H 'accept: application/json' >> vraca {"HEALTH": "OK"}

    - **Beleksa**: Ako koristits http://localhost:8081/docs#/ >> stisni na endpoint health[GET] >> try it out >> execute >> vraca {"HEALTH": "OK"}

    - **Response**: 200

# register-user:
    - Postman: http://udomi-ljubimca.com.internal/register-user >> metoda[POST] >> (body > raw > json) >> u body se upisuje /
             putem json-a {
                            "email" : "exemple@gmail.com",
                            "username" : "exemple",
                            "firstName" : "exemple",
                            "lastName" : "exemple",
                            "secret" : "exemple"
                          }  >> vraca {"message": "The user has been successfully created!"} i salje na email verifikaciju
    

    - Terminal: curl -X 'POST' \
        'http://localhost:8081/register-user' \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{
        "email" : "exemple@gmail.com",
            "username" : "exemple",
            "firstName" : "exemple",
            "lastName" : "exemple",
            "secret" : "exemple"
        }'  >> vraca {"message": "The user has been successfully created!"} i salje na email verifikaciju

    - Beleksa: Ako koristits http://localhost:8081/docs#/ stisni na endpoint register-user[POST] >> try it out >> popunis json >> execute >> vraca /
            {"message": "The user has been successfully created!"} i salje na email verifikaciju

    - Response: 200

    >!< Ako se dva puta unesu isti username ili email i pokusa kreirati user vraca response (409-Conflict {"detail": "User already exists"})
    >!< Ako imas Avast(ili neki drugi antivirus) iskljuci ga zato sto moze da blokira slanje emaila

# resend-email:
    - Postman: http://localhost:8081/resend-email >> metoda[POST] >> (body > raw > json) >> u body se upisuje /
             putem json-a {"username" : "exemple"}  >> vraca {"message": "The email has been successfully sent!"} i salje na email verifikaciju
    

    - Terminal:curl -X 'POST' \
        'http://localhost:8081/resend-email' \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{
        "username": "exemple"
        }' >> vraca {"message": "The email has been successfully sent!"} i salje na email verifikaciju


    - Beleksa: Ako koristits http://localhost:8081/docs#/ stisni na endpoint resend-email[POST] >> try it out >> popunis json >> execute >> vraca /
            {"message": "The email has been successfully sent!"} i salje na email verifikaciju

    - Response: 200

    >!< Ako se unese username koji nije postojeci vraca(404-Not found {"detail": "username does not exist"})
    >!< Ako imas Avast(ili neki drugi antivirus) iskljuci ga zato sto moze da blokira slanje emaila

# register-association:
    - Postman: http://udomi-ljubimca.com.internal/register-association >> metoda[POST] >> (body > raw > json) >> u body se upisuje /
             putem json-a {
            "email" : "exemple@gmail.com",
            "username_association" : "exemple",
            "secret" : "exemple"
            }  >> vraca {"message" : "The association has been successfully created!"} i salje na email verifikaciju

    - Terminal: curl -X 'POST' \
        'http://localhost:8081/register-association' \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{
        "email": "exemple@gmail.com",
        "username_association": "exemple",
        "secret": "exemple"
        }' >> vraca {"message" : "The association has been successfully created!"} i salje na email verifikaciju

    - Beleksa: Ako koristits http://localhost:8081/docs#/ stisni na endpoint register-user[POST] >> try it out >> popunis json >> execute >> vraca /
            {"message": "The association has been successfully created!"} i salje na email verifikaciju


    - Response: 200
    >!< Ako se dva puta unesu isti username ili email i pokusa kreirati user vraca response (409-Conflict {"detail": "association already exists"})
    >!< Ako imas Avast(ili neki drugi antivirus) iskljuci ga zato sto moze da blokira slanje emaila
