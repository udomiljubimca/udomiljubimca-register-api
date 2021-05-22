FROM udomiljubimca/base-image:1.0

ADD ./server.sh ./requirements.txt ./src /app/

RUN pip install --no-cache-dir -r /app/requirements.txt && \
    chown -R appuser:root /app && \
    chmod -R g=u /app

ENV FLASK_ENV ${FLASK_ENV}
ENV KEYCLOAK_ADMIN_USER ${KEYCLOAK_ADMIN_USER}
ENV KEYCLOAK_ADMIN_PASSWORD ${KEYCLOAK_ADMIN_PASSWORD}
ENV CLIENT_RELM_SECRET ${CLIENT_RELM_SECRET}
ENV CLIENT_RELM_NAME ${CLIENT_RELM_NAME}
ENV KEYCLOAK_URL ${KEYCLOAK_URL}
ENV KEYCLOAK_CLIENT_NAME ${KEYCLOAK_CLIENT_NAME}

WORKDIR /app

USER appuser

EXPOSE 8080

CMD ["/bin/bash", "server.sh"]