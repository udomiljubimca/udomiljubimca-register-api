FROM udomiljubimca/base-image:1.0

ADD ./requirements.txt server.sh ./src/* /app/

RUN pip install --no-cache-dir -r /app/requirements.txt && \
    chown -R appuser:appuser /app

ENV FLASK_ENV=development
ENV KYECLOAK_ADMIN_USER="admin"
ENV KYECLOAK_ADMIN_PASSWORD=""

WORKDIR /app

USER appuser

EXPOSE 8080

CMD ["/bin/bash", "/app/server.sh"]