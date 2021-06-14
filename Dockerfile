FROM python:3.9.5-buster AS easter_souls_env

RUN pip install pandas

# ----------------------------------------------------

FROM easter_souls_env AS easter_souls_app

WORKDIR /usr/src

COPY . .

ENTRYPOINT [ "python", "easter_egg_hunt.py" ]