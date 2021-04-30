FROM udomiljubimca/base-image:1.0

ADD ./server.sh ./requirements.txt ./src /app/

RUN pip install --no-cache-dir -r /app/requirements.txt && \
    chown -R appuser:root /app && \
    chmod -R g=u /app

ENV FLASK_ENV="development"
ENV KEYECLOAK_ADMIN_USER="admin"
ENV KEYECLOAK_ADMIN_PASSWORD=""
ENV CLIENT_RELM_SECRET=""
ENV CLIENT_RELM_NAME="udomiljubimcadev"
ENV KEYCLOAK_URL="http://nginx"
ENV KEYCLOAK_CLIENT_NAME="app"


WORKDIR /app

USER appuser

EXPOSE 8080

CMD ["/bin/bash", "server.sh"]